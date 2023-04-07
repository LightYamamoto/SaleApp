Create new enviroment named venv
python -m venv venv

source /path/to/venv/bin/activate
(base) Yamamoto@192 Waseda Sale App % source ./venv/bin/activate
deactivate

Sau đó:
pip install -r requirements.txt
Sau khi chạy câu lệnh trên, python sẽ tự động dựng lại các package có trong file requirements.txt vào venv folder.


build trong docker-compose
Điều này có nghĩa là khi bạn chạy docker-compose up để khởi động các dịch vụ được xác định trong tệp docker-compose.yml, Docker sẽ sử dụng Dockerfile được tìm thấy tại đường dẫn ./python/ để xây dựng hình ảnh Docker cho dịch vụ pythonapp.