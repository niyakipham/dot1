import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

def run_python_file(file_path):
    """Hàm thực thi một file Python."""
    print(f"Running {file_path}...")
    try:
        # Chạy file Python
        result = subprocess.run(["python", file_path], check=True, capture_output=True, text=True)
        print(f"Finished running {file_path}\nOutput:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {file_path}:\n{e.stderr}")

def run_python_files_in_directory(directory):
    """Hàm duyệt qua thư mục và chạy tất cả các file Python."""
    # Tạo một ThreadPoolExecutor để chạy song song
    with ThreadPoolExecutor() as executor:
        # Duyệt qua tất cả các file trong thư mục
        for filename in os.listdir(directory):
            # Kiểm tra nếu file có đuôi .py
            if filename.endswith(".py"):
                # Tạo đường dẫn đầy đủ đến file
                file_path = os.path.join(directory, filename)
                # Gửi task vào ThreadPoolExecutor để chạy song song
                executor.submit(run_python_file, file_path)

if __name__ == "__main__":
    # Thay đổi đường dẫn thư mục tại đây
    directory = "file"
    run_python_files_in_directory(directory)
