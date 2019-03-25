from imageio import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


def outputwordcloud(splittedContent,  background,  output,  maxwords):
    if isinstance(background, str):
        back_color = imread(background.replace('/', '\\'))  # 解析该图片
    elif isinstance(background, tuple):
        back_color = imread(background[0].replace('/', '\\'))  # 解析该图片

    wc = WordCloud(background_color='white',  # 背景颜色
                   max_words=maxwords,  # 最大词数
                   mask=back_color,  # 词云形状,以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                   max_font_size=100,  # 显示字体的最大值
                   stopwords=None,  # 使用内置的屏蔽词，再添加'苟利国'
                   font_path="msyh.ttc",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                   random_state=42,  # 为每个词返回一个PIL颜色
                   # width=1000,  # 图片的宽
                   # height=860  #图片的长
                   )
    # WordCloud各含义参数请点击 wordcloud参数

    # 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
    # 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
    # jieba.add_word('金三胖')

    # 打开词源的文本文件
    # text = open('cnword.txt').read()
    text = splittedContent

    wc.generate(text)
    # 基于彩色图像生成相应彩色
    image_colors = ImageColorGenerator(back_color)
    # 显示图片
    plt.imshow(wc)
    # 关闭坐标轴
    plt.axis('off')
    # 绘制词云
    print('正在生成图片')
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    # 保存图片
    if output == '':
        wc.to_file('output.png')
    else:
        wc.to_file(output + '\\output.png')
    print('图片已保存')

