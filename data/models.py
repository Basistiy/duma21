from django.db import models
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np



# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100)

class Oik(models.Model):
    name = models.CharField(max_length=100)

class Tik(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)


class Uik(models.Model):
    #регион
    region = models.CharField(max_length=100)
    #окружная избирательная комиссия
    oik = models.CharField(max_length=100)
    #территориальная избирательна комиссия
    tik = models.CharField(max_length=100)
    #название участковой избирательной комиссии(номер)
    name = models.CharField(max_length=100)
    # Число избирателей, внесенных в список избирателей на момент окончания голосования
    total_voters = models.IntegerField(default=0)
    # Число избирательных бюллетеней, полученных участковой избирательной комиссией
    ballots_recieved = models.IntegerField(default=0)
    # Число избирательных бюллетеней, выданных избирателям, проголосовавшим досрочно
    ballots_ahead = models.IntegerField(default=0)
    # Число избирательных бюллетеней, выданных в помещении для голосования в день голосования
    ballots_out = models.IntegerField(default=0)

    # Число избирательных бюллетеней, выданных вне помещения для голосования в день голосования
    ballots_in = models.IntegerField(default=0)

    # Число погашенных избирательных бюллетеней
    ballots_destroyed = models.IntegerField(default=0)

    # Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования
    ballots_collected_out = models.IntegerField(default=0)

    # Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования
    ballots_collected_in = models.IntegerField(default=0)

    # Число недействительных избирательных бюллетеней
    ballots_spoiled = models.IntegerField(default=0)

    # Число действительных избирательных бюллетеней
    ballots_ok = models.IntegerField(default=0)

    # Число утраченных избирательных бюллетеней
    ballots_lost = models.IntegerField(default=0)

    #Число избирательных бюллетеней, не учтенных при получении
    ballots_excess = models.IntegerField(default=0)

    # 1. Политическая партия "КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ"
    kprf = models.IntegerField(default=0)

    # 2. Политическая партия "Российская экологическая партия "ЗЕЛЁНЫЕ"
    green = models.IntegerField(default=0)

    # 3. Политическая партия ЛДПР – Либерально-демократическая партия России
    ldpr = models.IntegerField(default=0)

    # 4. Политическая партия "НОВЫЕ ЛЮДИ"
    new_people = models.IntegerField(default=0)

    # 5. Всероссийская политическая партия "ЕДИНАЯ РОССИЯ"
    er = models.IntegerField(default=0)

    # 6. Партия СПРАВЕДЛИВАЯ РОССИЯ – ЗА ПРАВДУ
    sr = models.IntegerField(default=0)

    # 7. Политическая партия "Российская объединенная демократическая партия "ЯБЛОКО"
    apple = models.IntegerField(default=0)

    # 8. Всероссийская политическая партия "ПАРТИЯ РОСТА"
    rost = models.IntegerField(default=0)

    # 9. Политическая партия РОССИЙСКАЯ ПАРТИЯ СВОБОДЫ И СПРАВЕДЛИВОСТИ
    rpss = models.IntegerField(default=0)

    # 10. Политическая партия КОММУНИСТИЧЕСКАЯ ПАРТИЯ КОММУНИСТЫ РОССИИ
    kpkr = models.IntegerField(default=0)

    # 11. Политическая партия "Гражданская Платформа"
    platform = models.IntegerField(default=0)

    # 12. Политическая партия ЗЕЛЕНАЯ АЛЬТЕРНАТИВА
    green_alternative = models.IntegerField(default=0)

    # 13. ВСЕРОССИЙСКАЯ ПОЛИТИЧЕСКАЯ ПАРТИЯ "РОДИНА"
    motherland = models.IntegerField(default=0)

    # 14. ПАРТИЯ ПЕНСИОНЕРОВ
    retired = models.IntegerField(default=0)

    # url
    url = models.CharField(max_length=200)
    # явка
    turnout = models.FloatField(default=0)

    # (ballots_ok + ballots_spoiled) / total_voters
    def __str__(self):
        return self.name

    def load_data_party(self, data):
        self.region = data.iloc[1]
        self.oik = data.iloc[2]
        self.tik = data.iloc[3]
        self.name = data.iloc[4]
        self.total_voters = data.iloc[5]
        self.ballots_recieved = data.iloc[6]
        self.ballots_ahead = data.iloc[7]
        self.ballots_out = data.iloc[8]
        self.ballots_in = data.iloc[9]
        self.ballots_destroyed = data.iloc[10]
        self.ballots_collected_out = data.iloc[11]
        self.ballots_collected_in = data.iloc[12]
        self.ballots_spoiled = data.iloc[13]
        self.ballots_ok = data.iloc[14]
        self.ballots_lost = data.iloc[15]
        self.ballots_excess = data.iloc[16]
        self.kprf = data.iloc[17]
        self.green = data.iloc[18]
        self.ldpr = data.iloc[19]
        self.new_people = data.iloc[20]
        self.er = data.iloc[21]
        self.sr = data.iloc[22]
        self.apple = data.iloc[23]
        self.rost = data.iloc[24]
        self.rpss = data.iloc[25]
        self.kpkr = data.iloc[26]
        self.platform = data.iloc[27]
        self.green_alternative = data.iloc[28]
        self.motherland = data.iloc[29]
        self.retired = data.iloc[30]
        self.url = data.iloc[31]



class Country(models.Model):
    name = "Russia"

    def get_voters_number(self):
        df = pd.DataFrame(list(Uik.objects.all().values('total_voters')))
        total = df.sum()
        return (total[0])

    def get_total_ballots_ok(self):
        df = pd.DataFrame(list(Uik.objects.all().values('ballots_ok')))
        total = df.sum()
        return (total[0])

    def get_total_ballots_spoiled(self):
        df = pd.DataFrame(list(Uik.objects.all().values('ballots_spoiled')))
        total = df.sum()
        return (total[0])

    def get_total_ballots_ok(self, turnout):
        df = pd.DataFrame(list(Uik.objects.filter(turnout__lte=turnout).values('ballots_ok')))
        total = df.sum()
        return (total[0])

    def get_total_ballots_spoiled(self, turnout):
        df = pd.DataFrame(list(Uik.objects.filter(turnout__lte=turnout).values('ballots_spoiled')))
        total = df.sum()
        return (total[0])

    def get_total_kprf(self):
        df = pd.DataFrame(list(Uik.objects.all().values('kprf')))
        total = df.sum()
        return(total[0])

    def get_total_kprf_turnout(self, turnout):
        df = pd.DataFrame(list(Uik.objects.filter(turnout__lte=turnout).values('kprf')))
        total = df.sum()
        return(total[0])

    def get_total_er(self):
        df = pd.DataFrame(list(Uik.objects.all().values('er')))
        total = df.sum()
        return (total[0])

    def get_total_er_turnout(self, turnout):
        df = pd.DataFrame(list(Uik.objects.filter(turnout__lte=turnout).values('er')))
        total = df.sum()
        return(total[0])

    def get_kprf_final_percent(self):
        total = self.get_total_ballots_ok() + self.get_total_ballots_spoiled()
        kprf = self.get_total_kprf()
        return (kprf/total)

    def get_er_final_percent(self):
        total = self.get_total_ballots_ok() + self.get_total_ballots_spoiled()
        er = self.get_total_er()
        return (er/total)

    def get_kprf_final_percent_turnout(self, turnout):
        total = self.get_total_ballots_ok(turnout) + self.get_total_ballots_spoiled(turnout)
        kprf = self.get_total_kprf_turnout(turnout)
        return (kprf/total)

    def get_er_final_percent_turnout(self, turnout):
        total = self.get_total_ballots_ok(turnout) + self.get_total_ballots_spoiled(turnout)
        er = self.get_total_er_turnout(turnout)
        return (er/total)

    def get_final_percent_all(self, turnout):
        total = self.get_total_ballots_ok(turnout) + self.get_total_ballots_spoiled(turnout)
        parties = ['kprf', 'green', 'ldpr', 'new_people', 'er', 'sr', 'apple', 'rost', 'rpss', 'kpkr', 'platform', 'green_alternative', 'motherland', 'retired']
        df = pd.DataFrame(list(Uik.objects.filter(turnout__lte=turnout).values('kprf', 'green', 'ldpr', 'new_people', 'er', 'sr', 'apple', 'rost', 'rpss', 'kpkr', 'platform', 'green_alternative', 'motherland', 'retired')))
        result = {}
        for party in parties:
            sum = df[party].sum()
            result[party] = sum/total
        return (result)

    def get_final_percent_all_df(self, turnout):
        turnout = turnout/100
        total = self.get_total_ballots_ok(turnout) + self.get_total_ballots_spoiled(turnout)
        parties = ['kprf', 'green', 'ldpr', 'new_people', 'er', 'sr', 'apple', 'rost', 'rpss', 'kpkr', 'platform', 'green_alternative', 'motherland', 'retired']
        df = pd.DataFrame(list(Uik.objects.filter(turnout__lte=turnout).values('kprf', 'green', 'ldpr', 'new_people', 'er', 'sr', 'apple', 'rost', 'rpss', 'kpkr', 'platform', 'green_alternative', 'motherland', 'retired')))
        result = df.sum()/total

        return (result.round(decimals = 2))

    def create_final_percent_plot(self, turnout):
        turnout = turnout/100
        total = self.get_total_ballots_ok(turnout) + self.get_total_ballots_spoiled(turnout)
        df = pd.DataFrame(list(
            Uik.objects.filter(turnout__lte=turnout).values('kprf', 'ldpr', 'new_people', 'er', 'sr')))
        result = df.sum()/total
        labels = ('КПРФ', 'ЛДПР', 'НЛ', 'ЕР', 'СР')
        y_pos = np.arange(len(labels))
        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(y_pos, result, align='center', color=['red', 'olive', 'c', 'blue', 'orange'])
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Итоговый результат голосования, %')
        ax.set_title('Учтены голоса на участках с явкой менее ' +str(turnout*100) +'%')
        for i, v in enumerate(result):
            ax.text(v / 2, i, str(round(v*100, 2)), color='white', fontweight='bold')

        # plt.show()

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data