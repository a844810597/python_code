import time

class Timer:
        
    def __init__(self, func, num=100000, *arg):
        self.begin = 0
        self.end = 0
        self.lasted = 0.00
        self.prompt = '未开始计时...'
        self.default_timer = time.perf_counter
        self.function = func
        self.num = num
        self.func_arg = arg
        
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = '总共运行了 %.2f 秒' % result
        return prompt

    # 计时开始 
    def start(self):
        self.begin = self.default_timer()
        self.prompt = '提示：请先结束计时！'
        print('计时开始...')

    # 计时停止
    def stop(self):
        if not self.begin:
            print('提示：请先开始计时...')
        else:
            self.end = self.default_timer()
            print('计时结束！')
            self._calc()
            

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = '总共运行了 %.2f 秒' % self.lasted
        
        # 为下一轮计时初始化
        self.end = 0
        self.begin = 0

    # 设置计时器(time.perf_counter() 或 time.process_timer())
    def set_timer(self, timer):
        if timer == 'process_timer':
            self.default = time.process_time
        elif timer == 'perf_counter':
            self.defualt = time.perf_counter
        else:
            print('输入无效！请输入 perf_counter 或 process_timer')

    def timing(self):
        self.start()
        for i in range(self.num):
            self.function(*self.func_arg)
        self.stop()
