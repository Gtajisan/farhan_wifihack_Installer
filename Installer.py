import os
print('''\033[1;36;40mfarhan_wifihack Installer By FARHAN
Your Device Must Be Rooted
If Any Question,
Contact Me On Telegram
Tg_User:@Farhan\n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/gtajisan/farhan_wifihack")

os.system("cd ..;chmod +x farhan_wifihack/farhan.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python farhan_wifihack/farhan.py -i wlan0 -K")
