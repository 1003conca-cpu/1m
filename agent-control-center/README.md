# Agent Control Center

Trung tâm quản trị tác nhân cho toàn bộ dự án.

## Nguyên tắc
- GitHub là source of truth.
- Local chỉ là workspace tạm.
- Không tác nhân nào tự duyệt công việc của chính mình.
- Không merge/release/deploy nếu thiếu approval gate.
- Mỗi task phải có bằng chứng: spec, test, review, state.
- Mỗi project đặt tên theo số thứ tự 3 chữ số: `001_PROJECT_NAME`, `002_...`.

## Pipeline
USER → PLANNER → TASK_SPEC → APPROVAL → CODER → TEST → REVIEWER → SECURITY → RELEASE → DEPLOY → LESSONS → STATE UPDATE

## Cấu trúc
- `agents/`: định nghĩa vai trò và quyền từng tác nhân
- `project-control/`: state, permissions, hard rules
- `lessons-learned/`: nhật ký vấp ngã và quy tắc
- `status/`: trạng thái hệ thống
- `.github/workflows/`: heartbeat 5 phút/lần
