# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import finish_1700 as f

text = f.full_text

# 94 words to trim:
cuts = [
    ("Đi xem bóng đá nhưng ngỡ như lạc vào bến cảng sầm uất. Mọi tiện ích đều nhét gọn bên trong từng chiếc container tiêu chuẩn.", "Đi xem bóng đá nhưng ngỡ như lạc vào bến cảng sầm uất. Mọi tiện ích đều nhét gọn trong từng chiếc container."), # -7
    ("Sân 974 thi công đúng theo nguyên lý đó, nhưng ở quy mô khổng lồ.", "Sân 974 thi công đúng nguyên lý đó, nhưng ở quy mô khổng lồ."), # -1
    ("Khi cẩu đặt thùng vào đúng ngàm, người thợ chỉ cần vặn then xoay chín mươi độ. Cạch một cái! Chiếc then ăn sâu vào góc đúc container, khóa cứng hai khối thép thành khối vững như bàn thạch.", "Khi cẩu đặt thùng vào đúng ngàm, thợ chỉ cần vặn then xoay chín mươi độ. Cạch một cái! Chiếc then ăn sâu góc đúc container, khóa cứng hai khối thép vững như bàn thạch."), # -7
    ("Nó hoàn toàn không có máy lạnh! \n\nBí mật nằm ở vị trí sát mép nước.", "Nó hoàn toàn không có máy lạnh!\n\nBí mật nằm ở vị trí sát mép nước."), # 0
    ("Công trình còn tiết kiệm tới bốn mươi phần trăm nước sạch suốt quá trình xây dựng, thi công chưa đầy hai năm là xong.", "Công trình còn tiết kiệm tới bốn mươi phần trăm nước sạch, thi công chưa đầy hai năm là xong."), # -5
    
    # p2:
    ("Chuyện gì xảy ra với các sân vận động khổng lồ sau tiếng còi mãn cuộc?", "Chuyện gì xảy ra với các sân vận động khổng lồ sau tiếng còi mãn cuộc?"), # 0
    ("Sân Green Point ở Cape Town ngốn sáu trăm triệu đô la sau World Cup 2010 vắng bóng người, mỗi năm chính quyền cắn răng chi hàng triệu đô quét mạng nhện, cắt cỏ.", "Sân Green Point ở Cape Town ngốn sáu trăm triệu đô la sau World Cup 2010 vắng bóng người, mỗi năm chính quyền phải chi hàng triệu đô quét mạng nhện, cắt cỏ."), # -1
    ("Hay sân Arena da Amazonia ở Brazil năm 2014, ngốn hơn ba trăm triệu đô giữa rừng già, biến thành bãi đỗ xe buýt và chuồng thả gia súc. Những nhà thi đấu đổ nát ở Hy Lạp sau Olympic 2004 thành vết sẹo bê tông gặm nhấm tài chính suốt nhiều năm trời.", "Hay sân Arena da Amazonia ở Brazil năm 2014 ngốn hơn ba trăm triệu đô giữa rừng già, thành bãi đỗ xe buýt và chuồng gia súc. Các nhà thi đấu đổ nát ở Hy Lạp sau Olympic 2004 thành vết sẹo bê tông gặm nhấm tài chính suốt nhiều năm."), # -13
    ("Nếu xây bằng bê tông vĩnh cửu, tám sân vận động đó sẽ thành tám chiếc máy nghiền tiền, mỗi năm nuốt chửng hàng chục triệu đô bảo dưỡng. Người giàu thừa tiền, nhưng không ai tự trói mình vào đống nợ nần vô nghĩa.", "Nếu xây bằng bê tông vĩnh cửu, tám sân vận động đó sẽ thành tám chiếc máy nghiền tiền, mỗi năm ngốn hàng chục triệu đô bảo dưỡng. Người giàu thừa tiền, nhưng không ai tự trói mình vào đống nợ vô nghĩa."), # -5
    ("Sau khi tổ chức trọn vẹn bảy trận đấu đỉnh cao, đỉnh điểm là chiến thắng bốn một của Brazil trước Hàn Quốc đêm mùng năm tháng mười hai năm 2022, sân 974 lập tức hạ màn. Không bỏ hoang, không cỏ dại mọc um tùm. Nó hoàn thành nhiệm vụ lịch sử và sẵn sàng rời đi trong danh dự.", "Sau khi tổ chức trọn vẹn bảy trận đấu đỉnh cao, đỉnh điểm là chiến thắng bốn một của Brazil trước Hàn Quốc đêm mùng năm tháng mười hai năm 2022, sân 974 lập tức hạ màn. Không bỏ hoang, không cỏ dại. Nó hoàn thành nhiệm vụ và sẵn sàng rời đi trong danh dự."), # -6
    
    # p3:
    ("Ý tưởng ban đầu của Qatar là sau khi tháo rời, toàn bộ 974 container và ba vạn tấn thép sẽ được bốc lên tàu biển tặng lại cho một quốc gia đang phát triển ở châu Phi hoặc Nam Mỹ để ráp thành sân vận động mới, hoặc chia nhỏ làm trường học, trạm y tế. Kế hoạch nghe qua tưởng như hoàn hảo.", "Ý tưởng ban đầu của Qatar là sau khi tháo rời, toàn bộ 974 container và ba vạn tấn thép sẽ được bốc lên tàu biển tặng cho một quốc gia đang phát triển ở châu Phi hoặc Nam Mỹ để ráp thành sân mới, hoặc chia nhỏ làm trường học, trạm y tế. Kế hoạch nghe qua tưởng như hoàn hảo."), # -4
    ("Thế nhưng khi bắt tay vào làm, người ta mới vấp phải rào cản khổng lồ: chi phí hậu cần và chuỗi cung ứng! Tháo dỡ hàng vạn tấn thép, kiểm định an toàn, đóng gói rồi thuê tàu chuyên dụng chở xuyên đại dương... ngốn khoản tiền ước tính hàng chục triệu đô la.", "Thế nhưng khi bắt tay vào làm, người ta mới vấp phải rào cản khổng lồ: chi phí hậu cần và chuỗi cung ứng! Tháo dỡ hàng vạn tấn thép, kiểm định, đóng gói rồi thuê tàu chuyên dụng chở xuyên đại dương... ngốn khoản tiền ước tính hàng chục triệu đô la."), # -2
    ("Chưa hết, nước nhận viện trợ vẫn phải tự bỏ tiền giải phóng mặt bằng, đào móng, đổ trụ chịu lực và thuê kỹ sư ráp lại. Nếu không có sẵn tiền đối ứng, món quà thiện chí bỗng chốc trở thành gánh nặng tài chính mới. Vì bài toán phức tạp này, sân 974 được giữ lại tổ chức thêm một số sự kiện âm nhạc và thể thao, trước khi từng bước chuyển giao theo lộ trình phù hợp.", "Chưa hết, nước nhận viện trợ vẫn phải tự bỏ tiền giải phóng mặt bằng, đào móng, đổ trụ và thuê kỹ sư ráp lại. Nếu không có sẵn tiền đối ứng, món quà bỗng thành gánh nặng tài chính mới. Vì bài toán phức tạp này, sân 974 được giữ lại tổ chức thêm sự kiện âm nhạc và thể thao, trước khi từng bước chuyển giao theo lộ trình."), # -12
    ("Robot và máy cắt tự động gia công từng thanh thép, từng chiếc container trong nhà máy với độ chính xác đến từng mi-li-mét. Mang ra hiện trường chỉ việc bắt ốc vít và khóa then. Nhanh gọn, chính xác và sạch sẽ tuyệt đối.", "Robot và máy cắt tự động gia công từng thanh thép, từng chiếc container với độ chính xác đến từng mi-li-mét. Mang ra hiện trường chỉ việc bắt ốc vít và khóa then. Nhanh gọn, chính xác và sạch sẽ."), # -8
    ("Nhìn chuyện xứ người, chúng ta không khỏi giật mình ngẫm lại chuyện nước mình. Việt Nam có ngành cơ khí chế tạo và kết cấu thép rất phát triển, tay nghề thợ cơ khí nước mình rất khéo. Ngay tại World Cup Qatar, chính bàn tay tài ba của thợ cơ khí Việt Nam – từ các xưởng kết cấu thép lớn như Đại Dũng – đã trực tiếp gia công hàng vạn tấn cấu kiện thép siêu trường siêu trọng, gọt giũa chính xác từng mối hàn xuất khẩu sang Trung Đông dựng nên những sân vận động biểu tượng. Năng lực kỹ thuật của người thợ Việt hoàn toàn không thua kém ai.", "Nhìn chuyện xứ người, chúng ta không khỏi ngẫm lại chuyện nước mình. Việt Nam có ngành cơ khí chế tạo và kết cấu thép phát triển, tay nghề thợ cơ khí nước mình rất khéo. Ngay tại World Cup Qatar, chính bàn tay tài ba của thợ cơ khí Việt Nam – từ các xưởng kết cấu thép lớn như Đại Dũng – đã trực tiếp gia công hàng vạn tấn cấu kiện thép siêu trường siêu trọng, gọt giũa chính xác từng mối hàn xuất khẩu sang Trung Đông dựng nên những sân vận động biểu tượng. Năng lực kỹ thuật của người thợ Việt không thua kém ai."), # -8
    ("Thế nhưng ở nhiều địa phương, chúng ta vẫn thấy bóng dáng của những con voi trắng mini: những sân vận động ngốn hàng trăm, hàng nghìn tỷ đồng ngân sách chỉ để phục vụ một kỳ đại hội thể thao vài tuần lễ, rồi đóng cửa cài then suốt nhiều năm ròng cho cỏ mọc bò gặm.", "Thế nhưng ở nhiều địa phương, chúng ta vẫn thấy bóng dáng những con voi trắng mini: những sân vận động ngốn hàng trăm, hàng nghìn tỷ đồng ngân sách chỉ để phục vụ một kỳ đại hội vài tuần lễ, rồi đóng cửa cài then suốt nhiều năm cho cỏ mọc bò gặm."), # -9
    ("Nếu thay đổi tư duy, áp dụng cách làm linh hoạt như sân 974: chỉ xây quy mô vừa đủ nhu cầu thực tế, kết hợp mô-đun thép tháo rời khi cần mở rộng sự kiện lớn, ngân sách sẽ tiết kiệm được biết bao nhiêu tiền của.", "Nếu thay đổi tư duy, áp dụng cách làm linh hoạt như sân 974: chỉ xây quy mô vừa đủ nhu cầu, kết hợp mô-đun thép tháo rời khi cần mở rộng sự kiện, ngân sách sẽ tiết kiệm được biết bao nhiêu tiền của."), # -5
    
    # p_conc:
    ("Nó chứng minh rằng: Một công trình thực sự vĩ đại không nhất thiết phải trường tồn hàng trăm năm bằng bê tông cốt thép nặng nề. Vĩ đại đôi khi chỉ đơn giản là hoàn thành xuất sắc sứ mệnh của mình, mang lại niềm vui trọn vẹn cho hàng triệu con người, rồi lặng lẽ rời đi mà không để lại gánh nặng nào cho tương lai.", "Nó chứng minh rằng: Một công trình thực sự vĩ đại không nhất thiết phải trường tồn hàng trăm năm bằng bê tông cốt thép nặng nề. Vĩ đại đôi khi chỉ đơn giản là hoàn thành xuất sắc sứ mệnh của mình, mang lại niềm vui cho hàng triệu con người, rồi lặng lẽ rời đi mà không để lại gánh nặng cho tương lai."), # -3
    ("Vậy theo bạn, liệu mô hình lắp ghép tháo rời này có thể thành giải pháp cho các sân vận động nghìn tỷ đang đắp chiếu ở nước mình hay không?", "Vậy theo bạn, liệu mô hình lắp ghép tháo rời này có thể thành giải pháp cho các sân vận động nghìn tỷ đang đắp chiếu ở nước mình?"), # -3
]

for src, rep in cuts:
    if src in text:
        text = text.replace(src, rep)
    else:
        print("CUT NOT FOUND:", src[:30])

w = text.split()
print("AFTER CUTS:", len(w))
print("DIFF TO 1700:", len(w) - 1700)
