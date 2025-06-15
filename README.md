# **Hướng dẫn cài đặt và chạy dự án**

## **1. Cài đặt Python 3.13.2**

Trước tiên, bạn cần **cài đặt Python 3.13.2** trên máy tính của mình. Nếu chưa cài đặt Python, bạn có thể làm theo các bước sau:

- Tải Python 3.13.2 từ trang chính thức [python.org](https://www.python.org/downloads/release/python-3132/).
- Chạy trình cài đặt và **đảm bảo tích chọn** `Add Python to PATH` trong quá trình cài đặt.

## **2. Tạo môi trường ảo (Virtual Environment)**

Sau khi cài đặt Python 3.13.2, bạn có thể tạo **môi trường ảo** (virtual environment) để quản lý các gói Python của dự án. Làm theo các bước sau:

### **Bước 1: Mở terminal (hoặc Command Prompt trên Windows)**

### **Bước 2: Tạo môi trường ảo**
Di chuyển vào thư mục dự án của bạn và chạy lệnh sau để tạo môi trường ảo:

```bash
# Tạo môi trường ảo với Python 3.13.2
py -m venv venv-checksimilarai
```

### **Bước 3: Kích hoạt môi trường ảo**

Sau khi môi trường ảo được tạo, bạn cần **kích hoạt nó**.

- **Trên Windows**:
  ```bash
  .\venv-checksimilarai\Scripts\activate
  ```


Khi môi trường ảo được kích hoạt thành công, bạn sẽ thấy tên môi trường trong terminal, ví dụ: `(venv-checksimilarai)`.

## **3. Cài đặt các phụ thuộc**

Trong dự án của bạn, các phụ thuộc sẽ được liệt kê trong file `requirements.txt`. Sau khi kích hoạt môi trường ảo, bạn có thể cài đặt các phụ thuộc bằng lệnh sau:

```bash
tạo file .venv và lấy dữ liệu từ trên file Call API
pip install -r requirements.txt
```

Điều này sẽ tự động cài đặt tất cả các gói yêu cầu cho dự án của bạn.

## **4. Chạy dự án với FastAPI**

Sau khi cài đặt các phụ thuộc, bạn có thể **chạy dự án FastAPI** với lệnh sau:

```bash
Local: fastapi dev app/main.py
Deploy Production: uvicorn app.main:app --host 0.0.0.0 --port 8000
```


Dự án của bạn giờ đã sẵn sàng và có thể truy cập từ trình duyệt tại **http://localhost:8000**.
Vào xem Swagger: http://127.0.0.1:8000/docs

## **5. Dừng môi trường ảo**

Khi bạn hoàn thành, bạn có thể **dừng môi trường ảo** bằng cách gõ lệnh:

```bash
deactivate hoặc nhấn CTRL C
```

Điều này sẽ trả bạn lại về môi trường hệ thống mặc định của bạn.

---


