import re

text = """# ĐẠI DŨNG LÀM SÂN WORLD CUP: VÌ SAO KHÁCH HÀNG QUỐC TẾ CHỌN DOANH NGHIỆP VIỆT?

Thưa anh em, có một câu chuyện mà mỗi lần nhắc lại, méo hiểu kiểu gì mình vẫn thấy lấn cấn. 

Cách đây vài năm, World Cup 2022 ở Qatar, bá tánh toàn cầu dán mắt vào tivi xem Messi nâng cúp vàng. Oách xà lách! Nhưng hỡi ơi, cái mà anh em ít để ý, là ngay trên đầu Messi, che nắng che mưa cho 80.000 con người ở sân Lusail Iconic, hay cái sân 974 ráp bằng container độc lạ nhất thế giới — đều được làm từ những khối thép do chính tay thợ Việt Nam nhào nặn. Tiền tươi thóc thật, hàng chục ngàn tấn thép được chở từ những xưởng cơ khí ở nước ta sang tận vùng Vịnh. 

Thế quái nào ở ngoài người ta nể anh em mình như thế, mà về nhà giang cư mận vẫn ca bài ca "đã làm được con ốc vít chưa?"

Ngay sau đây, mình cùng anh em bóc tách luôn nhé.

---

Anh em phải hiểu, Qatar đăng cai World Cup không phải để đá bóng cho vui. Họ vung ra sương sương 220 tỷ đô — 220 nghìn tỏi tiền ta đấy anh em nhá. Tiền nhiều đè chết người, chất ra đệm nằm đè lên cũng êm hơn đệm Kymdan. Vậy mà đùng một cái, doanh nghiệp Đại Dũng của Việt Nam trúng thầu cung cấp kết cấu thép cho không phải một, mà là hai cái sân xịn nhất nhì đại hội.

Nếu như anh cả Hòa Phát chuyên đúc thép cây vươn vai làm bá chủ nội địa, anh hai Hoa Sen lướt sóng tôn mạ, thì người anh em Đại Dũng sinh năm 1995 lại chọn con đường chông gai hơn: kết cấu thép siêu trường siêu trọng đi đánh xứ người. Từ một xưởng cơ khí lụp xụp lợp tôn mỏng dính ngày xưa ở Sài Gòn, giờ đã bôn tẩu giang hồ khắp 30 quốc gia. Gã này không ồn ào phô trương, nhưng lẳng lặng cắn trọn gói thầu thi công World Cup trước mũi mấy ông lớn ngoại quốc.

Quay lại chuyện hai cái sân. Đầu tiên là sân Lusail Iconic — nơi đá trận chung kết, nơi những tỷ phú, chính khách ngự tọa. Mình góp nhẹ nhàng gần 6.000 tấn thép khung vòm. 

Thứ hai là sân 974, cái sân ráp từ 974 cái container chở hàng, tháo ra lắp vào phà phà như anh em chơi Lego. Toàn bộ 28.000 tấn thép khung sườn là hàng Việt Nam 100%.

Anh em tính thử nhé. 28.000 tấn thép. Một cái xe hơi thông thường nặng chừng 1,5 tấn. 28.000 tấn tức là anh em vác gần 19.000 cái xe hơi chất đống lên nhau. Làm thầu sợ nhất mấy ông lắm tiền mà khó tính. Qatar họ thừa tiền, vẫy tay một cái là Tây Âu, Mỹ, Oa Khấu, Hàn Xẻng xếp hàng dài. Thế nhưng họ chốt sổ Đại Dũng. Má nó oách!

---

Nhiều cao nhân sẽ lập tức phán: "Chắc là bán phá giá lấy tiếng chứ gì, rẻ thì bọn nó mua." Sai bét!

Anh em nghĩ làm cái sân World Cup là trò đùa à? Sai một li, đi một dặm, nhưng trong ngành kết cấu thép, "một li" ấy đo bằng sinh mạng vạn con người và đền bù tiền tỷ.

Nắng sa mạc bên đó nóng như lò nung. Tính nhanh thế này: một thanh thép 30 mét, nhiệt độ tăng 10 độ C — giãn thêm 3 đến 4 mm. Mỏng hơn cái móng tay. Cơ mà nếu anh em có hệ thống mái vòm hàng trăm mét, giãn nở cộng dồn lại nó lệch cả chục phân. Lỗ bu lông không đút lọt, lập tức thành sắt vụn. 

Chưa hết. Thép chịu lực sân vận động nó dày hàng chục phân. Thợ hàn phải thi tuyển gắt gao, mỗi mối hàn xong là phải lấy máy siêu âm khuyết tật rà lại y hệt như siêu âm bà bầu. Có một hạt xỉ nhỏ bằng đầu tăm lọt vào là cắt bỏ làm lại. Một ngày cắm mặt vào tia lửa hàn sáng lòa, mắt mờ đi, mũi hít đầy khói độc, người thì nóng ran như đứng trong mâm lửa. 

Mấy ngài chuyên gia từ châu Âu cầm kính lúp đi soi từng centimet, lệch chuẩn một ly là ăn thẻ đỏ tắp lự. Bên Qatar đưa đề bài: mày ở Việt Nam, cách tao 7.000 cây số. Mày làm xong từng khúc thép khổng lồ chở sang đây, tao cẩu lên ráp vào là phải ăn khớp từng lỗ bu lông. Lệch chuẩn đúng 0,1mm là trả hàng. Chấp cả Hàn Xẻng nghe xong cũng toát mồ hôi hột.

Đại Dũng làm thế nào? Họ thi triển võ công cực dị: Lắp thử ngay tại Việt Nam. Đem cái ghép hình khổng lồ ra bãi đất siêu to ráp vào nhau thử. Khớp 100%. Dỡ ra, đóng gói, chuyển sang Qatar lắp lại phà phà. Tây nhìn mồ hôi nhễ nhại rớt đùng đùng cũng phải nể phục. Đừng bảo Tây chọn mình vì rẻ, nó chọn vì năng lực thi công của mình đã đạt tầm quốc tế. Giao vào tay anh em thợ Việt, nó yên tâm cái bụng!

---

Bây giờ mình đặt lên bàn cân cho anh em xem. Ông Tây làm cũng được, nhưng báo giá trên trời, chi phí nhân công châu Âu đắt lòi kèn. 10.000 đô một tháng cho một kỹ sư giám sát là ít. 

Thế nhưng anh em thợ Việt Nam thì sao? 

Mình nói xanh chín, thợ hàn Việt Nam là những con người chịu thương chịu khó nhất quả đất. Tiếng búa gõ leng keng rền khắp xưởng lợp tôn từ lúc trời chưa sáng. Hít khói bụi, mồ hôi nhễ nhại, tia lửa hàn bắn xèo xèo vào áo bảo hộ dày bịch giữa cái nắng 40 độ.

Anh em thử làm một phép tính thời gian sống. Lương thợ hàn tay xoa cọc tiền cuối tháng chắc chừng 15 củ. Trừ tiền nhà trọ, tiền ăn, bỉm sữa, cất được 5 củ. Trong khi đó, một chuyến bay khứ hồi, cộng tiền ăn ở, tiền vé xem chung kết World Cup ở Qatar nhẹ nhàng ngốn khoảng 200 củ. 
200 triệu chia 15 triệu bằng hơn 13 tháng. Hơn một năm trời cày cuốc không ngừng nghỉ, không ốm đau, không đám hiếu hỉ — chỉ để đổi lấy 90 phút ngồi trên cái khán đài dưới chính mái vòm do tay mình làm ra. Bảy tháng tuổi trẻ, mười ba tháng thanh xuân — đổi lấy một giấc mơ. Xót xa không?

Thế nhưng, chính giá nhân công cạnh tranh cộng với tay nghề chịu cày chịu ải của thợ nhà mình đã tạo ra món hàng vừa ngon, vừa bổ, vừa hợp ví. Cạnh tranh toàn cầu phũ phàng thế đấy. Anh em không vắt kiệt mồ hôi công sức, làm gì có vé vào sân chơi 220 tỏi đô?

---

Và đây mới là chỗ mình muốn anh em suy nghĩ. Một sự thật chớ trêu.

Đại Dũng mang ngoại tệ về, làm nhà máy lọc dầu, nhiệt điện trải dài từ Nam chí Bắc. Tham gia xây nhà ga T3 Tân Sơn Nhất, sân bay Long Thành. Những khối thép khổng lồ "Made in Vietnam" đứng sừng sững ở Úc, Mỹ, Nhật. Oai phong lẫm liệt.

Nhưng cứ lướt cõi mạng mà xem. Đăng bài tự hào về công nghiệp cơ khí Việt Nam một cái, đảm bảo 5 phút sau có chục cao nhân copy paste câu thần chú: "Đã làm được con ốc vít chưa mà gáy?"

Ảo diệu ứ chịu được! Cầm cái thước 20 phân đi đo sông Mê Kông! 

Người ta làm dàn mái vòm che 80.000 khán giả, thì bĩu môi chê "toàn gia công cắt sắt". Còn không đúc được con ốc vít thì rủa xả "nền công nghiệp số không, đi làm mướn". Làm được cái lớn thì bảo đấy là trò trẻ con, không làm được cái nhỏ thì bảo kém cỏi toàn diện. Tiêu chuẩn kép như thế thì méo hiểu kiểu gì luôn!

Thế giới phân công lao động hết rồi. Đức sản xuất ô tô siêu sang nhưng đất hiếm cũng phải mua từ bên Tàu. Việt Nam mạnh gia công cơ khí chính xác khối lớn, chế tạo kết cấu thép siêu trường siêu trọng, thì vã cái đó. Còn ốc vít, một bịch 500 con bán chợ giá 15.000 đồng. Đầu tư dàn máy trăm tỏi dập triệu con ốc chỉ để vuốt ve cái tôi trên mạng, trong khi Tàu nó làm rẻ bằng một nửa? Đó không phải phát triển công nghiệp, đó là giải trí tốn kém! Doanh nghiệp họ khôn lắm, họ đánh vào đâu để cắn lãi đậm, chứ không phải đi đoạt cúp "ốc vít vô địch" trên Facebook.

Vỗ ngực chê bai thì dễ. Ngồi máy lạnh gõ phím "chưa làm được cái đinh" ai chả làm được. Cơ mà ra ngoài xưởng lợp tôn cầm mỏ hàn giữa trời nắng 40 độ thì mới thấy ngàn cân trèo sợi bún.

---

Thôi lan man đến đâu rồi, quay về chuyện cái sân vận động.

World Cup kết thúc. Cái sân 974 ráp bằng container, xong giải là Qatar tháo dỡ ra ngay để xây khu thương mại. Những thanh thép Việt Nam lại tháo rời, xếp lên tàu, đi làm nhiệm vụ khác. 

Nó y hệt như số phận thợ cơ khí nhà mình. Lặng lẽ làm, xây xong một công trình vĩ đại, chép miệng tự hào một xíu, rồi lại xách đồ nghề đi công trường mới. Không phông bạt sống ảo, không gáy đạo lý. Người làm ra giá trị thật thì lặng lẽ như bóng đêm. Kẻ chê bai bôi nhọ thì rực rỡ dưới ánh đèn màn hình.

Nhưng cái sân Lusail Iconic thì vẫn đứng đó, oách xà lách, như một đài kỷ niệm lấp lánh giữa sa mạc. Và nó sẽ còn đứng đó hàng chục năm nữa, nhắc cho thế giới nhớ rằng: Việt Nam không chỉ xuất khẩu gạo, cà phê. Chúng ta xuất khẩu cả những khối thép khổng lồ, xuất khẩu cả chất xám kỹ thuật và sự chính xác đến từng mi-li-mét.

Đừng nghĩ đi gia công là hèn. Hàn Quốc, Đài Loan thập niên 80 cũng đi gia công bục mặt cho Nhật, Mỹ. Phải chịu đấm ăn xôi, học mót bản vẽ kỹ thuật mới có ngày vươn vai hóa rồng. 

Cuộc kháng chiến công nghiệp này thắng hay thua chưa biết. Chỉ biết anh em thợ ngoài kia vẫn đổ mồ hôi, hỏng mắt vì tia hàn để mang tiền thật về cho đất nước. Còn giang cư mận, gáy xong phủi đít đi chơi ai sợ nữa đây?

Con ốc vít không có lỗi. Lỗi là mình đứng tầng 4 tưởng tầng 8. Cháy nhà mới ra mặt chuột, đến lúc Tây nó vào chiếm sạch thị trường, công nhân mất việc, thì lúc đấy gào lên "ốc vít" chả ai nghe. Má nó cay.

Ý kiến của bạn về vấn đề này thế nào? Hãy để dưới bình luận nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa.
"""

import re
words = re.findall(r'\b\S+\b', text)
print(len(words))
with open('outputs/2026-09-26_Dai_Dung_World_Cup_Cu_Dau/06_kich_ban_hoan_thien.md', 'w', encoding='utf-8') as f:
    f.write(text)
