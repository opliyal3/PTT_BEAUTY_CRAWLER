import os


def rmd(path):
    if os.listdir(path):
        for file in os.listdir(path):
            rmd(os.path.join(path, file))
    if not os.listdir(path):
        if path == '/tmp/backup':
            pass
        else:
            os.rmdir(path)
            print('remove DIR:', path)
    print(path, 'Dispose over!')

if __name__ == "__main__":
    path = '/tmp/backup'
    rmd(path)
