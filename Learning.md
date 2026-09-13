# 📖 Learning.md — Nhật Ký Học Hỏi

> Ghi chép những bài học rút ra từ quá trình sản xuất kịch bản. Cập nhật sau mỗi Postmortem.

---

## 2026-09-09 — Câu chuyển cảnh mặc định "Ngay sau đây..." → BẮT BUỘC cho kịch bản dài ≥1000 từ (v3.5)

Sếp xác nhận lại: Câu *"Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."* KHÔNG phải câu dẫn rỗng — mà là **câu chuyển cảnh cố định** đặt SAU câu cầu nối nêu vấn đề, trước khi vào thân bài. Cấu trúc chuẩn:

```
[Hook] → [Câu cầu nối nêu vấn đề cụ thể] → "Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé." → [Thân bài]
```

**Phạm vi áp dụng:**
- ✅ Kịch bản YouTube dài ≥1000 từ: BẮT BUỘC có câu chuyển cảnh này
- ❌ Bài viết ngắn <1000 từ (Facebook, Shorts...): KHÔNG cần

**Lưu ý quan trọng:** Câu chuyển cảnh KHÔNG thay thế câu cầu nối. Câu cầu nối vẫn phải nêu CỤ THỂ vấn đề gì — câu chuyển cảnh chỉ là khớp nối cuối cùng.

### Đã cập nhật vào hệ thống:
- `GEMINI.md` §3.2b — thêm quy tắc v3.5, gỡ lệnh cấm
- `AGENTS.md` — thêm quy tắc v3.5, gỡ lệnh cấm
- `checklist.md` — tiêu chí #1b cập nhật v3.5
- `.shared/hook_formulas.md` — sửa cấu trúc + ví dụ
- `Learning.md` — ghi nhận bài học

---

## 2026-09-03 — 4 Bài học từ bài viết "Siêu Công Trình Việt Nam" (Sếp chấn chỉnh trực tiếp) ⭐ BẮT BUỘC VĨNH VIỄN

Sếp phát hiện và chấn chỉnh 4 lỗi nghiêm trọng trong quá trình viết bài giải thích dạng dài (~1200 từ). Toàn bộ bài học dưới đây BẮT BUỘC áp dụng vĩnh viễn cho mọi Agent, mọi phiên làm việc:

### Bài học 1: Mỗi phương án Hook phải có câu cầu nối RIÊNG
- **Lỗi cũ:** Viết 2 phương án Hook (nghịch lý + cảm xúc) nhưng gắn chung 1 câu cầu nối → câu nối chỉ ăn khớp Hook 2, lệch hoàn toàn so với Hook 1.
- **Quy tắc:** Khi biên soạn nhiều phương án Hook, TUYỆT ĐỐI KHÔNG viết chung câu cầu nối. Mỗi Hook phải kèm câu cầu nối "may đo" riêng, bắt rễ từ ý tứ của chính Hook đó.
- **Đã cập nhật:** `.shared/hook_formulas.md` — Quy tắc Hook #8.

### Bài học 2: CẤM "Nhưng khoan đã" và các cụm bẻ lái giật gân
- **Lỗi cũ:** Dùng "Nhưng khoan đã" trong bài viết dạng giải thích → nghe giật gân rẻ tiền, không phù hợp phong cách giải thích sâu, đàng hoàng.
- **Quy tắc:** Không dùng các cụm từ bẻ lái đột ngột kiểu YouTube drama. Dẫn dắt bằng logic tự nhiên.
- **Đã cập nhật:** `.shared/tu_cam.md` — Mục I (bảng từ cấm & thay thế).

### Bài học 3: Câu nối cuối mỗi phần phải tạo LÝ DO TÒ MÒ, không chỉ "giới thiệu phần tiếp"
- **Lỗi cũ:** Câu nối giữa các mục chỉ đóng vai "biển chỉ đường" (giới thiệu phần kế tiếp) mà không gieo sự tò mò hay mâu thuẫn nào để bắt buộc người xem đọc tiếp.
- **Quy tắc:** Câu cuối mỗi phần phải gieo 1 trong 3 thứ: (a) câu hỏi thực tế; (b) mâu thuẫn/nghịch lý; (c) lợi ích/thiệt hại cụ thể — mà người đọc chỉ tìm thấy câu trả lời ở phần sau. Nó phải là "miếng mồi" chứ không phải "biển báo".
- **Đã cập nhật:** `.shared/nhip_giu_chan_va_van_noi.md` — KT16 mới.

### Bài học 4: TUYỆT ĐỐI KHÔNG dùng ngôn ngữ khẩu hiệu / đao to búa lớn trong câu nối
- **Lỗi cũ:** Dùng các cụm từ "đanh thép", "quyền lực", "xả băng", "con rồng ngủ quên", "thỏi nam châm hút cạn dòng tiền" trong câu nối → lẫn giọng tuyên truyền vào bài viết bình dân.
- **Quy tắc:** Mọi câu nối/transition phải viết bằng ngôn ngữ quán trà đá. Test: "Mẹ mình nghe câu nối này có thấy tự nhiên không?". Nếu không → sửa ngay.
- **Đã cập nhật:** `.shared/tu_cam.md` — Mục I (bảng 11 cụm cấm + thay thế bình dân). `.shared/nhip_giu_chan_va_van_noi.md` — KT16 (quy tắc ngôn ngữ bắt buộc).

### Tóm gọn 1 câu:
> **Viết giải thích dễ gần = câu nối phải tạo tò mò thật, ngôn ngữ phải mộc mạc thật, và tuyệt đối không được lẫn giọng khẩu hiệu hay giật gân vào.**

---

## 2026-08-21 — Quy tắc "Câu Cầu Nối Nêu Vấn Đề" giữa Hook và Thân Bài (Sếp chấn chỉnh trực tiếp) ⭐ BẮT BUỘC VĨNH VIỄN

Sếp phát hiện lỗi nghiêm trọng: Hook mạnh nhưng nhảy thẳng vào thân bài KHÔNG có câu dẫn dắt → người đọc/xem bị **CỤT**, mất mạch, lướt đi. Đây là **1 trong những yếu tố mấu chốt giữ chân người xem/đọc ngay từ đầu**.

### Quy tắc (BẮT BUỘC VĨNH VIỄN — v3.4 → cập nhật v3.5):
- **SAU MỖI HOOK**, BẮT BUỘC có 1-2 câu hỏi hoặc câu khẳng định ngắn gọn **nêu rõ vấn đề cốt lõi** mà bài viết/kịch bản sắp giải đáp.
- Chức năng: (1) Người đọc biết "mình sắp được hiểu cái gì"; (2) Tạo đà dẫn dắt tự nhiên, không nhảy vọt ý.
- **Kịch bản dài ≥1000 từ:** `[Hook] → [Câu cầu nối nêu vấn đề] → "Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé." → [Thân bài]`
- **Bài viết ngắn <1000 từ:** `[Hook] → [Câu cầu nối nêu vấn đề] → [Thân bài]` (không cần câu chuyển cảnh)
- Câu chuyển cảnh KHÔNG thay thế câu cầu nối — câu cầu nối vẫn phải nêu vấn đề cụ thể.

### Ví dụ SAI (Sếp chỉ ra):
> Hook: *"Mảnh đất ấy, ông bà để lại... Giờ Chính phủ đặt lên bàn một đề xuất mới."*
> ~~*"Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."*~~ → SAI vì dùng câu chuyển cảnh MÀ KHÔNG CÓ câu cầu nối trước đó.

### Ví dụ ĐÚNG:
> Hook: *"Dân mình cày cuốc cả đời không mua nổi cái nhà..."*
> **Câu cầu nối:** *"Nhưng rốt cuộc ai đang 'đội' giá, đội bằng cách nào, và liệu có cách nào kéo nó xuống không?"*
> **Câu chuyển cảnh (nếu kịch bản ≥1000 từ):** *"Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."*
> → Thân bài bóc tách chi tiết...

### Đã cập nhật vào hệ thống:
- `.shared/hook_formulas.md` — mục riêng "Câu Cầu Nối Nêu Vấn Đề"
- `GEMINI.md` §3.2b — quy tắc trung tâm
- `AGENTS.md` — quy tắc cho mọi Agent
- `CLAUDE.md` — điểm vào cho Claude
- `checklist.md` — tiêu chí kiểm định #1b

---

## 2026-08-20 — Khả năng đặc biệt: Bóc tách vấn đề xã hội "Sâu mà dễ nuốt" ⭐ BẮT BUỘC VĨNH VIỄN

Sếp yêu cầu học cách tiếp cận vấn đề xã hội sâu sắc, đa chiều, thú vị từ kịch bản mẫu "Giang hồ mạng nhập kho — Sợ vs Tôn trọng". Đã phân tích, đúc kết thành **Module đặc biệt**: `.shared/boc_tach_van_de_xa_hoi.md`.

### 6 vũ khí tiếp cận (vận dụng LINH HOẠT tùy chủ đề, KHÔNG áp cứng):
1. **Mở bằng sự kiện → lật sang câu hỏi sâu hơn** (hỏi "tại sao" 3 lần để tìm gốc rễ)
2. **Đào vào tâm lý con người** — không phán xét, mà giải thích NHU CẦU ẩn phía dưới
3. **Tái hiện đối thoại thực** — một đoạn đối thoại sống = mười đoạn phân tích
4. **Đưa ra Framework bất ngờ** — "kim cương" của bài viết (thang bậc, quy trình ngầm, ma trận)
5. **Ví von từ lĩnh vực hoàn toàn khác** — càng xa mà vẫn map được → càng "wow"
6. **Kết bằng câu hỏi gốc rễ hoặc nghịch lý** — không giáo điều, để lại dư âm

### Quy tắc vận dụng (Sếp chấn chỉnh trực tiếp):
- **VẪN TUÂN THỦ 100%** mọi thiết lập trước đó (8 Module, 33 tiêu chí, pipeline, tone, từ cấm...)
- Module này là **vũ khí bổ sung** — KHÔNG phải công thức cứng nhắc
- Trước mỗi bài, phải **nghiên cứu kỹ chủ đề** rồi chọn vũ khí phù hợp, kết hợp sáng tạo
- Có bài chỉ cần 2-3 vũ khí. Có bài cần cả 6. **Mục tiêu là bài viết HAY — không phải tick đủ checkbox**
- **KHÔNG máy móc, KHÔNG cứng nhắc** — vận dụng sao cho bài viết thật sâu, thật thu hút, thật tự nhiên

---

## 2026-08-07 — Bài học về Tình báo Đối thủ Thực tế & Tránh Ảo tưởng Dữ liệu (Sếp chấn chỉnh trực tiếp) ⭐ BẮT BUỘC

Rút kinh nghiệm sâu sắc từ đợt trinh sát trend & tình báo đối thủ (07/08/2026). AI đã bị Sếp chấn chỉnh trực tiếp ("tào lao quá") khi đưa dữ liệu phán đoán chủ quan, sai lệch hoàn toàn so với thực tế kênh Tuấn Tiền Tỷ (`@TuanTienTi2911`). 

### 5 Quy tắc Kỷ luật Tình báo BẮT BUỘC áp dụng vĩnh viễn:

1. **TUYỆT ĐỐI KHÔNG ẢO TƯỞNG / BỊA DỮ LIỆU TÌNH BÁO:**
   - *Lỗi cũ:* Phán đoán Tuấn Tiền Tỷ "ra bài chậm, chưa động đến vụ bà Hằng" dựa trên dữ liệu web cũ. Trong khi THỰC TẾ kênh đã ra bài 13h trước với 172K views (*"Giải mã buổi livestream kỷ lục 2,1 triệu người..."*).
   - *Quy tắc mới:* Tình báo đối thủ phải đọc trực tiếp **exact channel feed 24h gần nhất** (Tiêu đề, Lượt xem, Ngày/Giờ đăng). Không được phán đoán bề nổi.

2. **DỪNG NAY VIỆC LÀM LẠI GÓC NÓNG ĐỐI THỦ ĐÃ XÀO (Né Đại Dương Đỏ):**
   - Khi đối thủ lớn (Tuấn Tiền Tỷ) đã xào góc *"Tại sao người ta donate cho tỷ phú"*, Giải Mã 360 TUYỆT ĐỐI KHÔNG làm lại câu hỏi này để tránh mang tiếng "đu đuôi" ăn thừa view.

3. **TÌM ĐIỂM TRỐNG ĐỘC BẢN (Đại Dương Xanh):**
   - Tình báo chính xác là để tìm ra **cái đối thủ CHƯA LÀM**. Tuấn Tiền Tỷ châm biếm donate, Củ Đậu Story giật tít drama. Giải Mã 360 sẽ chiếm mảng **Vén màn thị trường kim cương & bẫy ngáo giá hàng xa xỉ** — giải thích bản chất kinh tế bằng ngôn ngữ quán nước bình dân.

4. **TÔN TRỌNG THỰC TẾ & PHẢN ỨNG THỰC CHIẾN (Agile Re-strategizing):**
   - Khi phát hiện dữ liệu sai lệch, lập tức nhìn thẳng thực tế, điều chỉnh ma trận đối đầu ngay lập tục mà không được chống chế hay bào chữa.

5. **GIỮ VỮNG PERSONA "HỘP ĐEN TRI THỨC":**
   - Dù bắt trend drama nóng, nội dung của mình phải đạt chuẩn "mẹ/bà nội nghe qua hiểu liền và phục lăn" vì học được bài học quản lý tiền bạc thực chất.

---

## 2026-04-20 — Ngày thành lập hệ thống

- Hoàn thành Prompt "Người Giải Mã" V5.1 — tích hợp 17 file phân tích kênh đối thủ TTT
- Xây dựng hệ thống GiaiMa360 với cấu trúc đầy đủ
- Bài học quan trọng:
  - Câu hỏi tu từ phải có 3 CHỨC NĂNG (tò mò + nhấn mạnh + dẫn dắt), không chỉ dùng để chuyển đoạn
  - Thán từ là "hơi thở" của kịch bản — 3-5 lần/bài, rải đều
  - Phải luôn "đánh vào nỗi đau" — kéo người xem vào câu chuyện
  - Liên hệ lịch sử VN phải TỰ NHIÊN — nếu không phù hợp thì BỎ QUA
- **Bài học từ kịch bản "Luật Đất Đai & TP Đồng Nai" (20/4):** Khi không có điểm nóng quốc tế, ta hoàn toàn có thể triển khai xuất sắc phân tích "Địa chính trị nội bộ" (quy hoạch, luật pháp). Bóc tách luật khô cứng thành câu chuyện túi tiền bằng ngôn ngữ đời thường (nồi lẩu, thuốc đắng, "vặt lông gà") sẽ gây đồng cảm mạnh mẽ cho người xem bình dân.

## 2026-07-05 — 4 nguyên tắc "cuốn hút" (Sếp góp ý từ kịch bản Sân Trống Đồng) ⭐ BẮT BUỘC

Sếp chỉ ra 4 điểm yếu cốt lõi. Đã ghi thẳng vào DNA hệ thống để mọi phiên sau tự áp dụng, KHÔNG cần nhắc lại:

1. **Mạch phải LIỀN, không rời rạc** → `tone_guide.md` mục "KẾT NỐI MẠCH VĂN". Dùng liên từ–thán từ làm "chất keo", móc xích giữa các đoạn (câu cuối đoạn gieo tò mò, câu đầu đoạn sau trả lời). Kiểm bằng checklist #19b.
2. **Diệt chữ hàn lâm, ví von phải SÁT** → `tone_guide.md` mục "VĂN NÓI BÌNH DÂN". Bảng thay chữ (chủ thể→người bỏ tiền, cơ chế→cách nó chạy…). Test "mẹ mình có hiểu không". Kiểm bằng checklist #19c.
3. **Khai thác tối đa chi tiết thú vị — QUY ĐỔI mọi con số khủng** → `storytelling_arsenal.md` KỸ THUẬT 7 (Number Anchoring, 5 cách quy đổi). Con số phải làm khán giả bật "so sánh hay quá!". Kiểm bằng checklist #12b.
4. **Nêu vấn đề bất ngờ TRƯỚC, giải thích cặn kẽ SAU** → `tone_guide.md` mục "NÊU VẤN ĐỀ TRƯỚC". Ưu tiên số 1: gài nghịch lý khiến "ơ sao lại thế?" rồi mới bung giải thích tường tận, không nhảy cóc. Kiểm bằng checklist #12c.

## 2026-07-05 (bổ sung) — 5 nâng cấp + Agent 05 Hook Master (v3.3) ⭐ BẮT BUỘC

Sếp góp ý vòng 2 từ kịch bản Sân Trống Đồng. Đã cài vào hệ thống:

5. **Câu chuyển cảnh mặc định sau câu cầu nối (kịch bản ≥1000 từ)** = *"Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."* — đặt SAU câu cầu nối nêu vấn đề, TRƯỚC thân bài. → `.shared/hook_formulas.md`. **(v3.5: chính thức hóa làm quy tắc bắt buộc cho kịch bản dài ≥1000 từ)**
6. **Agent 05 Hook Master** — agent chuyên trị Hook, quy trình 5 bước (mổ tư tưởng → định vị điểm chạm nỗi đau/xu hướng/mâu thuẫn → bóc lớp 1-2-3 → viết 3-5 phương án chấm điểm 5 thước đo → mài câu đầu ≤15 từ + open loop). File: `.agent/agents/05_Hook_Master.md`. Chèn vào pipeline Bước 3.5.
7. **Dồn chi tiết đắt lên NỬA ĐẦU** (chống rơi rụng 1/3 đầu) → `storytelling_arsenal.md` KT8. Checklist #12d.
8. **CTA sau CAO TRÀO** — kêu gọi like/share/đăng ký chèn khéo ngay sau chi tiết ấn tượng, gắn vào cảm xúc vừa tạo, không van nài → `tone_guide.md`. Checklist #12f.
9. **Đào tới BẢN CHẤT + liên hệ sự kiện thế giới** (hỏi "vì sao" tới gốc, mỗi tầng kèm ví von; dẫn case nước ngoài đã kiểm chứng khi làm bài sâu hơn) → `storytelling_arsenal.md` KT9. Checklist #12e.
10. **CHỈ GIAO `.docx`** ở mọi công đoạn; `.md` chỉ là nháp nội bộ trong `scratch/` → GEMINI.md §8.1b + CLAUDE.md.

## 2026-04-21 — Tối ưu hóa quy trình sản xuất (Protocol 2.5)

Rút kinh nghiệm từ chiến dịch "Binh pháp đêm 21/04", hệ thống chính thức áp dụng 5 trụ cột tối ưu:
1. **Chiến thuật 5 Angle Độc Bản (Tiền Tác Chiến):** Bắt buộc phải trình Sếp 5 góc nhìn (Kinh tế, Binh pháp, Lịch sử, Âm mưu, Phản biện) trước khi làm dàn ý. Không làm tắt.
2. **Tổ chức Quân Doanh (Workspace):** Mỗi tập video bắt buộc lưu trong một thư mục riêng biệt định dạng `outputs/YYYY-MM-DD_Ten_Chu_De/` và phải chia làm 2 thư mục con: `YouTube` và `Facebook`.
3. **Định dạng thư mục YouTube:** Gồm các file bắt buộc: (1) `06_script_final.md`; (2) `06_script_final.docx` (Tích hợp cả kịch bản và 20 tiêu đề ở cuối); (3) `06b_tieu_de.md`; (4) `thumbnail.jpg` (ảnh minh họa).
4. **Định dạng thư mục Facebook:** Gồm các file bắt buộc: (1) `06d_fb_post.md`; (2) `06d_fb_post.docx` (Tích hợp nội dung bài viết và 20 tiêu đề gợi ý ở cuối như file kịch bản Youtube); (3) `06b_tieu_de.md` (20 tiêu đề cho bài Face); (4) `06e_fb_seeding.md` (file seeding/bình luận); (5) `thumbnail.jpg`.
5. **Cơ chế Dự phòng Đồ họa:** Nếu AI tạo ảnh thất bại/sập server (lỗi 503) hoặc tải ảnh lỗi, KHÔNG tự ý tải ảnh linh tinh. Bắt buộc phải tạo một file text chứa Promt tạo ảnh cực kỳ chi tiết (ví dụ: `06c_image_prompt.md`) đặt vào thư mục và báo cáo lại ngay cho Sếp để Sếp tự tạo.

## 2026-04-22 — Bài học từ kịch bản "Trump & 5 Tháng Lịch Sử"

Sếp đã rút kinh nghiệm trực tiếp trong quá trình sản xuất. Toàn bộ bài học dưới đây **BẮT BUỘC** áp dụng cho mọi phiên sau:

### A. Hành văn — Mượt mà, Hài hước mà Sâu sắc
> **Triết lý của Sếp:** Kịch bản phải mượt mà, hài hước mà sâu sắc, thú vị, lôi cuốn. AI phải không ngừng học hỏi để hoàn thiện văn phong theo hướng này.

1. **Trị bệnh lạm dụng tiểu từ "nhá":**
   - KHÔNG gắn "nhá" vào mọi câu. Tối đa **2-3 lần/kịch bản**, phải đặt đúng ngữ cảnh (nhấn mạnh, dặn dò).
   - Ở câu CTA (kêu gọi hành động) → dùng **"nhé"** thay "nhá" (nhẹ nhàng, lịch sự hơn).
   - Ở câu hỏi tu từ, câu chuyển ý → **BỎ HẲN** tiểu từ nếu không cần thiết.
   - ❌ *"Công bằng mà nói nhá,"* → ✅ *"Công bằng mà nói,"*
   - ❌ *"Thử nghĩ xem nhá:"* → ✅ *"Thử nghĩ xem:"*
   - ❌ *"Rồi bây giờ nhá,"* → ✅ *"Rồi bây giờ,"*

2. **Chống lạm dụng dấu gạch ngang (—) để nối ý:**
   - Dấu gạch ngang chỉ dùng khi tạo **ngắt nhịp kịch tính** hoặc **chèn thông tin phụ**.
   - KHÔNG dùng thay từ nối. Hãy dùng **từ nối tự nhiên** (chỉ, mà, rồi, thì).
   - ❌ *"giao cho tôi — 5 tháng là xong"* → ✅ *"giao cho tôi chỉ 5 tháng là xong"*

3. **Xóa cụm từ lệch tone, không ăn khớp:**
   - Khi viết châm biếm, câu cảm thán phải **khớp giọng** với ngữ cảnh. Nếu đoạn trước đang phân tích nghiêm túc → câu châm biếm phải tinh tế, KHÔNG suồng sã.
   - ❌ *"Nghe oai lắm. Đến chịu luôn."* → ✅ *"Nghe oai lắm."* (bỏ câu thừa, để giọng sắc hơn)

4. **Linh hoạt dùng liệt kê khi cần MẠCH LẠC:**
   - Quy tắc "CẤM liệt kê" trong `tu_cam.md` KHÔNG phải tuyệt đối. Khi đoạn văn cần trình bày **nhiều ý rõ ràng** (3 vấn đề, 3 lý do...) → PHẢI dùng cấu trúc liệt kê tự nhiên.
   - ❌ *"Ông Trump đang gặp 3 vấn đề. Tỷ lệ ủng hộ giảm. Phe bảo thủ chia rẽ. Và ông ấy cần chiến tích."*
   - ✅ *"Ông Trump đang gặp 3 vấn đề cùng lúc. Vấn đề đầu tiên đó là tỷ lệ ủng hộ giảm. Vấn đề thứ 2, phe bảo thủ chia rẽ. Và vấn đề thứ 3 là ông ấy cần chiến tích."*

5. **Câu chuyển ý phải có LỰC và SANG:**
   - Câu mời gọi người xem phải đẳng cấp, thể hiện vị thế "người am hiểu mời khách", không phải ra lệnh.
   - ❌ *"Pha ấm trà đi, rồi mình nói chuyện kỹ."*
   - ✅ *"Nào, pha ấm trà thôi, rồi mời các bác cùng bàn luận."*

### B. Quy trình Xuất Bản — Format chuyên nghiệp
6. **File Word (.docx) BẮT BUỘC sinh tự động:** Markdown cho AI, Word cho con người. Không cần Sếp nhắc.
7. **Quy chuẩn format Word (dành cho Đạo diễn/Biên tập viên):**
   - Font: **Times New Roman**, cỡ **14**
   - Khổ giấy: **A4**, lề đều **2cm** (trên, dưới, trái, phải)
   - Căn đều 2 bên (**Justify**), giãn dòng **1.25**
8. **Mã hóa giọng điệu bằng màu sắc trong file Word:**
   - 🔴 **Đỏ (CC0000):** Nhấn mạnh cực độ, bức xúc, sự thật sốc
   - 🟢 **Xanh lá (008000):** Dữ liệu, con số, năm tháng khách quan
   - 🔵 **Xanh dương (0066CC):** Mỉa mai, châm biếm, trào phúng
   - 🟠 **Cam (E65000):** Câu hỏi, tò mò, gợi mở
   - **In đậm:** Punch words — nhấn âm
   - *In nghiêng:* Đọc chậm, rải nhịp, tạo khoảng lặng
   - <u>Gạch chân:</u> Chốt hạ, ngắt nhịp dứt khoát

---

## 2026-05-23 — Tối ưu token v3.1

Sau audit toàn diện dự án v3.0 (38 skills), thực hiện 7 quick win KHÔNG đụng 8 Module/Anti-AI/33 tiêu chí:

**Hành động thực thi:**
1. **Move `agent-evaluation`** (943 lines, ~10.5k token) → `.agent/skills/community/_lazy/` + thêm pattern vào `.antigravityignore` để không index ngầm. Invoke explicit qua `/kiem_dinh` deep mode.
2. **Slim `.shared/to_mo_loi_ich_module.md` §5 Mental Models** (72→40 lines, -44%) — gom chi tiết 5 model về skill `marketing-psychology` duy nhất, file `.shared/` chỉ giữ tên + quy tắc dùng.
3. **Compact GEMINI.md §6 CẤU TRÚC** (138→30 lines) — convert text list thành tree compact, tách full paths sang `docs/structure_reference.md` (lazy companion).
4. **Compact GEMINI.md §10 Community Skills** (~135→60 lines) — gom Phase 3 Tier B thành 1 dòng, tách ví dụ prompt + flow chi tiết sang `docs/gemini_companion.md` (lazy companion).
5. **Tạo `.agent/metrics/skill_usage.md`** — template log skill trigger frequency mỗi video, quy trình 3-video review để move skill noise sang `_lazy/`.
6. **Bump GEMINI.md v3.0 → v3.1** + cập nhật Agent 03 reference path `_lazy/` cho `agent-evaluation`.

**Kết quả đo được:**
- GEMINI.md: 515 → 279 lines (-46% size, -13.4KB) → mỗi session tiết kiệm ~5-8k token always-loaded
- to_mo_loi_ich_module.md: 72 → 40 lines (-44%)
- Tổng token tiết kiệm/session: ~25k (15-20% context window)
- 0 thay đổi pipeline production. 8 Module + Anti-AI 3 tầng + 33 tiêu chí + Persona "Người Giải Mã" GIỮ NGUYÊN.

**Bài học:**
- **Lazy companion pattern**: file chi tiết tách ra `docs/*.md`, GEMINI.md chỉ giữ ref. Antigravity semantic match vẫn tìm thấy khi cần, me không tốn token always-load.
- **`.antigravityignore` + `_lazy/`**: skill nặng (>500 lines) NÊN move sang `_lazy/` + ignore pattern thay vì xóa — giữ nguyên capability, chỉ giảm cost index.
- **3-video review rule**: skill không trigger sau 3 video → downgrade tier hoặc move lazy. `.agent/metrics/skill_usage.md` track tự động.
- **Centralize duplication**: mental models (Loss Aversion, ...) đã trùng 200 lines giữa `to_mo_loi_ich_module.md` ↔ `marketing-psychology` → gom về 1 source, file kia chỉ giữ tên + ref.
9. **Chú giải bảng màu:** Đặt ngay ĐẦU FILE Word, ngay sau tiêu đề, trước nội dung kịch bản.
10. **Chèn tiêu đề A/B Test lên đầu kịch bản:** Đưa thẳng 2 phương án tiêu đề chính lên chóp file kịch bản để Đạo diễn duyệt ngay, không cần mở file SEO riêng.

### C. Kỷ luật Xuất bản (Fanpage & Đồ họa)
11. **TUYỆT ĐỐI KHÔNG QUÊN MEGA COMMENTS:** Khi phát sóng bài Facebook (Bước 6d), bắt buộc phải sinh luôn file `06e_mega_comments.json` chứa các bình luận mồi (seeding) và 2 CTA. Đừng đợi Sếp nhắc "thế file comment đâu em?".
12. **Ảnh Thumbnail YouTube PHẢI LÀ 16:9:** Kích thước cho ảnh thumbnail kênh YouTube mặc định là tỷ lệ 16:9 (1280x720). Đừng nhầm lẫn với tỷ lệ 1.91:1 (1200x630) của ảnh bài đăng Facebook. Phải tự động tạo và lưu vào đúng thư mục `YouTube/thumbnail.png`.

---

## 2026-07-30 — Quy chuẩn Trinh Sát Trend Đa Nguồn Chi Tiết 100% (v3.4 - Sếp duyệt) ⭐ BẮT BUỘC

Khi thực hiện Bước 0 (`/tim_trend`), hệ thống **TUYỆT ĐỐI KHÔNG** được chỉ liệt kê chung chung tên nguồn mà **BẮT BUỘC PHẢI DẪN BẰNG CHỨNG DỮ LIỆU CỤ THỂ 100%** từ 7 kênh thông tin sau:


1. **Google Trends VN:** Dẫn từ khóa tìm kiếm nóng + % tăng trưởng lượt tìm kiếm thực tế.
2. **Báo chí chính thống VN & Quốc tế:** Dẫn cụ thể tên bài báo, tiêu đề, mã bài, ngày đăng, nội dung cốt lõi từ *24h.com.vn, Dân Trí, VietNamNet, VnExpress, Reuters, AP, Fox News*.
3. **Mạng xã hội & Cộng đồng (Threads, Facebook, Reddit, X):** Dẫn cụ thể nội dung bài đăng hot, luồng tranh luận 2 chiều, số lượng tương tác (likes/comments), trào lưu thảo luận.
4. **YouTube Đối thủ:** Bóc tách chính xác video mới nhất vừa đăng của *CD Media (Why?), Kiến Thức Thú Vị, Tuấn Tiền Tỷ, Củ Đậu Story, Spiderum* (Tiêu đề, lượt xem, ngày đăng, góc nhìn họ làm, và lỗ hổng/cơ hội cho Giải Mã 360).
5. **Hot trend TikTok & Facebook Reels (Short-form):** Dẫn cụ thể trào lưu short-form video hot (Hashtag, lượt xem tổng, dạng clip viral POV/map 3D/audio).
6. **Sổ trí nhớ kênh (`so_tri_nho_kenh.md`):** Dẫn cụ thể ngày đăng, tiêu đề video cũ, luận điểm chốt để nối mạch "Vòng về video cũ" (Loopback).
7. **News Sentiment Engine:** Phân tích chỉ số cảm xúc cộng đồng (% Tò mò/Lo lắng, Tranh luận, Tự hào/Tri ân).

---

## 2026-09-12 — 5 Bài học từ bài viết "Vị thế Việt Nam tại châu Âu" (Sếp chấn chỉnh trực tiếp) ⭐ BẮT BUỘC VĨNH VIỄN

Sếp phát hiện và chấn chỉnh 5 lỗi liên tiếp trong quá trình viết bài ngắn ~200 từ về chuyến công du châu Âu của Tổng Bí thư Tô Lâm. Toàn bộ bài học dưới đây BẮT BUỘC áp dụng vĩnh viễn:

### Bài học 1: Bài viết PHẢI neo chặt vào bối cảnh sự kiện cụ thể ngay từ đầu
- **Lỗi cũ:** Viết chung chung "châu Âu", "phương Tây" mà không nêu rõ ai, ở đâu, ngày nào, sự kiện gì → người đọc không biết đang nói chuyện gì.
- **Quy tắc:** Mọi bài viết phải xác định rõ **bối cảnh sự kiện cụ thể** (tên người, địa danh, thời gian, diễn biến) để người đọc hình dung được ngay.

### Bài học 2: Bối cảnh phải đặt ngay sau Hook — đúng vị trí, đúng chức năng
- **Lỗi cũ:** Bối cảnh sự kiện bị nhét vào phụ chú cuối bài hoặc trộn lẫn trong thân bài → người đọc phải đọc xong mới hiểu đang nói về chuyện gì.
- **Quy tắc:** Cấu trúc bắt buộc cho bài viết ngắn có bối cảnh thời sự: `[Hook cảm xúc] → [Câu cầu nối] → [ĐOẠN BỐI CẢNH: dữ kiện cứng — ngày, nơi, sự kiện, kết quả] → [Thân bài: đối chiếu/bóc tách ý nghĩa] → [Chốt + CTA]`.

### Bài học 3: Hook, bối cảnh, thân bài — mỗi tầng mang MỘT loại thông tin riêng biệt, TUYỆT ĐỐI KHÔNG đạp lên nhau
- **Lỗi cũ:** Hook nhắc "Paris, Macron, kỵ binh bồng gươm" → bối cảnh lại nhắc lại "Điện Invalides, Macron, lễ đón" → trùng lặp ý dù khác câu chữ.
- **Quy tắc (đặc biệt quan trọng với bài ngắn ~200 từ):**
  - **Hook** = cú đấm cảm xúc thuần túy, CHỈ gợi hình ảnh nghịch lý (không nhắc tên riêng, địa danh cụ thể)
  - **Bối cảnh** = dữ kiện cứng 100% (ngày tháng, tên người, địa điểm, kết quả ngoại giao cụ thể)
  - **Thân bài** = đối chiếu lịch sử + bóc tách ý nghĩa (không lặp lại bất kỳ thông tin nào đã nêu ở 2 tầng trên)
- Bài ~200 từ rất ít dung lượng, **mỗi câu phải mang thông tin mới**, lặp ý là lãng phí chết.

### Bài học 4: Cực kỳ cẩn thận khi nhắc đến lãnh tụ, lãnh đạo — KHÔNG dùng chi tiết dễ bị hiểu sai là hạ thấp
- **Lỗi cũ:** Viết "Bác Hồ ngày xưa đến Paris chỉ là anh phụ bếp gầy gò, không ai thèm nhìn" → dù đặt trong ngữ cảnh đối chiếu tích cực, vẫn có thể bị hiểu sai là hạ thấp hình ảnh lãnh tụ.
- **Quy tắc:** Khi cần đối chiếu lịch sử thuộc địa, nói CHUNG về **"ông cha mình", "người Việt ngày xưa"** thay vì gán trực tiếp chi tiết nhạy cảm cho cá nhân lãnh tụ cụ thể. Ví dụ thay thế: *"Ngày xưa ông cha mình sang đất Pháp chỉ với thân phận phu khuân vác, bồi bàn, đi đâu cũng cúi mặt."*

### Bài học 5: Rà soát chính sách nền tảng YouTube TRƯỚC KHI xuất bản — CẤM từ miệt thị sắc tộc và ngôn từ bạo lực dù trong ngữ cảnh lịch sử
- **Lỗi cũ:** Dùng từ "mọi" (miệt thị sắc tộc), "hạng bét" (phân biệt đối xử), "đè đầu cưỡi cổ" (bạo lực) → YouTube có thể flag là hate speech dù đặt trong ngữ cảnh lịch sử.
- **Quy tắc:** TUYỆT ĐỐI KHÔNG dùng từ miệt thị trực tiếp. Diễn đạt gián tiếp vẫn truyền tải đủ ý mà an toàn:
  - ~~"gọi mình là mọi, dân bản xứ hạng bét"~~ → *"không thèm ngó tới mình, coi dân ta chẳng ra gì"*
  - ~~"đè đầu cưỡi cổ"~~ → *"từng bị coi thường"*
- **Nguyên tắc chung:** Nếu một từ/cụm từ khi tách ra khỏi ngữ cảnh vẫn có thể bị coi là hate speech → KHÔNG DÙNG, tìm cách nói khác.

### Đã cập nhật vào hệ thống:
- `Learning.md` — ghi nhận 5 bài học (mục này)
- `.shared/compliance_shield.md` — bổ sung quy tắc YouTube-safe language + nhạy cảm lãnh tụ

