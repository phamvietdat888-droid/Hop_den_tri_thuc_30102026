import codecs
import re

try:
    with open('.shared/nhat_ky_hoc_hoi.md', 'rb') as f:
        raw_bytes = f.read()
    # Try decoding assuming utf-8, but replace errors. If it was Windows-1252 it'll just be messy text
    content = raw_bytes.decode('utf-8', errors='replace')
    
    # Check if there is mangled ENTRY 011
    idx = content.find('ENTRY #011')
    if idx != -1:
        # Let's find the last separator '---' before the corrupted ENTRY #011
        idx_dash = content.rfind('---', 0, idx)
        if idx_dash != -1:
            content = content[:idx_dash].strip()
        else:
            content = content[:idx].strip()
            
    correct_entry = """

---

## ENTRY #011 — Bài "Đại Dũng Làm Sân World Cup" phong cách CỦ ĐẬU (26/09/2026)

**File:** `outputs/2026-09-26_Dai_Dung_World_Cup_Cu_Dau/06_kich_ban_hoan_thien.md` | **Dung lượng:** 1916 từ | **Đề tài:** Năng lực doanh nghiệp Việt Nam — Thép Đại Dũng xuất khẩu.

### ✅ 3 CÂU HAY NHẤT

**1.** *"Cầm cái thước 20 phân đi đo sông Mê Kông!"*
- **Tại sao hay:** Ví von đường phố mạnh, chỉ ra sự vô lý của "ốc vít" khi so với làm sân vận động khổng lồ.
- **Nguyên lý:** NL1 (Quy đổi xuống đời thường)

**2.** *"Bảy tháng tuổi trẻ, mười ba tháng thanh xuân — đổi lấy một giấc mơ. Nghĩ mà nó xót xa."*
- **Tại sao hay:** Live Math kết hợp thời gian sống (SP5) quy đổi mức lương người thợ cơ khí với giá trị chuyến đi xem World Cup, tạo điểm thắt cảm xúc cực mạnh (đáy).
- **Nguyên lý:** SP5 (Life-Time Conversion)

**3.** *"Người làm ra giá trị thật cho đất nước thì lặng lẽ như bóng đêm. Kẻ chê bai bôi nhọ thì rực rỡ dưới ánh đèn màn hình."*
- **Tại sao hay:** Đối lập cùng câu (NL11) giữa thợ thi công và "giang cư mận" ảo trên mạng. Cực kỳ thấm.
- **Nguyên lý:** NL11 (Đối lập cùng câu)

### ❌ 3 CÂU CẦN CẢI THIỆN
**1.** *"Từ một xưởng cơ khí lụp xụp lợp tôn mỏng dính ngày xưa ở Sài Gòn..."* — Vẫn hơi dài, có thể cắt gọn thành *"Từ cái xưởng lợp tôn mỏng dính ngày xưa..."*
**2.** *"Nó y hệt như số phận của những người thợ cơ khí nhà mình."* — "Y hệt" hơi yếu. Lần sau dùng *"Khác gì..."* sẽ nghe phố hơn.
**3.** *"Cuộc kháng chiến công nghiệp này thắng hay thua chưa biết."* — Dùng từ "kháng chiến công nghiệp" hơi học thuật. Nên dùng *"Cuộc cày cuốc công nghiệp này..."*

### 🔧 KỸ THUẬT DÙNG TỐT
| Kỹ thuật | Ghi chú |
|---|---|
| **Live Math (CĐ1)** | Tính toán nhiệt độ giãn nở 3-4mm, tính thời gian làm việc để mua vé xem World Cup |
| **So sánh chéo (SP2)** | Nhân công Tây 10.000 đô vs Thợ Việt 15 củ. |
| **Gia Phả Giang Hồ (CĐ10 biến thể)** | So sánh 3 anh em ngành thép: Hòa Phát, Hoa Sen, Đại Dũng. Rất đắt giá! |

### 💎 BÀI HỌC CỐT LÕI #011
> **"Kết hợp 'Gia phả giang hồ' để hệ thống hóa ngành thép giúp bài viết có quy mô bao quát hơn hẳn. Và Live Math quy đổi thu nhập thành 'chuyến đi xem World Cup' mang lại một cú đấm cảm xúc bất ngờ, kéo người đọc từ hào nhoáng về với sự trần trụi của người lao động. Đôi khi không cần nhồi nhét quá nhiều từ lóng, chỉ cần so sánh đúng chỗ là bài viết đã cực 'đời'."**
"""
    content += correct_entry
    
    with open('.shared/nhat_ky_hoc_hoi.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(f"Error: {e}")
