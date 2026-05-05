# Hệ Thống Real Estate Photo → Instagram Pipeline (n8n Automation)

## 1. Tổng Quan Dự Án
Hệ thống **Real Estate Photo → Instagram Pipeline** là một luồng tự động hóa (workflow) nâng cao được xây dựng trên nền tảng n8n. Dự án giúp các đại lý bất động sản và chuyên viên marketing tự động hóa toàn bộ quy trình sản xuất nội dung mạng xã hội (Instagram) từ những bức ảnh thô. Bằng việc kết hợp sức mạnh của AI phân tích hình ảnh (Google Gemini) và quy trình xét duyệt nội dung qua Telegram, hệ thống giúp tối ưu hóa thời gian và đảm bảo chất lượng bài đăng một cách chuyên nghiệp.

---

## 2. Kiến Trúc Kỹ Thuật & Các Tính Năng Cốt Lõi

### 2.1. Nhận Diện & Trích Xuất Dữ Liệu Tự Động (Automated Trigger & Fetching)
- **Google Drive Integration:** Hệ thống tự động lắng nghe (poll) sự kiện thư mục cụ thể trên Google Drive. Ngay khi có một bức ảnh bất động sản mới được tải lên, hệ thống sẽ kích hoạt luồng làm việc (trigger) và tải ảnh về để xử lý tiếp.

### 2.2. Phân Tích Hình Ảnh AI & Sáng Tạo Nội Dung (AI Vision & Content Generation)
- Sử dụng **Google Gemini Vision** thông qua LangChain Agent đóng vai trò như một chuyên gia marketing bất động sản.
- **Phân tích hình ảnh chuyên sâu:** Nhận diện loại phòng, phong cách thiết kế, đặc điểm nổi bật, ánh sáng và không gian của bức ảnh.
- **Tạo Instagram Caption:** Tự động soạn thảo nội dung (150-200 từ) chuẩn SEO cho Instagram, nêu bật các ưu điểm của bất động sản, kết hợp emoji chuyên nghiệp, lời kêu gọi hành động (Call-to-Action) và bộ 15-20 hashtag tối ưu.
- **Gợi ý thiết kế:** Đề xuất phong cách thiết kế Canva (ví dụ: 'Modern Minimal', 'Luxury Gold') phù hợp với 'mood' của bức ảnh để phục vụ cho các bước thiết kế tiếp theo.

### 2.3. Xử Lý Dữ Liệu Phức Tạp (Data Parsing & Structuring)
- Sử dụng mã JavaScript tùy chỉnh (Code Node) để trích xuất, chuẩn hóa định dạng dữ liệu (JSON) trả về từ AI. Đảm bảo dữ liệu luôn ở trạng thái cấu trúc hoàn chỉnh trước khi chuyển sang các bước tiếp theo, đồng thời tích hợp cơ chế dự phòng (fallback) nếu AI gặp lỗi phản hồi.

### 2.4. Quy Trình Xét Duyệt Human-in-the-Loop (Approval Workflow)
- **Telegram Bot Integration:** Tự động gửi toàn bộ nội dung đã phân tích (thông tin phòng, phong cách, caption, đặc điểm nổi bật) kèm liên kết xem ảnh thô đến Telegram của người quản lý (Manager).
- **Interactive Inline Keyboard:** Tích hợp trực tiếp các nút bấm **Approve** (Duyệt) và **Reject** (Từ chối) ngay trong tin nhắn Telegram.
- **Webhook & Wait Node:** Hệ thống tự động tạm dừng luồng làm việc, chờ phản hồi từ người quản lý thông qua Webhook, đảm bảo không có nội dung nào được xuất bản nếu chưa qua kiểm duyệt.

### 2.5. Điều Phối Kịch Bản Rẽ Nhánh (Conditional Logic & Notifications)
- **Tự động hóa quyết định:** Hệ thống đọc dữ liệu phản hồi (Callback Query) từ Telegram để phân nhánh quá trình xử lý.
- **Thông báo kết quả:** Trả về thông báo thành công khi bài viết đã sẵn sàng lên sóng (Published), hoặc thông báo hủy bỏ luồng khi nội dung bị từ chối (Rejected).

---

## 4. Giá Trị Kinh Doanh & Hiệu Quả Hoạt Động (Business Impact)
- **Tối ưu hóa thời gian sản xuất nội dung:** Loại bỏ hoàn toàn thao tác thủ công trong việc quan sát, đánh giá ảnh và viết caption cho bất động sản, tiết kiệm hàng giờ làm việc mỗi ngày.
- **Đảm bảo chất lượng & Tính nhất quán:** Content được sản xuất bởi AI luôn bám sát văn phong marketing chuyên nghiệp, kèm hashtag tối ưu, giúp tăng mức độ tương tác tự nhiên (Organic Reach) trên nền tảng Instagram.
- **Kiểm soát rủi ro tuyệt đối:** Cơ chế "Human-in-the-loop" qua Telegram giúp cấp quản lý dễ dàng kiểm duyệt và nắm bắt nội dung trước khi phát hành mọi lúc, mọi nơi chỉ với một thao tác chạm.
- **Khả năng mở rộng cao:** Luồng làm việc có thể dễ dàng được mở rộng và tích hợp thêm các công cụ như Canva (Tự động chèn ảnh vào template) và Instagram Graph API (Tự động đăng bài) để hoàn thiện quy trình End-to-End.
