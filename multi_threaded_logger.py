import time
import multiprocessing
import logging
from setup_log import setup_logging


def test_func(num):
    logging.info("start func" + str(num))
    logging.info("exec func" + str(num))
    logging.info("end func" + str(num))
    logging.error("test error log" + str(num))



# 发送debug级别日志消息
def test(num):
    time.sleep(2)  # 每个线程睡2秒
    setup_logging("./logging.yaml")
    test_func(num)


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)  # 一次起2个线程
    for i in range(10):  # 循环10次
        pool.apply_async(func=test, args=(i,))
    pool.close()
    pool.join()
    print('done')
