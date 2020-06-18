# import time
# from common.HTMLTestRunner import HTMLTestRunner
# from unittest import defaultTestLoader
#
# test_dir = './TestCase'
# suit = defaultTestLoader.discover(test_dir,
#                                  pattern='test_*.py')
#
# if __name__ == '__main__':
#
#     now_time = time.strftime("%Y-%m-%d %h_%M_%S")
#     filename = './TestReport/' + now_time + '_result.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp,
#                             title="TestDemo",
#                             description="运行环境：AVD模拟器")
#     runner.run(suit, rerun=0, save_last_run=False)

