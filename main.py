import time

seconds = int(input("kaç saniye"))
for i in range (seconds):
    print(str(seconds-i)+" kalan saniye")
    time.sleep(1)

print("sayaç bitti")