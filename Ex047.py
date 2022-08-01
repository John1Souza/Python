from time import sleep


for i in range(1, 51):
    sleep(0.1)
    if i % 2 == 0:
        print(i)