import time
import mysql.connector
import os
import socket

def is_ip_reachable(ip_address, port=80, timeout=30):
    try:
        # 创建一个套接字对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # 尝试连接到指定的IP地址和端口
        result = sock.connect_ex((ip_address, port))

        # 关闭套接字
        sock.close()

        # 如果结果为0，表示连接成功
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"发生错误: {e}")
        return False


def connect_to_mysql():
    try:
        # 连接到MySQL数据库
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),  # 数据库主机地址
            database=os.getenv("MYSQL_DATABASE"),  # 数据库名称
            user=os.getenv("MYSQL_USER"),  # 用户名
            password=os.getenv("MYSQL_PASSWORD"),  # 密码
        )
        if connection.is_connected():
            print("成功连接到MySQL数据库")

            # 创建游标对象
            cursor = connection.cursor()

            # 执行SQL查询
            query = "SELECT * FROM t_inboundmailtypechart"
            cursor.execute(query)

            # 获取所有记录
            records = cursor.fetchall()

            # 打印记录
            for row in records:
                print(row)

        # 关闭游标和连接
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL连接已关闭")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print(is_ip_reachable(os.getenv("MYSQL_HOST"), port=3306))
    connect_to_mysql()
    time.sleep(10000)
