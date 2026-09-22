# HARD RULES

1. GitHub là source of truth.
2. Không sửa file ngoài scope.
3. Không tuyên bố hoàn tất nếu chưa có test bắt buộc.
4. UI có reference thì reference là source of truth.
5. Yêu cầu mới nhất của người dùng thắng yêu cầu cũ nếu xung đột.
6. Không tự ý đổi kiến trúc/dependency/API/UI ngoài scope.
7. Không merge/release/deploy nếu thiếu approval gate.
8. Không tác nhân nào tự duyệt công việc của chính mình.
9. Không kéo toàn bộ lịch sử vào mỗi task; chỉ dùng context cần thiết.
10. Không commit secrets, token, API key hoặc .env.
11. Fail 2 lần liên tiếp → trả về Planner phân tích lại.
12. Không retry vô hạn.
