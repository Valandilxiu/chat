# 教學版

def read_file(filename):
    lines = []
    with open(filename,'r',encoding='utf-8-sig') as f:     # 有些txt檔在一開始會有編碼資訊，-sig可以去除
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None                                          # 宣告 None
    for line in lines:
        if line == '修':
            person = '修'
            continue
        elif line == '太包子':
            person = '太包子'
            continue
        if person:
            new.append(person + ': ' + line) 
    return new
    
def write_file(filename, lines):
    with open(filename,'w',encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)


main()                                                     # 程式的進入點

