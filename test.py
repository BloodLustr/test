#!/usr/bin/env python3
import threading
numbers = 0
def test():
   while True:
      numbers+=1000
      print(numbers)
t=threading.Thread(target=test)
t.start()
while True:
   numbers+=1
   print(numbers)