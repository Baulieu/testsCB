# -*- coding=utf-8 -*-

""" transcription of an analysis into an Excel workbook """

import xlsxwriter


class Xlswriter:

    def __init__(self):
        self.full_analysis = []

    def add_analysis(self, analysis, name, i):  # adds one single analysis -> best way
        self.full_analysis.append((name, i, analysis))

    def write(self):
        workbook = xlsxwriter.Workbook('analyse.xlsx')
        data = workbook.add_worksheet('data')
        i = 1
        for a in self.full_analysis:
            data.write(2, i, a[0])
            data.write(3, i, a[1])
            data.write(4, i, a[1])
            data.write(5, i, a[2].imgs)
            data.write(6, i, a[2].tauxProfondeur)
            data.write(7, i, a[2].fiabiliteTaille)
            data.write(8, i, a[2].nbTargets)
            data.write(9, i, a[2].nbPoints)
            data.write(10, i, a[2].nbPertes)
            data.write(11, i, a[2].perf)
            i += 1
        charts = workbook.add_worksheet('charts')
        chartImgs = workbook.add_chart({'type': 'column'})
        chartImgs.add_series({'values': '=data!$A$5:$E$5'})
        chartImgs.add_series({'values': '=data!$F$5:$J$5'})
        chartImgs.add_series({'values': '=data!$K$5:$O$5'})
        chartImgs.add_series({'values': '=data!$P$5:$Y$5'})
        chartImgs.add_series({'values': '=data!$Z$5:$AI$5'})
        chartImgs.add_series({'values': '=data!$AJ$5:$AS$5'})
        chartTauxProf = workbook.add_chart({'type': 'column'})
        chartTauxProf.add_series({'values': '=data!$A$6:$E$6'})
        chartTauxProf.add_series({'values': '=data!$F$6:$J$6'})
        chartTauxProf.add_series({'values': '=data!$K$6:$O$6'})
        chartTauxProf.add_series({'values': '=data!$P$6:$Y$6'})
        chartTauxProf.add_series({'values': '=data!$Z$6:$AI$'})
        chartTauxProf.add_series({'values': '=data!$AJ$:$AS$'})
        chartFiabTaille = workbook.add_chart({'type': 'column'})
        chartFiabTaille.add_series({'values': '=data!$A$7:$E$7'})
        chartFiabTaille.add_series({'values': '=data!$F$7:$J$7'})
        chartFiabTaille.add_series({'values': '=data!$K$7:$O$7'})
        chartFiabTaille.add_series({'values': '=data!$P$7:$Y$7'})
        chartFiabTaille.add_series({'values': '=data!$Z$7:$AI$7'})
        chartFiabTaille.add_series({'values': '=data!$AJ$7:$AS$7'})
        chartNbTargets = workbook.add_chart({'type': 'column'})
        chartNbTargets.add_series({'values': '=data!$A$8:$E$8'})
        chartNbTargets.add_series({'values': '=data!$F$8:$J$8'})
        chartNbTargets.add_series({'values': '=data!$K$8:$O$8'})
        chartNbTargets.add_series({'values': '=data!$P$8:$Y$8'})
        chartNbTargets.add_series({'values': '=data!$Z$8:$AI$8'})
        chartNbTargets.add_series({'values': '=data!$AJ$8:$AS$'})
        chartNbPoints = workbook.add_chart({'type': 'column'})
        chartNbPoints.add_series({'values': '=data!$A$9:$E$9'})
        chartNbPoints.add_series({'values': '=data!$F$9:$J$9'})
        chartNbPoints.add_series({'values': '=data!$K$9:$O$9'})
        chartNbPoints.add_series({'values': '=data!$P$9:$Y$9'})
        chartNbPoints.add_series({'values': '=data!$Z$9:$AI$9'})
        chartNbPoints.add_series({'values': '=data!$AJ$9:$AS$9'})
        chartNbPertes = workbook.add_chart({'type': 'column'})
        chartNbPertes.add_series({'values': '=data!$A$10:$E$10'})
        chartNbPertes.add_series({'values': '=data!$F$10:$J$10'})
        chartNbPertes.add_series({'values': '=data!$K$10:$O$10'})
        chartNbPertes.add_series({'values': '=data!$P$10:$Y$10'})
        chartNbPertes.add_series({'values': '=data!$Z$10:$AI$10'})
        chartNbPertes.add_series({'values': '=data!$AJ$10:$AS$10'})
        chartPerf = workbook.add_chart({'type': 'column'})
        chartPerf.add_series({'values': '=data!$A$11:$E$11'})
        chartPerf.add_series({'values': '=data!$F$11:$J$11'})
        chartPerf.add_series({'values': '=data!$K$11:$O$11'})
        chartPerf.add_series({'values': '=data!$P$11:$Y$11'})
        chartPerf.add_series({'values': '=data!$Z$11:$AI$11'})
        chartPerf.add_series({'values': '=data!$AJ$11:$AS$11'})
        charts.insert_chart('C3', chartImgs)
        charts.insert_chart('C3', chartFiabTaille)
        charts.insert_chart('C3', chartNbPertes)
        charts.insert_chart('C3', chartNbPoints)
        charts.insert_chart('C3', chartNbTargets)
        charts.insert_chart('C3', chartPerf)
        charts.insert_chart('C3', chartTauxProf)
