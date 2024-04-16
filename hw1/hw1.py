#!/home/hyluo/anaconda3/bin/python
"""
File: hw1.py
----------------------
Based Stanford CS41 lab1

Author: Huiyu Luo, 4/13/2023
"""

def nothing_implemented():
    """
    This prints a message that shows nothing is implemented
    """
    str = "|     Nothing implemented!     |"
    bar = "-" * len(str) + "\n"
    print((str + "\n").join([bar] * 2))

def say_hello():
    """Prints "Hello, world!" """
    # Comment out nothing_implemented(), and add your code here
    print("Hello, world!")

def print_tictactoe():
    """Print out a tic tac toe board using print's `sep` keyword argument
      |  |
    ---------
      |  |
    ---------
      |  |
    """
    # Comment out nothing_implemented(), and add your code here
    a="  |  |   "
    b="-" * len(a)
    print(a,b,a,b,a,sep="\n")

def print_super_tictactoe():
    """Prints a super tic-tac-toe board using string's join method.
    You can read nothing_implemented() for some hint.
        |  |  H  |  |  H  |  |
      --+--+--H--+--+--H--+--+--
        |  |  H  |  |  H  |  |
      --+--+--H--+--+--H--+--+--
        |  |  H  |  |  H  |  |
      ========+========+========
        |  |  H  |  |  H  |  |
      --+--+--H--+--+--H--+--+--
        |  |  H  |  |  H  |  |
      --+--+--H--+--+--H--+--+--
        |  |  H  |  |  H  |  |
      ========+========+========
        |  |  H  |  |  H  |  |
      --+--+--H--+--+--H--+--+--
        |  |  H  |  |  H  |  |
      --+--+--H--+--+--H--+--+--
        |  |  H  |  |  H  |  |
    """
    # Comment out nothing_implemented(), and add your code here
    a="  |  |  H  |  |  H  |  |  " + "\n"
    b="--+--+--H--+--+--H--+--+--" + "\n"
    c="========+========+========" + "\n"
    d=(b.join([a] * 3))
    print(c.join([d] * 3))

def fizzbuzz(n):
    """Returns the sum of all numbers < n divisible by 3 or 5.

    If you want to write this in one line, the following will work:
        return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

    Another approach, as we'll learn about soon, is to use `filter`:
        return sum(filter(lambda i: i % 3 == 0 and i % 5 == 0, range(n)))

    For a job this simple, the iterative approach will suffice.
    """
    # Comment out nothing_implemented(), and add your code here
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

def collatz_len(n):
    """用循环的方法，计算Collatz序列的长度。注意，你只需要返回序列长度，不必返回或打印整个序列。

    Collatz在1937年提出的这个序列，它从n开始，持续进行下面的操作一直到结果 <= 1：
    1）如果当前值是偶数，那么序列的下一个值是 n//2；
    2）如果当前值是奇数，那么序列的下一个值是 3*n+1。

    有一个数学猜想，所有从正数开始的Collztz序列都会以1结束，你可以测试一下，你所得到的序列，是不是总会以1结束。
    """
    # Comment out nothing_implemented(), and add your code here
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def max_collatz_len(n):
    """Computes the longest Collatz sequence length for starting numbers < n
       计算所有小于n的正数作初始值时，能够产生的最长的Collatz序列为多少？
    
    提示：
    1）在解决这个问题的时候，你应该用到上面定义的collatz_len()。
    2）试一下，你能不能用collatz_len(), max()函数和list comprehension，只用一行代码解决这个问题？
    """
    # Comment out nothing_implemented(), and add your code here
    return max(collatz_len(i) for i in range(1, n))


def collatz_len_recur(n):
    """用迭代的方法解决Collatz序列长度的问题。
    """
    # Comment out nothing_implemented(), and add your code here
    if n <=1:
        length = 1
    elif n % 2 == 0:
        n = n // 2
        length = collatz_len_recur(n) + 1
    else:
        n = 3 * n + 1
        length = collatz_len_recur(n) + 1
    return length

def collatz_len_fast(n, cache):
    """类似于测验中遇到的爬楼梯问题，设计一个更高效的迭代方法，使用字典cache来存储已经算出的Collatz序列长度
    Slightly faster way to compute the length of Collatz sequence

    A dictionary is used as a cache of previous results, and since the dictionary nothing_implemented()ed in is mutable, 
    our changes will reflect in the caller.
    """
    # Comment out nothing_implemented(), and add your code here
    if n in cache:
        return cache[n]
    elif n == 1:
        length = 1
    elif n % 2 == 0:
        n = n // 2
        length = collatz_len_fast(n, cache) + 1
    else:
        n = 3 * n + 1
        length = collatz_len_fast(n, cache) + 1
    return length
def max_collatz_len_fast(n):
    """使用上面的collatz_len_fast()函数来计算初始值小于n的最长Collatz序列的长度
    Slightly faster way to compute the longest Collatz sequence for starting numbers < n

    如果你只用一行代码解决了max_collatz_len，那这道题只需要两行代码。
    """
    # Comment out nothing_implemented(), and add your code here
    cache = {}
    return max(collatz_len_fast(i, cache) for i in range(1, n))

def convert_fahr_to_cels(deg_fahr):
    """Converts a temperature in degrees Fahrenheit to degrees Celsius.
    将华氏温度转化为摄氏温度，它们之间的关系是：
    摄氏 = （华氏 - 32）*5/9
    """
    # Comment out nothing_implemented(), and add your code here
    celsius = (deg_fahr - 32) * 5 / 9
    return celsius

def converter():
    """Converts user-specified temperatures from Fahrenheit to Celsius.
    让用户输入一个浮点数（float）的华氏温度，将它转化为摄氏温度，打印出来。
    假如用户输入任何非数字的输入，则退出程序。

    提示：
    1）用户输入可以用：fahr_str = input("Temperature F? ")
    2）你可以用至少两种方法来测试fahr_str是否一个正确的浮点数：
       -- 将其中的一个小数点"."转化为空字符""，然后测试结果是否都是数字，用str的isdigit方法
       -- 用try/except/else，直接调用float(fahr_str)，如果遇到except，就代表转化失败，可以退出函数
    """
    # Comment out nothing_implemented(), and add your code here
    while True:
        fahr_str = input("Temperature F? ")
        if not fahr_str.replace(".",'').isdigit():
            break
        try:
            fahr = float(fahr_str)
            celsius = (fahr - 32) * 5 / 9
            print(f"摄氏温度为：{celsius:.2f}")
        except ValueError:
            break

if __name__ == '__main__':
    """Runs each of the lab solution functions and prints the attached docstring and source."""
    cache = {}
    fns = [
        # Comment out any functions that you do not want to run
        (say_hello, (), {}, None),
        (print_tictactoe, (), {}, None),
        (print_super_tictactoe, (), {}, None),
        (fizzbuzz, (1001,), {}, 234168),
        (collatz_len, (501,), {}, 111),
        (max_collatz_len, (1000,), {}, 179),
        (collatz_len_recur, (501,), {}, 111),
        (collatz_len_fast, (1000000, cache), {}, 153),
        (max_collatz_len_fast, (1000000,), {}, 525),
        (converter, (), {}, None),
    ]
    for fn, args, kwargs, ans in fns:
        name = fn.__name__
        print("*" * len(name))        # header
        print(name)                   # function name
        print(fn.__doc__)             # function docstring
        print(f"{name}(", end="")
        output = ", ".join([str(a) for a in args]+[f"{k}={v}" for k, v in kwargs.items()])
        print(output, end="")
        print(")")

        # Call the function and get the result
        res = fn(*args, **kwargs)     # variadic argument unpacking - cool stuff!
        if ans and res:
            if res == ans:
                print(f"Your result matches the answer: {res}.")
            else:
                print(f"Your result {res} does not match the answer {ans}.")
        input("Press [ENTER] to continue...")
        print("")
    print("Done!")
