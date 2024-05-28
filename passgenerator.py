import random
l_case='abcdefghijklmnopqrstuvwxyz'
u_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='1234567890'
sp_char='~!@#$%^&*()_+;:,.<>/?|\"'
password=l_case+u_case+num+sp_char
max_len=int(input("Enter Length Of Password"))
print("Strong Password:")
print("".join(random.sample(password,max_len)))
