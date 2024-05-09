import open3d as o3d

# 点群モデルの読み込む
pcd = o3d.io.read_point_cloud("testmeiji2 1.pts")

# 点群モデルを表示する
o3d.visualization.draw_geometries([pcd])