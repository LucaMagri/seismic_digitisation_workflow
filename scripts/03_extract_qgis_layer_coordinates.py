layer = QgsProject.instance().mapLayersByName("Exon_2006_274_03")[0]
output = []

for feature in layer.getFeatures():
    geom = feature.geometry()
    for pt in geom.vertices():
        output.append(f"{pt.x()},{pt.y()}")

with open(r"C:\Users\lmag0269\OneDrive - The University of Sydney (Staff)\Coral_Sea_QGIS\coord_exported\Exon_2006_274_03.txt", "w") as f:
    f.write("\n".join(output))
