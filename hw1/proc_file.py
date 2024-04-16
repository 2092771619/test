#!/home/hyluo/anaconda3/bin/python
"""
File: proc_file.py
练习处理文件

Author: Huiyu Luo, 4/13/2023
"""
import os

def count(fileName):
    """
    计算字符在文件fielName中出现的次数
    @fileName: path to the file
    @return: None
    """
    # 读取文件
    with open(fileName, 'r') as f:
        # 将文件全部读到变量lines里，
        # lines是一个list，其中每个元素是文件的一行
        lines = f.readlines()
    # 任务三
    line = len(lines)
    print(f"在{os.path.split(fileName)[1]}中行数为：{line}")
    space = 0
    comma = 0
    period = 0
    colon = 0
    quote = 0
    exclamation = 0
    question = 0
    # 查看文件的每一行
    for line in lines:
        # 查看一行中的每一个字符
        for c in line:
            if c == ' ':
                space += 1
            elif c == '，':
                comma += 1
            elif c == '。':
                period += 1
            elif c == '：':
                colon += 1
            elif c == '“':
                quote += 1
            elif c == '！':
                exclamation += 1
            elif c == '？':
                question += 1
        # 打印结果
    print(f"在{os.path.split(fileName)[1]}中空格次数为：{space}")
    print(f"在{os.path.split(fileName)[1]}中逗号次数为：{comma}")
    print(f"在{os.path.split(fileName)[1]}中句号次数为：{period}")
    print(f"在{os.path.split(fileName)[1]}中冒号次数为：{colon}")
    print(f"在{os.path.split(fileName)[1]}中引号次数为：{quote*2}")
    print(f"在{os.path.split(fileName)[1]}中感叹号次数为：{exclamation}")
    print(f"在{os.path.split(fileName)[1]}中问号次数为：{question}")
    # 任务四
    content = ''.join(lines)
    content = content.replace(" ","")
    content = content.replace("\n","")

    # 任务五
    while True:
        # 让用户输入字符
        word = input("请输入字符:(退出请输入'exit')")
        if word == 'exit':
            break
        count = 0
        # 查找字符在content中出现次数
        word_length = len(word)
        for i in range(len(content) - word_length + 1):
            if content[i:i+word_length] == word:
                count += 1
        print(f"'{word}'在{os.path.split(fileName)[1]}中出现次数为：{count}")
 
def count(file_name):
    # 任务六
    with open(file_name, 'r', ) as f:
        contents = f.read()
    # 统计金陵十二钗姓名出现的次数
    characters = ['林黛玉', '贾宝玉', '薛宝钗', '王熙凤', '史湘云', '贾探春', '贾元春', '贾迎春', '贾惜春', '王熙凤', '李纨', '秦可卿']
    character_count = {char: contents.count(char) for char in characters}
    sorted_character_count = dict(sorted(character_count.items(), key=lambda x: x[1], reverse=True))
    top_three = list(sorted_character_count.items())[:3]
    print("金陵十二钗出现次数排前三位的是：", top_three)
    # 任务七
    single = {}
    double = {}
    triple = {}
    for i in range(len(contents)):
        if i < len(contents):
            single_char = contents[i]
            if single_char in single:
                single[single_char] += 1
            else:
                single[single_char] = 1
        if i < len(contents) - 1:
            double_char = contents[i:i+2]
            if double_char in double:
                double[double_char] += 1
            else:
                double[double_char] = 1
        if i < len(contents) - 2:
            triple_char = contents[i:i+3]
            if triple_char in triple:
                triple[triple_char] += 1
            else:
                triple[triple_char] = 1
    # 任务八
    # 对三个字典的结果按次数排序
    sorted_single = dict(sorted(single.items(), key=lambda x: x[1], reverse=True))
    sorted_double = dict(sorted(double.items(), key=lambda x: x[1], reverse=True))
    sorted_triple = dict(sorted(triple.items(), key=lambda x: x[1], reverse=True))
    # 将排序后的结果写入到文件中
    with open('result.txt', 'w') as f:
        f.write(f"单个字符出现次数:\n{sorted_single}\n")
        f.write(f"两个连续字符出现次数:\n{sorted_double}\n")
        f.write(f"三个连续字符出现次数：:\n{sorted_triple}\n")
if __name__ == "__main__":
    # 《围城》
    fileName = "data/fortressBesieged.txt"
    count(fileName)
    # 《红楼梦》
    file_name = "data/hongloumeng.txt"
    count(file_name)
