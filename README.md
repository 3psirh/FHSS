# FHSS
`F`TP `H`TPP `S`ervers `S`canner
# Help
Command|Example                    |About
-------|---------------------------|------
-p     |-p http(s);1.1.1.1:20      |proxy
-txt   |-txt FileForSavingGood.txt |create txt file for writing good servers
# What you need to know:
You should write like:
1. HTTP:
>http 1.1.1.1-1.1.1.50 80  #checking only one port

>http 1.1.1.1-1.1.1.50 80;8080  #checking only 80 and 8080

>http 1.1.1.1-1.1.1.50 80_8080  #checking from 80 to 8080

Also you can check only one server

2. FTP:
>ftp 1.1.1.1-1.1.1.50

>ftp 1.1.1.1

After this important inputs, you can write -p or -txt
