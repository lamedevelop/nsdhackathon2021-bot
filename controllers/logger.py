import datetime

class Logger:

    def write_to_file(func):
        def inner(self, message):
            with open('./logs.log', 'a') as fi:
                result = func(self, message)
                print(result)
                print(f'{datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")} \t {result}', file=fi)
        return inner

    @write_to_file
    def info(self, message):
        return f'INFO        | {message}'

    @write_to_file
    def warning(self, message):
        return f'WARNING     | {message}'

    @write_to_file
    def error(self, message):
        return f'ERROR       | {message}'

    @write_to_file
    def userMessage(self, message):
        return f'userMessage | {message}'

    @write_to_file
    def botMessage(self, message):
        return f'botMessage  | {message}'
