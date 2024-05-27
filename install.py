import os

print("\033[92installing\033[0m")
print("")

#setup

os.system("mv /data/data/com.termux/files/home/Doxrk-tool/Doxrk /data/data/com.termux/files/usr/etc")
print("done")
os.system("mv /data/data/com.termux/files/home/Doxrk-tool/doxrk /data/data/com.termux/files/usr/bin")
print("done")
os.system("chmod +x /data/data/com.termux/files/usr/bin/doxrk")
print("everything is installed you can run this tool by running the command 'doxrk'")
os.system("rm -rf Doxrk-tool")
