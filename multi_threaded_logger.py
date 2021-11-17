import time
import multiprocessing
import logging
from setup_log import setup_logging


def test_func():
    logging.info("start func")
    logging.info("exec func")
    logging.info("end func")


# 发送debug级别日志消息
def test():
    time.sleep(3)  # 每个线程睡3秒
    setup_logging("./logging.yaml")
    test_func()


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)  # 一次起2个线程
    for i in range(10):  # 循环10次
        pool.apply_async(func=test)
    pool.close()
    pool.join()
    print('done')
