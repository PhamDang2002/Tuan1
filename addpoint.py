#Hàm này trả về một danh sách các lớp có tên ‘beever_bonds’ trong dự án QGIS hiện tại.
layers=QgsProject.instance () .mapLayersByName('beever_bonds')

#Hàm này tạo một lớp vector mới từ nguồn dữ liệu của lớp đầu tiên trong danh sách layers
layer= QgsVectorLayer (layers [0].dataProvider().dataSourceUri (), '', 'ogr')

#Hàm này trả về các khả năng của nhà cung cấp dữ liệu cho lớp, ví dụ như khả năng thêm, xóa hoặc chỉnh sửa các đối tượng.
caps= layer.dataProvider () .capabilities ()

if caps & QgsVectorDataProvider.AddFeatures:

#Hàm này tạo một đối tượng mới với các trường giống như lớp đã cho.
    feat= QgsFeature(layer.fields())

#Hàm này thiết lập các thuộc tính cho đối tượng.
    feat.setAttributes ([0, 'added programatically'])

#Hàm này thiết lập hình dạng cho đối tượng dựa trên một điểm XY.
    feat.setGeometry (QgsGeometry.fromPointXY (QgsPointXY (111, 12)))

#Hàm này thêm đối tượng vào nhà cung cấp dữ liệu của lớp.
    res, outFeats= layer.dataProvider().addFeatures([feat])
