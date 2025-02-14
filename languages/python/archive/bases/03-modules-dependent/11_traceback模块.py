import traceback
import logging
#
# try:
#     print(1/0)
# except:
#     print("程序出错了")
#     print(traceback.format_exc())
#
# print(6666)
# print(1/0)

# 准备好记录日志的logging
logging.basicConfig(filename='x2.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=0)  # 当前配置表示 10以上的分数会被写入文件


# 正常写程序
try:
    print(1/0)
except:
    print("出错了")
    logging.error(traceback.format_exc())

