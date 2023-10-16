from qgis.core import QgsProject
from qgis.gui import QgsMapToolEmitPoint
from qgis.PyQt.QtGui import QColor

# Lấy lớp hiện tại
layer = QgsProject.instance().mapLayersByName('beever_bonds')[0]

# Tạo một biểu đồ mới và thay đổi thành màu đỏ
symbol = QgsMarkerSymbol.createSimple({'name': 'retangle', 'color': 'red'})

# Đặt kích thước cho biểu đồ
symbol.setSize(5)

# Áp dụng biểu đồ cho lớp
renderer = layer.renderer()
renderer.setSymbol(symbol)

# Cập nhật lớp
layer.triggerRepaint()

# Tạo một công cụ bản đồ mới để xử lý sự kiện nhấp chuột
class PointTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def canvasReleaseEvent(self, event):
        # Khi nhấp chuột, thay đổi màu sắc của ký hiệu
        if symbol.color().name() == '#ff0000':
            symbol.setColor(QColor(0,0,0))  # Đổi màu thành đen
        else:
            symbol.setColor(QColor(255,0,0))  # Đổi màu thành đỏ
        layer.triggerRepaint()

# Kích hoạt công cụ bản đồ
canvas = iface.mapCanvas()
tool = PointTool(canvas)
canvas.setMapTool(tool)
