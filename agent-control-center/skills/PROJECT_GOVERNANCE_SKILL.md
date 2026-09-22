---
name: project-governance
description: Điều phối và giám sát toàn bộ vòng đời dự án theo mô hình GitHub-first, phân vai Planner/Coder/Reviewer, approval gate bắt buộc, nhật ký vấp ngã, quy tắc đặt tên và bằng chứng ở từng công đoạn.
---

# PROJECT GOVERNANCE SKILL

## Quy tắc trung tâm
- GitHub là source of truth.
- Local chỉ là workspace tạm.
- Mọi thay đổi quan trọng phải commit + push.
- Không tác nhân nào tự duyệt chính công việc của mình.
- Không được nhảy bước.
- Không được tuyên bố hoàn tất nếu thiếu bằng chứng.

## Pipeline bắt buộc
USER_REQUEST
→ ANALYSIS
→ TASK_SPEC
→ READY_FOR_APPROVAL
→ APPROVED
→ CODING
→ TESTING
→ REVIEWING
→ SECURITY_CHECK
→ READY_FOR_RELEASE
→ FINAL_APPROVAL
→ MERGE
→ RELEASE
→ DEPLOY
→ LESSONS_UPDATE
→ STATE_UPDATE

## Vai trò
### Planner
Đọc yêu cầu/state/lessons; chia task; khóa scope; tạo acceptance criteria. Không code, không merge, không release.

### Coder
Chỉ sửa đúng scope trên task branch; chạy test/build; trả diff/log. Không merge/release/deploy, không tự review pass.

### Reviewer
Kiểm diff/test/regression/hard rules; chỉ trả REVIEW_PASS hoặc REVIEW_FAIL. Không sửa rồi tự duyệt.

### Release Manager
Chỉ chuẩn bị RC/release khi đã đủ TEST_PASS + REVIEW_PASS + SECURITY_PASS + FINAL_APPROVED.

### Deploy Agent
Chỉ deploy artifact đã duyệt; không tự build lại hay đổi version.

### State Monitor
Chỉ đọc trạng thái và cập nhật heartbeat; không sửa source/merge/release/deploy.

## Naming
Project dùng số thứ tự 3 chữ số:
001_HBM_CAM
002_X79
003_GRAM_TOKEN

Không dùng new/new2/final/final-final/test123.

## Lessons learned
Mỗi lỗi ghi:
ID, DATE, PROJECT, CONTEXT, WHAT_WENT_WRONG, ROOT_CAUSE, CORRECT_ACTION, RULE_TO_PREVENT_REPEAT, STATUS.
Lỗi lặp 2 lần trở lên phải nâng thành HARD_RULE.

## Hard gates
- Không APPROVED → không code.
- Không TEST_PASS → không review pass.
- Không REVIEW_PASS → không release candidate.
- Không FINAL_APPROVED → không merge/release/deploy.
- Fail 2 lần liên tiếp → trả về Planner phân tích lại.
