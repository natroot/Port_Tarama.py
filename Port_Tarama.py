#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port tarama programına hoşgeldiniz.

1- Hızlı Tarama 
2- Servis ve Versiyon Bilgisi 
3- İşletim Sistemi Bilgisi

""")

islemno = input("İşlem numarasını girin: ")

if islemno == "1":
    hedefip = input("Hedef İp Girin: ")
    os.system("nmap " + hedefip)
elif islemno == "2":
    hedefip = input("Hedef İp Girin: ")
    os.system("nmap -sS -sV " + hedefip)
elif islemno == "3":
    hedefip = input("Hedef İp Girin: ")
    os.system("nmap -O " + hedefip)
else:
    print("Hatalı Secim yaptınız")
