# 🏥 SKILL KHÁM KÊNH — Chuyên Gia Tư Vấn Phát Triển Kênh YouTube
> **Phiên bản:** 1.1 (v1.1 — Phase 3: Tích hợp community skill `hybrid-search-implementation` cho semantic search transcript đối thủ)
> **Ngày tạo:** 2026-04-29 | **Update:** 2026-05-23
> **Vai trò:** YouTube Channel Doctor — "Bác sĩ chuyên khoa" cho kênh YouTube
> **Vị trí trong Pipeline:** Hoạt động **SONG SONG** với Pipeline chính, gọi bất cứ lúc nào
> **Thay thế:** `phan_tich_studio_skill.md` (61 dòng) — kế thừa + mở rộng toàn diện

## 🆕 v1.1 — Hybrid Search trên transcript đối thủ

> Khi cần trả lời câu hỏi *"5 kênh đối thủ tuần này nói NHIỀU NHẤT về chủ đề gì?"* — không thể đọc thủ công 50+ video. Dùng community skill `hybrid-search-implementation` (vector + keyword search) để semantic search trên transcript đã download.
>
> **Pipeline mới:**
> 1. `video-transcript-downloader` (skill cộng đồng hiện có) → download transcript top 10 video tuần từ 5 kênh
> 2. `hybrid-search-implementation` → index transcript thành vector DB + keyword index
> 3. Query: *"Tìm tất cả đoạn nói về [chủ đề]"* → trả về top matches kèm timestamp + kênh
> 4. Output: bảng tổng hợp "chủ đề X xuất hiện Y lần ở Z kênh, thời điểm cao nhất ngày DD"
>
> **Trigger semantic:** *"Dùng hybrid-search-implementation: index 50 transcript đối thủ tuần này, query chủ đề [...], trả về heat map theo kênh + thời gian"*

---

## 🎯 SỨ MỆNH

Biến dãy số khô khan trong YouTube Studio thành **hành động cụ thể, có thể thực hiện ngay**, bằng cách kết hợp:
- **Phân tích định lượng:** Đọc số liệu Studio, tính toán xu hướng, so sánh benchmark
- **Phân tích định tính:** Đánh giá tiêu đề, thumbnail, nội dung, phong cách
- **Tư vấn chiến lược:** Khuyến nghị phát triển kênh dài hạn dựa trên data thực

**Không chỉ khám 1 video — mà khám TOÀN BỘ "cơ thể" kênh.**

---

## 🔗 KẾT NỐI HỆ SINH THÁI

| Skill liên quan | Kết nối |
|---|---|
| `viet_tieu_de_skill.md` | Data CTR theo Formula → feed vào chọn Formula tiêu đề |
| `giai_ma_360_skill.md` | Khuyến nghị nội dung → feed vào Bước 2 chọn Angle |
| `trinh_sat_trend_skill.md` | Benchmarking đối thủ → bổ sung data cho Nguồn 5 |
| `do_hoa_fanpage_skill.md` | Đánh giá Thumbnail → feed vào cải thiện thiết kế |
| Kho Vũ Khí (`.shared/kho_vu_khi/`) | Tự động cập nhật hook/ví von hiệu quả từ data thực |
| `Đối_thủ/` | Cập nhật hồ sơ đối thủ mới nhất |

---

## ⚡ 3 CHẾ ĐỘ VẬN HÀNH (Slash Commands)

| Lệnh | Chế độ | Thời gian | Mô tả |
|---|---|---|---|
| `/kham_kenh` | **A. Tổng Kiểm Tra** | ~15-20 phút | Khám toàn diện: tổng quan + nội dung + khán giả + traffic + đối thủ + khuyến nghị |
| `/kham_kenh 90d` | A. Tổng Kiểm Tra (90 ngày) | ~15-20 phút | Như trên nhưng kỳ phân tích 90 ngày |
| `/kham_video [video_id]` | **B. Khám Video Đơn Lẻ** | ~8-10 phút | Phân tích sâu 1 video: CTR, AVD, retention, tiêu đề, thumbnail |
| `/kham_nhanh` | **C. Pulse Check** | ~3-5 phút | Kiểm tra nhanh: số liệu 7 ngày + cảnh báo bất thường |

> **Kỳ phân tích mặc định:** 28 ngày. Thêm `90d` hoặc `365d` để thay đổi.

---

## 📋 PHƯƠNG PHÁP THU THẬP DỮ LIỆU

### Phương pháp chính: YouTube Studio (Browser)

**Tool:** `browser_subagent` truy cập `https://studio.youtube.com`

**Quy trình thu thập:**

```
1. Mở YouTube Studio → Tab Overview (Dashboard)
   → Ghi nhận: Views, Watch Time, Subscribers, Revenue (28d/90d)
   → Ghi nhận: Xu hướng tăng/giảm (% thay đổi)
   → Ghi nhận: Top videos hiện tại

2. Chuyển sang Tab Content
   → Ghi nhận: Danh sách video gần nhất (20 video)
   → Với mỗi video: Title, Views, Upload date, Likes, Comments
   → Click vào từng video top: CTR, AVD, Impressions, Traffic sources

3. Chuyển sang Tab Analytics → Overview
   → Ghi nhận: Biểu đồ xu hướng Views/Watch Time/Subscribers
   → Ghi nhận: Realtime views (48h)
   → Ghi nhận: Top content trong kỳ

4. Chuyển sang Tab Analytics → Audience
   → Ghi nhận: Returning vs New viewers
   → Ghi nhận: Demographics (Age, Gender, Location)
   → Ghi nhận: When viewers are on YouTube
   → Ghi nhận: Other channels/videos audience watches

5. Chuyển sang Tab Analytics → Reach
   → Ghi nhận: Impressions, CTR, Traffic sources
   → Ghi nhận: Top search terms
   → Ghi nhận: External traffic sources
```

> [!IMPORTANT]
> **Quy tắc:** Khi truy cập Studio, agent PHẢI đợi mỗi tab load hoàn toàn (3-5 giây) trước khi đọc data. Data YouTube Studio thường render chậm. Nếu thấy số "0" hoặc "—" bất thường → reload trang và đọc lại.

### Phương pháp bổ sung: Kênh công khai (Browser)

**Tool:** `browser_subagent` truy cập `https://www.youtube.com/@[channel_handle]`

**Dùng khi:** Không cần đăng nhập, chỉ cần data công khai (views, likes, comments, upload date).

---

## 🔬 7 MODULE PHÂN TÍCH

---

### MODULE 1: TỔNG QUAN KÊNH (Channel Health Check)

**Mục tiêu:** Đánh giá "sức khỏe tổng thể" — kênh đang khỏe hay đang chết dần?

**Nguồn dữ liệu:** YouTube Studio → Tab Overview

#### Chỉ số thu thập:

| Nhóm | Chỉ số | Cách lấy | Benchmark kênh 30K subs |
|---|---|---|---|
| **Tăng trưởng** | Subscribers (net gain/loss) | Studio Overview | ≥ +50/tháng = Khỏe |
| | Subscribers gained vs lost | Studio Overview | Lost < 10% Gained |
| | Tốc độ tăng sub (%/tháng) | Tính: gained/total × 100 | ≥ 0.5%/tháng |
| **Lưu lượng** | Views (28d) | Studio Overview | ≥ 20.000/tháng |
| | Watch Time (giờ, 28d) | Studio Overview | ≥ 500 giờ/tháng |
| | Views/Video trung bình | Tính: total views / số video đăng trong kỳ | ≥ 1.000/video |
| **Kiếm tiền** | Revenue (28d) | Studio Overview | Tùy thuộc CPM ngách |
| | RPM (Revenue per 1000 views) | Studio → Revenue tab | $0.5-2.0 (VN) |
| **So kỳ trước** | % thay đổi Views | Studio Overview (có sẵn) | Dương = tốt |
| | % thay đổi Watch Time | Studio Overview | Dương = tốt |
| | % thay đổi Subscribers | Studio Overview | Dương = tốt |

#### Thang đánh giá sức khỏe:

| Trạng thái | Tiêu chí | Icon |
|---|---|---|
| **Khỏe mạnh** | Cả 3 chỉ số chính (Views, Watch Time, Subs) đều tăng so kỳ trước | 🟢 |
| **Ổn định** | 2/3 chỉ số tăng hoặc đi ngang, không có chỉ số nào tụt >20% | 🟡 |
| **Suy giảm** | 2/3 chỉ số giảm, hoặc 1 chỉ số tụt >30% | 🟠 |
| **Nguy hiểm** | Cả 3 giảm, hoặc subscriber net < 0 (mất sub), hoặc không đăng video >30 ngày | 🔴 |

#### Phân tích đặc biệt — Phát hiện "Bệnh hôn mê":

```
NẾU ngày_hiện_tại - ngày_video_cuối > 14 ngày:
  → CẢNH BÁO: "Kênh đang ngừng hoạt động [X] ngày"
  → Tính: Tốc độ mất subscriber/ngày
  → Tính: Impressions hiện tại vs trung bình khi đang đăng đều
  → Dự báo: Nếu tiếp tục không đăng, bao lâu nữa sẽ mất [X]% impressions
```

---

### MODULE 2: PHÂN TÍCH NỘI DUNG (Content Performance)

**Mục tiêu:** Video nào ăn, video nào flop? Thể loại nào hiệu quả nhất? Formula tiêu đề nào cho CTR cao?

**Nguồn dữ liệu:** YouTube Studio → Tab Content + Analytics

#### Bước 2.1: Thu thập data Top 20 video gần nhất

Với **MỖI video** trong Top 20 gần nhất, thu thập:

| Chỉ số | Nguồn | Ghi chú |
|---|---|---|
| Tiêu đề | Content tab | Ghi nguyên văn |
| Upload date | Content tab | Format DD/MM/YYYY |
| Views | Content tab | Số tuyệt đối |
| Impressions | Click vào video → Analytics | Số tuyệt đối |
| CTR (%) | Click vào video → Analytics | Tỷ lệ nhấp |
| AVD (phút:giây) | Click vào video → Analytics | Thời lượng xem TB |
| Likes | Content tab | Số tuyệt đối |
| Comments | Content tab | Số tuyệt đối |
| Video length | Content tab | Tổng thời lượng video |
| Engagement Rate | Tính: (Likes + Comments) / Views × 100 | % |

#### Bước 2.2: Phân loại hiệu suất

Tính **trung bình kênh** (Average) cho mỗi chỉ số từ 20 video, sau đó phân loại từng video:

| Phân loại | Tiêu chí | Ý nghĩa |
|---|---|---|
| 🟢🟢 **Star** | Views > 2× Average AND CTR > Average | Video đột phá — cần phân tích TẠI SAO |
| 🟢 **Performer** | Views > Average | Trên trung bình — tốt |
| 🟡 **Average** | Views ≈ Average (±20%) | Bình thường |
| 🔴 **Underperformer** | Views < 0.5× Average | Dưới kỳ vọng — cần phân tích TẠI SAO |
| 🔴🔴 **Flop** | Views < 0.25× Average AND CTR < Average | Thất bại — bài học quan trọng |

#### Bước 2.3: Phân tích theo THỂ LOẠI nội dung

Gom nhóm 20 video theo thể loại, tính trung bình mỗi nhóm:

| Thể loại | Số video | Views TB | CTR TB | AVD TB | Engagement TB | Verdict |
|---|---|---|---|---|---|---|
| Kinh tế VN | _ | _ | _ | _ | _ | ✅ Nên làm thêm / ❌ Bỏ |
| Chính trị quốc tế | _ | _ | _ | _ | _ | _ |
| Xã hội / An ninh | _ | _ | _ | _ | _ | _ |
| Tự hào dân tộc | _ | _ | _ | _ | _ | _ |
| Lịch sử | _ | _ | _ | _ | _ | _ |
| Khác | _ | _ | _ | _ | _ | _ |

#### Bước 2.4: Phân tích TIÊU ĐỀ

Cross-reference tiêu đề với 13 Formula trong `viet_tieu_de_skill.md`:

| Formula | Số lần dùng | CTR trung bình | Views TB | Hiệu quả? |
|---|---|---|---|---|
| F1: Shock + Promise | _ | _ | _ | ✅/❌ |
| F2: News Breaking | _ | _ | _ | ✅/❌ |
| F3: Fear/FOMO | _ | _ | _ | ✅/❌ |
| ... | ... | ... | ... | ... |

→ **Output:** "Formula [X] cho CTR cao nhất, nên ưu tiên dùng. Formula [Y] đang flop, nên tránh."

#### Bước 2.5: Phân tích THUMBNAIL (Đánh giá bằng mắt)

Dùng `browser_subagent` xem thumbnail của Top 5 video (cao view nhất) và Bottom 5 (thấp view nhất):

| Tiêu chí | Top 5 có? | Bottom 5 có? | Kết luận |
|---|---|---|---|
| Mặt người cận cảnh (emotion) | _/5 | _/5 | Có mặt người → CTR cao hơn? |
| Text trên thumbnail | _/5 | _/5 | Chữ to dễ đọc trên mobile? |
| Màu sắc tương phản cao | _/5 | _/5 | Nổi bật trên feed? |
| Cờ quốc gia / biểu tượng | _/5 | _/5 | Dấu hiệu nhận biết nhanh? |
| Số liệu / con số | _/5 | _/5 | Gây tò mò? |

---

### MODULE 3: PHÂN TÍCH KHÁN GIẢ (Audience Intelligence)

**Mục tiêu:** Khán giả là ai? Đến từ đâu? Xem lúc nào? Đang mở rộng hay thu hẹp?

**Nguồn dữ liệu:** YouTube Studio → Tab Audience

#### Chỉ số thu thập:

| Nhóm | Chỉ số | Benchmark |
|---|---|---|
| **Loyalty** | Returning viewers (%) | ≥ 30% = tốt |
| | New viewers (%) | Cần cả 2 cân bằng |
| | Subscribers watching (%) | ≥ 20% = sub chất lượng |
| **Demographics** | Giới tính (Nam/Nữ %) | Kênh chính trị: Nam ~80% |
| | Top 3 nhóm tuổi | Target: 25-44 |
| | Top 5 quốc gia/thành phố | VN phải > 80% |
| **Hành vi** | Thời điểm online nhiều nhất | → Tối ưu lịch đăng |
| | Other channels audience watches | → Phát hiện đối thủ mới |
| | Other videos audience watched | → Phát hiện trend tiềm năng |

#### Phân tích: Xây dựng Persona khán giả

```markdown
## 👤 PERSONA KHÁN GIẢ LÝ TƯỞNG

- **Tên gọi:** [Ví dụ: "Anh Minh — Công nhân Bình Dương"]
- **Giới tính:** [từ data]
- **Độ tuổi:** [từ data]
- **Vị trí:** [từ data]
- **Quan tâm:** [suy luận từ other channels + other videos]
- **Nỗi đau chính:** [suy luận từ video nào có engagement cao nhất]
- **Thời điểm xem:** [từ data]
- **Thiết bị:** Mobile (>70% tại VN)
```

#### Phân tích: Sức khỏe tệp khán giả

| Tín hiệu | Tốt | Xấu |
|---|---|---|
| Returning viewers | Tăng hoặc ổn định | Giảm liên tục |
| New viewers % | 40-60% | < 20% (không thu hút mới) hoặc > 80% (không giữ chân) |
| Sub watching % | Tăng | Giảm → sub "chết" |
| Demographics shift | Mở rộng nhóm tuổi mới | Thu hẹp về 1 nhóm duy nhất |

---

### MODULE 4: PHÂN TÍCH TRAFFIC & SEO

**Mục tiêu:** Khán giả đến từ đâu? SEO đang hoạt động không? Nguồn traffic nào cần đẩy mạnh?

**Nguồn dữ liệu:** YouTube Studio → Tab Reach (hoặc Analytics → Reach)

#### Chỉ số thu thập:

| Chỉ số | Ý nghĩa | Benchmark |
|---|---|---|
| **Impressions** | YouTube "cho" bao nhiêu slot hiển thị | Tăng = thuật toán tin kênh |
| **CTR trung bình kênh** | Tỷ lệ click khi thấy thumbnail | ≥ 5% = tốt, ≥ 8% = xuất sắc |
| **Traffic từ Browse** | Trang chủ + Subscriptions | ≥ 30% = kênh mạnh |
| **Traffic từ Suggested** | Video đề xuất bên phải | ≥ 25% = nội dung liên kết tốt |
| **Traffic từ Search** | Tìm kiếm YouTube/Google | ≥ 15% = SEO tốt |
| **Traffic từ External** | Facebook, Google, website | Bonus — kênh đa nền tảng |
| **Top search terms** | Từ khóa dẫn đến kênh | → Feed vào SEO strategy |

#### Phân tích Traffic Mix:

```
Kênh khỏe mạnh (benchmark):
├── Browse/Home:     30-40%  ← YouTube tin tưởng đề xuất
├── Suggested:       25-35%  ← Nội dung liên kết với kênh khác
├── Search:          15-25%  ← SEO tốt, evergreen content
├── External:         5-10%  ← Facebook, Google, website
└── Other:            5-10%  ← Direct, Playlists, etc.

⚠️ Red flags:
├── Search > 50%    → Kênh phụ thuộc SEO, không được thuật toán đề xuất
├── Browse < 10%    → YouTube không tin tưởng kênh
├── External > 40%  → Kênh sống nhờ social, không tự chủ
└── Suggested = 0%  → Video không được liên kết, cần tối ưu tags/descriptions
```

#### Phân tích SEO Keywords:

| Từ khóa tìm kiếm | Views từ Search | Trend | Hành động |
|---|---|---|---|
| [Từ khóa 1] | _ | ↑/↓/→ | Tạo thêm video về chủ đề này / Tối ưu lại tags |
| [Từ khóa 2] | _ | _ | _ |
| ... | ... | ... | ... |

→ **Output:** "Từ khóa [X] đang mang nhiều view nhất từ search. Nên tạo thêm video cùng cluster."

---

### MODULE 5: BENCHMARKING ĐỐI THỦ (Competitive Intelligence)

**Mục tiêu:** So sánh kênh mình với đối thủ cùng ngách — ai đang thắng, ai đang thua, học gì được?

**Nguồn dữ liệu:** `browser_subagent` truy cập kênh đối thủ + thư mục `Đối_thủ/`

#### Danh sách đối thủ (kế thừa từ `trinh_sat_trend_skill.md`):

| # | Kênh | Subs | URL | Ghi chú |
|---|---|---|---|---|
| 1 | Tuấn Tiền Tỷ | ~200K | `@TuanTienTi2911` | Benchmark phong cách dân dã |
| 2 | Củ Đậu Story | ~727K | `@CuDauStory` | Phân tích sự thật |
| 3 | Tuyền Văn Hóa | ~2.34M | `@MrTVHChanelOfficial` | ⚠️ Chỉ video ≥100K views |
| 4 | CD Media | ~2M | Quét qua search_web | Chuyên nghiệp |
| 5 | Kiến Thức Thú Vị | ~1M+ | Quét qua search_web | Kiến thức tổng hợp |

#### Thu thập (cho mỗi đối thủ — 5 video gần nhất):

| Chỉ số | Cách lấy |
|---|---|
| Tần suất đăng video | Đếm số video trong 28 ngày |
| Views trung bình/video | Tính từ 5 video gần nhất |
| Tiêu đề style | Ghi nhận formula đang dùng |
| Thumbnail style | Mô tả: có mặt người? text? màu sắc? |
| Engagement (ước tính) | Likes + Comments / Views |
| Thể loại nội dung | Gom nhóm chủ đề |

#### Bảng so sánh output:

| Tiêu chí | Kênh mình | Đối thủ 1 | Đối thủ 2 | Đối thủ 3 |
|---|---|---|---|---|
| Subscribers | _ | _ | _ | _ |
| Videos/tháng | _ | _ | _ | _ |
| Views TB/video | _ | _ | _ | _ |
| CTR ước tính | _ | N/A | N/A | N/A |
| Engagement Rate | _ | _ | _ | _ |
| Thể loại mạnh nhất | _ | _ | _ | _ |
| Tiêu đề Formula | _ | _ | _ | _ |
| Thumbnail Style | _ | _ | _ | _ |

#### Phân tích Gap:

```
✅ Mình MẠNH HƠN đối thủ ở: [...]
❌ Mình YẾU HƠN đối thủ ở: [...]
🎯 CƠ HỘI: Thể loại/góc nhìn đối thủ CHƯA làm mà data cho thấy tiềm năng: [...]
⚠️ ĐE DỌA: Đối thủ đang làm tốt ở thể loại mình cũng đang làm: [...]
```

---

### MODULE 6: KHUYẾN NGHỊ CHIẾN LƯỢC (Strategic Rx)

**Mục tiêu:** Tổng hợp 5 Module trên → Đưa ra khuyến nghị cụ thể, phân loại theo mức độ ưu tiên.

#### Cấu trúc khuyến nghị:

Mỗi khuyến nghị **BẮT BUỘC** gồm 5 phần:

```markdown
### 💊 KHUYẾN NGHỊ [#]: [Tên ngắn gọn]
- **Ưu tiên:** 🚨 Khẩn cấp / ⚠️ Quan trọng / 💡 Tối ưu
- **Dựa trên data:** [Module nào? Chỉ số nào? Con số cụ thể]
- **Hành động cụ thể:** [Làm gì? Bao giờ? Ai làm?]
- **Kết quả kỳ vọng:** [Chỉ số nào sẽ cải thiện? Bao nhiêu %?]
- **Skill liên quan:** [Gọi skill nào để thực hiện?]
```

#### 7 Danh mục khuyến nghị (luôn cover đủ):

| # | Danh mục | Module nguồn | Ví dụ |
|---|---|---|---|
| 1 | **Nội dung** | Module 2 | "Tăng tỷ lệ video Kinh tế VN lên 60%, giảm Chính trị quốc tế xuống 20%" |
| 2 | **Tiêu đề** | Module 2 | "Formula F3 (FOMO) cho CTR cao nhất, ưu tiên dùng. Tránh F7 (Tổng hợp)" |
| 3 | **Thumbnail** | Module 2 | "Top 5 video đều có mặt người + text lớn. Bottom 5 không có → thêm mặt người" |
| 4 | **Lịch đăng** | Module 1+3 | "Khán giả online nhiều nhất 20h-22h T3 và T5 → đăng 19h30 T3+T5" |
| 5 | **SEO** | Module 4 | "Từ khóa 'giá xăng' đang mang 30% search traffic → tạo thêm video cluster" |
| 6 | **Khán giả** | Module 3 | "Nhóm 35-44 đang tăng → content nên mature hơn, ít meme hơn" |
| 7 | **Cảnh báo** | Tất cả | "🚨 Không đăng video 14+ ngày → thuật toán đang quên kênh" |

---

### MODULE 7: CẬP NHẬT THUẬT TOÁN & CHÍNH SÁCH (Algorithm & Policy Radar)

**Mục tiêu:** Nắm bắt sớm các thay đổi thuật toán và chính sách mới nhất của YouTube để đi trước đối thủ, tránh rủi ro tụt view, bóp tương tác hoặc dính "gậy" vi phạm (đặc biệt quan trọng với kênh địa chính trị).

**Nguồn dữ liệu:** `search_web` + `read_url_content`

#### Nguồn quét:
1. Thông báo chính thức: `Creator Insider` (YouTube channel), `YouTube Official Blog`.
2. Dư luận Creator: Reddit `r/PartneredYoutube`, `r/NewTubers`, Twitter/X `#YouTubeAlgorithm`.
3. Tìm kiếm tin tức: `"YouTube algorithm update 2026"`, `"YouTube monetization policy changes"`.

#### Thông tin thu thập:
| Hạng mục | Ví dụ |
|---|---|
| **Thuật toán đề xuất** | YouTube đang ưu tiên trọng số AVD (thời gian xem) hay CTR (tỷ lệ nhấp) hơn? Đang đẩy mạnh Shorts hay Long-form? |
| **Chính sách nội dung** | Có siết chặt từ ngữ nhạy cảm chính trị, chiến tranh không? (Rủi ro vàng tiền/tắt kiếm tiền). |
| **Tính năng mới** | Có tính năng mới nào trong Studio (như A/B test thumbnail tự động) có thể tận dụng ngay? |

#### Phân tích & Đánh giá rủi ro:
- **Tác động:** Thay đổi này có ảnh hưởng tiêu cực/tích cực đến phong cách hiện tại của kênh không?
- **Ví dụ:** "Thuật toán mới đang bóp reach các video dùng từ khóa bạo lực trong 30s đầu → Ảnh hưởng trực tiếp đến cách viết Hook của kênh."

---

## 🔍 BỘ TỪ ĐIỂN CHẨN ĐOÁN

> **Kế thừa + mở rộng từ `phan_tich_studio_skill.md` cũ.**

### BỆNH LÝ BÊN NGOÀI (Bao bì — Packaging)

**Chỉ số bắt mạch:** `CTR` + `Impressions`

| Triệu chứng | Chẩn đoán | Thuốc chữa |
|---|---|---|
| Impressions CAO + CTR < 4% | Bao bì thất bại. YouTube cho cơ hội nhưng khán giả không click. Thumbnail/Tiêu đề không hấp dẫn. | **Ngay:** Đổi tiêu đề sang biến thể Aggressive từ Gói SEO. Tăng font chữ Thumbnail cho mobile. Dùng Formula F1 hoặc F3. |
| Impressions RẤT THẤP + CTR > 8% | "Hàng ngon nhưng để trong ngõ hẻm." Chủ đề quá ngách hoặc YouTube chưa bám hành vi. | **Ngay:** Chia sẻ trên Tab Cộng đồng. Update tags + mô tả. Cross-post Facebook. Tạo Shorts từ video dài. |
| Impressions GIẢM liên tục (tuần/tuần) | YouTube đang "quên" kênh. Thường do: không đăng đều, hoặc CTR thấp nhiều video liên tiếp. | **Ngay:** Đăng video mới trong 48h. Kiểm tra lịch đăng. Tạo Community Post hàng ngày. |
| CTR TỤT so kỳ trước (>2%) | Tiêu đề/Thumbnail đang kém đi. Hoặc đối thủ đang làm tốt hơn → khán giả có lựa chọn khác. | **Ngay:** Đối chiếu Thumbnail với đối thủ (Module 5). A/B test tiêu đề. Review lại Formula đang dùng. |

### BỆNH LÝ BÊN TRONG (Kịch bản — Content)

**Chỉ số bắt mạch:** `AVD` + `Engagement Rate` + `Retention curve`

| Triệu chứng | Chẩn đoán | Thuốc chữa |
|---|---|---|
| AVD tụt thê thảm ở 30s-1min đầu | Hook lỗi. Mở đầu không đi vào trọng tâm. Mâu thuẫn giữa tiêu đề (hứa) và nội dung (thực). | **Hồ sơ:** Ghi vào Learning. Kịch bản sau dùng "Drop in Media Res". Cập nhật `kho_vu_khi/hook_test.md`. |
| Khán giả thoát hàng loạt giữa video | Chuyển ý lỏng lẻo. Thiếu bridge hook. Lỗi "Rơi tự do." | **Hồ sơ:** Bắt buộc thêm bridge hook trước mỗi chuyển cảnh. VD: "Nhưng đó chưa phải điều tồi tệ nhất..." |
| AVD tốt NHƯNG Engagement thấp | Nội dung ổn nhưng không kích thích tương tác. Thiếu câu hỏi mở, thiếu CTA. | **Ngay:** Thêm câu hỏi gây tranh cãi ở cuối. Pin comment có tính chất "mồi nhử". |
| Like/Dislike ratio < 90% | Nội dung gây phản cảm hoặc sai sự thật. Hoặc clickbait quá mức so với nội dung thực. | **Ngay:** Đọc top comments tiêu cực. Xác định điểm gây phản cảm. Điều chỉnh tone. |

### BỆNH LÝ HỆ THỐNG (Chiến lược — Strategy)

| Triệu chứng | Chẩn đoán | Thuốc chữa |
|---|---|---|
| Sub tăng nhưng Views giảm | "Sub chết" — subscriber đăng ký nhưng không quay lại xem. YouTube phạt kênh có engagement/sub ratio thấp. | **Trung hạn:** Tăng Community Post. Tạo Series để sub quay lại. Shorts để re-engage. |
| Views tăng nhưng Sub không tăng | Video viral nhưng không tạo loyalty. Nội dung "ăn liền," xem xong quên. | **Trung hạn:** Thêm branding vào video. CTA subscribe mạnh hơn. Tạo "nhân vật" nhất quán. |
| 1-2 video viral, còn lại flop | Kênh phụ thuộc "may mắn," không có baseline ổn định. Thể loại nội dung quá phân tán. | **Dài hạn:** Phân tích video viral (Module 2) → xác định "công thức chiến thắng" → lặp lại có hệ thống. |
| Đối thủ tăng nhanh hơn mình | Mất lợi thế cạnh tranh. Có thể do: tần suất thấp, tiêu đề yếu, hoặc chậm trend. | **Ngay:** Chạy Module 5 chi tiết. Xác định gap. Tăng tần suất + cải thiện bao bì. |

---

## 📝 3 OUTPUT FORMAT

### A. BÁO CÁO TỔNG KIỂM TRA (`/kham_kenh`)

```markdown
══════════════════════════════════════════════════
🏥 BÁO CÁO TỔNG KIỂM TRA KÊNH — [Tên kênh]
📅 Ngày: [DD/MM/YYYY] | Kỳ: [28 ngày / 90 ngày]
══════════════════════════════════════════════════

🫀 SỨC KHỎE TỔNG THỂ: [🟢 Khỏe / 🟡 Ổn / 🟠 Suy giảm / 🔴 Nguy hiểm]
📊 Điểm sức khỏe: [__/100]

══ MODULE 1: TỔNG QUAN ══
[Bảng số liệu + xu hướng + so kỳ trước]

══ MODULE 2: HIỆU QUẢ NỘI DUNG ══
[Top 5 Star videos + Bottom 5 Flop + Phân tích thể loại + Formula tiêu đề]

══ MODULE 3: CHÂN DUNG KHÁN GIẢ ══
[Persona + Demographics + Hành vi + Sức khỏe tệp khán giả]

══ MODULE 4: TRAFFIC & SEO ══
[Traffic mix + Top search terms + Red flags]

══ MODULE 5: BENCHMARKING ĐỐI THỦ ══
[Bảng so sánh + Gap analysis]

══ MODULE 7: THUẬT TOÁN & CHÍNH SÁCH ══
[Cập nhật thuật toán mới nhất + Đánh giá rủi ro + Tác động]

══════════════════════════════════════════════════
💊 MODULE 6: KHUYẾN NGHỊ CHIẾN LƯỢC
══════════════════════════════════════════════════

🚨 KHẨN CẤP (Làm trong 48h):
1. [Khuyến nghị + Data + Hành động]
2. [...]

⚠️ QUAN TRỌNG (Làm trong 1-2 tuần):
3. [...]
4. [...]

💡 TỐI ƯU (Làm trong 1 tháng):
5. [...]
6. [...]
7. [...]

🎯 LỆNH TIẾP THEO GỢI Ý:
→ [/tac_chien ... / /tieu_de ... / /tim_trend ...]
```

**Lưu báo cáo:** `outputs/kham_kenh/[YYYY-MM-DD]_tong_kiem_tra.md`

---

### B. BÁO CÁO KHÁM VIDEO (`/kham_video [video_id]`)

```markdown
══════════════════════════════════════════════════
🚑 BÁO CÁO KHÁM VIDEO: [Tên Video]
⏰ Mốc: [X] giờ sau đăng | 📅 [DD/MM/YYYY]
══════════════════════════════════════════════════

📊 SỐ LIỆU:
| Chỉ số | Giá trị | vs TB kênh | Đánh giá |
|---|---|---|---|
| Views | _ | ↑/↓ __% | 🟢/🟡/🔴 |
| Impressions | _ | ↑/↓ __% | 🟢/🟡/🔴 |
| CTR | _% | ↑/↓ __% | 🟢/🟡/🔴 |
| AVD | _:__ | ↑/↓ __% | 🟢/🟡/🔴 |
| Engagement | _% | ↑/↓ __% | 🟢/🟡/🔴 |

🔬 CHẨN ĐOÁN:
- Bao bì (Tiêu đề + Thumbnail): [Khỏe/Yếu] → [Chi tiết]
- Sức bền (Nội dung): [Khỏe/Yếu] → [Chi tiết]
- Tiêu đề Formula: [F__] → CTR [__]% → [Hiệu quả/Không]
- Retention: [Mô tả đường cong — tụt đâu? Giữ đâu?]

🆚 SO SÁNH VỚI TOP VIDEO:
- So [video này] vs [top video kênh]: [Giống/Khác gì?]

💊 LỆNH ĐIỀU ĐỘNG:
1. [Hành động 1 — VD: Đổi tiêu đề biến thể F3]
2. [Hành động 2 — VD: Ghi sổ hook kém vào Learning]
3. [Hành động 3 — VD: Cập nhật Kho Vũ Khí]

📝 BÀI HỌC RÚT RA:
→ Tự động cập nhật vào `kho_vu_khi/hook_test.md`
→ Tự động cập nhật vào `kho_vu_khi/noi_dau_hieu_qua.md`
```

**Lưu báo cáo:** `outputs/kham_kenh/[YYYY-MM-DD]_kham_video_[tên_video].md`

---

### C. PULSE CHECK (`/kham_nhanh`)

```markdown
⚡ PULSE CHECK — [DD/MM/YYYY HH:MM]

📊 7 NGÀY QUA:
• Views:        [X] (↑↓ Y% vs tuần trước)
• Watch Time:   [X]h (↑↓ Y%)
• Sub net:      [+/-X]
• CTR TB:       [X]%
• Impressions:  [X] (↑↓ Y%)

🔥 VIDEO NÓNG NHẤT: "[Tên]" — [X] views ([Y]% của tổng)
📉 VIDEO YẾU NHẤT:  "[Tên]" — [X] views

🚨 CẢNH BÁO: [Có/Không]
  → [Nếu có: mô tả ngắn + hành động gợi ý]

⏱️ VIDEO CUỐI CÙNG: [Tên] — đăng [X] ngày trước
  → [Nếu > 7 ngày: ⚠️ Cần đăng video mới!]

🎯 GỢI Ý: [1 hành động cụ thể nhất]
```

**Pulse Check KHÔNG lưu file** — chỉ hiển thị trực tiếp cho Sếp.

---

## 📏 QUY TẮC VẬN HÀNH

### 1. Đọc trước khi khám
- **BẮT BUỘC** đọc lịch sử kham_kenh gần nhất (nếu có) trong `outputs/kham_kenh/` trước khi chạy khám mới → để so sánh tiến triển.
- Đọc `kho_vu_khi/hook_test.md` để đối chiếu data CTR/AVD.

### 2. Data phải có số
- **KHÔNG BAO GIỜ** viết "tương đối tốt," "khá ổn" mà không kèm con số.
- Mỗi nhận định PHẢI dẫn nguồn data cụ thể: "CTR 7.4% (so benchmark 5% → vượt 48%)"

### 3. Khuyến nghị phải hành động được
- **KHÔNG** viết: "Cần cải thiện content" (quá chung chung).
- **PHẢI** viết: "Tăng tỷ lệ video Kinh tế VN từ 30% lên 60%. Cụ thể: 4 video tới, làm 3 video Kinh tế VN + 1 video Chính trị quốc tế."

### 4. Tự động cập nhật Kho Vũ Khí
- Sau mỗi lần `/kham_video`: Tự động ghi bổ sung vào `kho_vu_khi/hook_test.md` với data CTR + AVD thực tế.
- Sau mỗi lần `/kham_kenh`: Tự động ghi Top Formula hiệu quả vào note.

### 5. So sánh với lần khám trước
- Nếu có báo cáo khám kênh trước đó trong `outputs/kham_kenh/`:
  - **BẮT BUỘC** so sánh: chỉ số nào cải thiện, chỉ số nào tệ hơn
  - Đánh giá: khuyến nghị lần trước có được thực hiện không? Kết quả ra sao?

### 6. Trung thực tuyệt đối
- Nếu data xấu → NÓI THẲNG, không nịnh Sếp.
- Nếu kênh đang "chết" → nói "kênh đang chết" + giải pháp cứu, không nói "đang ổn định."
- Nếu không có đủ data (ví dụ: video chưa đủ 48h) → nói rõ hạn chế, không suy diễn.

### 7. Lưu trữ có hệ thống
- Tạo thư mục `outputs/kham_kenh/` nếu chưa có.
- `/kham_kenh` → `outputs/kham_kenh/[YYYY-MM-DD]_tong_kiem_tra.md`
- `/kham_video` → `outputs/kham_kenh/[YYYY-MM-DD]_kham_video_[slug].md`
- `/kham_nhanh` → KHÔNG lưu file (chỉ hiển thị).

---

## ⚡ SLASH COMMANDS

| Lệnh | Chức năng |
|---|---|
| `/kham_kenh` | Tổng Kiểm Tra kênh (28 ngày, 7 Module, Full report) |
| `/kham_kenh 90d` | Tổng Kiểm Tra kênh kỳ 90 ngày |
| `/kham_kenh 365d` | Tổng Kiểm Tra kênh kỳ 1 năm |
| `/kham_video [video_id hoặc tên]` | Khám chi tiết 1 video (so sánh với TB kênh) |
| `/kham_nhanh` | Pulse Check nhanh 5 phút (7 ngày, không lưu file) |

---

## 📎 THAM CHIẾU

| Tài liệu | Đường dẫn |
|---|---|
| Gói tiêu đề 13 Formula | `skills/viet_tieu_de_skill.md` |
| Pipeline sản xuất | `skills/giai_ma_360_skill.md` |
| Trinh sát trend + Đối thủ | `skills/trinh_sat_trend_skill.md` |
| Kho Vũ Khí (Hook, Ví von, Nỗi đau) | `.shared/kho_vu_khi/` |
| Hồ sơ Đối thủ | `Đối_thủ/` |
| Prompt gốc V5.1 | `prompts/nguoi_giai_ma_v1.md` |

---

> **Ghi nhớ:** Skill này là "BÁC SĨ" — không chỉ đo mạch mà phải KÊ ĐƠN THUỐC. Mỗi con số phải dẫn đến một hành động. Phân tích mà không có khuyến nghị = vô nghĩa. Khuyến nghị mà không có data = tào lao.
