# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work5-3.py -*-
# -*- data: 2019-12-06 -*-

dt = {"姓名":["张唐","李丽"],"学号":["201805160021","201805160022"],"成绩":{"英语":[89,95],"政治":[98,80],"Python程序设计":[90,95]} }
print("张唐 英语、政治、Python三门课程平均成绩为：", "%.1f" % float((dt["成绩"]["英语"][0] + dt["成绩"]["政治"][0] + dt["成绩"]["Python程序设计"][0])/3))
print("李丽 英语、政治、Python三门课程平均成绩为：", "%.1f" % float((dt["成绩"]["英语"][1] + dt["成绩"]["政治"][1] + dt["成绩"]["Python程序设计"][1])/3))
