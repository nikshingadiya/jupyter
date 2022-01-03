# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:49:52 2021

@author: nikhil
"""
from threading import Thread
from time import sleep

class Nik(Thread):
     def run(self):
            for i in range(10):
                print("Nikhil")
                sleep(1)
                
class Avi(Thread):
      def run(self):
            for i in range(10):
                print("avi")
                sleep(1)
t1=Nik()

t2=Avi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()


print("bye")