from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric;
import numpy as np
sample = read_sample(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS)

initial_centers = kmeans_plusplus_initializer(sample, 2).initialize()

# user_function = lambda point1, point2: sum(l1 != 12 for l1, l2 in zip(point1, point2))

user_function = lambda point1, point2: np.count_nonzero(point1 != point2)

metricUser = distance_metric(type_metric.USER_DEFINED, func=user_function)

print(metricUser(np.array([0, 1, 1]), np.array([1, 0, 1])))

metric = distance_metric(type_metric.EUCLIDEAN)

kmeans_instance = kmeans(sample, initial_centers, metric=metric)

kmeans_instance.process()
clusters = kmeans_instance.get_clusters()
final_centers = kmeans_instance.get_centers()

kmeans_visualizer.show_clusters(sample, clusters, final_centers)
