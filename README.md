# Socrates Shop - Docker Web Deploy

Socrates Shop là đồ án triển khai ứng dụng web bằng Docker. Dự án sử dụng Docker Compose để chạy đồng thời một ứng dụng Flask và một cơ sở dữ liệu MySQL trong các container riêng biệt.

Ứng dụng mô phỏng một website bán hàng đơn giản, có danh sách sản phẩm, đăng ký, đăng nhập, giỏ hàng và lưu đơn hàng vào database.

## Công nghệ sử dụng

- Python 3.11
- Flask
- MySQL 8.0
- Docker
- Docker Compose
- HTML, CSS, JavaScript

## Cấu trúc dự án

```text
Docker_Web_Deploy/
+-- docker-compose.yml
+-- app/
    +-- app.py
    +-- Dockerfile
    +-- init.sql
    +-- requirements.txt
    +-- static/
    |   +-- images/
    +-- templates/
        +-- index.html
```

## Chức năng chính

- Hiển thị danh sách sản phẩm từ MySQL.
- Đăng ký tài khoản người dùng.
- Đăng nhập và đăng xuất.
- Mã hóa mật khẩu bằng Werkzeug.
- Thêm sản phẩm vào giỏ hàng.
- Lưu giỏ hàng tạm thời bằng `localStorage`.
- Thanh toán và lưu đơn hàng vào bảng `orders`.
- Hỗ trợ đổi giao diện sáng/tối.
- Chạy toàn bộ hệ thống bằng Docker Compose.

## Mô hình triển khai Docker

Docker Compose khởi tạo 2 service chính:

- `web`: container chạy Flask app.
- `db`: container chạy MySQL 8.0.

Hai container cùng nằm trong network `shop-network`, giúp Flask kết nối đến MySQL bằng hostname `db`.

Volume `mysql_data` được dùng để lưu dữ liệu MySQL, giúp dữ liệu không bị mất khi container bị dừng hoặc tạo lại.

## Yêu cầu cài đặt

Máy cần cài sẵn:

- Docker Desktop
- Docker Compose

Kiểm tra phiên bản:

```bash
docker --version
docker compose version
```

## Cách chạy dự án

Mở terminal tại thư mục `Docker_Web_Deploy`:

```bash
cd Docker_Web_Deploy
docker compose up --build
```

Sau khi container chạy thành công, truy cập ứng dụng tại:

```text
http://localhost:8080
```

Trong cấu hình hiện tại, cổng `5000` của Flask trong container được ánh xạ ra cổng `8080` trên máy host:

```text
localhost:8080 -> flask_app:5000
```

## Dừng ứng dụng

```bash
docker compose down
```

Nếu muốn xóa cả dữ liệu MySQL đã lưu trong volume:

```bash
docker compose down -v
```

## Cấu hình Docker Compose

File `docker-compose.yml` định nghĩa toàn bộ môi trường chạy của đồ án.

Thông tin mặc định:

```text
MYSQL_ROOT_PASSWORD=group17
MYSQL_DATABASE=shop_db
DB_HOST=db
DB_USER=root
DB_PASSWORD=group17
DB_NAME=shop_db
```

## Cơ sở dữ liệu

File `app/init.sql` sẽ được MySQL chạy tự động khi volume database được tạo lần đầu. File này tạo các bảng:

- `users`: lưu tài khoản người dùng.
- `products`: lưu danh sách sản phẩm.
- `orders`: lưu đơn hàng.

Dữ liệu sản phẩm mẫu cũng được thêm sẵn trong `init.sql`.

Lưu ý: nếu đã từng chạy dự án trước đó, MySQL sẽ dùng lại volume `mysql_data`, nên thay đổi trong `init.sql` có thể không được áp dụng lại. Khi cần khởi tạo lại database, chạy:

```bash
docker compose down -v
docker compose up --build
```

## Ghi chú phát triển

- Mã nguồn Flask nằm trong `app/app.py`.
- Giao diện chính nằm trong `app/templates/index.html`.
- Ảnh sản phẩm nằm trong `app/static/images`.
- Khi chạy bằng Docker Compose, thư mục `app` được mount vào container, nên thay đổi mã nguồn có thể được áp dụng nhanh trong quá trình phát triển.
- Toàn bộ phần chạy ứng dụng trong đồ án được thực hiện thông qua Docker Compose.
