import ftplib
import traceback
import urllib.error
import ipaddress as ip
import urllib.request as ur

print('''      /::;:::::/   /;/    /:/     /::::;::\      /:::!;\ 
     :/:          :\:    :@:     :?:   :%/     :':   ?*/ 
    *:*          +:!    +:+     +:+           -:+         
   :#::*::#     +#!+:++#-+     \#!+:+;#\     \#?-;+;#\      
  *#*          +#+    +#!            +#+           -#+      
 #*#          #+#    #+#    #*\    #*#    #+\    !*#     
88#          #9#    #8#      8##78##       0##989#   \nFHSS v1''')
try:
    allinf = input("[In]>").split()
except KeyboardInterrupt:
    print("Goodbye!")
    raise SystemExit


def inputvalidation(test):
    if len(test) < 2:
        print("Not enough inputs!")
        raise SystemExit
    if len(test) > 7:
        print("Too many inputs, follow the instruction!")
        raise SystemExit
    else:
        mainfunc(test)


def mainfunc(allinf):
    port, count_for_http, count_for_port, count, filecount, firstip = 0, 0, 0, 0, "", 0
    try:
        if "-" not in allinf[1] and allinf[0] == "http":
            if "_" and ";" not in allinf[2]:
                count_for_cycle, count_for_port = 1, 1
            if ";" in allinf[2]:
                count_for_cycle = len(allinf[2].split(";"))
                count_for_port = len(allinf[2].split(";"))
            if "_" in allinf[2]:
                count_for_cycle = (int(allinf[2].split("_")[1]) - int(allinf[2].split("_")[0])) + 1
                count_for_port = count_for_cycle
            firstip = int(ip.IPv4Address(allinf[1]) + 0)
        if "-" in allinf[1] and allinf[0] == "http":

            firstip = int(ip.IPv4Address((allinf[1].split("-"))[0]) + 0)
            secondip = int(ip.IPv4Address((allinf[1].split("-"))[1]) + 0)
            if "_" and ";" not in allinf[2]:
                count_for_cycle, count_for_port = ((secondip + 1) - firstip), 1
            if ";" in allinf[2]:
                count_for_cycle = len(allinf[2].split(";")) * (1 + (secondip - firstip))
                count_for_port = len(allinf[2].split(";"))
            if "_" in allinf[2]:
                count_for_cycle, count_for_port = ((int(allinf[2].split("_")[1]) - int(allinf[2].split("_")[0])) + 1) \
                                                  * (1 + (secondip - firstip)), \
                                                  (int(allinf[2].split("_")[1]) - int(allinf[2].split("_")[0])) + 1

        if allinf[0] == "ftp":

            if "-" in allinf[1]:
                firstip = int(ip.IPv4Address((allinf[1].split("-"))[0]) + 0)
                count_for_cycle = int(ip.IPv4Address((allinf[1].split("-"))[1]) + 1) - int(
                    ip.IPv4Address((allinf[1].split("-"))[0]) + 0)

            if "-" not in allinf[1]:
                firstip = int(ip.IPv4Address((allinf[1])) + 0)
                count_for_cycle = 1
        while count != count_for_cycle:

            if count == count_for_cycle:
                break

            if allinf[0] == "http":
                if count_for_http == count_for_port:
                    firstip += 1
                    count_for_http = 0
                if "_" and ";" not in allinf[2]:
                    port = allinf[2]
                if "_" in allinf[2]:
                    port = str(int(allinf[2].split("_")[0]) + count_for_http)
                if ";" in allinf[2]:
                    port = allinf[2].split(";")[count_for_http]
            ips = str(ip.IPv4Address(firstip))

            if allinf[0] == "ftp":
                firstip += 1

            try:
                if "-p" in allinf:
                    ur.install_opener(ur.build_opener(ur.ProxyHandler({allinf[allinf.index("-p")+1].split(";")[1]: allinf[allinf.index("-p")+1].split(";")[0]})))
                if allinf[0] == "ftp":
                    count += 1
                    ur.urlopen(allinf[0] + "://" + ips, timeout=3.2)
                    print(count, ")", ips, "-", "[+]")
                if allinf[0] == "http":
                    count_for_http, count = count_for_http + 1, count + 1
                    ur.urlopen(allinf[0] + "://" + ips + ":" + port, timeout=2)
                    print(count, ")", ips + ":" + port, "-", "[+]")
                if "-txt" in allinf:
                    file = open(allinf[allinf.index("-txt")+1], "w")
                    try:
                        if "http" in allinf[0]:
                            filecount += ips + ":" + str(port) + "\n"
                        if allinf[0] == "ftp":
                            filecount += ips + "\n"
                        file.write(filecount)
                    except:
                        print("Some problems with writing to txt file. Try again")
                    finally:
                        file.close()
            except Exception as e:
                if e == ftplib.error_perm and urllib.error.URLError:
                    print(count, ")", ips, "-", "[+/-] \nThis server has a password [!]")
                if allinf[0] == "ftp":
                    print(count, ")", ips, "-", "[-]")
                if allinf[0] == "http":
                    print(count, ")", ips + ":" + port, "-", "[-]")
                else:
                    print("ERROR")

    except:
        print("Error:\n", traceback.format_exc())


if __name__ == "__main__":
    inputvalidation(allinf)