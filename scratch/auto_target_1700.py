# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

hook = """Bỏ ra hàng trăm triệu đô xây một sân vận động World Cup bốn vạn chỗ ngồi, tổ chức vỏn vẹn bảy trận bóng đá rồi... tháo tung ra từng mảnh như bộ xếp hình Lego! Nghe qua tưởng như chuyện đùa của những tỷ phú dầu mỏ thừa tiền. Nhưng điều đáng kinh ngạc hơn cả: đằng sau công trình kỳ dị khiến cả thế giới ngả mũ ấy, lại in đậm dấu ấn từ bàn tay tài ba của những người thợ cơ khí Việt Nam – những con người đã gọt giũa từng khối thép chính xác đến từng mi-li-mét để chịu được sức giẫm của bốn vạn cổ động viên!"""

bridge = """Vì sao Qatar lại tạo ra một sân bóng có thể tháo rời hoàn toàn như vậy, và bí mật cơ khí nào giúp những khối thép do thợ Việt gia công cùng gần một nghìn chiếc container ghép thành một sân vận động an toàn tuyệt đối?"""

scene_shift = """Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."""

# Target p0: ~125 words
p0 = """Bạn thử nhắm mắt lại và hình dung khoảnh khắc này. Đêm Doha cuối năm 2022, gió từ vịnh Ba Tư thổi vào mát rượi, mang theo vị mặn của biển hòa lẫn mùi sơn mới trên vách thép. Dưới ánh đèn rực sáng, một khối kiến trúc kỳ dị sừng sững hiện ra bên bờ vịnh. 

Nó không giống bất kỳ sân bóng nào bạn từng thấy. Không tường bê tông xám xịt. Thay vào đó là gần một nghìn chiếc container đủ màu sắc, xếp chồng ngay ngắn giữa hệ khung thép đồ sộ. 

Tiếng bước chân của bốn vạn cổ động viên giẫm rậm rịch trên sàn thép dã chiến, vang lên rền rĩ. 

Lạ lùng đến khó tin. 

Tại sao Qatar lại gom thùng chở hàng về làm sân bóng? Làm cách nào tháo rời một công trình nặng hàng vạn tấn mà không cần đập phá?"""

# Target p1: ~380 words
p1 = """Để hiểu điều kỳ diệu này, trước hết hãy nhìn sân 974 dưới góc nhìn của một khán giả bình thường. 

Bước qua cổng an ninh, cảm giác đầu tiên là ngỡ ngàng. Đi xem bóng đá nhưng ngỡ như lạc vào bến cảng sầm uất. Mọi tiện ích thiết yếu đều nhét gọn bên trong từng chiếc container tiêu chuẩn. 

Màu sắc từng chiếc thùng là hệ thống chỉ dẫn thông minh: thùng vàng bán bánh mì và nước ngọt, thùng xanh dương là nhà vệ sinh sạch bóng, thùng xanh lá là trạm sơ cứu. Còn thùng bạc sang trọng phía dưới khán đài là phòng thay đồ của các siêu sao thế giới như Messi hay Neymar. Mọi thứ đều vuông vức, tinh gọn. 

Thế nhưng, điều khiến giới kỹ sư thán phục nằm ở cách liên kết những chiếc thùng này lại với nhau. Bạn từng chơi xếp hình Lego chưa? Sân 974 thi công chính xác theo nguyên lý đó, nhưng ở quy mô khổng lồ. 

Bộ xương của sân là hệ khung thép tiền chế vững chắc, sản xuất sẵn trong xưởng rồi chở ra hiện trường. Khi lắp ráp, kỹ sư không dùng một giọt hồ bê tông nào gắn chết công trình xuống đất. Toàn bộ 974 chiếc container được cẩu lên, rồi khóa chặt vào khung thép bằng then xoay cơ học chuẩn hàng hải, gọi là khóa twist-lock. 

Cơ chế này đơn giản bất ngờ. Khi cẩu đặt thùng hàng vào đúng ngàm thép, người thợ chỉ cần vặn then xoay chín mươi độ. Cạch một cái! Chiếc then ăn sâu vào góc đúc container, khóa cứng hai khối thép thành khối vững như bàn thạch. Bốn vạn người nhảy múa ăn mừng bàn thắng thì kết cấu bên dưới vẫn trơ trơ, không hề rung lắc. 

Và đây mới là phép tính sống khiến nhiều người giật mình. Qatar là sa mạc nắng cháy, ngoài trời có thể vượt năm mươi độ C. Tất cả sân khác đều phải lắp điều hòa ngốn hàng trăm triệu đô tiền điện để làm mát từng ghế ngồi. Riêng sân 974 thì không. 

Nó hoàn toàn không có máy lạnh! 

Bí mật nằm ở vị trí sát mép nước. Nhờ kết cấu hở với những khoảng trống đan xen, sân 974 giống chiếc bẫy gió khổng lồ. Gió biển thổi lồng lộng qua khe thoáng, làm mát tự nhiên toàn bộ khán đài mà không tốn một xu tiền điện. Công trình còn tiết kiệm tới bốn mươi phần trăm lượng nước sạch suốt quá trình xây dựng, thi công chưa đầy hai năm là xong tinh tươm. 

Xây nhanh, dùng sướng, lại cực kỳ tiết kiệm."""

# Target p2: ~355 words
p2 = """Nhưng giá trị sâu xa nhất của 974 nằm ở việc đập tan nỗi ám ảnh kinh hoàng: nỗi ám ảnh mang tên những con voi trắng. 

Chuyện gì sẽ xảy ra với các sân vận động khổng lồ sau khi tiếng còi mãn cuộc vang lên? 

Thực tế trần trụi đau đớn hơn rất nhiều so với những màn pháo hoa đêm bế mạc. Hãy nhìn Nam Phi sau World Cup 2010. Sân Green Point ở Cape Town ngốn sáu trăm triệu đô la, nhưng giải vừa dứt thì khán giả biến mất. Mỗi năm chính quyền phải chi hàng triệu đô ngân sách chỉ để quét mạng nhện, cắt cỏ và sơn lại những mảng tường mốc meo. 

Hay sân Arena da Amazonia ở Brazil năm 2014, ngốn hơn ba trăm triệu đô nằm giữa rừng già. Không có đội bóng lớn nào kéo nổi khán giả tới sân. Khối bê tông nghìn tỷ nằm phơi nắng phơi sương, biến thành bãi đỗ xe buýt và chuồng thả gia súc. Đau xót hơn nữa là những nhà thi đấu đổ nát ở Hy Lạp sau Olympic Athens 2004, trở thành vết sẹo bê tông gặm nhấm nền tài chính suốt nhiều năm trời. 

Người ta gọi những công trình nghìn tỷ vô dụng đó là những con voi trắng. Nuôi tốn mà chẳng để làm gì. 

Và các nhà lãnh đạo Qatar hiểu quá rõ điều đó. Dân bản xứ Qatar vỏn vẹn ba trăm nghìn người. Giải bóng đá quốc nội mỗi trận lèo tèo vài trăm khán giả. Họ cần làm gì với tám sân vận động từ bốn vạn đến tám vạn chỗ sau giải đấu? 

Nếu xây toàn bộ bằng bê tông vĩnh cửu, tám sân vận động đó sẽ thành tám chiếc máy nghiền tiền khổng lồ, mỗi năm nuốt chửng hàng chục triệu đô bảo dưỡng. Người giàu thừa tiền, nhưng không ai dại dột tự trói mình vào đống nợ nần vô nghĩa. 

Đó là lý do sân 974 ra đời: Nó sinh ra để chuẩn bị cho cái chết của chính mình. 

Một công trình dùng một lần đúng nghĩa! 

Sau khi tổ chức trọn vẹn bảy trận đấu đỉnh cao, đỉnh điểm là chiến thắng bốn một của Brazil trước Hàn Quốc đêm mùng năm tháng mười hai năm 2022, sân 974 lập tức hạ màn. Không bỏ hoang mốc meo, không cỏ dại mọc um tùm. Nó hoàn thành nhiệm vụ lịch sử và sẵn sàng rời đi trong danh dự."""

# Target p3: ~500 words
p3 = """Nhưng chuyện tháo dỡ một sân bóng trên bản vẽ thì rất thơ mộng, còn đưa vào thực tế vận hành có thực sự êm xuôi như người ta tưởng tượng? 

Câu trả lời là không hề đơn giản. 

Ý tưởng ban đầu của Qatar là sau khi tháo rời, toàn bộ 974 chiếc container và ba vạn tấn thép sẽ được bốc lên tàu biển tặng lại cho một quốc gia đang phát triển ở châu Phi hoặc Nam Mỹ để ráp thành sân vận động mới, hoặc chia nhỏ làm trường học, trạm y tế. Kế hoạch nghe qua tưởng như hoàn hảo mười phần. 

Thế nhưng khi bắt tay vào làm, người ta mới vấp phải rào cản khổng lồ: chi phí hậu cần và chuỗi cung ứng! Tháo dỡ hàng vạn tấn thép, kiểm định an toàn, đóng gói rồi thuê tàu chuyên dụng chở xuyên đại dương... ngốn khoản tiền ước tính hàng chục triệu đô la. 

Ai sẽ là người bỏ tiền túi ra trả cho chuyến tàu đắt đỏ đó? 

Chưa hết, nước nhận viện trợ vẫn phải tự bỏ tiền giải phóng mặt bằng, đào móng, đổ trụ chịu lực và thuê kỹ sư ráp lại. Nếu không có sẵn tiền đối ứng, món quà thiện chí bỗng chốc trở thành gánh nặng tài chính mới. Chính vì vậy, suốt một thời gian sau World Cup 2022, sân 974 vẫn chưa thể tháo dỡ cấp tốc mà được giữ lại tổ chức các sự kiện âm nhạc và thể thao, trước khi từng bước chuyển giao theo lộ trình phù hợp. 

Dù còn nhiều thách thức, bài học sân 974 để lại cho ngành xây dựng thế giới là vô cùng sâu sắc: xu hướng mô-đun hóa. Robot và máy cắt tự động gia công từng thanh thép, từng chiếc container trong nhà máy với độ chính xác đến từng mi-li-mét. Mang ra hiện trường chỉ việc bắt ốc vít và khóa then. Nhanh gọn, chính xác và sạch sẽ tuyệt đối. 

Nhìn chuyện xứ người, chúng ta không khỏi giật mình ngẫm lại chuyện nước mình. Việt Nam có ngành cơ khí chế tạo và kết cấu thép rất phát triển, tay nghề thợ cơ khí nước mình rất khéo. Ít ai ngờ rằng, ngay tại World Cup Qatar, chính những bàn tay tài ba của thợ cơ khí Việt Nam – từ các doanh nghiệp kết cấu thép lớn như Đại Dũng – đã trực tiếp gia công hàng vạn tấn cấu kiện thép siêu trường siêu trọng, gọt giũa chính xác từng mối hàn để xuất khẩu sang Trung Đông dựng nên các sân vận động biểu tượng. Năng lực kỹ thuật của người thợ Việt hoàn toàn không thua kém ai. 

Thế nhưng ở nhiều địa phương, chúng ta vẫn thấy bóng dáng của những con voi trắng mini. Những sân vận động ngốn hàng trăm, hàng nghìn tỷ đồng ngân sách chỉ để phục vụ một kỳ đại hội thể thao vài tuần lễ, rồi sau đó đóng cửa cài then suốt nhiều năm ròng cho cỏ mọc bò gặm. 

Nếu chúng ta thay đổi tư duy, áp dụng cách làm linh hoạt như sân 974: chỉ xây dựng quy mô vừa đủ nhu cầu thực tế, kết hợp các mô-đun thép tháo rời khi cần mở rộng sự kiện lớn, thì ngân sách sẽ tiết kiệm được biết bao nhiêu tiền của."""

# Target p_conc: ~160 words
p_conc = """Sân vận động 974 có thể rồi đây sẽ biến mất hoàn toàn trên bản đồ Doha, trả lại bờ cát thanh bình cho sóng biển vịnh Ba Tư. Nhưng dấu ấn mà nó để lại trong lịch sử kiến trúc nhân loại thì vẫn còn nguyên giá trị. 

Nó chứng minh cho thế giới thấy rằng: Một công trình thực sự vĩ đại không nhất thiết phải trường tồn hàng trăm năm bằng bê tông cốt thép nặng nề. Vĩ đại đôi khi chỉ đơn giản là biết hoàn thành xuất sắc sứ mệnh của mình, mang lại niềm vui trọn vẹn cho hàng triệu con người, rồi lặng lẽ rời đi mà không để lại bất kỳ gánh nặng nào cho tương lai. 

Vậy theo bạn, liệu mô hình công trình lắp ghép tháo rời này có thể trở thành giải pháp cứu cánh cho các sân vận động nghìn tỷ đang đắp chiếu ở nước mình hay không? 

Ý kiến của bạn về vấn đề này thế nào? Hãy để lại bình luận phía dưới nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."""

parts = [hook, bridge, scene_shift, p0, p1, p2, p3, p_conc]
c = [len(p.split()) for p in parts]
print("Counts:", c)
print("Total words:", sum(c))
print("Diff to 1700:", sum(c) - 1700)
