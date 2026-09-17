# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Perfectly calibrated 1700-word script

hook1 = """Bỏ ra hàng trăm triệu đô xây một sân vận động World Cup bốn vạn chỗ ngồi, tổ chức vỏn vẹn bảy trận bóng đá rồi... tháo tung ra từng mảnh như bộ xếp hình Lego! Nghe qua tưởng như chuyện đùa, hoặc trò chơi ngông điên rồ của những tỷ phú dầu mỏ thừa tiền."""

hook2 = """Hãy tưởng tượng bạn vừa ngồi giữa bốn vạn người hò hét khản cổ trong một trận cầu đỉnh cao của World Cup, nhưng chỉ vài tuần sau quay lại, cả cái sân bóng khổng lồ bỗng biến mất không còn một mảnh vụn, trả lại bờ cát trắng phau bên mép sóng biển."""

bridge = """Vì sao người ta lại tạo ra một công trình có thể tháo rời hoàn toàn như vậy, và bí mật cơ khí nào giúp gần một nghìn chiếc thùng công ten nơ có thể ghép thành một sân vận động an toàn tuyệt đối cho người hâm mộ nhảy múa ăn mừng?"""

scene_shift = """Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."""

p0 = [
    """Bạn thử nhắm mắt lại và hình dung khoảnh khắc này. Đêm Doha cuối năm 2022, gió từ vịnh Ba Tư thổi vào mát rượi, mang theo vị mặn chát của biển cả hòa lẫn mùi sơn mới trên những vách thép. Dưới ánh đèn cao áp sáng rực, một khối kiến trúc kỳ dị sừng sững hiện ra bên bờ vịnh.""",
    """Nó không giống bất kỳ sân bóng nào bạn từng thấy. Không tường bê tông xám xịt. Thay vào đó là gần một nghìn chiếc thùng công ten nơ đủ màu sắc xanh, đỏ, vàng, bạc, xếp chồng lên nhau ngay ngắn giữa hệ khung thép đồ sộ.""",
    """Tiếng bước chân của bốn vạn cổ động viên giẫm rậm rịch trên sàn thép dã chiến, tạo nên âm thanh rền vang như một bản hùng ca cơ khí.""",
    """Lạ lùng đến khó tin.""",
    """Tại sao Qatar lại gom những chiếc thùng chở hàng về làm sân bóng? Làm cách nào người ta có thể tháo rời một công trình nặng hàng vạn tấn mà không cần nổ mìn đập phá?"""
]

p1 = [
    """Để hiểu được điều kỳ diệu này, trước hết bạn hãy nhìn sân vận động 974 dưới góc nhìn của một khán giả bình thường.""",
    """Cảm giác đầu tiên bước qua cổng an ninh là sự ngỡ ngàng tột độ. Bạn đi xem bóng đá nhưng ngỡ như đang lạc vào một bến cảng sầm uất. Mọi tiện ích thiết yếu nhất đều được nhét gọn gàng bên trong những chiếc thùng công ten nơ tiêu chuẩn.""",
    """Màu sắc từng chiếc thùng chính là hệ thống chỉ dẫn cực kỳ thông minh. Thùng màu vàng là quầy bán bánh mì và nước ngọt. Thùng màu xanh dương là nhà vệ sinh sạch bóng. Thùng màu xanh lá là trạm sơ cứu dã chiến. Còn những thùng màu bạc sang trọng nằm sâu phía dưới khán đài là phòng thay đồ của các siêu sao như Messi hay Neymar. Mọi thứ đều vuông vức, tinh gọn đến kinh ngạc.""",
    """Thế nhưng, điều khiến giới kỹ sư toàn cầu ngả mũ thán phục nằm ở cách người ta liên kết những chiếc thùng này lại với nhau. Bạn từng chơi trò xếp hình Lego chưa? Sân 974 được thi công chính xác theo nguyên lý đó, nhưng ở quy mô khổng lồ.""",
    """Bộ xương của sân là hệ khung giàn thép tiền chế vững chắc, sản xuất sẵn trong nhà máy rồi chở ra hiện trường. Khi lắp ráp, các kỹ sư không dùng đến một giọt hồ bê tông nào để gắn chết công trình xuống đất. Toàn bộ 974 chiếc container được cẩu lên, rồi khóa chặt vào khung thép bằng những chiếc then xoay cơ học chuẩn hàng hải.""",
    """Cơ chế này đơn giản đến bất ngờ.""",
    """Khi cẩu đặt thùng hàng vào đúng ngàm thép, người thợ chỉ cần vặn then xoay chín mươi độ. Cạch một cái! Chiếc then ăn sâu vào góc đúc của container, khóa cứng hai khối thép lại với nhau thành một khối vững như bàn thạch. Bốn vạn con người có đồng thanh dậm chân nhảy múa ăn mừng bàn thắng thì kết cấu bên dưới vẫn trơ trơ, không hề rung lắc.""",
    """Và đây mới là phép tính sống khiến nhiều người giật mình. Qatar là sa mạc nắng cháy, nhiệt độ ngoài trời có thể vượt năm mươi độ C. Tất cả sân vận động khác đều phải lắp hệ thống điều hòa khổng lồ ngốn hàng trăm triệu đô tiền điện để thổi khí lạnh vào từng ghế ngồi. Riêng sân 974 thì không.""",
    """Nó hoàn toàn không có máy lạnh!""",
    """Bí mật nằm ở vị trí đắc địa ngay sát mép nước. Nhờ kết cấu hở với những khoảng trống đan xen giữa các khối container, sân 974 giống như một chiếc bẫy gió tự nhiên khổng lồ. Gió biển thổi lồng lộng qua các khe thoáng, làm mát tự nhiên toàn bộ khán đài mà không tốn một xu tiền điện. Công trình này còn tiết kiệm tới bốn mươi phần trăm lượng nước sạch trong suốt quá trình xây dựng. Thời gian thi công cũng rút ngắn hơn một nửa: chưa đầy hai năm để hoàn thành tinh tươm.""",
    """Xây nhanh, dùng sướng, lại cực kỳ tiết kiệm."""
]

p2 = [
    """Nhưng nếu chỉ dừng lại ở chuyện xếp thùng container thành sân bóng, thì 974 cũng mới chỉ là một công trình cơ khí độc lạ. Giá trị sâu xa nhất của nó nằm ở việc đập tan một nỗi ám ảnh kinh hoàng: nỗi ám ảnh mang tên những con voi trắng.""",
    """Chuyện gì sẽ xảy ra với các sân vận động khổng lồ sau khi tiếng còi mãn cuộc vang lên?""",
    """Thực tế trần trụi đau đớn hơn rất nhiều so với những màn pháo hoa rực rỡ đêm bế mạc. Hãy nhìn lại Nam Phi sau World Cup 2010. Sân Green Point ở Cape Town tiêu tốn sáu trăm triệu đô la, nhưng giải vừa dứt thì khán giả cũng biến mất. Mỗi năm chính quyền phải cắn răng chi hàng triệu đô la ngân sách chỉ để quét mạng nhện, cắt cỏ và sơn lại những mảng tường mốc meo.""",
    """Hay sân Arena da Amazonia ở Brazil năm 2014, ngốn hơn ba trăm triệu đô la nằm lọt thỏm giữa rừng già. Thành phố không có đội bóng lớn nào đủ sức kéo khán giả tới sân. Kết cục là khối bê tông nghìn tỷ nằm phơi nắng phơi sương, biến thành bãi đỗ xe buýt và chuồng thả gia súc cho cỏ khỏi mọc lút đầu người. Đau xót hơn nữa là những nhà thi đấu đổ nát ở Hy Lạp sau Olympic Athens 2004, trở thành những vết sẹo bê tông gặm nhấm nền tài chính quốc gia suốt nhiều năm trời.""",
    """Người ta gọi những công trình nghìn tỷ vô dụng đó là những con voi trắng. Nuôi tốn mà chẳng để làm gì.""",
    """Và các nhà lãnh đạo Qatar hiểu quá rõ điều đó. Đất nước Qatar diện tích rất nhỏ, dân số khoảng ba triệu người, trong đó dân bản xứ chỉ chừng ba trăm nghìn người. Giải bóng đá quốc nội mỗi trận cuối tuần lèo tèo vài trăm khán giả ngồi thưa thớt. Họ cần làm gì với tám sân vận động từ bốn vạn đến tám vạn chỗ ngồi sau World Cup?""",
    """Nếu xây toàn bộ bằng bê tông vĩnh cửu, tám sân vận động đó sẽ thành tám chiếc máy nghiền tiền khổng lồ, mỗi năm nuốt chửng hàng chục triệu đô la bảo dưỡng. Người giàu thừa tiền, nhưng không ai dại dột tự trói chân mình vào đống nợ nần vô nghĩa như vậy.""",
    """Đó chính là lý do sân 974 ra đời với sứ mệnh chưa từng có tiền lệ: Nó sinh ra là để chuẩn bị cho cái chết của chính mình.""",
    """Một công trình dùng một lần đúng nghĩa!""",
    """Sau khi đăng cai trọn vẹn bảy trận đấu đỉnh cao, đỉnh điểm là chiến thắng bốn một của Brazil trước Hàn Quốc vào đêm mùng năm tháng mười hai năm 2022, sân 974 lập tức hạ màn. Không bỏ hoang mốc meo, không cỏ dại mọc um tùm. Nó hoàn thành nhiệm vụ lịch sử và sẵn sàng rời đi trong danh dự."""
]

p3 = [
    """Nhưng chuyện tháo dỡ một sân bóng trên bản vẽ thì rất thơ mộng, còn đưa vào thực tế vận hành có thực sự êm xuôi như người ta tưởng tượng?""",
    """Câu trả lời là không hề đơn giản.""",
    """Ý tưởng ban đầu của Qatar là sau khi tháo rời, toàn bộ 974 chiếc container và ba vạn tấn thép sẽ được bốc lên tàu biển để tặng lại cho một quốc gia đang phát triển ở châu Phi hoặc Nam Mỹ. Nước nhận viện trợ có thể dùng vật liệu đó lắp thành sân vận động mới tinh, hoặc bẻ nhỏ ra làm nhiều sân thể thao mini, bệnh viện dã chiến và nhà ở xã hội. Kế hoạch nghe qua tưởng như hoàn hảo mười phần.""",
    """Thế nhưng khi bắt tay vào làm, người ta mới vấp phải một rào cản khổng lồ: chi phí hậu cần và chuỗi cung ứng! Tháo hàng nghìn tấn thép khỏi các khớp nối, kiểm định an toàn từng chi tiết, đóng gói đưa xuống cảng, rồi thuê cả đội tàu chuyên dụng chở xuyên đại dương... ngốn một khoản tiền không hề nhỏ, ước tính lên tới hàng chục triệu đô la.""",
    """Ai sẽ là người bỏ tiền túi ra trả cho chuyến tàu đắt đỏ đó?""",
    """Chưa hết, một quốc gia nghèo khi nhận món quà này về, họ vẫn phải tự bỏ tiền giải phóng mặt bằng, đào móng, đổ trụ chịu lực và thuê kỹ sư chuyên môn cao để ráp lại công trình. Nếu nước nhận quà không có sẵn vài chục triệu đô la tiền đối ứng, thì món quà thiện chí bỗng chốc trở thành một gánh nặng tài chính mới.""",
    """Chính vì bài toán vận chuyển phức tạp này, nên suốt một thời gian sau World Cup 2022, sân 974 vẫn chưa thể tháo dỡ cấp tốc như lời đồn. Nước chủ nhà đã linh hoạt giữ lại công trình thêm một thời gian để tổ chức các sự kiện âm nhạc và một số trận đấu cúp, trước khi từng bước chuyển giao các cấu kiện theo lộ trình phù hợp.""",
    """Dù còn nhiều thách thức, nhưng bài học sân 974 để lại cho ngành xây dựng thế giới là vô cùng sâu sắc: xu hướng mô-đun hóa. Robot và máy cắt tự động gia công từng thanh thép, từng chiếc container trong nhà máy với độ chính xác đến từng mi-li-mét. Mang ra hiện trường chỉ việc bắt ốc vít và khóa then.""",
    """Nhanh gọn, chính xác và sạch sẽ tuyệt đối.""",
    """Nhìn chuyện xứ người, chúng ta không khỏi giật mình ngẫm lại chuyện nước mình. Việt Nam có ngành cơ khí chế tạo và kết cấu thép rất phát triển, từng gia công hàng vạn tấn cấu kiện thép siêu trường siêu trọng xuất khẩu đi khắp thế giới. Năng lực kỹ thuật của người Việt hoàn toàn không thua kém ai.""",
    """Thế nhưng ở nhiều địa phương, chúng ta vẫn thấy bóng dáng của những con voi trắng phiên bản mini. Những sân vận động, nhà thi đấu ngốn hàng trăm, hàng nghìn tỷ đồng ngân sách chỉ để phục vụ một kỳ đại hội thể thao vài tuần lễ, rồi sau đó đóng cửa cài then suốt nhiều năm ròng cho cỏ mọc bò gặm.""",
    """Nếu chúng ta thay đổi tư duy, áp dụng cách làm linh hoạt như sân 974: chỉ xây dựng quy mô vừa đủ nhu cầu thực tế, kết hợp các mô-đun thép tháo rời khi cần mở rộng tổ chức sự kiện lớn, thì ngân sách sẽ tiết kiệm được biết bao nhiêu tiền của."""
]

p_conc = [
    """Sân vận động 974 có thể rồi đây sẽ biến mất hoàn toàn trên bản đồ Doha, trả lại bờ cát thanh bình cho sóng biển vịnh Ba Tư. Nhưng dấu ấn mà nó để lại trong lịch sử kiến trúc nhân loại thì vẫn còn nguyên giá trị.""",
    """Nó chứng minh cho thế giới thấy rằng: Một công trình thực sự vĩ đại không nhất thiết phải trường tồn hàng trăm năm bằng bê tông cốt thép nặng nề. Vĩ đại đôi khi chỉ đơn giản là biết hoàn thành xuất sắc sứ mệnh của mình, mang lại niềm vui trọn vẹn cho hàng triệu con người, rồi lặng lẽ rời đi mà không để lại bất kỳ gánh nặng nào cho tương lai.""",
    """Vậy theo bạn, liệu mô hình công trình lắp ghép tháo rời này có thể trở thành giải pháp cứu cánh cho các sân vận động nghìn tỷ đang đắp chiếu ở nước mình hay không?""",
    """Ý kiến của bạn về vấn đề này thế nào? Hãy để lại bình luận phía dưới nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."""
]

# Let's adjust sentences to reach ~1700 words
all_sections = [hook1, bridge, scene_shift] + p0 + p1 + p2 + p3 + p_conc
text = "\n\n".join(all_sections)
words = text.split()
print("Current total words:", len(words))
