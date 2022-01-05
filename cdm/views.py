from django.shortcuts import render
from django.http import HttpResponse
from cdm.models import ConditionOccurrence_ANAM, Death_ANAM, Person_ANAM, ProcedureOccurrence_ANAM
from cdm.models import ConditionOccurrence_ANSAN, Death_ANSAN, Person_ANSAN, ProcedureOccurrence_ANSAN
from cdm.models import ConditionOccurrence_GURO, Death_GURO, Person_GURO, ProcedureOccurrence_GURO
from django.db.models import Count, Sum
from cdm.fusioncharts import FusionCharts

from scipy import stats


from django.http.response import HttpResponseRedirect
from collections import OrderedDict
import csv
import numpy as np
import pandas as pd

import datetime

import matplotlib.pyplot as plt
import plotly
from sksurv.nonparametric import kaplan_meier_estimator

import matplotlib
matplotlib.use('Agg')


def Main(request):
	return render(request,'main.html')

def Person(request):
	# members = Person.objects.all().order_by('id')
	## http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API

	### ANAM

	gender_anam = Person_ANAM.objects.all().values('gender_concept_id').annotate(Count('gender_concept_id'))

	dataSource_ANAM = OrderedDict()
	dataSource_ANAM["data"] = []

	for k in range(len(gender_anam)):
		if gender_anam[k]['gender_concept_id'] == 8532:
			gender_anam[k]['gender_concept_id'] = "FEMALE"
		elif gender_anam[k]['gender_concept_id'] == 8507:
			gender_anam[k]['gender_concept_id'] = "MALE"
		else:
			gender_anam[k]['gender_concept_id'] = "OTHERS"

	gen_1 = gender_anam[0]['gender_concept_id__count']
	gen_1_lab = gender_anam[0]['gender_concept_id']
	gen_2 = gender_anam[1]['gender_concept_id__count']
	gen_2_lab = gender_anam[1]['gender_concept_id']
	gen_3 = gender_anam[2]['gender_concept_id__count']
	gen_3_lab = gender_anam[2]['gender_concept_id']

	dataSource_ANAM["data"].append({"label": gen_1_lab, "value": gen_1})
	dataSource_ANAM["data"].append({"label": gen_2_lab, "value": gen_2})
	dataSource_ANAM["data"].append({"label": gen_3_lab, "value": gen_3})

	chartConfig = OrderedDict()
	chartConfig["caption"] = "안암병원 진료 환자 성별 분포표"
	chartConfig["plottooltext"] = "<b>$percentValue</b> 의 환자가 <b>$label</b> 입니다."
	chartConfig["showlegend"] = "0"
	chartConfig["showpercentvalues"] = "1"
	chartConfig["defaultcenterlabel"] = "환자 수"
	chartConfig["aligncaptionwithcanvas"] = "0"
	chartConfig["captionpadding"] = "0"
	chartConfig["decimals"] = "1"
	chartConfig["legendposition"] = "bottom"
	chartConfig["centerlabel"] = "$value"
	chartConfig["usedataplotcolorforlabels"] = "1"
	chartConfig["theme"] = "fusion"

	dataSource_ANAM["chart"] =chartConfig

	chartObj1 = FusionCharts('doughnut2d', 'ex1', '400', '300', 'chart-1', 'json', dataSource_ANAM)

	### ANSAN

	gender_ansan = Person_ANSAN.objects.all().values('gender_concept_id').annotate(Count('gender_concept_id'))

	dataSource_ANSAN = OrderedDict()
	dataSource_ANSAN["data"] = []

	for k in range(len(gender_ansan)):
		if gender_ansan[k]['gender_concept_id'] == 8532:
			gender_ansan[k]['gender_concept_id'] = "FEMALE"
		elif gender_ansan[k]['gender_concept_id'] == 8507:
			gender_ansan[k]['gender_concept_id'] = "MALE"
		else:
			gender_ansan[k]['gender_concept_id'] = "OTHERS"

	gen_1 = gender_ansan[0]['gender_concept_id__count']
	gen_1_lab = gender_ansan[0]['gender_concept_id']
	gen_2 = gender_ansan[1]['gender_concept_id__count']
	gen_2_lab = gender_ansan[1]['gender_concept_id']
	gen_3 = gender_ansan[2]['gender_concept_id__count']
	gen_3_lab = gender_ansan[2]['gender_concept_id']

	dataSource_ANSAN["data"].append({"label": gen_1_lab, "value": gen_1})
	dataSource_ANSAN["data"].append({"label": gen_2_lab, "value": gen_2})
	dataSource_ANSAN["data"].append({"label": gen_3_lab, "value": gen_3})

	chartConfig2 = OrderedDict()
	chartConfig2["caption"] = "안산병원 진료 환자 성별 분포표"
	chartConfig2["plottooltext"] = "<b>$percentValue</b> 의 환자가 <b>$label</b> 입니다."
	chartConfig2["showlegend"] = "0"
	chartConfig2["showpercentvalues"] = "1"
	chartConfig2["defaultcenterlabel"] = "환자 수"
	chartConfig2["aligncaptionwithcanvas"] = "0"
	chartConfig2["captionpadding"] = "0"
	chartConfig2["decimals"] = "1"
	chartConfig2["legendposition"] = "bottom"
	chartConfig2["centerlabel"] = "$value"
	chartConfig2["usedataplotcolorforlabels"] = "1"
	chartConfig2["theme"] = "fusion"

	dataSource_ANSAN["chart"] = chartConfig2

	chartObj3 = FusionCharts('doughnut2d', 'ex3', '400', '300', 'chart-3', 'json', dataSource_ANSAN)


	### GURO

	gender_guro = Person_GURO.objects.all().values('gender_concept_id').annotate(Count('gender_concept_id'))

	dataSource_GURO = OrderedDict()
	dataSource_GURO["data"] = []

	for k in range(len(gender_guro)):
		if gender_guro[k]['gender_concept_id'] == 8532:
			gender_guro[k]['gender_concept_id'] = "FEMALE"
		elif gender_guro[k]['gender_concept_id'] == 8507:
			gender_guro[k]['gender_concept_id'] = "MALE"
		else:
			gender_guro[k]['gender_concept_id'] = "OTHERS"

	gen_1 = gender_guro[0]['gender_concept_id__count']
	gen_1_lab = gender_guro[0]['gender_concept_id']
	gen_2 = gender_guro[1]['gender_concept_id__count']
	gen_2_lab = gender_guro[1]['gender_concept_id']
	gen_3 = gender_guro[2]['gender_concept_id__count']
	gen_3_lab = gender_guro[2]['gender_concept_id']

	dataSource_GURO["data"].append({"label": gen_1_lab, "value": gen_1})
	dataSource_GURO["data"].append({"label": gen_2_lab, "value": gen_2})
	dataSource_GURO["data"].append({"label": gen_3_lab, "value": gen_3})

	chartConfig3 = OrderedDict()
	chartConfig3["caption"] = "구로병원 진료 환자 성별 분포표"
	chartConfig3["plottooltext"] = "<b>$percentValue</b> 의 환자가 <b>$label</b> 입니다."
	chartConfig3["showlegend"] = "0"
	chartConfig3["showpercentvalues"] = "1"
	chartConfig3["defaultcenterlabel"] = "환자 수"
	chartConfig3["aligncaptionwithcanvas"] = "0"
	chartConfig3["captionpadding"] = "0"
	chartConfig3["decimals"] = "1"
	chartConfig3["legendposition"] = "bottom"
	chartConfig3["centerlabel"] = "$value"
	chartConfig3["usedataplotcolorforlabels"] = "1"
	chartConfig3["theme"] = "fusion"

	dataSource_GURO["chart"] = chartConfig3

	chartObj4 = FusionCharts('doughnut2d', 'ex4', '400', '300', 'chart-4', 'json', dataSource_GURO)


	year = Person_ANAM.objects.all().values('year_of_birth').annotate(Count('year_of_birth'))

	categoriesConfig1 =OrderedDict()
	datasetConfig1 = OrderedDict()

	categoriesConfig1["category"] = []
	datasetConfig1["data"] = []
	datasetConfig1["seriesname"] = "ANAM Hospital"

	for i in range(len(year)):
		categoriesConfig1["category"].append({"label": str(year[i]["year_of_birth"])})
		datasetConfig1["data"].append({"value": year[i]["year_of_birth__count"]})


	### ANSAN

	year = Person_ANSAN.objects.all().values('year_of_birth').annotate(Count('year_of_birth'))

	categoriesConfig2 =OrderedDict()
	datasetConfig2 = OrderedDict()

	categoriesConfig2["category"] = []
	datasetConfig2["data"] = []
	datasetConfig2["seriesname"] = "ANSAN Hospital"

	for i in range(len(year)):
		categoriesConfig2["category"].append({"label": str(year[i]["year_of_birth"])})
		datasetConfig2["data"].append({"value": year[i]["year_of_birth__count"]})


	### GURO

	year = Person_GURO.objects.all().values('year_of_birth').annotate(Count('year_of_birth'))

	categoriesConfig3 =OrderedDict()
	datasetConfig3 = OrderedDict()

	categoriesConfig3["category"] = []
	datasetConfig3["data"] = []
	datasetConfig3["seriesname"] = "GURO Hospital"

	for i in range(len(year)):
		categoriesConfig3["category"].append({"label": str(year[i]["year_of_birth"])})
		datasetConfig3["data"].append({"value": year[i]["year_of_birth__count"]})

	chartConfig1 = OrderedDict()
	chartConfig1["caption"] = "다기관 진료 환자 생년 분포표"
	chartConfig1["subcaption"] = "[1889-2021]"
	chartConfig1["theme"] = "fusion"
	chartConfig1["showvalues"] = "0"
	chartConfig1["numvisibleplot"] = "80"
	chartConfig1["plottooltext"] = "In $label, <b>$dataValue</b> patients were born in $seriesName database."


	dataSource_ANAM_year = OrderedDict()
	dataSource_ANAM_year["chart"] = chartConfig1
	dataSource_ANAM_year["dataset"] = [datasetConfig1, datasetConfig2, datasetConfig3]
	dataSource_ANAM_year["categories"] = [categoriesConfig1, categoriesConfig2, categoriesConfig3]

	chartObj2 = FusionCharts('scrollline2d', 'ex2', '1000', '400', 'chart-2', 'json', dataSource_ANAM_year)


	# Tests

	anam_pd = pd.DataFrame(list(gender_anam))
	ansan_pd = pd.DataFrame(list(gender_ansan))
	guro_pd = pd.DataFrame(list(gender_guro))

	st = []
	st.append(list(stats.mstats.ttest_ind(pd.DataFrame(list(gender_anam)).gender_concept_id__count, pd.DataFrame(list(gender_ansan)).gender_concept_id__count)))
	st.append(list(stats.mstats.ttest_ind(pd.DataFrame(list(gender_anam)).gender_concept_id__count, pd.DataFrame(list(gender_guro)).gender_concept_id__count)))
	st.append(list(stats.mstats.ttest_ind(pd.DataFrame(list(gender_ansan)).gender_concept_id__count, pd.DataFrame(list(gender_guro)).gender_concept_id__count)))

	st1 =[]
	st1.append(list(stats.mstats.chisquare([anam_pd.gender_concept_id__count.drop(1), ansan_pd.gender_concept_id__count.drop(1), guro_pd.gender_concept_id__count.drop(1)])))

	st2 = []
	st2.append(list(stats.mstats.pearsonr(pd.DataFrame(list(gender_anam)).gender_concept_id__count, pd.DataFrame(list(gender_ansan)).gender_concept_id__count)))
	st2.append(list(stats.mstats.pearsonr(pd.DataFrame(list(gender_anam)).gender_concept_id__count, pd.DataFrame(list(gender_guro)).gender_concept_id__count)))
	st2.append(list(stats.mstats.pearsonr(pd.DataFrame(list(gender_ansan)).gender_concept_id__count, pd.DataFrame(list(gender_guro)).gender_concept_id__count)))
	print(st2)


	return render(request, 'person.html', {'output1': chartObj1.render(), 'output2': chartObj2.render(), 'output3': chartObj3.render(), 'output4': chartObj4.render(), 'st': st, 'st1':st1, 'st2':st2})



def Condition_Occurr(request):
	condition = ConditionOccurrence_ANAM.objects.all().values('condition_concept_id').annotate(Count('condition_concept_id')).order_by("-condition_concept_id__count")

	dataSource_ANAM = OrderedDict()
	dataSource_ANAM["data"] = []

	aa = condition[0:10]

	for i in range(10):
		tmp = aa[i]["condition_concept_id"]
		if tmp == 320128:
			tmp = "Essential hypertension"
		elif tmp == 4193704:
			tmp = "Type 2 diabetes mellitus without complication"
		elif tmp == 4144111:
			tmp = "Gastroesophageal reflux disease without esophagitis"
		elif tmp == 201340:
			tmp = "Gastritis"
		elif tmp == 30437:
			tmp = "Gastro-esophageal reflux disease with esophagitis"
		elif tmp == 432867:
			tmp = "Hyperlipidemia"
		elif tmp == 321318:
			tmp = "Angina pectoris"
		elif tmp == 197032:
			tmp = "Hyperplasia of prostate"
		elif tmp == 133424:
			tmp = "Primary malignant neoplasm of thyroid gland"
		elif tmp == 257012:
			tmp = "Chronic sinusitis"
		elif tmp == 4191597:
			tmp = "Disorder of refraction"
		elif tmp == 4289526:
			tmp = "Nonulcer dyspepsia"
		elif tmp == 378416:
			tmp = "Retinal disorder"
		elif tmp == 257007:
			tmp = "Allergic rhinitis"
		elif tmp == 4162253:
			tmp = "Primary malignant neoplasm of breast"
		elif tmp == 439674:
			tmp = "Chronic viral hepatitis B without delta-agent"
		elif tmp == 77670:
			tmp = "Chest pain"


		dataSource_ANAM["data"].append({"label": str(tmp), "value": aa[i]["condition_concept_id__count"]})
		#print(str(aa[i]["condition_concept_id"]))


	chartConfig = OrderedDict()
	chartConfig["caption"] = "안암병원 내원 질병 상위 10개 분포표"
	chartConfig["plottooltext"] = "<b>$percentValue</b> 의 환자가 <b>$label</b>로 방문했습니다."
	chartConfig["showlegend"] = "1"
	chartConfig["showpercentvalues"] = "1"
	chartConfig["defaultcenterlabel"] = "환자 수"
	chartConfig["aligncaptionwithcanvas"] = "0"
	chartConfig["captionpadding"] = "0"
	chartConfig["decimals"] = "1"
	chartConfig["legendposition"] = "bottom"
	chartConfig["centerlabel"] = "$value"
	chartConfig["usedataplotcolorforlabels"] = "1"
	chartConfig["theme"] = "fusion"

	dataSource_ANAM["chart"] = chartConfig

	chartObj1 = FusionCharts('doughnut2d', 'ex1', '800', '400', 'chart-1', 'json', dataSource_ANAM)



	condition = ConditionOccurrence_ANSAN.objects.all().values('condition_concept_id').annotate(Count('condition_concept_id')).order_by("-condition_concept_id__count")

	dataSource_ANSAN = OrderedDict()
	dataSource_ANSAN["data"] = []

	aa = condition[0:10]

	for i in range(10):
		tmp = aa[i]["condition_concept_id"]
		if tmp == 320128:
			tmp = "Essential hypertension"
		elif tmp == 4193704:
			tmp = "Type 2 diabetes mellitus without complication"
		elif tmp == 4144111:
			tmp = "Gastroesophageal reflux disease without esophagitis"
		elif tmp == 201340:
			tmp = "Gastritis"
		elif tmp == 30437:
			tmp = "Gastro-esophageal reflux disease with esophagitis"
		elif tmp == 432867:
			tmp = "Hyperlipidemia"
		elif tmp == 321318:
			tmp = "Angina pectoris"
		elif tmp == 197032:
			tmp = "Hyperplasia of prostate"
		elif tmp == 133424:
			tmp = "Primary malignant neoplasm of thyroid gland"
		elif tmp == 257012:
			tmp = "Chronic sinusitis"
		elif tmp == 4191597:
			tmp = "Disorder of refraction"
		elif tmp == 4289526:
			tmp = "Nonulcer dyspepsia"
		elif tmp == 378416:
			tmp = "Retinal disorder"
		elif tmp == 257007:
			tmp = "Allergic rhinitis"
		elif tmp == 4162253:
			tmp = "Primary malignant neoplasm of breast"
		elif tmp == 439674:
			tmp = "Chronic viral hepatitis B without delta-agent"
		elif tmp == 77670:
			tmp = "Chest pain"


		dataSource_ANSAN["data"].append({"label": str(tmp), "value": aa[i]["condition_concept_id__count"]})
		#print(str(aa[i]["condition_concept_id"]))


	chartConfig2 = OrderedDict()
	chartConfig2["caption"] = "안산병원 내원 질병 상위 10개 분포표"
	chartConfig2["plottooltext"] = "<b>$percentValue</b> 의 환자가 <b>$label</b>로 방문했습니다."
	chartConfig2["showlegend"] = "1"
	chartConfig2["showpercentvalues"] = "1"
	chartConfig2["defaultcenterlabel"] = "환자 수"
	chartConfig2["aligncaptionwithcanvas"] = "0"
	chartConfig2["captionpadding"] = "0"
	chartConfig2["decimals"] = "1"
	chartConfig2["legendposition"] = "bottom"
	chartConfig2["centerlabel"] = "$value"
	chartConfig2["usedataplotcolorforlabels"] = "1"
	chartConfig2["theme"] = "fusion"

	dataSource_ANSAN["chart"] = chartConfig2

	chartObj2 = FusionCharts('doughnut2d', 'ex2', '800', '400', 'chart-2', 'json', dataSource_ANSAN)


	condition = ConditionOccurrence_GURO.objects.all().values('condition_concept_id').annotate(Count('condition_concept_id')).order_by("-condition_concept_id__count")

	dataSource_GURO = OrderedDict()
	dataSource_GURO["data"] = []

	aa = condition[0:10]

	for i in range(10):
		tmp = aa[i]["condition_concept_id"]
		if tmp == 320128:
			tmp = "Essential hypertension"
		elif tmp == 4193704:
			tmp = "Type 2 diabetes mellitus without complication"
		elif tmp == 4144111:
			tmp = "Gastroesophageal reflux disease without esophagitis"
		elif tmp == 201340:
			tmp = "Gastritis"
		elif tmp == 30437:
			tmp = "Gastro-esophageal reflux disease with esophagitis"
		elif tmp == 432867:
			tmp = "Hyperlipidemia"
		elif tmp == 321318:
			tmp = "Angina pectoris"
		elif tmp == 197032:
			tmp = "Hyperplasia of prostate"
		elif tmp == 133424:
			tmp = "Primary malignant neoplasm of thyroid gland"
		elif tmp == 257012:
			tmp = "Chronic sinusitis"
		elif tmp == 4191597:
			tmp = "Disorder of refraction"
		elif tmp == 4289526:
			tmp = "Nonulcer dyspepsia"
		elif tmp == 378416:
			tmp = "Retinal disorder"
		elif tmp == 257007:
			tmp = "Allergic rhinitis"
		elif tmp == 4162253:
			tmp = "Primary malignant neoplasm of breast"
		elif tmp == 439674:
			tmp = "Chronic viral hepatitis B without delta-agent"
		elif tmp == 77670:
			tmp = "Chest pain"


		dataSource_GURO["data"].append({"label": str(tmp), "value": aa[i]["condition_concept_id__count"]})
		#print(str(aa[i]["condition_concept_id"]))


	chartConfig3 = OrderedDict()
	chartConfig3["caption"] = "구로병원 내원 질병 상위 10개 분포표"
	chartConfig3["plottooltext"] = "<b>$percentValue</b> 의 환자가 <b>$label</b>로 방문했습니다."
	chartConfig3["showlegend"] = "1"
	chartConfig3["showpercentvalues"] = "1"
	chartConfig3["defaultcenterlabel"] = "환자 수"
	chartConfig3["aligncaptionwithcanvas"] = "0"
	chartConfig3["captionpadding"] = "0"
	chartConfig3["decimals"] = "1"
	chartConfig3["legendposition"] = "bottom"
	chartConfig3["centerlabel"] = "$value"
	chartConfig3["usedataplotcolorforlabels"] = "1"
	chartConfig3["theme"] = "fusion"

	dataSource_GURO["chart"] = chartConfig3

	chartObj3 = FusionCharts('doughnut2d', 'ex3', '800', '400', 'chart-3', 'json', dataSource_GURO)


	return render(request,'list.html', {'output1': chartObj1.render(), 'output2': chartObj2.render(), 'output3': chartObj3.render()})


def Death(request):
	#death = pd.DataFrame(list(Death_ANAM.objects.all().distinct('person_id').values('person_id', 'death_date')))
	#procedure = pd.DataFrame(list(ProcedureOccurrence_ANAM.objects.all().distinct('person_id').values('person_id', 'procedure_concept_id')))

	### 각 질병 별 수술 종류로 KM curve 그리기 (5개 질병만)
	### ConditionOccurrence_ANAM
	tmp = 0
	if tmp == 320128:
		tmp = "Essential hypertension"
	elif tmp == 4193704:
		tmp = "Type 2 diabetes mellitus without complication"
	elif tmp == 4144111:
		tmp = "Gastroesophageal reflux disease without esophagitis"
	elif tmp == 201340:
		tmp = "Gastritis"
	elif tmp == 30437:
		tmp = "Gastro-esophageal reflux disease with esophagitis"

	## condition occurrence인 person_id 찾기, 이 person id 중에 procedure가 있는 것 찾기, 그 person id 중에 death date가 있는 값 찾기기

	condition = pd.DataFrame(list(ConditionOccurrence_ANAM.objects.filter(condition_concept_id='320128').distinct('person_id').values('person_id', 'condition_concept_id', 'condition_start_date')))
	#print(len(condition))

	count = 0

	tmp_1 = []

	procedure = pd.DataFrame(list(ProcedureOccurrence_ANAM.objects.all().distinct('person_id').values('person_id', 'procedure_concept_id')))
	death = pd.DataFrame(list(Death_ANAM.objects.all().distinct('person_id').values('person_id', 'death_date')))
	for i in range(len(condition)):
		pro_tmp = procedure.loc[procedure.person_id==condition.person_id[i], 'procedure_concept_id']
		if len(pro_tmp):
			dead_tmp = death.loc[death.person_id==condition.person_id[i], 'death_date']
			if len(dead_tmp):

				tmp_1.append([condition.person_id[i], pro_tmp.iloc[0], condition.condition_start_date[i], dead_tmp.iloc[0]])
				count = count+1

	tmp_1 = np.asarray(tmp_1)


	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)

	for uni in np.unique(tmp_1[:, 1]):
		mask = tmp_1[:,1] == uni
		if sum(mask) < 50: continue
		OS = (tmp_1[mask,3]-tmp_1[mask,2])/datetime.timedelta(days=1)

		time_cell, survival_prob_cell = kaplan_meier_estimator(np.ones((sum(mask)), dtype=bool), OS)

		ax.step(time_cell, survival_prob_cell, where="post", label="%s (n = %d)" % (str(uni), sum(mask)))

	plt.ylim(0,1)
	graph_div1 = plotly.offline.plot(plotly.tools.mpl_to_plotly(fig), auto_open=False, output_type="div")



	condition = pd.DataFrame(list(
		ConditionOccurrence_ANAM.objects.filter(condition_concept_id='4193704').distinct('person_id').values('person_id',
																											'condition_concept_id',
																											'condition_start_date')))

	count = 0

	tmp_1 = []

	procedure = pd.DataFrame(
		list(ProcedureOccurrence_ANAM.objects.all().distinct('person_id').values('person_id', 'procedure_concept_id')))
	death = pd.DataFrame(list(Death_ANAM.objects.all().distinct('person_id').values('person_id', 'death_date')))
	for i in range(len(condition)):
		pro_tmp = procedure.loc[procedure.person_id == condition.person_id[i], 'procedure_concept_id']
		if len(pro_tmp):
			dead_tmp = death.loc[death.person_id == condition.person_id[i], 'death_date']
			if len(dead_tmp):
				tmp_1.append(
					[condition.person_id[i], pro_tmp.iloc[0], condition.condition_start_date[i], dead_tmp.iloc[0]])
				count = count + 1

	tmp_1 = np.asarray(tmp_1)

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	for uni in np.unique(tmp_1[:, 1]):
		mask = tmp_1[:, 1] == uni
		if sum(mask) < 50: continue
		OS = (tmp_1[mask, 3] - tmp_1[mask, 2]) / datetime.timedelta(days=1)

		time_cell, survival_prob_cell = kaplan_meier_estimator(np.ones((sum(mask)), dtype=bool), OS)

		ax.step(time_cell, survival_prob_cell, where="post", label="%s (n = %d)" % (str(uni), sum(mask)))

	plt.ylim(0, 1)
	graph_div2 = plotly.offline.plot(plotly.tools.mpl_to_plotly(fig), auto_open=False, output_type="div")



	condition = pd.DataFrame(list(
		ConditionOccurrence_ANAM.objects.filter(condition_concept_id='4144111').distinct('person_id').values('person_id',
																											'condition_concept_id',
																											'condition_start_date')))

	count = 0

	tmp_1 = []

	procedure = pd.DataFrame(
		list(ProcedureOccurrence_ANAM.objects.all().distinct('person_id').values('person_id', 'procedure_concept_id')))
	death = pd.DataFrame(list(Death_ANAM.objects.all().distinct('person_id').values('person_id', 'death_date')))
	for i in range(len(condition)):
		pro_tmp = procedure.loc[procedure.person_id == condition.person_id[i], 'procedure_concept_id']
		if len(pro_tmp):
			dead_tmp = death.loc[death.person_id == condition.person_id[i], 'death_date']
			if len(dead_tmp):
				tmp_1.append(
					[condition.person_id[i], pro_tmp.iloc[0], condition.condition_start_date[i], dead_tmp.iloc[0]])
				count = count + 1

	tmp_1 = np.asarray(tmp_1)

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	for uni in np.unique(tmp_1[:, 1]):
		mask = tmp_1[:, 1] == uni
		if sum(mask) < 50: continue
		OS = (tmp_1[mask, 3] - tmp_1[mask, 2]) / datetime.timedelta(days=1)

		time_cell, survival_prob_cell = kaplan_meier_estimator(np.ones((sum(mask)), dtype=bool), OS)

		ax.step(time_cell, survival_prob_cell, where="post", label="%s (n = %d)" % (str(uni), sum(mask)))

	plt.ylim(0, 1)
	graph_div3 = plotly.offline.plot(plotly.tools.mpl_to_plotly(fig), auto_open=False, output_type="div")



	condition = pd.DataFrame(list(
		ConditionOccurrence_ANAM.objects.filter(condition_concept_id='201340').distinct('person_id').values('person_id',
																											'condition_concept_id',
																											'condition_start_date')))

	count = 0

	tmp_1 = []

	procedure = pd.DataFrame(
		list(ProcedureOccurrence_ANAM.objects.all().distinct('person_id').values('person_id', 'procedure_concept_id')))
	death = pd.DataFrame(list(Death_ANAM.objects.all().distinct('person_id').values('person_id', 'death_date')))
	for i in range(len(condition)):
		pro_tmp = procedure.loc[procedure.person_id == condition.person_id[i], 'procedure_concept_id']
		if len(pro_tmp):
			dead_tmp = death.loc[death.person_id == condition.person_id[i], 'death_date']
			if len(dead_tmp):
				tmp_1.append(
					[condition.person_id[i], pro_tmp.iloc[0], condition.condition_start_date[i], dead_tmp.iloc[0]])
				count = count + 1

	tmp_1 = np.asarray(tmp_1)

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	for uni in np.unique(tmp_1[:, 1]):
		mask = tmp_1[:, 1] == uni
		if sum(mask) < 50: continue
		OS = (tmp_1[mask, 3] - tmp_1[mask, 2]) / datetime.timedelta(days=1)

		time_cell, survival_prob_cell = kaplan_meier_estimator(np.ones((sum(mask)), dtype=bool), OS)

		ax.step(time_cell, survival_prob_cell, where="post", label="%s (n = %d)" % (str(uni), sum(mask)))

	plt.ylim(0, 1)
	graph_div4 = plotly.offline.plot(plotly.tools.mpl_to_plotly(fig), auto_open=False, output_type="div")



	condition = pd.DataFrame(list(
		ConditionOccurrence_ANAM.objects.filter(condition_concept_id='30437').distinct('person_id').values('person_id',
																											'condition_concept_id',
																										'condition_start_date')))
	count = 0

	tmp_1 = []

	procedure = pd.DataFrame(
		list(ProcedureOccurrence_ANAM.objects.all().distinct('person_id').values('person_id', 'procedure_concept_id')))
	death = pd.DataFrame(list(Death_ANAM.objects.all().distinct('person_id').values('person_id', 'death_date')))
	for i in range(len(condition)):
		pro_tmp = procedure.loc[procedure.person_id == condition.person_id[i], 'procedure_concept_id']
		if len(pro_tmp):
			dead_tmp = death.loc[death.person_id == condition.person_id[i], 'death_date']
			if len(dead_tmp):
				tmp_1.append(
					[condition.person_id[i], pro_tmp.iloc[0], condition.condition_start_date[i], dead_tmp.iloc[0]])
				count = count + 1

	tmp_1 = np.asarray(tmp_1)

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	for uni in np.unique(tmp_1[:, 1]):
		mask = tmp_1[:, 1] == uni
		if sum(mask) < 50: continue
		OS = (tmp_1[mask, 3] - tmp_1[mask, 2]) / datetime.timedelta(days=1)

		time_cell, survival_prob_cell = kaplan_meier_estimator(np.ones((sum(mask)), dtype=bool), OS)

		ax.step(time_cell, survival_prob_cell, where="post", label="%s (n = %d)" % (str(uni), sum(mask)))

	plt.ylim(0, 1)
	graph_div5 = plotly.offline.plot(plotly.tools.mpl_to_plotly(fig), auto_open=False, output_type="div")


	return render(request,'death.html', {'graph_div1': graph_div1, 'graph_div2': graph_div2, 'graph_div3': graph_div3, 'graph_div4': graph_div4, 'graph_div5': graph_div5})

def index(request):
	return HttpResponse("Hello, world. This is sookelly!")
