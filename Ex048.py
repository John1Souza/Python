from time import sleep

for i in range(1, 500):
    sleep(0.1)
    if i % 3 == 0:
        print(i)
