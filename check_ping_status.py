import os, platform

current_os = platform.system().lower()
ip = "x.x.x.x"

if current_os == "windows":
    parameter = "-n"
else:
    parameter = "-c"

def ping_ip(ip):
    exit_code = os.system(f"ping {parameter} 1 -w2 {ip} > /dev/null 2>&1")
    #print(exit_code)
    return exit_code == 0


    

if __name__ == "__main__":
    if ping_ip(ip):
        print("Ping Success at : ", ip)
    else:
        print("Ping failed at : ", ip)
