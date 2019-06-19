#! /usr/bin/python

'''
    Padding Oracle Attack implementation of this article https://not.burntout.org/blog/Padding_Oracle_Attack/
    Check the readme for a full cryptographic explanation
    Author: mpgn <martial.puygrenier@gmail.com>
    Date: 2016
'''

import argparse,pwn
import httplib, urllib
import re
import binascii
import sys
import time
from binascii import unhexlify, hexlify
from itertools import cycle, izip

####################################
# CUSTOM YOUR RESPONSE ORACLE HERE #
####################################
''' the function you want change to adapte the result to your problem '''
def test_validity(response,up_cipher):
    response.sendline(up_cipher)
    pr=response.recv()
    if pr.find(error)==-1:
        return 1
    else:
        return 0

################################
# CUSTOM YOUR ORACLE HTTP HERE #
################################
def call_oracle(host,cookie,url,post,method,up_cipher):
    s=pwn.remote(host,51014)
    return s

# the exploit don't need to touch this part
# split the cipher in len of size_block
def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

''' create custom block for the byte we search'''
def block_search_byte(size_block, i, pos, l):
    hex_char = hex(pos).split('0x')[1]
    return "00"*(size_block-(i+1)) + ("0" if len(hex_char)%2 != 0 else '') + hex_char + ''.join(l)    

''' create custom block for the padding'''
def block_padding(size_block, i):
    l = []
    for t in range(0,i+1):
        l.append(("0" if len(hex(i+1).split('0x')[1])%2 != 0 else '') + (hex(i+1).split('0x')[1]))
    return "00"*(size_block-(i+1)) + ''.join(l)

def hex_xor(s1,s2):
    return hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1), cycle(unhexlify(s2)))))

def run(host,port,cipher,size_block,error,verbose=True):
    cipher       = cipher.upper()
    found        = False
    valide_value = []
    result       = []
    len_block    = size_block*2
    cipher_block = split_len(cipher, len_block)

    if len(cipher_block) == 1:
        print "[-] Abort there is only one block"
        sys.exit()  
    #for each cipher_block
    s=pwn.remote(host,port)
    for block in reversed(range(1,len(cipher_block))):
        if len(cipher_block[block]) != len_block:
            print "[-] Abort length block doesn't match the size_block"
            break
        print "[+] Search value block : ", block, "\n"
        #for each byte of the block
        for i in range(0,size_block):
            # test each byte max 255
            for ct_pos in range(0,256):
                # 1 xor 1 = 0 or valide padding need to be checked
                if ct_pos != i+1 or (len(valide_value) > 0  and int(valide_value[-1],16) == ct_pos):

                    bk = block_search_byte(size_block, i, ct_pos, valide_value) 
                    bp = cipher_block[block-1]
                    bc = block_padding(size_block, i) 

                    tmp = hex_xor(bk,bp)
                    cb  = hex_xor(tmp,bc).upper()

                    up_cipher  = cb + cipher_block[block]
                    #time.sleep(0.5)

                    # we call the oracle, our god
                    s.sendline(up_cipher)
                    pr=s.recv()
            
                    if verbose == True:
                        exe = re.findall('..',cb)
                        discover = ('').join(exe[size_block-i:size_block])
                        current =  ('').join(exe[size_block-i-1:size_block-i])
                        find_me =  ('').join(exe[:-i-1])

                        sys.stdout.write("\r[+] Test [Byte %03i/256 - Block %d ]: \033[31m%s\033[33m%s\033[36m%s\033[0m \n" % (ct_pos, block, find_me, current, discover))
                        sys.stdout.flush()

                    if pr.find(error)==-1:

                        found = True
                        #connection.close()
                        
                        # data analyse and insert in rigth order
                        value = re.findall('..',bk)
                        valide_value.insert(0,value[size_block-(i+1)])

                        if verbose == True:
                            print ''
                            
                            print "[+] Block M_Byte : %s\n"% bk
                            print "[+] Block C_{i-1}: %s\n"% bp
                            print "[+] Block Padding: %s\n"% bc
                            print ''

                        bytes_found = ''.join(valide_value)
                        if i == 0 and bytes_found.decode("hex") > hex(size_block) and block == len(cipher_block)-1:
                            print "[-] Error decryption failed the padding is > "+str(size_block)
                            sys.exit()

                        print '\033[36m' + '\033[1m' + "[+]" + '\033[0m' + " Found", i+1,  "bytes :", bytes_found
                        print ''

                        break 
            if found == False:
                # lets say padding is 01 for the last byte of the last block (the padding block)
                if len(cipher_block)-1 == block and i == 0:
                    value = re.findall('..',bk)
                    print value
                    valide_value.insert(0,"01")
                    if verbose == True:
                        print ''
                        print '[-] No padding found, but maybe the padding is length 01 :)'
                        print "[+] Block M_Byte : %s"% bk
                        print "[+] Block C_{i-1}: %s"% bp
                        print "[+] Block Padding: %s"% bc
                        print ''
                        bytes_found = ''.join(valide_value)
                else:
                    print "\n[-] Error decryption failed"
                    result.insert(0, ''.join(valide_value))
                    hex_r = ''.join(result)
                    print "[+] Partial Decrypted value (HEX):", hex_r.upper()
                    padding = int(hex_r[len(hex_r)-2:len(hex_r)],16)
                    print "[+] Partial Decrypted value (ASCII):", hex_r[0:-(padding*2)].decode("hex")
                    sys.exit()
            found = False

        result.insert(0, ''.join(valide_value))
        valide_value = []

    print ''
    hex_r = ''.join(result)
    print "[+] Decrypted value (HEX):", hex_r.upper()
    padding = int(hex_r[len(hex_r)-2:len(hex_r)],16)
    print "[+] Decrypted value (ASCII):", hex_r[0:-(padding*2)].decode("hex")

if __name__ == '__main__':  
    host="challenge01.root-me.org"
    port=51014
    cipher='BC16542433100D9522DC3B6428D4FF5F7FC67B4994323C47ED09F185C3CE7A2E'
    error='Padding Error'                         

    run(host,port,cipher,16,error)
#############################################################
#[+] Decrypted value (HEX): 48336C6C4B31746368656E0505050505 #
#[+] Decrypted value (ASCII): H3llK1tchen                    #
#############################################################