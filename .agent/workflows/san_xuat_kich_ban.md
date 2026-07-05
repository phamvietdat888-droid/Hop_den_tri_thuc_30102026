# Workflow: Sản Xuất Kịch Bản — Pipeline chuẩn
> **Trigger chính:** `/tac_chien [chủ đề]`
> **Trigger trinh sát:** `/tim_trend [từ khóa]`
> **Trigger fanpage:** `/dang_fb [chủ đề]`

---

## Pipeline chính

```yaml
steps:
  - step: 0
    agent: 01_researcher
    action: TRINH SÁT TREND — Quét đa nguồn, chấm điểm 7 tiêu chí
    input: Từ khóa từ Sếp (hoặc quét tổng)
    output: Báo cáo trinh sát trend
    skill: skills/trinh_sat_trend_skill.md
    gate: CHỜ SẾP CHỌN CHỦ ĐỀ
    condition: Chỉ kích hoạt khi Sếp gõ /tim_trend
    note: Bước tùy chọn. Nếu Sếp đã có chủ đề → bỏ qua, vào thẳng Bước 1.
    sources:
      - Google Trends VN (ưu tiên số 1)
      - Báo VN (VnExpress, Tuổi Trẻ, Thanh Niên, Dân Trí, BBC VN, VOA VN)
      - Báo quốc tế (Reuters, BBC, Al Jazeera, SCMP, The Diplomat)
      - Facebook (Fanpage đối thủ + Group thời sự)
      - YouTube đối thủ (TTT, Tổ Buôn, Góc Nhìn Kinh Tế)
      - X (Twitter) + Reddit (r/geopolitics, r/worldnews, r/VietNam)
    
  - step: 1
    agent: 01_researcher
    action: Tiếp nhận đề bài, thu thập thông tin
    input: Chủ đề + Dữ liệu từ Sếp (hoặc từ Bước 0)
    output: 01_brief.md
    
  - step: 2
    agent: 01_researcher
    action: Đánh giá rủi ro YT, đề xuất 5 Angle + nỗi đau + lịch sử VN
    input: Brief (step 1)
    output: 02_angle.md
    gate: CHỜ SẾP CHỌN ANGLE
    
  - step: 3
    agent: 02_scriptwriter
    action: Xây dựng dàn ý Tam Giác Ngược
    input: Angle được duyệt + .shared/
    output: 03_outline.md
    gate: CHỜ SẾP DUYỆT DÀN Ý
    
  - step: 4
    agent: 02_scriptwriter
    action: Viết kịch bản nháp 1200-1600 từ (8 Module)
    input: Dàn ý (step 3) + .shared/ toàn bộ
    output: 04_script_draft.md
    skill: skills/giai_ma_360_skill.md
    references:
      - .shared/tone_guide.md
      - .shared/tu_cam.md
      - .shared/hook_formulas.md
      - .shared/storytelling_arsenal.md
      - .shared/to_mo_loi_ich_module.md
      - .shared/lich_su_vn_module.md
      - .shared/format_output.md
      - .shared/few_shot_examples.md
      - .shared/kho_vu_khi/
    
  - step: 5
    agent: 03_quality_inspector
    action: 🛡️ Quét Compliance Shield & Kiểm định 33 tiêu chí
    input: Kịch bản nháp (step 4)
    output: 05_review.md
    references:
      - .shared/compliance_shield.md
      - checklist.md
      - .shared/tu_cam.md
      - ERRORS.md
    loop: Nếu < 85 điểm → trả về step 4 kèm ghi chú lỗi (tối đa 3 vòng)
    
  - step: 6
    agent: 04_publisher
    action: Xuất bản cuối + cập nhật Kho Vũ Khí
    input: Kịch bản ĐẠT (step 5)
    output: 06_kich_ban_hoan_thien.md + .docx → outputs/[Topic]/YouTube/
    gate: CHỜ SẾP DUYỆT BẢN CUỐI
    condition: Chỉ kích hoạt khi Agent 03 cho ≥ 85 điểm
    references:
      - .shared/format_output.md          # ⚠️ BẮT BUỘC — Quy chuẩn DOCX Audio Clean
    tools:
      - scripts/md_to_docx_v2.py          # ⚠️ BẮT BUỘC — Script chuyển đổi MD → DOCX
    updates:
      - .shared/kho_vu_khi/vi_von_hay.md
      - .shared/kho_vu_khi/hook_test.md
      - .shared/kho_vu_khi/lich_su_vn.md
      - .shared/kho_vu_khi/noi_dau_hieu_qua.md

  - step: 6d
    agent: 04_publisher
    action: Phát Sóng Fanpage — Gọt kịch bản YT → Bài FB + Ảnh + Đăng FB
    input: 06_kich_ban_hoan_thien.md + 06b_goi_seo.md
    output: 06d_bai_dang_fb.md + .docx → outputs/[Topic]/Facebook/
    skill: skills/dang_fanpage_skill.md
    gate: CHỜ SẾP DUYỆT BÀI FB
    condition: Kích hoạt tự động sau Bước 6c HOẶC qua lệnh /dang_fb
    schedule: Hẹn đăng 19:00 VN (mặc định)
    references:
      - .shared/compliance_shield.md
      - .shared/format_facebook.md
      - .shared/tone_guide.md
      - .shared/tu_cam.md

  - step: 6e
    agent: 04_publisher
    action: Seeding Bình Luận — Mega Comments + 2 CTA
    input: 06d_bai_dang_fb.md
    output: 06e_mega_comments.json → outputs/[Topic]/Facebook/
    skill: skills/seeding_facebook_skill.md
    gate: 🛡️ COMPLIANCE GATE (Chặn nếu vi phạm ngôn từ thù ghét/tục tĩu)
    condition: Kích hoạt tự động sau Bước 6d

  - step: 6f
    agent: 04_publisher
    action: Chuyển thể YouTube Shorts — 2-3 Shorts ≤50s + SEO + Prompt ảnh + DOCX
    input: 06_kich_ban_hoan_thien.md
    output: YouTube_Shorts/short_01/, short_02/... → outputs/[Topic]/
    skill: skills/youtube_short_skill.md
    condition: Kích hoạt tự động sau Bước 6e HOẶC qua lệnh /tao_short
    note: Hook và kịch bản Shorts viết LẠI, không cắt từ bản dài (mô hình Hub & Spoke)

  - step: 7
    agent: 04_publisher
    action: Postmortem — rút kinh nghiệm từ data YouTube
    input: Data YouTube (Views, Retention, CTR, Comments)
    output: 07_postmortem.md + cập nhật Learning.md
    condition: Sau 48-72h video lên sóng
```

## Sơ đồ luồng

```
/tim_trend [từ khóa]          /tac_chien [chủ đề]
       │                              │
       ▼                              │
[Bước 0: TRINH SÁT]                  │
  Quét 6 nguồn                       │
  Chấm 7 tiêu chí                    │
  Top 5 chủ đề                       │
  [CHỜ SẾP CHỌN] ─────────────────→──┤
                                      │
                                      ▼
                              [Bước 1: BRIEF]
                                      │
                              [Bước 2: ANGLE]
                              [CHỜ SẾP CHỌN]
                                      │
                              [Bước 3: DÀN Ý]
                              [CHỜ SẾP DUYỆT]
                                      │
                              [Bước 4: VIẾT NHÁP]
                                      │
                              [Bước 5: KIỂM ĐỊNH]
                                 ĐẠT?──KHÔNG→↺Bước 4
                                      │
                              [Bước 6: XUẤT BẢN]
                              [CHỜ SẾP DUYỆT]
                                      │
                              [Bước 6d: PHÁT SÓNG FANPAGE] ★
                                 Gọt YT → FB 500-800 từ
                                 Tạo ảnh + Hẹn 19:00 VN
                              [CHỜ SẾP DUYỆT BÀI FB]
                                      │
                              [Bước 6f: YOUTUBE SHORTS] ★
                                 2-3 Shorts + SEO + Ảnh
                                        │
                              [Bước 7: POSTMORTEM]
                                      │
                                      ▼
                              [Sản phẩm] → outputs/
```

## Workflow phụ

### Trinh sát trend nhanh
```
Trigger: /tim_trend [từ khóa]
Pipeline: Agent 01 quét đa nguồn → Chấm 7 tiêu chí → Báo cáo Top 5
Skill: skills/trinh_sat_trend_skill.md
```

### Kiểm định nhanh
```
Trigger: /kiem_dinh
Pipeline: Agent 03 đọc kịch bản → Chạy 33 tiêu chí (checklist.md) → Báo cáo
```

### Xem Kho Vũ Khí
```
Trigger: /kho_vu_khi
Pipeline: Đọc .shared/kho_vu_khi/ → Trả về tổng hợp
```

### Báo cáo tiến độ
```
Trigger: /tien_do
Pipeline: Agent 00 rà soát drafts/ + outputs/ → Bảng tiến độ
```

### Đăng Fanpage Facebook ★
```
Trigger: /dang_fb [chủ đề]
Pipeline:
  Chế độ A (Có kịch bản): Gọt YT → Bài FB → Ảnh → Preview → [CHỜ SẾP] → Đăng
  Chế độ B (Độc lập): Viết mới → Chọn template → Ảnh → Preview → [CHỜ SẾP] → Đăng
Skill: skills/dang_fanpage_skill.md
Agent: 04_publisher
Schedule: Mặc định hẹn 19:00 VN
```

