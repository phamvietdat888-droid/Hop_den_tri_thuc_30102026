import codecs

entry = """
## ENTRY #011 — Bài "Mua được tàu, đã tự sửa được tàu chưa?" phong cách CỦ ĐẬU (26/09/2026)

**File:** `outputs/2026-09-26_Vinspeed_Chuyen_Giao_Cu_Dau/06_kich_ban_hoan_thien.md` | **Dung lượng:** ~1900 từ | **Đề tài:** Chuyển giao công nghệ / Lòng tự hào dân tộc

### ✅ 3 CÂU HAY NHẤT

**1.** *"Cầm cái thước 20 phân đi đo sông Mê Kông thì làm sao mà hiểu được đại cục. Anh em cầm định kiến của 10 năm trước để đo lường năng lực của Vinspeed ngày hôm nay, đó là một sai lầm."*
- **Tại sao hay:** Sử dụng ví von đường phố (NL1) cực đắt để giải thích sự thiển cận của cư dân mạng, đồng thời kết nối quá khứ với hiện tại.

**2.** *"Tiếng búa gõ leng keng vọng khắp xưởng, mùi mồ hôi chua loét của thợ máy Việt hòa lẫn mùi dầu mỡ. Kỹ sư Việt cầm cái cờ lê, soi đèn pin vào gầm tàu, tự tay thay thế từng má phanh, từng con ốc vít."*
- **Tại sao hay:** Sensory Anchor (KT13b) miêu tả sống động không khí làm việc vất vả, thực tế, trái ngược hoàn toàn với những thuyết âm mưu trên mạng.

**3.** *"Người làm ra giá trị thật cho đất nước thì lặng lẽ như bóng đêm. Kẻ chỉ trích giá trị thì rực rỡ dưới ánh đèn bàn phím."*
- **Tại sao hay:** Đối lập cùng câu (NL11) sắc bén, chốt thẳng vào tâm lý thích phán xét của mạng xã hội, tạo điểm nhấn sâu sắc cuối bài.

### ❌ 3 CÂU CẦN CẢI THIỆN
(Không có lỗi nổi bật, đã tuân thủ nghiêm ngặt các rút kinh nghiệm từ ENTRY #003 và ENTRY #005).

### 🔧 KỸ THUẬT DÙNG TỐT
- **Live Math (CĐ1):** Tính toán chi phí bảo trì mỗi năm bay 3 tỷ USD (75.000 tỷ đồng) tương đương 400.000 người làm việc cả năm không ăn không tiêu.
- **Nghịch lý xoáy (SP3):** Tại sao Hàn, Nhật đi mua công nghệ được khen, còn Việt Nam bị chê bai.
- **Quy đổi thời gian sống (SP5):** Quy đổi tiền bảo trì tàu sang số năm tuổi thanh xuân của công nhân phải đổ mồ hôi.

### 🆕 THU HOẠCH TỪ/CỤM MỚI
| Từ/cụm | Ngữ cảnh | Kho |
|---|---|---|
| *"máy hút máu thế kỷ"* | Ám chỉ công trình tỷ đô nếu phải phụ thuộc ngoại bang bảo trì | A (Ví von) |
| *"cầm cái thước 20 phân đi đo sông Mê Kông"* | Đánh giá sai quy mô bằng định kiến nhỏ hẹp | A (Ví von) |
| *"rực rỡ dưới ánh đèn bàn phím"* | Chỉ trích những anh hùng bàn phím | C (Mỉa mai) |

### 💎 BÀI HỌC CỐT LÕI #011
> **"Viết bài ca ngợi doanh nghiệp trong nước rất dễ sa vào quảng cáo. Nhưng bằng cách sử dụng phép toán 'Live Math' tàn khốc về chi phí bảo trì và 'Sensory Anchor' về mồ hôi dầu mỡ của kỹ sư, bài viết không cần sáo rỗng khen ngợi mà người đọc tự cảm nhận được sự vĩ đại và khát vọng tự cường của Vinspeed."**
"""

with codecs.open(r"d:\Antigravity+Codex\Hop_Den_Tri_Thuc\.shared\nhat_ky_hoc_hoi.md", "a", "utf-8") as f:
    f.write(entry)
