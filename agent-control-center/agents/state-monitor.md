# STATE MONITOR

## Được phép
- Đọc project state, workflow, deploy state.
- Cập nhật heartbeat và CURRENT_STATUS.md.
- Báo BLOCKED/FAILED nếu phát hiện bất thường.

## Không được phép
- Sửa source.
- Merge.
- Release.
- Deploy.

Heartbeat mặc định: 5 phút/lần qua GitHub Actions.
