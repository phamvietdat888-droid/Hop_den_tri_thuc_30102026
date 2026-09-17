# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Nấc 1: Visual Hook (15-25 words)
nac1 = """Bỏ hàng trăm triệu đô xây sân bóng bốn vạn chỗ ngồi, đá đúng bảy trận rồi... tháo tung ra như bộ xếp hình Lego!"""

# Nấc 2: Bối cảnh tối thiểu (15-20 words)
nac2 = """Đó là sân 974 tại Qatar, công trình kỳ dị sừng sững bên bờ biển Ba Tư rực sáng ánh đèn."""

# Nấc 3: Bóc cơ chế & Bằng chứng (80-100 words)
nac3 = """Bộ khung của sân hoàn toàn không dùng một giọt hồ bê tông nào gắn xuống đất. Thay vào đó, gần một nghìn chiếc container được cẩu lên và khóa chặt bằng then xoay cơ học chín mươi độ. Cạch một cái! Khóa cứng ngắc. Bốn vạn người nhảy múa thì kết cấu vẫn trơ trơ. 

Đặc biệt, ít ai ngờ rằng hàng vạn tấn kết cấu thép siêu trường siêu trọng để dựng nên sân bóng này lại do chính bàn tay tài hoa của thợ cơ khí Việt Nam gia công chính xác từng mối hàn trước khi xuất xưởng sang Trung Đông."""

# Nấc 4: Cú Twist nhận thức (30-40 words)
nac4 = """Sân bóng này sinh ra là để chuẩn bị cho cái chết của chính mình. Xong World Cup là dỡ bỏ, xóa sổ hoàn toàn nỗi ám ảnh mang tên những con voi trắng ngốn tiền tỷ bảo dưỡng."""

# Nấc 5: Kết mở độc lập (20-30 words)
nac5 = """Liệu tư duy lắp ghép tháo rời này có thể là lối thoát cho những sân vận động nghìn tỷ đang đắp chiếu bỏ hoang ở nước mình?"""

parts = [nac1, nac2, nac3, nac4, nac5]
counts = [len(p.split()) for p in parts]
print("5-stage counts:", counts)
total_5 = sum(counts)
print("Total 5 stages words:", total_5)
