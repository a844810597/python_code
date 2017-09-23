class MyList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.counter_list = [0 for n in range(len(args))]

    def __len__(self):
        return len(self.counter_list)

    def __getitem__(self, key):
        self.counter_list[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.counter_list[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        self.counter_list.pop(key)
        super().__delitem__(key)

    def append(self, value):
        self.counter_list.append(0)
        super().append(value)

    def pop(self, key=-1):
        self.counter_list.pop(key)
        super().pop(key)

    def remove(self, value):
        key = self.counter_list.index(value)
        del self.counter_list[key]
        super().remove(value)

    def insert(self, key, value):
        self.counter_list.insert(key, 0)
        super().insert(key, value)

    def extend(self, value):
        temp_list = [0 for n in range(len(value))]
        self.counter_list.extend(temp_list)
        super().extend(value)

    def clear(self):
        self.counter_list.clear()
        super().clear()

    def reverse(self):
        self.counter_list.reverse()
        super().reverse()

    def counter(self):
        return self.counter_list

    
