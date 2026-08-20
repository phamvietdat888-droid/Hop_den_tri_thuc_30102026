# Workflow: Trinh Sát Trend
> **Trigger:** `/tim_trend [từ khóa]` (từ khóa tùy chọn)

## Nhiệm vụ
Hệ thống tự động sử dụng Agent để quét đa nguồn, chấm điểm các chủ đề dựa trên 7 tiêu chí và đề xuất Top 5 chủ đề tiềm năng nhất để sản xuất kịch bản.

## Pipeline chính

```yaml
steps:
  - step: 1
    agent: 01_researcher
    action: Quét tin bài Đa nguồn
    input: Từ khóa từ user (nếu có, không có sẽ quét diện rộng)
    output: Danh sách các tin tức, sự kiện nổi bật trong 24-48h
    sources:
      - Google Trends VN
      - Báo VN (VnExpress, Dân Trí, Tuổi Trẻ, etc.)
      - Báo Quốc tế (Reuters, BBC, Bloomberg)
      - MXH (Facebook, X/Twitter, Reddit)
      
  - step: 2
    agent: 01_researcher
    action: Tình báo cục bộ (Check Đối thủ)
    input: Đọc file `Đối_thủ/bao_cao_tinh_bao.md`
    output: Biết được đối thủ đã làm trend này chưa, góc nhìn của họ là gì
    note: Đảm bảo không đụng hàng hoặc chọn góc nhìn ngược lại hoàn toàn so với đối thủ.

  - step: 2b
    agent: 01_researcher
    action: Quét Sổ trí nhớ kênh (news-jacking & vòng về video cũ)
    input: Đọc file `.shared/kho_vu_khi/so_tri_nho_kenh.md`
    output: Video cũ nào liên quan tin nóng → đề xuất mở bài kiểu "phần tiếp theo" + gắn link video cũ ở mô tả & comment ghim
    note: Chỉ vòng về khi liên quan THẬT; không tự khen "mình đã đoán đúng" quá 1 câu. Chi tiết `.shared/chien_luoc_de_tai_tieu_de_tri_nho_kenh.md` mục E.
    
  - step: 3
    agent: 01_researcher  
    action: Lọc và Chấm điểm Trend
    input: Danh sách tin tức thô
    output: Top 5 chủ đề được chấm điểm cao nhất
    skill: skills/trinh_sat_trend_skill.md
    criteria: "7 tiêu chí đánh giá Trend + checklist đề tài 'Hồ sơ giải phẫu' (5 câu hỏi, đạt >= 4/5 mới đề xuất — .shared/chien_luoc_de_tai_tieu_de_tri_nho_kenh.md mục A)"
    
  - step: 4
    agent: 00_coordinator
    action: Báo cáo & Đề xuất (BẮT BUỘC BẢN SIÊU CHI TIẾT 100%)
    input: Danh sách Top 5
    output: BÁO CÁO SIÊU CHI TIẾT 100% ĐẦY ĐỦ 5 PHẦN theo đúng mẫu `.shared/template_bao_cao_trinh_sat_trend.md` (Bóc đủ 8 mục cho CẢ 5 CHỦ ĐỀ, KHÔNG tóm tắt hay cắt ngắn) + đính kèm file DOCX
    gate: CHỜ SẾP CHỌN CHỦ ĐỀ
    
  - step: 5
    agent: 00_coordinator
    action: Chuyển tiếp Tác chiến
    input: Quyết định của Sếp (Ví dụ: "Chọn chủ đề số 2")
    output: Tự động kích hoạt luồng `/tac_chien [chủ đề Sếp chọn]`
```
