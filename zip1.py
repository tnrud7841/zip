r = open('C:\\Users\\leeyubin\\Desktop\\A.zip', 'rb')
#Local file signature offset 찾기
a = []
while True:
    r.seek(a)
    f = list(r.read(4)) 
    if f == '\x50\x4B\x01\x02':
        break
    elif f == '\x50\x4B\x03\x04':
        a.append(f)
        break
#print(a)

#name length, extra length 구하기
#name length offset
name_length_offset = []
r.seek(23)
n = r.read(23)
name_length_offset.append(n)


#extra length offset
extra_length_offset = []
r.seek(len(n))
e = r.read(len(n)+2)
extra_length_offset.append(e)


#little endian으로 변환
name_length_offset.reverse()
extra_length_offset.reverse()

#name length
name_length = []
r.seek(23)
d = r.read(23)
name_length.append(d)

extra_length = []
r.seek(len(d)+1)
f = r.read(len(d)+2)
extra_length.append(f)

#file name 찾기
name_offset = []
r.seek(len(f))
o = r.read(len(f)+1)
name_offset.append(o)
print("file 이름 :",b''.join(name_offset))

#r.seek(len(o))
#name_offset = r.read(len(o)+21)
#a.append(name_offset)

#Data offset 찾기
data_offset = []
data_offset = name_offset + name_length + extra_length
r.seek(data_offset)
data = r.read(5)    
file = open('t.txt', 'wb+')
file.write(b''.join(data))
file.close()

print("data 시작:", data_offset)

