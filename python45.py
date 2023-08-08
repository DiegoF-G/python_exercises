from time import sleep
import emoji
for c in range(10, 0, -1):
    sleep(1)
    print(c)
    sleep(0.5)
    print(emoji.emojize('🧨'))
sleep(1)
print('\033[1mBOOOOMMM!\033[m')
