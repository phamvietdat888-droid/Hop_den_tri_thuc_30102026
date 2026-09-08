# test script
import sys

sec0 = """Sáng ngày 5/9/2026, hàng triệu khán giả xem truyền hình cả nước ngỡ ngàng khi ống kính lễ khai giảng không còn chĩa vào các trường chuyên danh tiếng ở Hà Nội hay TP.HCM, mà đổ dồn về rẻo cao Mường Khương (Lào Cai) để phát sóng trực tiếp lễ khánh thành đồng loạt hơn 100 ngôi trường nội trú bề thế vừa dựng xong sau 10 tháng thần tốc.

Vì sao một đỉnh đèo hiểm trở như Mường Khương lại được chọn làm 'trái tim' của lễ khai giảng cả nước, và bằng cách làm quái kiệt nào mà Việt Nam hoàn thành hơn 100 ngôi trường to đùng nơi biên cương nhanh đến vậy?"""

sec_mk = """Câu trả lời nằm ở một bước chuyển chưa từng có tiền lệ. Năm học 2026-2027 là năm học đầu tiên triển khai Nghị quyết Đại hội 14 của Đảng với phương châm nói thật, làm thật và ra kết quả thật. Thay vì ngồi hội trường nghe báo cáo, cả nước hướng trọn vẹn máy quay về rẻo cao biên giới để chứng kiến kết quả bằng xương bằng thịt: hơn 100 ngôi trường hiện đại mọc lên giữa đại ngàn chỉ sau 10 tháng. 

Vậy vì sao lại là Mường Khương mà không phải nơi nào khác? 

Thứ nhất, Mường Khương là mảnh đất phên dậu hiểm trở bậc nhất phía Bắc, nơi bà con đồng bào Mông, Dao, Tày, Giáy, Tu Dí... cùng sinh sống. Chọn Mường Khương làm điểm phát sóng trực tiếp là lời khẳng định đanh thép: Nơi nào gian nan nhất, nơi đó được Đảng và Nhà nước ưu tiên hàng đầu. Thứ hai, ngôi trường 257 tỷ đồng này đẹp như một kiệt tác giữa núi rừng: nhìn từ trên cao y hệt một cuốn vở khổng lồ đang mở ra giữa ngàn mây trắng, tường sơn hoa văn thổ cẩm tinh xảo. Với 9 khối nhà kiên cố liên hoàn từ lớp học, nhà ăn, ký túc xá tới sân thể thao ngoài trời cho gần 1.000 học sinh, Mường Khương chính là 'ngôi trường mẫu' chuẩn chỉ nhất cho toàn bộ 248 trường biên giới sau này.

Chưa hết, triệu người xem truyền hình hôm đó đã nổi da gà trước màn 'điểm danh xuyên núi - xuyên biển'. Cầu truyền hình nối thẳng từ đỉnh sương mù Mường Khương ra 4 điểm trường ngoài đảo xa Song Tử Tây, Sinh Tồn, Đá Tây, Trường Sa. Tiếng trống trường dội vào vách đá hòa cùng tiếng sóng biển gầm vang, làm bùng cháy niềm tự hào chủ quyền thiêng liêng. Đặc biệt, ít ai biết những ngôi trường này được đúc bê tông chịu lực cực mạnh, vừa để dạy học, vừa đóng vai trò như một 'pháo đài trú ẩn an toàn' cho cả bản làng mỗi khi có bão lũ quét tràn qua."""

sec_kho = """Thế nhưng, để có được những thước phim rực rỡ trên sóng truyền hình ấy, ít ai hình dung nổi 10 tháng trước, nơi đây chỉ là những sườn đồi hoang vu. Chuyện bắt đầu từ giữa năm 2025, Bộ Chính trị chốt chủ trương xây 248 trường nội trú liên cấp cho các xã biên giới. Sau chỉ đạo của Tổng Bí thư Tô Lâm, ngày 27/8/2025, Thủ tướng họp khẩn và phát lệnh: Đợt một phải xong gọn 100 trường trước 30/8/2026 để kịp năm học mới. 

Hạn chót đúng 10 tháng. Dân công trình nghe xong ai nấy đều lắc đầu lè lưỡi. Bởi vì sao?

Muốn biết khó ra sao, cứ thử một lần chạy xe lên mấy xã vùng sâu biên giới là hiểu ngay. Đường sá toàn dốc ngược, cua gấp khúc, mưa xuống là bùn đỏ nhão nhoét trơn như bôi mỡ. Chở một bao xi măng hay khối cát sỏi lên đỉnh đèo, cánh tài xế phải nín thở ôm vô lăng, tiền cước đội lên gấp ba bốn lần. Giá vật tư lúc đó lại nhảy múa liên tục khiến nhiều nhà thầu chỉ dám đứng từ xa dòm ngó vì sợ ôm nợ.

Thế nhưng, đường khó đi vẫn chưa là gì so với khâu mặt bằng. Trong 100 điểm trường, có tới 86 trường vướng vào đất nương rẫy của bà con. Ở vùng cao, mảnh nương là chén cơm manh áo qua bao đời, bảo bà con nhường đất trong ngày một ngày hai mà làm không khéo là tắc tị ngay. Nếu cứ túc tắc làm giấy tờ theo lối cũ thì đôi ba năm chưa chắc đã xong cái móng. Vậy các bác lãnh đạo đã gỡ mớ bòng bong này thế nào?"""

sec_tien = """Chìa khóa đầu tiên là tiền phải rót tận tay và làm ăn dứt khoát. Thấy vật tư trượt giá làm đội thêm hơn 4.654 tỷ đồng kinh phí, trên không chần chừ nửa lời. Ngày 1/4/2026, Chính phủ duyệt chi thẳng hơn 12.905 tỷ đồng tiền tươi thóc thật bổ sung ngay cho 100 trường. Có tiền lận lưng kịp thời, các nhà thầu thở phào nhẹ nhõm, công trường cứ thế cắm đầu tăng tốc mà không sợ đói vốn giữa đường.

Chưa hết, các bộ ngành phối hợp mượt như bôi dầu. Bộ Xây dựng tung ngay 14 mẫu thiết kế chuẩn chỉ, có đủ lớp học, ký túc xá, sân bóng và tính luôn cả nước chống bão lũ sạt lở. Bộ Nội vụ lo sẵn chính sách để thầy cô yên tâm cắm bản lâu dài. Ở địa phương, Bí thư Tỉnh ủy đích thân làm Trưởng ban chỉ đạo. Nhiều tỉnh như Lai Châu, Đắk Lắk còn bạo tay xuất ngân sách địa phương đền bù trước, lo chỗ ở mới cho dân bản để có ngay đất sạch giao cho thợ đào móng.

Tiền sẵn trong túi, đất sạch trên bàn, nhưng khi mùa mưa rừng tháng 7 ập xuống, cuộc đua lúc này mới thực sự nghẹt thở."""

sec_chay = """Càng về những tháng cuối, không khí trên các sườn đèo càng căng như dây đàn. Tại Cao Bằng, lãnh đạo tỉnh chuyển hẳn sang chế độ chỉ huy chiến dịch. Ngay cổng công trường ở xã vùng cao, người ta dựng luôn một chiếc đồng hồ điện tử khổng lồ, nhảy từng con số đỏ rực đếm lùi từng ngày từng giờ tới mốc 30/8. Nhìn con số đỏ lòm nhấp nháy giữa rừng đêm, thợ thuyền bảo nhau không ai dám chậm một bước chân.

Lúc này, bộ đội nhảy vào cuộc tiếp sức. Tại Y Tý trên đỉnh mây mù, lính công binh Binh đoàn 12 mở đợt cao điểm '68 ngày đêm quyết thắng'. Ở Quảng Trị, bộ đội Trung đoàn 996 cùng dân quân xắn quần lội bùn sâu đến gối, cõng từng thanh sắt qua dốc trơn dựng trường Thượng Trạch. Bữa cơm trưa ăn vội ổ bánh mì hay gói mì tôm ngay trên cabin xe tải; đêm xuống thì dàn đèn pha rực sáng một góc rừng, máy trộn bê tông chạy rầm rập thâu đêm.

Mồ hôi đổ ròng rã suốt 300 ngày đêm. Để rồi đúng sáng 5/9/2026, tiếng trống khai trường đã vang rền khắp các nẻo biên cương."""

sec_truong = """Không riêng gì Mường Khương, nhìn sang Lai Châu, trường liên cấp Phong Thổ còn làm dân tình choáng váng hơn: tổng mức đầu tư 280 tỷ đồng, rộng hơn 6 héc-ta, có tới 30 phòng học, 16 phòng bộ môn, nhà đa năng và cả bể bơi trong nhà to đùng phục vụ hơn một nghìn học sinh. Làn sóng trường mới này chạy dọc từ Gia Lai (Ia Pếch), qua Đà Nẵng (Tây Giang), lên Điện Biên (Si Pa Phìn, Thanh Nưa), rồi vươn thẳng ra biển lớn với các trường khang trang tại đảo Trường Sa và đảo Minh Châu.

Bỏ ra cả đống tiền và công sức thần tốc như vậy cho học sinh vùng biên, tính toán sâu xa phía sau của Nhà nước là gì?"""

sec_ket = """Thực ra, đây là một bước chuyển đổi tư duy rất lớn và cực kỳ thực tế. Chúng ta không còn loanh quanh dựng lớp học tạm bợ xóa mù chữ nữa, mà làm hẳn một nơi nuôi dạy đàng hoàng từ A đến Z. Lãnh đạo từng tâm sự rất thật lòng: Ngôi trường có to đẹp, tiện nghi, có cơm ngon áo ấm thì lũ trẻ mới mê đến lớp; thầy cô mới có động lực bám bản; và bà con dân bản mới yên tâm tuyệt đối gửi con em mình cho nhà trường dạy dỗ.

Năm học 2026-2027 này là năm học mở màn triển khai Nghị quyết Đại hội 14 của Đảng, với phương châm nói thật, làm thật và ra kết quả thật. Kỳ tích dựng xong hơn 100 ngôi trường trong 10 tháng chính là bằng chứng rõ nhất cho thấy: Khi lòng dân đã thuận và ý Đảng đã thông thì việc khó mấy cũng làm xong. Những ánh đèn lớp học bừng sáng giữa đại ngàn đêm nay không chỉ soi đường cho con trẻ, mà mỗi ngôi trường sừng sững ấy chính là một cột mốc tri thức kiên cố nhất để giữ yên từng tấc đất biên cương của Tổ quốc.

Ý kiến của bạn về kỳ tích xây trường vùng biên này thế nào? Hãy để lại bình luận phía dưới nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."""

all_text = [sec0, sec_mk, sec_kho, sec_tien, sec_chay, sec_truong, sec_ket]
for i, s in enumerate(all_text):
    print(f"Sec {i}: {len(s.split())} words")
total = sum(len(s.split()) for s in all_text)
print(f"Total words: {total}")
