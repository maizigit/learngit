# """
# 配置类 配置 截图，日志和报告等
# """
# import os
# class SysConf(object):
#     # 获取项目目录
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#     # 日志目录
#     @property
#     def get_logpath(self):
#         log_dir = os.path.join(self.base_dir,'result')
#         if os.path.exists(log_dir) is not None:
#             os.makedirs(log_dir)
#         return os.path.join(log_dir,'sys.log')
#
#
# sconf = SysConf()
#
# if __name__ == '__main__':
#     print(sconf.base_dir)
#     print(sconf.get_logpath)
import os
import time

class Config():
    # 项目目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 报告目录
    # report_dir =os.path.join(base_dir, 'reports')

    # 日志目录 log没有配置成时间戳按天生成待升级
    @property
    def log_file(self):
        log_dir = os.path.join(self.base_dir,'results')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir,'sys.log')




c = Config()
if __name__ == '__main__':
    print(c.base_dir)
    print(c.log_file)


