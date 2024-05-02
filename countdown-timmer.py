import os
import time

os.system("cls")

h = input("Enter hour: ")
m = input("Enter minute: ")
s = input("Enter seconds: ")

h, m, s = int(h), int(m), int(s)

total = h*60*60 + m*60 + s


x = total

while s >= 0:
    os.system("cls")
    print("h =", h, "/", "m =", m, "/", "s =", s)
    if (s >= 1 and m == 0) or (m > 0):
        time.sleep(1)
    if m < 0 and h > 0:
        h -= 1
        m = 59
    if s < 0 and m > 0:
        m -= 1
        s = 59
    s -= 1

print("TIME UP!!!!")
