# Hàm này trả về một danh sách các lớp có tên ‘beever_bonds’ trong dự án QGIS hiện tại.
layers = QgsProject.instance().mapLayersByName('beever_bonds')

# Hàm này tạo một lớp vector mới từ nguồn dữ liệu của lớp đầu tiên trong danh sách layers
layer = QgsVectorLayer(layers[0].dataProvider().dataSourceUri(), '', 'ogr')

# Hàm này trả về các khả năng của nhà cung cấp dữ liệu cho lớp, ví dụ như khả năng thêm, xóa hoặc chỉnh sửa các đối tượng.
caps = layer.dataProvider().capabilities()

if caps & QgsVectorDataProvider.ChangeGeometries:
    # Lấy tất cả các đối tượng từ lớp
    all_features = layer.getFeatures()

    # Tạo một danh sách chứa ID của các đối tượng từ hàng thứ 5,6 đếm từ 0
    ids_to_change = [f.id() for f in all_features if f.id() in [0]]

    # Thay đổi vị trí không gian của các đối tượng
    for id in ids_to_change:
        new_geom = QgsGeometry.fromPointXY(QgsPointXY(111, 12)) # Tạo một hình dạng mới tại vị trí (108, 11)
        layer.dataProvider().changeGeometryValues({id: new_geom})
