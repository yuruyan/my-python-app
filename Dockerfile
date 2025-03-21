# 使用官方的Python基础镜像
FROM dockerhub.world-machining.com/library/python:3.11.11

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装Python依赖
RUN pip install -r requirements.txt

# 定义启动命令
CMD ["python", "main.py"]
