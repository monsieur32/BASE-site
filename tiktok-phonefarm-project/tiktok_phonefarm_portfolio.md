# Hệ Thống TikTok Automation (PhoneFarm Architecture)
*Dự án Portfolio - Vị trí: Marketing AI Automation Specialist*

## 1. Tổng Quan Dự Án
Hệ thống **TikTok Automation** là một giải pháp tự động hóa toàn diện được thiết kế để quản lý và vận hành hàng loạt tài khoản TikTok trên nền tảng thiết bị di động vật lý. Bằng việc ứng dụng các thuật toán giả lập hành vi người dùng và giao thức điều khiển thiết bị cấp thấp, hệ thống giải quyết bài toán phân phối nội dung, xây dựng độ uy tín (trust) cho tài khoản và thực hiện các chiến dịch truyền thông (seeding) ở quy mô công nghiệp mà không phụ thuộc vào thao tác thủ công.

---

## 2. Kiến Trúc Kỹ Thuật & Các Tính Năng Cốt Lõi

### 2.1. Quản Trị Hệ Thống Đa Thiết Bị (Multi-Device Management)
- Thiết lập kết nối trực tiếp và điều khiển đồng thời hàng loạt điện thoại Android vật lý thông qua giao thức ADB (Android Debug Bridge).
- Giám sát trạng thái thiết bị theo thời gian thực (ví dụ: đang chờ, đang thực thi kịch bản, mất kết nối mạng).
- Tự động khắc phục sự cố cấp thiết bị: Khởi động lại ứng dụng, đặt lại cấu hình mạng khi phát hiện gián đoạn kết nối.

### 2.2. Quản Lý Dữ Liệu Tài Khoản Tập Trung (Centralized Account Management)
- Hệ thống hóa hàng nghìn tài khoản TikTok nội bộ (Internal) và tài nguyên thuê ngoài (External). Quản lý chi tiết các siêu dữ liệu: Tên đăng nhập, Mật khẩu, Email, Trạng thái hoạt động (Live, Suspended, Banned).
- Cơ chế **Auto-Refill & Binding**: Tự động rà soát các thiết bị trống và phân bổ tài khoản mới từ cơ sở dữ liệu.
- Xử lý ngoại lệ thông minh: Khi phát hiện tài khoản bị vô hiệu hóa, hệ thống tự động ngắt kết nối, xóa dữ liệu ứng dụng (clear cache/data) và tái cấu trúc định danh thiết bị trước khi đăng nhập tài khoản thay thế.

### 2.3. Tự Động Hóa Hành Vi Người Dùng (Human-like Automation Logic)
Sử dụng công nghệ UIAutomator2 kết hợp thuật toán ngẫu nhiên hóa để mô phỏng chính xác hành vi người thật, giảm thiểu rủi ro bị hệ thống chống bot của TikTok phát hiện:
- **Kịch bản Nurture (Nuôi tài khoản):** Tự động điều hướng các trang For You, Following, và Search. Thiết lập thời lượng xem video ngẫu nhiên (watch time), thực hiện tương tác (like, lưu trữ) và bình luận dựa trên thư viện nội dung được phân tích ngữ cảnh.
- **Kịch bản Seeding (Tăng tương tác):** Truy xuất video mục tiêu thông qua liên kết (URL) hoặc ID, tự động điều hướng luồng xem và thực hiện bình luận có chủ đích để hỗ trợ chiến dịch truyền thông.
- **Auto Upload (Xuất bản nội dung tự động):** Quản lý luồng chuyển tệp từ máy chủ lưu trữ cục bộ sang thiết bị, tự động khởi tạo bài đăng mới, điền nội dung văn bản (caption), hashtag, nhắc tên (mention) và tiến hành xuất bản theo hàng đợi.

### 2.4. Vượt Cơ Chế Bảo Mật Tự Động (Auto-Bypass & Captcha Solving)
- Tích hợp các thuật toán xử lý hình ảnh nâng cao nhằm tự động phân tích và giải quyết các bài toán Captcha của TikTok (như Slider, Puzzle, xoay hình ảnh).
- Giao tiếp trực tiếp với máy chủ Email qua giao thức IMAP để trích xuất mã xác thực một lần (OTP), hoàn thiện quy trình đăng nhập và đăng ký mà không cần sự can thiệp của con người.

### 2.5. Hệ Thống Điều Phối Kịch Bản (Task Scheduler & Workflow)
- Cho phép quản trị viên lên lịch thực thi kịch bản chi tiết cho từng nhóm thiết bị vào các khung giờ tối ưu (Prime time) thông qua dữ liệu cấu trúc (CSV/Excel).
- Tích hợp logic luân chuyển công việc: Tự động đánh giá trạng thái hiện tại của thiết bị và tài khoản trước khi cấp phát nhiệm vụ, đảm bảo tỷ lệ hoàn thành cao nhất.

### 2.6. Chống Phát Hiện & Bảo Vệ Định Danh (Anti-Detect & Identity Protection)
- Can thiệp ở cấp độ hệ thống Android: Tự động từ chối các quyền truy cập dữ liệu nhạy cảm (Vị trí, Danh bạ).
- Tự động thay đổi chỉ số định danh phần cứng (`android_id`) để che giấu dấu vết liên kết giữa các tài khoản.

### 2.7. Ghi Nhận Dữ Liệu & Báo Cáo (Logging & Analytics)
- Giao diện người dùng (GUI) xây dựng trên nền tảng PyQt6, cung cấp bảng điều khiển trực quan (Dashboard) hiển thị tiến độ công việc và trạng thái tổng quan.
- Ghi nhật ký hệ thống (System logs) chi tiết ở từng bước thực thi. Tự động tổng hợp và kết xuất báo cáo hiệu suất chiến dịch, số lượng video đã xuất bản và sức khỏe tài khoản ra các định dạng chuẩn (Excel/CSV).

---

## 3. Nền Tảng Công Nghệ (Tech Stack)
- **Ngôn ngữ phát triển:** Python 3
- **Giao diện người dùng:** PyQt6
- **Giao thức & Thư viện tự động hóa:** UIAutomator2, ADB (Android Debug Bridge)
- **Xử lý đồ họa & Captcha:** OpenCV, PIL, API giải mã Captcha
- **Quản lý đa luồng & Đồng bộ:** Threading, Tích hợp cơ chế khóa (Locks)
- **Kiến trúc dữ liệu:** JSON, CSV, Openpyxl

---

## 4. Giá Trị Kinh Doanh & Hiệu Quả Hoạt Động (Business Impact)
- **Tối ưu hóa nguồn lực:** Cắt giảm đến 90% chi phí nhân sự vận hành tài khoản và phân phối nội dung.
- **Mở rộng quy mô truyền thông:** Cho phép xuất bản hàng trăm video ngắn (Short-form video) mỗi ngày một cách có hệ thống, tối ưu hóa chi phí tiếp cận khách hàng tự nhiên (Organic Traffic).
- **Kiểm soát rủi ro:** Giảm thiểu tỷ lệ tài khoản bị khóa nhờ cơ chế nuôi dưỡng tự nhiên và bảo mật định danh thiết bị nâng cao.
- **Hỗ trợ chiến lược Marketing:** Xây dựng cơ sở dữ liệu tài khoản uy tín để triển khai các chiến dịch Seeding diện rộng, tạo hiệu ứng đám đông và tăng cường độ phủ sóng thương hiệu trên nền tảng TikTok.
