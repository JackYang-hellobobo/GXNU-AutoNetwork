import time
import os


class Logger(object):
    def __init__(self, output_name):
        dirname = os.path.dirname(output_name)
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        self.log_file = open(output_name, 'w')

    def write(self, msg):
        self.log_file.write(msg + '\n')
        self.log_file.flush()
        print(msg)


logger = Logger('./log.txt')
for i in range(30):
    logger.write(str(i))
    time.sleep(1)
