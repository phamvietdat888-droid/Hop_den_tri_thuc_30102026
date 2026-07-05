# Workflow: Quét Đối Thủ (Competitor Intelligence)
> **Trigger:** `/quet_doi_thu` (Quét toàn bộ) hoặc `/quet_doi_thu [tên]` (Quét 1 đối thủ riêng biệt)

## Nhiệm vụ
Giám sát, phân tích và cập nhật tình hình hoạt động của 4 đối thủ chính trong ngách (Tuấn Tiền Tỉ, Kiến Thức Thú Vị, CD Media, Củ Đậu Story). Tự động cập nhật hồ sơ và báo cáo tình báo.

## Pipeline chính

```yaml
steps:
  - step: 1
    agent: 01_researcher
    action: Thu thập dữ liệu YouTube
    input: Lệnh từ user
    output: Dữ liệu 5 video gần nhất (Tiêu đề, Views, Thời gian đăng)
    targets: 
      - Tuấn Tiền Tỉ
      - Kiến Thức Thú Vị
      - CD Media - Why?
      - Củ Đậu Story

  - step: 2  
    agent: 01_researcher
    action: Phân tích nội dung và Dữ liệu
    input: Dữ liệu từ step 1
    output: Nhận định về xu hướng, chủ đề nóng, định hướng nội dung của các đối thủ
    
  - step: 3
    agent: 01_researcher
    action: Quét Mạng Xã Hội (Facebook)
    input: Fanpage/Group của đối thủ (nếu có)
    output: Các bài post hot nhất trong tuần, nội dung đang được khán giả đối thủ quan tâm
    
  - step: 4
    agent: 00_coordinator
    action: Cập nhật Hồ sơ Đối thủ
    input: Phân tích từ step 2 và 3
    output: Cập nhật dữ liệu mới vào các file tương ứng (01_tuan_tien_ti.md, 02_kien_thuc_thu_vi.md, 03_cd_media_why.md, 04_cu_dau_story.md)
    
  - step: 5
    agent: 00_coordinator
    action: Cập nhật Báo cáo Tình báo
    input: Hồ sơ đối thủ đã được update
    output: Ghi đè/Nối thêm thông tin vào file `bao_cao_tinh_bao.md`
    note: Đưa ra cảnh báo nếu đối thủ có dấu hiệu thay đổi chiến lược hoặc đang làm trend quá tốt.
```
