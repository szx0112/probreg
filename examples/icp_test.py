import copy
import numpy as np
import open3d as o3
import utils

source, target = utils.prepare_source_and_target_rigid_3d('bunny.pcd')

vis = o3.Visualizer()
vis.create_window()
result = copy.deepcopy(source)
source.paint_uniform_color([1, 0, 0])
target.paint_uniform_color([0, 1, 0])
result.paint_uniform_color([0, 0, 1])
vis.add_geometry(source)
vis.add_geometry(target)
vis.add_geometry(result)
threshold = 0.05
icp_iteration = 100
save_image = False

for i in range(icp_iteration):
    reg_p2l = o3.registration_icp(result, target, threshold,
                np.identity(4), o3.TransformationEstimationPointToPoint(),
                o3.ICPConvergenceCriteria(max_iteration=1))
    result.transform(reg_p2l.transformation)
    vis.update_geometry()
    vis.poll_events()
    vis.update_renderer()
    if save_image:
        vis.capture_screen_image("image_%04d.jpg" % i)
vis.run()