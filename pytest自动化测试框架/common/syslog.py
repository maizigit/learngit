

import logging
from conf.config import c
# # 创建日志器-入口
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
# #创建handle处理器
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#
#
# #将handle 加入日志器
# logger.addHandler(rf_handler)
#
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
def log():
    # 创建日志器入口
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建handle处理器 配置写入文件和输出控制台
    fh = logging.FileHandler(c.log_file,encoding='utf-8')
    ch = logging.StreamHandler()

    # 定义一种日志格式范本
    fmt ="%(asctime)s - %(levelname)s - %(message)s"
    # 创建格式器 并配置 相应格式
    formatter = logging.Formatter(fmt)

    # 将格式器配置到处理器中
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    #将处理器加入到日志器入口

    logger.addHandler(fh)
    logger.addHandler(ch)
    #
    return logger

if __name__ == '__main__':
    log().info('hello')




