import json
from io import StringIO

import pandas as pd
from django.db import models
from django.http import Http404
from django.shortcuts import render
from matplotlib import pyplot as plt, markers as markers

from data.models import Region, Tik, Uik, Country
from tikPlot.forms import TikForm, TurnoutForm

# Create your views here.
from django.views import View


class TikPlot(View):

    def get(self, request, *args, **kwargs):
        tikId = kwargs['tikId']
        tik = Tik.objects.get(id=tikId)
        plot = EKplot()
        plot.tik_name = tik.name
        plot.get_tik_data()
        plot.remove_small_uik(200)
        graph = plot.create_plot()
        json_records = plot.table_data.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        context = {'data': graph, 'table': data}
        return render(request, 'turnout.html', context)



class CountryView(View):
    def get(self, request, *args, **kwargs):
        regions = Region.objects.all()
        form = TurnoutForm(initial={'turnout': 100})
        russia = Country()
        graph = russia.create_final_percent_plot(100)
        context = {'regions': regions, 'form' : form, 'graph' : graph}
        return render(request, 'country.html', context)

    def post(self, request, *args, **kwargs):
        form = TurnoutForm(request.POST)
        regions = Region.objects.all()
        if form.is_valid():
            turnout = form.cleaned_data['turnout']
            russia = Country()
            graph = russia.create_final_percent_plot(turnout)
            context = {'regions': regions, 'form': form, 'graph': graph}
            return render(request, 'country.html', context)

        else:
            return Http404


class RegionView(View):
    def get(self, request, *args, **kwargs):
        regionId = kwargs['regionId']
        region = Region.objects.get(id = regionId)
        tiks = Tik.objects.filter(region=region.name)
        context = {'tiks': tiks}
        return render(request, 'region.html', context)


class EKplot():
    tik_name = ''
    tik = pd.DataFrame()
    table_data = pd.DataFrame()

    def get_tik_data(self):
        self.tik = pd.DataFrame(list(Uik.objects.filter(tik=self.tik_name).values('name','kprf','er', 'ballots_spoiled', 'ballots_ok', 'total_voters')))

    def remove_small_uik(self, voters_number):
        self.tik = self.tik[self.tik['ballots_ok'] > voters_number]



    def create_plot(self):
        total_votes = self.tik['total_voters']
        total_came = self.tik['ballots_ok'] + self.tik['ballots_spoiled']
        er_percent = self.tik['er'].div(total_came) * 100
        com_percent = self.tik['kprf'].div(
            total_came) * 100
        came_percent = total_came.div(total_votes) * 100
        max = came_percent.max()/100
        fig = plt.figure()
        self.table_data = self.tik
        self.table_data['turnout'] = came_percent.round(decimals=1)
        self.table_data = self.table_data.sort_values(by=['turnout'])
        plt.scatter(came_percent, com_percent, color='white', s=1000, edgecolors='red', zorder=5)
        marker = markers.MarkerStyle(marker='s')
        plt.scatter(came_percent, er_percent, color='white', marker=marker, s=1000, edgecolors='blue', zorder=0)
        plt.xlabel("явка, %,  " + self.tik_name)
        plt.ylabel("% за КПРФ(круг) и ЕР(квадрат) ")
        uik = self.tik['name']

        for i, txt in enumerate(uik):
            plt.annotate(txt[5:], (came_percent.iloc[i] - 3*max*max, com_percent.iloc[i]), zorder=10)
            plt.annotate(txt[5:], (came_percent.iloc[i] - 3*max*max, er_percent.iloc[i]), zorder=10)

            plt.xlim(0, 100)
            plt.ylim(0, 100)

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data












