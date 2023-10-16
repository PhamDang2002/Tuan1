# Hàm này trả về một danh sách các lớp có tên ‘beever_bonds’ trong dự án QGIS hiện tại.
layers = QgsProject.instance().mapLayersByName('beever_bonds')

# Hàm này tạo một lớp vector mới từ nguồn dữ liệu của lớp đầu tiên trong danh sách layers
layer = QgsVectorLayer(layers[0].dataProvider().dataSourceUri(), '', 'ogr')

# Hàm này trả về các khả năng của nhà cung cấp dữ liệu cho lớp, ví dụ như khả năng thêm, xóa hoặc chỉnh sửa các đối tượng.
caps = layer.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteFeatures:
    # Lấy tất cả các đối tượng từ lớp
    all_features = layer.getFeatures()

    # Tạo một danh sách chứa ID của các đối tượng từ hàng thứ 2 trở xuống
    ids_to_delete = [f.id() for f in all_features if f.id() >= 1]

    # Xóa các đối tượng
    res = layer.dataProvider().deleteFeatures(ids_to_delete)
