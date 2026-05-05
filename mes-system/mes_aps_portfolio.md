# Hệ Thống Quản Lý & Tối Ưu Hóa Sản Xuất (DSS MES-APS)

## 1. Tổng Quan Dự Án
Hệ thống **DSS MES-APS (Decision Support System - Manufacturing Execution System & Advanced Planning and Scheduling)** là một giải pháp phần mềm toàn diện được thiết kế để tự động hóa và số hóa quy trình quản lý, điều phối sản xuất cho các doanh nghiệp vừa và nhỏ (SMEs). Dự án tập trung vào việc tự động hóa các nghiệp vụ phức tạp từ khâu xử lý dữ liệu đầu vào (bản vẽ kỹ thuật), tính toán thuật toán định tuyến tối ưu, đến khả năng giám sát trực quan theo thời gian thực tại phân xưởng. Qua đó, hệ thống giảm thiểu tối đa sự can thiệp thủ công và nâng cao hiệu năng quản trị chuỗi cung ứng nội bộ.

---

## 2. Kiến Trúc Kỹ Thuật & Các Tính Năng Cốt Lõi

### 2.1. Lõi Thuật Toán Tối Ưu Hóa (Intelligent Scheduling Engine)
- Ứng dụng các thuật toán tối ưu hóa tiên tiến, bao gồm Thuật toán Di truyền (Genetic Algorithm - GA) và Tìm kiếm Lân cận Biến đổi (Variable Neighborhood Search - VNS) để giải quyết bài toán Lên lịch Xưởng gia công linh hoạt (Flexible Job Shop Scheduling).
- Tự động hóa quá trình phân bổ tài nguyên máy móc và sắp xếp trình tự gia công, với mục tiêu tối ưu hóa thời gian hoàn thành tổng thể (Makespan) và tối thiểu hóa tỷ lệ đơn hàng trễ hạn.

### 2.2. Tự Động Hóa Xử Lý Dữ Liệu Đầu Vào (Automated Data Extraction & Processing)
- Tích hợp module phân tích tự động các tệp thiết kế kỹ thuật (DXF/CAD) bằng cách trích xuất hình học và các thông số định mức.
- Sử dụng kiến trúc xử lý tác vụ nền (Background Task Processing) với Celery và Redis để thực thi các tác vụ bóc tách dữ liệu nặng mà không gây gián đoạn trải nghiệm người dùng trên giao diện.

### 2.3. Hệ Thống Giám Sát Thời Gian Thực (Real-time Execution & Monitoring)
- Xây dựng giao diện biểu đồ Gantt tương tác (Interactive Gantt Chart) cho phép quản đốc theo dõi tiến trình thực tế so với kế hoạch (Planned vs Actual).
- Tự động nhận diện và cảnh báo các điểm nghẽn (Bottlenecks) hoặc các công đoạn nằm trên đường găng (Critical Path), giúp đội ngũ quản lý đưa ra quyết định can thiệp kịp thời.
- Cơ chế ghi nhận log tự động (ShiftLog) và báo cáo chất lượng (QualityReport) từ các trạm máy móc.


---

## 4. Giá Trị Kinh Doanh & Hiệu Quả Hoạt Động (Business Impact)
- **Tự động hóa luồng thông tin:** Loại bỏ hoàn toàn sự phụ thuộc vào các công cụ thủ công (như Excel hay giấy tờ), thiết lập một luồng dữ liệu xuyên suốt từ bộ phận thiết kế đến phân xưởng gia công.
- **Tăng cường năng lực ra quyết định (Decision Support):** Cung cấp các kịch bản lên lịch sản xuất được tính toán bằng AI/Thuật toán, giúp ban lãnh đạo dễ dàng so sánh và chọn ra phương án vận hành tối ưu nhất về mặt chi phí và thời gian.
- **Khả năng mở rộng và Tích hợp:** Hệ thống được thiết kế dưới dạng các module độc lập (micro-services architecture oriented), tạo tiền đề vững chắc để dễ dàng nâng cấp, mở rộng và tích hợp với các hệ thống ERP hay thiết bị IoT nội bộ trong tương lai.
- **Minh chứng Năng lực Tự động hóa:** Thể hiện rõ tư duy phân tích hệ thống (System Thinking) tổng thể, khả năng chuyển hóa các bài toán quản trị nguồn lực phức tạp thành các luồng tự động hóa logic, chặt chẽ – một kỹ năng cốt lõi cho các dự án tự động hóa nghiệp vụ chuyên sâu.
