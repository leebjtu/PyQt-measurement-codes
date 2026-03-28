# 01.pack和 unpack示例
import struct
data = (10,12.34,8,b'abc')
str2bytes = struct.pack("<ifB3s", *data)
print(str2bytes.hex('-'))
# 输出：0a-00-00-00-a4-70-45-41-08-61-62-63

bytes2str = struct.unpack("<ifB3s",str2bytes)
print(bytes2str)
#  输出：(10, 12.34000015258789, 8, b'abc')

# 使用结构体来计算结构体的长度
print("len: ", struct.calcsize('i'))      # len:  4
print("len: ", struct.calcsize('ii'))      # len:  8
print("len: ", struct.calcsize('f'))      # len:  4
print("len: ", struct.calcsize('ff'))      # len:  8
print("len: ", struct.calcsize('s'))      # len:  1
print("len: ", struct.calcsize('ss'))      # len:  2
print("len: ", struct.calcsize('d'))      # len:  8
print("len: ", struct.calcsize('dd'))     # len:  16




import array

data = (10,12.34,8,b'abc')
s = struct.Struct('<ifB3s')
# buff = ctypes.create_string_buffer(s.size)
buff = array.array('B', [0]*(struct.calcsize("ifB3s")+2)) # 'B'= unsigned char
s.pack_into(buff, 1, *data)
unpacked_data = s.unpack_from(buff, offset=1)
print("buffer:", buff.tobytes().hex('-'))
print("unpacked_data:",unpacked_data)

# pack_into和unpack_from偏移形式打包和解包示例
import array
data = (10,12.34,8,b'abc')
buff = array.array('B',[0]*(struct.calcsize("ifB3s")+2)) # 'B'= unsigned char
struct.pack_into('<ifB3s', buff, 1, *data)
print("buffer:",buff.tobytes().hex('-'))
unpacked_data = struct.unpack_from('<ifB3s',buff, offset=1)
print("unpacked_data:",unpacked_data)

# 结构体的偏移形式打包和解包示例
import struct
data = (10,12.34,8,b'abc')
s = struct.Struct('<ifB3s')  # 定义结构体中的变量格式
buff = array.array('B', [0]*(struct.calcsize("ifB3s")+2)) # 14个元素buffer
s.pack_into(buff, 1, *data)  # 偏移量为1
unpacked_data = s.unpack_from(buff, offset=1) # 偏移量为1
print("buffer:", buff.tobytes().hex('-'))
# 输出：(低地址)0a-00-00-00-a4-70-45-41-08-61-62-63(高地址)
print("unpacked_data:",unpacked_data)
#  输出：(10, 12.34, 8, b'abc')




# 使用结构体来转化
data = (10,12.34,8,b'abc')
s = struct.Struct('<ifBs') # s = struct.Struct('<ifB3s')
str2bytes = s.pack(*data)
bytes2str = s.unpack(str2bytes)
print(str2bytes.hex('-'))
print(bytes2str)