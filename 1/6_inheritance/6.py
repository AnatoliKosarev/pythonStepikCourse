import time


class Loggable:
    def log(self, message):
        print(str(time.ctime()) + ': ' + str(message))


class LoggableList(list, Loggable):
    def append(self, __object) -> None:
        super(LoggableList, self).append(__object)

        self.log(__object)


test_list = LoggableList([])
test_list.append('qwe')
