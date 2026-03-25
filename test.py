
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())  # 将输出的字符串复制到配置文件中
