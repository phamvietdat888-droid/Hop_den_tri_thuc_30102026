# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import exact_cut_94 as e

t = e.text

# 33 words to trim:
extra_cuts = [
    ("Nó không giống bất kỳ sân bóng nào bạn từng thấy. Không tường bê tông xám xịt.", "Nó không giống bất kỳ sân bóng nào bạn từng thấy: không tường bê tông xám xịt."), # -2
    ("Mọi thứ vuông vức, tinh gọn.", "Mọi thứ vuông vức, tinh gọn đến lạ."), # +2
    ("Cơ chế này đơn giản bất ngờ. Khi cẩu đặt thùng vào đúng ngàm, thợ chỉ cần vặn then xoay chín mươi độ.", "Cơ chế đơn giản bất ngờ: khi cẩu đặt thùng vào đúng ngàm, thợ chỉ cần vặn then chín mươi độ."), # -5
    ("Chuyện gì xảy ra với các sân vận động khổng lồ sau tiếng còi mãn cuộc?", "Chuyện gì xảy ra với các sân vận động sau tiếng còi mãn cuộc?"), # -2
    ("Dân bản xứ Qatar vỏn vẹn ba trăm nghìn người, giải quốc nội mỗi trận lèo tèo vài trăm khán giả.", "Dân bản xứ Qatar vỏn vẹn ba trăm nghìn người, giải quốc nội lèo tèo vài trăm khán giả."), # -3
    ("Nhưng chuyện tháo dỡ một sân bóng trên bản vẽ thì rất thơ mộng, còn đưa vào thực tế vận hành có thực sự êm xuôi như người ta tưởng tượng?", "Nhưng chuyện tháo dỡ một sân bóng trên bản vẽ rất thơ mộng, còn thực tế có êm xuôi như người ta tưởng tượng?"), # -6
    ("Thế nhưng khi bắt tay vào làm, người ta mới vấp phải rào cản khổng lồ: chi phí hậu cần và chuỗi cung ứng!", "Khi bắt tay vào làm, người ta mới vấp phải rào cản khổng lồ: chi phí hậu cần chuỗi cung ứng!"), # -5
    ("Ai sẽ là người bỏ tiền túi ra trả cho chuyến tàu đắt đỏ đó?", "Ai sẽ bỏ tiền túi trả cho chuyến tàu đắt đỏ đó?"), # -3
    ("Sân vận động 974 có thể biến mất hoàn toàn trên bản đồ Doha, trả lại bờ cát thanh bình cho sóng biển vịnh Ba Tư.", "Sân 974 có thể biến mất trên bản đồ Doha, trả lại bờ cát cho sóng biển vịnh Ba Tư."), # -6
    ("Ý kiến của bạn về vấn đề này thế nào? Hãy để lại bình luận phía dưới nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa.", "Ý kiến của bạn thế nào? Hãy để lại bình luận phía dưới nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."), # -3
    
    # 6 words to hit EXACTLY 1700:
    ("Dưới ánh đèn rực sáng, một khối kiến trúc kỳ dị sừng sững bên bờ vịnh.", "Dưới ánh đèn rực sáng, khối kiến trúc kỳ dị sừng sững bên bờ vịnh."), # -1
    ("Tiếng bước chân của bốn vạn người giẫm rậm rịch trên sàn thép dã chiến, vang lên rền rĩ.", "Tiếng bước chân của bốn vạn người giẫm rậm rịch trên sàn thép, vang lên rền rĩ."), # -2
    ("Nếu xây bằng bê tông vĩnh cửu, tám sân vận động đó sẽ thành tám chiếc máy nghiền tiền, mỗi năm ngốn hàng chục triệu đô bảo dưỡng.", "Nếu xây bằng bê tông vĩnh cửu, tám sân bóng đó thành tám cỗ máy nghiền tiền, mỗi năm ngốn hàng chục triệu đô bảo dưỡng."), # -3
    
    # Exactly 1 word:
    ("Bộ xương của sân là hệ khung thép tiền chế vững chắc, sản xuất sẵn trong xưởng chở ra hiện trường.", "Bộ khung của sân là hệ thép tiền chế vững chắc, sản xuất sẵn trong xưởng chở ra hiện trường.") # -1
]

for src, rep in extra_cuts:
    if src in t:
        t = t.replace(src, rep)
    else:
        print("EXTRA NOT FOUND:", src[:30])

w = t.split()
print("FINAL WORD COUNT:", len(w))
print("DIFF TO 1700:", len(w) - 1700)

if len(w) == 1700:
    with open("scratch/final_exact_1700_text.txt", "w", encoding="utf-8") as out:
        out.write(t)
    print("SUCCESSFULLY SAVED TO scratch/final_exact_1700_text.txt!")
