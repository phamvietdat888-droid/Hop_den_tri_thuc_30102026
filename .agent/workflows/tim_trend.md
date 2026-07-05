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
    
  - step: 3
    agent: 01_researcher  
    action: Lọc và Chấm điểm Trend
    input: Danh sách tin tức thô
    output: Top 5 chủ đề được chấm điểm cao nhất
    skill: skills/trinh_sat_trend_skill.md
    criteria: "Sử dụng 7 tiêu chí đánh giá Trend"
    
  - step: 4
    agent: 00_coordinator
    action: Báo cáo & Đề xuất
    input: Danh sách Top 5
    output: Trình bày một cách rõ ràng cho Sếp lựa chọn
    gate: CHỜ SẾP CHỌN CHỦ ĐỀ
    
  - step: 5
    agent: 00_coordinator
    action: Chuyển tiếp Tác chiến
    input: Quyết định của Sếp (Ví dụ: "Chọn chủ đề số 2")
    output: Tự động kích hoạt luồng `/tac_chien [chủ đề Sếp chọn]`
```
