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
        chartHistory = workbook.add_chart({'type': 'column'})
        chartHistory.add_series({'values': '=data!$A$5:$E$5', 'name': 'images/s'})
        chartHistory.add_series({'values': '=data!$A$6:$E$6', 'name': 'récupération profondeur'})
        chartHistory.add_series({'values': '=data!$A$7:$E$7', 'name': 'fiabilité height'})
        chartHistory.add_series({'values': '=data!$A$8:$E$8', 'name': 'proportion de cibles'})
        chartHistory.add_series({'values': '=data!$A$9:$E$9', 'name': 'nombre de points'})
        chartHistory.add_series({'values': '=data!$A$10:$E$10', 'name': 'nombre de pertes'})
        chartHistory.add_series({'values': '=data!$A$11:$E$11', 'name': 'indice de performance'})
        chartHistory.set_title({'name': 'history'})
        chartPointsMin = workbook.add_chart({'type': 'column'})
        chartPointsMin.add_series({'values': '=data!$F$5:$J$5', 'name': 'images/s'})
        chartPointsMin.add_series({'values': '=data!$F$6:$J$6', 'name': 'récupération profondeur'})
        chartPointsMin.add_series({'values': '=data!$F$7:$J$7', 'name': 'fiabilité height'})
        chartPointsMin.add_series({'values': '=data!$F$8:$J$8', 'name': 'proportion de cibles'})
        chartPointsMin.add_series({'values': '=data!$F$9:$J$9', 'name': 'nombre de points'})
        chartPointsMin.add_series({'values': '=data!$F$10:$J$10', 'name': 'nombre de pertes'})
        chartPointsMin.add_series({'values': '=data!$F$11:$J$11', 'name': 'indice de performance'})
        chartPointsMin.set_title({'name': 'points_min'})
        chartSurfMin = workbook.add_chart({'type': 'column'})
        chartSurfMin.add_series({'values': '=data!$K$5:$O$5', 'name': 'images/s'})
        chartSurfMin.add_series({'values': '=data!$K$6:$O$6', 'name': 'récupération profondeur'})
        chartSurfMin.add_series({'values': '=data!$K$7:$O$7', 'name': 'fiabilité height'})
        chartSurfMin.add_series({'values': '=data!$K$8:$O$8', 'name': 'proportion de cibles'})
        chartSurfMin.add_series({'values': '=data!$K$9:$O$9', 'name': 'nombre de points'})
        chartSurfMin.add_series({'values': '=data!$K$10:$O$10', 'name': 'nombre de pertes'})
        chartSurfMin.add_series({'values': '=data!$K$11:$O$11', 'name': 'indice de performance'})
        chartSurfMin.set_title({'name': 'surface_min'})
        chartBetweenTargets = workbook.add_chart({'type': 'column'})
        chartBetweenTargets.add_series({'values': '=data!$P$5:$Y$5', 'name': 'images/s'})
        chartBetweenTargets.add_series({'values': '=data!$P$6:$Y$6', 'name': 'récupération profondeur'})
        chartBetweenTargets.add_series({'values': '=data!$P$7:$Y$7', 'name': 'fiabilité height'})
        chartBetweenTargets.add_series({'values': '=data!$P$8:$Y$8', 'name': 'proportion de cibles'})
        chartBetweenTargets.add_series({'values': '=data!$P$9:$Y$9', 'name': 'nombre de points'})
        chartBetweenTargets.add_series({'values': '=data!$P$10:$Y$10', 'name': 'nombre de pertes'})
        chartBetweenTargets.add_series({'values': '=data!$P$11:$Y$11', 'name': 'indice de performance'})
        chartBetweenTargets.set_title({'name': 'durée entre deux cibles'})
        chartDist3d = workbook.add_chart({'type': 'column'})
        chartDist3d.add_series({'values': '=data!$Z$5:$AI$5', 'name': 'images/s'})
        chartDist3d.add_series({'values': '=data!$Z$6:$AI$6', 'name': 'récupération profondeur'})
        chartDist3d.add_series({'values': '=data!$Z$7:$AI$7', 'name': 'fiabilité height'})
        chartDist3d.add_series({'values': '=data!$Z$8:$AI$8', 'name': 'proportion de cibles'})
        chartDist3d.add_series({'values': '=data!$Z$9:$AI$9', 'name': 'nombre de points'})
        chartDist3d.add_series({'values': '=data!$Z$10:$AI$10', 'name': 'nombre de pertes'})
        chartDist3d.add_series({'values': '=data!$Z$11:$AI$11', 'name': 'indice de performance'})
        chartDist3d.set_title({'name': 'distance 3d'})
        chartSizeMin = workbook.add_chart({'type': 'column'})
        chartSizeMin.add_series({'values': '=data!$AJ$5:$AS$5', 'name': 'images/s'})
        chartSizeMin.add_series({'values': '=data!$AJ$6:$AS$6', 'name': 'récupération profondeur'})
        chartSizeMin.add_series({'values': '=data!$AJ$7:$AS$7', 'name': 'fiabilité height'})
        chartSizeMin.add_series({'values': '=data!$AJ$8:$AS$8', 'name': 'proportion de cibles'})
        chartSizeMin.add_series({'values': '=data!$AJ$9:$AS$9', 'name': 'nombre de points'})
        chartSizeMin.add_series({'values': '=data!$AJ$10:$AS$10', 'name': 'nombre de pertes'})
        chartSizeMin.add_series({'values': '=data!$AJ$11:$AS$11', 'name': 'indice de performance'})
        chartSizeMin.set_title({'name': 'nombre de pertes de cible'})
        charts.insert_chart('C3', chartHistory)
        charts.insert_chart('K3', chartPointsMin)
        charts.insert_chart('S3', chartSizeMin)
        charts.insert_chart('AA3', chartDist3d)
        charts.insert_chart('C18', chartBetweenTargets)
        charts.insert_chart('K18', chartSurfMin)
        workbook.close()
