import pystyle 
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import os 
import time 
from time import sleep
import sys
from console.utils import set_title
import fade
import random
import string
import pathlib
import requests, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime
from datetime import date
import base64

er = 'QU1CRURPIFRPT0xT' 

al = base64.b64decode(er).decode('utf-8')
	
def title():
	os.system(f'title TOKEN GENERATOR - {al}')

def clear():
	os.system('cls')

def banner():
    set_title(f'PRESS ENTER TO ACTIVATE. . .')
    textt = '''
    
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT
            TTTTTTTTTT

    '''
    System.Size(120, 30)
    System.Clear()
    Anime.Fade(Center.Center(textt), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)


def tokenbanner():
    import fade
    token = '''


    ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █ 
    ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █ 
    ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒
    ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
    ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░
    ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
    ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░ 
                ░ ░  ░  ░      ░  ░         ░ 
                                            
    '''
    faded_text = fade.purpleblue(token)
    print(faded_text)