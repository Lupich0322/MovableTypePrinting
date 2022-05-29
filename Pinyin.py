from pydub import AudioSegment
from xpinyin import Pinyin
import csv


class Read:
    def __init__(self, message):
        self.m1 = message

    def HuoZiYinShua(self):

        sets = ["/", '\\', ':', '*', '?', '"', '<', '>', '|']
        namefile = self.m1

        p = Pinyin()
        csvFile = open(r"D:\pythonProject\Xpinyin\dictionary.csv", "r")
        reader = csv.reader(csvFile)
        pinyin_dict = {}
        for item in reader:
            pinyin_dict[item[0]] = item[1]
        message2 = ' '.join(pinyin_dict.get(a, a) for a in self.m1)
        wordlist = message2.split(" ")

        for i in range(len(wordlist)):
            wordlist[i] = p.get_pinyin(wordlist[i])

        print(wordlist)

        playlist = AudioSegment.empty()

        for i in range(len(wordlist)):
            try:
                filename = "D:\pythonProject\Xpinyin/otto/" + wordlist[i] + ".wav"
                playlist += AudioSegment.from_file(filename, format="wav")
            except:
                playlist += AudioSegment.silent(duration=250)

        for i in namefile:
            if i in sets:
                namefile = namefile.replace(i, ' ')

        filename = "D:\pythonProject\Xpinyin/output/" + namefile + ".wav"
        playlist.export(filename, format="wav")
        print("印刷成功。。。")
        # print(os.getcwd().replace('\\','/'))

    # 倒放
    # def reHuoZiYinShua(self):
    #     filename = "D:/A-workspace/Xpinyin/output/" + self.m1 + ".wav"
    #     temp = AudioSegment.from_file(filename,format="wav")
    #     backtemp = temp.reverse()
    #     filename1 = "D:/A-workspace/Xpinyin/output/" + self.m1[::-1] + ".wav"
    #     backtemp.export(filename1)
