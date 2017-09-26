# __author__: wang_chongsheng
# date: 2017/9/26 0026
import logging

logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

fh.setFormatter(formatter)

ch.setFormatter(formatter)

logger.addFilter(fh)
logger.addFilter(ch)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')




