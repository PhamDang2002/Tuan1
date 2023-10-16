from qgis.core import QgsProject

# Lấy lớp hiện tại
layer = QgsProject.instance().mapLayersByName('beever_bonds')[0]

# Tạo một biểu đồ mới và thay đổi thành màu đỏ
symbol = QgsMarkerSymbol.createSimple({'name': 'circle', 'color': 'red'})

# Đặt kích thước cho biểu đồ

symbol.setSize(11)

# Áp dụng biểu đồ cho lớp
renderer = layer.renderer()
renderer.setSymbol(symbol)

# Cập nhật lớp
layer.triggerRepaint()
