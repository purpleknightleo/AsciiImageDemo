from PIL import Image
import argparse

# 命令行执行：
# python3 main.py files/lakers.jpeg files/lakers_ascii.txt


# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('input')  # 输入文件
parser.add_argument('output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.input
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # RGB转换成灰度值

    unit = (256 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    # 字符画输出到文件
    with open(OUTPUT, 'w') as f:
        f.write(txt)
