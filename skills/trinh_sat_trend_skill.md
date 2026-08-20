# 🔍 SKILL: TRINH SÁT TREND — "Bước 0" Trước Khi Ra Trận
> **Phiên bản:** 2.0 | **Cập nhật:** 2026-04-20
> **Vai trò:** Geopolitical Trend Scout — Radar quét sóng cho kênh địa chính trị
> **Vị trí trong Pipeline:** BƯỚC 0 — Trước khi khởi động `/tac_chien`

---

## 📋 CONTEXT

Kênh YouTube của Sếp chuyên phân tích tin tức **chính trị — xã hội** trong nước và quốc tế, phong cách "Hộp Đen Tri Thức". Đối tượng khán giả: nam giới Việt Nam 25-50 tuổi, quan tâm đến "chuyện ngoài kia ảnh hưởng gì đến túi tiền nhà mình".

**Mục tiêu của Skill này:** Quét toàn bộ "chiến trường thông tin" để tìm ra chủ đề **ĐÁNG LÀM VIDEO NHẤT** tại thời điểm hiện tại — dựa trên dữ liệu thực tế, không phải cảm tính.

**Khi nào dùng:**
- Sếp chưa có chủ đề cụ thể, muốn tìm trend đang nóng
- Sếp có vài ý tưởng, muốn so sánh cái nào "ngon" hơn
- Sếp muốn biết đối thủ đang làm gì, mình nên đánh hướng nào

**Lệnh kích hoạt:** `/tim_trend [từ khóa]` hoặc `/tim_trend` (quét tổng)

---

## ⚙️ ACTION — QUY TRÌNH TRINH SÁT 5 BƯỚC

### BƯỚC 1: NHẬN LỆNH TRINH SÁT

**Sếp có thể giao lệnh theo 3 cách:**

```
Cách 1 — Có từ khóa:
/tim_trend chiến tranh thương mại Mỹ Trung

Cách 2 — Quét tổng:
/tim_trend
→ AI tự quét các nguồn nóng nhất hôm nay

Cách 3 — So sánh:
/tim_trend so_sanh: đất hiếm, BRICS, Biển Đông
→ So sánh 3 chủ đề, chọn cái "ngon" nhất
```

**Nếu Sếp chỉ gõ `/tim_trend` (không có từ khóa):**
→ AI tự quét các nguồn, tìm TOP 5 chủ đề nóng nhất liên quan đến chính trị — xã hội — kinh tế.

---

### BƯỚC 2: QUÉT ĐA NGUỒN (Song Song)

#### 🏆 NGUỒN 1: GOOGLE TRENDS (ƯU TIÊN SỐ 1)

**Đây là nguồn quan trọng nhất — phản ánh thực tế người Việt đang tìm gì.**

**Tool:** `search_web` + `read_url_content`

**Queries chạy:**
- `[từ_khóa] google trends vietnam`
- `[từ_khóa] xu hướng tìm kiếm google việt nam`
- `google trends vietnam today politics`
- `xu hướng tìm kiếm nổi bật hôm nay việt nam`

**URL truy cập trực tiếp (BẮT BUỘC):**
- `https://trends.google.com.vn/trending?geo=VN` — Radar số 1, phản ánh thực tế người Việt tìm gì.
- `https://trends.google.com.vn/trending/trendingnow?geo=VN` — Xu hướng thời gian thực.
- `https://trends.google.com/trending?geo=US` — Xu hướng tại Mỹ (đối chiếu)

**Dữ liệu cần lấy:**
- Từ khóa liên quan đang tăng đột biến (Breakout / +5000%)
- Lượng tìm kiếm tương đối (0-100)
- Khu vực tìm kiếm nhiều nhất
- Các từ khóa liên quan (Related queries)

---

#### 📰 NGUỒN 2: BÁO CHÍ VIỆT NAM (Tin trong nước)

**Tool:** `search_web` + `read_url_content`

**Queries chạy:**
- `[từ_khóa] site:vnexpress.net`
- `[từ_khóa] site:tuoitre.vn`
- `[từ_khóa] site:thanhnien.vn`
- `[từ_khóa] site:dantri.com.vn`
- `[từ_khóa] site:bbc.com/vietnamese`
- `[từ_khóa] site:voatiengviet.com`
- `[từ_khóa] tin nóng hôm nay`

**URL truy cập trực tiếp (quét trang chủ khi không có từ khóa):**
- `https://vnexpress.net/the-gioi` — Tin thế giới VnExpress
- `https://tuoitre.vn/the-gioi.htm` — Tin thế giới Tuổi Trẻ
- `https://thanhnien.vn/the-gioi.htm` — Tin thế giới Thanh Niên

**Mục đích:** Biết báo chí VN đang đưa tin gì → khán giả VN đang đọc gì → chủ đề nào đang nóng trên truyền thông.

---

#### 🌍 NGUỒN 3: BÁO CHÍ QUỐC TẾ (Tin thế giới)

**Tool:** `search_web` + `read_url_content`

**Queries chạy:**
- `[từ_khóa] site:reuters.com`
- `[từ_khóa] site:bbc.com/news`
- `[từ_khóa] site:aljazeera.com`
- `[từ_khóa] site:scmp.com` — South China Morning Post (góc nhìn châu Á)
- `[từ_khóa] site:thediplomat.com` — Chuyên về địa chính trị châu Á
- `[từ_khóa] geopolitics breaking news`

**Mục đích:** Nắm bắt tin quốc tế TRƯỚC KHI báo VN đưa → tạo lợi thế "người đầu tiên phân tích".

---

#### 📘 NGUỒN 4: FACEBOOK & THREADS — "Ổ kiến lửa" Viral

**Tool:** `search_web` + `browser_subagent` (nếu cần)

**Facebook Queries:**
- `site:facebook.com [từ_khóa] tranh luận`
- `[từ_khóa] facebook trending vietnam`
- **Group:** "Thời sự quốc tế", "Tin tức 24h", "Tổ Buôn 24/7".

**Threads Queries (Ưu tiên giới trẻ/tri thức):**
- `site:threads.net [từ_khóa] Việt Nam`
- `site:threads.net "địa chính trị" [từ_khóa]`
- `threads.net trending today vietnam`

**Dữ liệu cần lấy:**
- Bài post nào nhiều reaction/share nhất trong 24h?
- **Threads:** Giới trẻ đang quan tâm góc nhìn nào? (Soft power, kinh tế, lối sống).
- Đối thủ vừa đăng bài FB gì? (để TRÁNH trùng hoặc ĐÁNH NHANH HƠN).
- Comment nào nhiều "gạch đá" nhất? (gợi ý góc nhìn gây engagement).

---

#### 🎥 NGUỒN 5: YOUTUBE — Đối thủ cùng ngách

**Tool:** `search_web`

**Queries chạy:**
- `site:youtube.com [từ_khóa] phân tích chính trị 2026`
- `site:youtube.com "Tuấn Tiền Tỷ" [từ_khóa]`
- `site:youtube.com "Củ Đậu Story" [từ_khóa]`
- `[từ_khóa] youtube việt nam trending thời sự`

**Kênh đối thủ cần quét (BẮT BUỘC — dùng `browser_subagent`):**

| # | Kênh | URL | Ghi chú |
|---|---|---|---|
| 1 | Tuấn Tiền Tỷ | `https://www.youtube.com/@TuanTienTi2911/videos` | Benchmark phong cách dân dã |
| 2 | Củ Đậu Story | `https://www.youtube.com/@C%E1%BB%A7%C4%90%E1%BA%ADuStory/videos` | Phân tích sự thật, 727K subs |
| 3 | Tuyền Văn Hóa | `https://www.youtube.com/@MrTVHChanelOfficial/videos` | ⚠️ **CHỈ GHI NHẬN video ≥100k views** (kênh spam 3-4 video/ngày, 2.34M subs) |
| 4 | CD Media - Why? | Quét qua `search_web` | 2M+ subs, chuyên nghiệp |
| 5 | Kiến Thức Thú Vị | Quét qua `search_web` | Kiến thức tổng hợp |

> **⚠️ QUY TẮC TUYỀN VĂN HÓA:** Kênh này đăng quá nhiều video (3-4/ngày). Khi quét, CHỈ ghi nhận video đạt **≥ 100.000 views**. Video dưới 100k = bỏ qua hoàn toàn. Lý do: chỉ video 100k+ mới phản ánh chủ đề thực sự hot.

**Dữ liệu cần lấy:**
- Video nào trending trong ngách thời sự?
- Video đối thủ nào đạt view cao bất thường? (chủ đề đang hot)
- Video nào nhiều comment tranh cãi?
- Đối thủ CHƯA làm chủ đề gì mà đang nóng? (cơ hội vàng)
- **Tuyền Văn Hóa:** Video nào đạt ≥100k views? → Đó là tín hiệu trend nóng.

---

#### 🐦 NGUỒN 6: X (Twitter) & Reddit

**Tool:** `search_web` + `read_url_content`

**X (Twitter):**
- `site:x.com [từ_khóa] geopolitics`
- `[từ_khóa] twitter trending vietnam`
- Theo dõi: @Reuters, @BBCWorld, @AJEnglish, @SCMPNews

**Reddit:**
- `https://www.reddit.com/r/geopolitics/hot/`
- `https://www.reddit.com/r/worldnews/hot/`
- `https://www.reddit.com/r/VietNam/hot/`
- `https://www.reddit.com/search/?q=[từ_khóa]&sort=hot&t=week`

**Mục đích:** Nắm bắt góc nhìn quốc tế + dư luận cộng đồng → phát hiện trend chưa được báo chí VN đưa tin.

---

### BƯỚC 3: PHÂN TÍCH & CHẤM ĐIỂM

Với mỗi chủ đề tìm được, chấm điểm theo **7 tiêu chí đặc thù cho kênh địa chính trị:**

| # | Tiêu chí | Mô tả | Thang điểm |
|---|---|---|---|
| 1 | 🔥 **Độ hot** | Bao nhiêu nguồn nhắc đến? Google Trends tăng bao nhiêu %? | ⭐⭐⭐⭐⭐ |
| 2 | ⏰ **Độ mới** | Trong 24h / 48h / 7 ngày? Càng mới càng tốt. | ⭐⭐⭐⭐⭐ |
| 3 | 💬 **Độ tranh cãi** | Có ý kiến trái chiều? Nhiều comment/share? (gây engagement) | ⭐⭐⭐⭐⭐ |
| 4 | 💔 **Tiềm năng "chạm nỗi đau"** | Ảnh hưởng đến túi tiền, công việc, gia đình người VN? *(Tham chiếu: `.shared/to_mo_loi_ich_module.md`)* | ⭐⭐⭐⭐⭐ |
| 5 | 📜 **Tiềm năng liên hệ lịch sử VN** | Có sự tương đồng tự nhiên với sự kiện lịch sử VN không? *(Tham chiếu: `.shared/lich_su_vn_module.md` + `.shared/kho_vu_khi/lich_su_vn.md`)* | ⭐⭐⭐⭐⭐ |
| 6 | ⚠️ **Rủi ro YouTube** | Demonetize? Age-restrict? Vi phạm chính sách? (Thấp = tốt) | 🟢🟡🔴 |
| 7 | 🔄 **Đã làm chưa?** | Kiểm tra `outputs/` và `.shared/kho_vu_khi/` — tránh lặp chủ đề | ✅ Mới / ⚠️ Tương tự / ❌ Đã làm |

**Công thức tính điểm tổng:**
```
Điểm Trend = (Độ hot × 2) + (Độ mới × 2) + Tranh cãi + (Nỗi đau × 3) + Lịch sử VN - (Rủi ro YT × 2)
```
→ **Nỗi đau** có hệ số cao nhất (×3) vì đây là thứ quyết định Retention.
→ **Rủi ro YT** là hệ số trừ — chủ đề nóng nhưng nguy hiểm = không đáng.

---

### BƯỚC 4: BÁO CÁO TRINH SÁT (BẮT BUỘC ĐẦY ĐỦ 100% SIÊU CHI TIẾT)

> ⚠️ **QUY TẮC VĨNH VIỄN BẮT BUỘC (KHÔNG NGOẠI LỆ):**
> 1. Kết quả trả về của lệnh `/tim_trend` BẮT BUỘC phải tuân thủ đúng file template `.shared/template_bao_cao_trinh_sat_trend.md`.
> 2. BẮT BUỘC xuất ra bản báo cáo SIÊU CHI TIẾT 100% gồm đủ 5 Phần: (1) Tổng quan chiến trường & Thời sự nóng; (2) Top 5 chủ đề bóc tách ĐẦY ĐỦ 8 MỤC CHI TIẾT CHO CẢ 5 CHỦ ĐỀ; (3) Tình báo đối thủ đối chiếu trực tiếp; (4) Gợi ý 3 Tiêu đề Viral cho chủ đề #1; (5) Đề xuất hành động cho Sếp & Link đính kèm `.docx`.
> 3. TUYỆT ĐỐI KHÔNG xuất kết quả tóm tắt ngắn, KHÔNG cắt gọt 8 mục của bất kỳ chủ đề nào trong Top 5. Mọi trường hợp trả lời sơ sài/rút gọn đều là VI PHẠM QUY CHUẨN KÊNH.

#### Format output chuẩn: (Bắt buộc dùng mẫu `.shared/template_bao_cao_trinh_sat_trend.md`)

```markdown
# 🔍 BÁO CÁO TRINH SÁT TREND — BƯỚC 0 (GIẢI MÃ 360)
> **Ngày thực hiện:** [DD/MM/YYYY] | **Hệ thống:** Giải Mã 360 ("Hộp Đen Tri Thức")  
> **Đơn vị thực hiện:** 01_Researcher & 00_Coordinator

---

## 📊 1. TỔNG QUAN CHIẾN TRƯỜNG & THỜI SỰ NÓNG HÔM NAY

- **Google Trends Việt Nam (Radar số 1):** [...]
- **Mặt trận Mạng xã hội (Threads/Facebook):** [...]
- **Báo chí trong nước & quốc tế:** [...]
- **Sổ trí nhớ kênh (Vòng về bài cũ):** [...]

---

## 🏆 2. TOP 5 CHỦ ĐỀ ĐỀ XUẤT (XẾP THEO ĐIỂM SỐ 7 TIÊU CHÍ)

### 1️⃣ [Tên Chủ đề 1] — (KHUYÊN SẾP CHỌN 🥇 nếu tốt nhất)
- **Điểm tổng:** ⭐ **[X]/35**
- **Nguồn trích:** [...]
- **Tóm tắt sự kiện:** [...]
- **💔 Nỗi đau người dân bình dân:** [...]
- **📜 Lịch sử Việt Nam / Sổ trí nhớ:** [...]
- **⚠️ Rủi ro YouTube:** 🟢/🟡/🔴 [...]
- **🎯 Góc nhìn "Hộp Đen Tri Thức":** [...]
- **🎣 Gợi ý Hook (15s):** [...]

*(Tương tự bóc đủ 8 mục chi tiết cho Chủ đề 2️⃣, 3️⃣, 4️⃣, 5️⃣ — KHÔNG CẮT BỚT)*

---

## 🕵️ 3. TÌNH BÁO ĐỐI THỦ (ĐỐI CHIẾU TRỰC TIẾP)

- **Tuấn Tiền Tỷ / Củ Đậu Story / CD Media:** [...]
- **👉 Kết luận chiến thuật & khoảng trống vàng:** [...]

---

## 💡 4. GỢI Ý TIÊU ĐỀ VIRAL (CHO CHỦ ĐỀ #1)

• **[Tiêu đề 1 — Theo trend hot, gây tò mò]:** [...]  
• **[Tiêu đề 2 — Góc nhìn ngược, phản biện]:** [...]  
• **[Tiêu đề 3 — FOMO / Kéo về nỗi đau]:** [...]

---

## 🎯 5. ĐỀ XUẤT HÀNH ĐỘNG CHO SẾP

- 🥇 **Khuyên Sếp chọn:** **[Chủ đề]**
- **File đính kèm:** Link tới file tài liệu báo cáo DOCX tại `outputs/YYYY-MM-DD_De_Xuat_Trend/00_de_xuat_trend.docx`
- 📌 **Lệnh tiếp theo:** /tac_chien [chủ đề Sếp chọn]
```

---

### BƯỚC 5: CHUYỂN GIAO VÀO PIPELINE

Sau khi Sếp chọn chủ đề từ báo cáo:

```
Sếp: "Làm chủ đề số 1"
→ AI tự động: /tac_chien [chủ đề số 1]
→ Pipeline 7 bước khởi động ngay
→ Brief (Bước 1) được tạo tự động từ dữ liệu trinh sát
```

**Dữ liệu từ Bước 0 được chuyển sang Bước 1-2 của Pipeline:**
- Tóm tắt sự kiện → Brief (`01_brief.md`)
- Gợi ý Angle + Hook → Đề xuất Angle (`02_angle.md`)
- Link tham khảo → Dữ liệu đầu vào cho Agent 01 (Researcher)
- Gợi ý nỗi đau + lịch sử VN → Context cho Agent 02 (Scriptwriter)

---

## 🔗 THAM CHIẾU BẮT BUỘC

Trước khi tạo báo cáo, Agent PHẢI đọc:
- `.shared/kho_vu_khi/` — Tránh lặp chủ đề + ví von đã dùng
- `.shared/to_mo_loi_ich_module.md` — Đánh giá tiềm năng "chạm nỗi đau"
- `.shared/lich_su_vn_module.md` + `.shared/kho_vu_khi/lich_su_vn.md` — Đánh giá tiềm năng liên hệ lịch sử
- `.shared/hook_formulas.md` — Gợi ý Hook phù hợp
- `outputs/` — Kiểm tra đã từng làm chủ đề tương tự chưa

---

## 📝 HƯỚNG DẪN SỬ DỤNG

**Quét nhanh (không cần từ khóa):**
```
/tim_trend
→ AI tự quét Google Trends VN + báo chí + đối thủ → Top 5 chủ đề nóng nhất
```

**Tìm theo từ khóa:**
```
/tim_trend đất hiếm
→ Quét tất cả nguồn về "đất hiếm" → Báo cáo chi tiết
```

**So sánh nhiều từ khóa:**
```
/tim_trend so_sanh: Biển Đông, BRICS, thuế Trump
→ So sánh 3 chủ đề → Chọn cái đáng làm nhất
```

**Tìm + chỉ định nguồn:**
```
/tim_trend đất hiếm nguồn: google_trends, facebook, đối_thủ
→ Chỉ quét 3 nguồn được chỉ định
```

---

## ⚠️ LƯU Ý QUAN TRỌNG

1. **Google Trends là vua** — Nếu Google Trends VN không tăng, chủ đề dù hay cũng khó viral tại VN.
2. **Luôn ghi rõ nguồn** (link) cho mỗi trend tìm được.
3. **Ưu tiên 48h gần nhất** — YouTube thưởng video nhanh, đúng lúc.
4. **Đánh giá trung thực** — Nếu từ khóa không có trend rõ ràng → nói thẳng, đề xuất từ khóa khác.
5. **Đối thủ là la bàn** — Nếu đối thủ vừa đăng cùng chủ đề → mình phải có góc nhìn KHÁC hoặc SÂU HƠN.
6. **Nỗi đau là kim chỉ nam** — Chủ đề hot mà không chạm được nỗi đau người VN = view thấp.
7. **An toàn trước** — Chủ đề 🔴 Rủi ro cao → cân nhắc kỹ, hoặc tìm cách nói giảm nói tránh.
8. **Cập nhật danh sách đối thủ** — Khi phát hiện kênh mới cùng ngách → bổ sung vào Nguồn 4 & 5.
