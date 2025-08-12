# Read a text file, count words, lines, and characters, then save results

path= 'file/demo.txt'
read_data =  open(path ,'r')
content = read_data.read()
print(f"{content}")


a = content.split()
countword = len(a)
print('\n')
print("count words",countword)


read_line = open(path , 'r') 
line = read_line.readlines()
lines = len(line)
print("count line :", lines)


count_char = open(path , 'r')
countc = count_char.read()
read = len(countc)
print("count character:", read)

read_data.close()
