import urllib.request
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ("Google News VN Top", "https://news.google.com/rss?hl=vi&gl=VN&ceid=VN:vi"),
    ("Google News VN Xã hội", "https://news.google.com/rss/headlines/section/topic/NATION?hl=vi&gl=VN&ceid=VN:vi"),
    ("Google News VN Kinh doanh", "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=vi&gl=VN&ceid=VN:vi"),
    ("Google News VN Công nghệ", "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=vi&gl=VN&ceid=VN:vi"),
    ("Google News VN Thế giới", "https://news.google.com/rss/headlines/section/topic/WORLD?hl=vi&gl=VN&ceid=VN:vi"),
    ("Google Trends VN Daily", "https://trends.google.com.vn/trending/rss?geo=VN"),
]

with open("d:/Antigravity+Codex/Hop_Den_Tri_Thuc/.system_generated/google_news_feed.txt", "w", encoding="utf-8") as f:
    for name, url in urls:
        f.write(f"\n==================== {name} ====================\n")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            content = urllib.request.urlopen(req, timeout=10).read()
            root = ET.fromstring(content)
            items = root.findall('.//item')
            for item in items[:10]:
                title = item.find('title').text if item.find('title') is not None else ''
                pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ''
                desc = item.find('description').text if item.find('description') is not None else ''
                # strip html from desc
                import re
                desc = re.sub(r'<[^>]+>', ' ', desc).strip()
                f.write(f"- {title} [{pubDate}]\n  {desc[:150]}...\n")
        except Exception as e:
            f.write(f"Error: {e}\n")

print("Finished fetching Google News Feeds")
