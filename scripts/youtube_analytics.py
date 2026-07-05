import os
import pickle
import json
import argparse
from datetime import datetime, timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly', 'https://www.googleapis.com/auth/youtube.readonly']

# Credential nằm NGOÀI project để tránh rò rỉ secret khi index/commit.
# Có thể override bằng biến môi trường NKTC_CREDENTIALS_DIR.
CREDENTIALS_DIR = os.environ.get('NKTC_CREDENTIALS_DIR') or os.path.join(os.path.expanduser('~'), '.credentials', 'nktc')
CLIENT_SECRETS_PATH = os.path.join(CREDENTIALS_DIR, 'client_secrets.json')
TOKEN_PATH = os.path.join(CREDENTIALS_DIR, 'token.pickle')

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_PATH):
                print(f"❌ LỖI: Không tìm thấy client_secrets.json tại '{CLIENT_SECRETS_PATH}'.")
                print("   Xem hướng dẫn: docs/youtube_api_setup.md")
                return None, None

            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_PATH, SCOPES)
            creds = flow.run_local_server(port=0, open_browser=False)

        os.makedirs(CREDENTIALS_DIR, exist_ok=True)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    youtube = build('youtube', 'v3', credentials=creds)
    youtube_analytics = build('youtubeAnalytics', 'v2', credentials=creds)
    
    return youtube, youtube_analytics

def get_video_stats(youtube, video_id):
    """Lấy số View, Like, Comment cơ bản"""
    request = youtube.videos().list(
        part="statistics,snippet",
        id=video_id
    )
    response = request.execute()
    
    if not response['items']:
        return None
        
    return response['items'][0]

def get_video_analytics(youtube_analytics, video_id):
    """Lấy CTR và Average View Duration (10 tiếng/ngày gần nhất)"""
    # YouTube Analytics thường delay 1-2 ngày với thông số kênh lớn, 
    # nhưng chúng ta setup khung thời gian rộng nhất có thể
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d') # Quét trong 7 ngày
    
    try:
        request = youtube_analytics.reports().query(
            ids='channel==MINE',
            startDate=start_date,
            endDate=end_date,
            metrics='annotationClickThroughRate,averageViewDuration',
            filters=f'video=={video_id}'
        )
        response = request.execute()
        return response
    except Exception as e:
        print(f"⚠️ Chưa có data Analytics (delay 24-48h của YT) hoặc lỗi API: {e}")
        return None

def analyze_and_export(video_id):
    print("⏳ Đang kết nối Bộ tư lệnh (YouTube Studio)...")
    youtube, youtube_analytics = get_authenticated_service()
    
    if not youtube:
        return
        
    print(f"🔍 Đang truy xuất hồ sơ tác chiến của Video: {video_id}...")
    
    # 1. Lấy thông tin công khai
    stats = get_video_stats(youtube, video_id)
    if not stats:
        print("❌ Không tìm thấy Video ID. Vui lòng kiểm tra lại!")
        return
        
    title = stats['snippet']['title']
    view_count = stats['statistics'].get('viewCount', 0)
    like_count = stats['statistics'].get('likeCount', 0)
    comment_count = stats['statistics'].get('commentCount', 0)
    
    # 2. Lấy dữ liệu mật (Analytics)
    # Ghi chú: Chức năng này sẽ ra data khi API YouTube kịp cập nhật (thường YouTube delay Analytic 1-2 ngày). 
    # Nhưng nếu lấy qua Data API (view, like) thì là realtime.
    # Để đáp ứng nhu cầu 10 giờ của Sếp, hệ thống sẽ sử dụng chỉ báo sớm (Bình luận/View tỷ lệ).
    
    engagement_rate = (int(like_count) + int(comment_count)) / max(1, int(view_count)) * 100
    
    # Xuất Report
    report = f"""# 📊 BÁO CÁO KHÁM NGHIỆM SAU 10 GIỜ ĐẦU
> **Video:** {title}
> **Thời điểm xuất:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## SỐ LIỆU TÁC CHIẾN:
- **Lượt xem (Views):** {view_count}
- **Lượt tương tác (Likes & Comments):** {int(like_count) + int(comment_count)}
- **Tỷ lệ thả tim/Bình luận:** {engagement_rate:.2f}%

*(Lưu ý: Dữ liệu CTR và Retention chi tiết từ YouTube Analytics thường bị delay 24-48 tiếng từ máy chủ Google. Tuy nhiên tỷ lệ tương tác 10h đầu > 5% là một tín hiệu an toàn cực mạnh).*
"""
    
    os.makedirs('../outputs', exist_ok=True)
    report_path = f'../outputs/report_{video_id}.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
        
    print(f"✅ Đã xuất báo cáo trinh sát tại: {report_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trích xuất YouTube Analytics')
    parser.add_argument('--video', type=str, help='Video ID cần khám nghiệm', required=True)
    args = parser.parse_args()
    
    analyze_and_export(args.video)
