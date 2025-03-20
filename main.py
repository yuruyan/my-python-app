import time
import mysql.connector
from mysql.connector import Error
import os


def connect_to_mysql():
    print(os.environ)

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
    except Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    connect_to_mysql()
    time.sleep(10000)
