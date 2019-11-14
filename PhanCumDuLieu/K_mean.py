 
import numpy as np # thư viện tính toán toán học
import matplotlib.pyplot as plt # visualize data sử dụng đồ thị
from scipy.spatial.distance import cdist # Hỗ trợ tính khoảng cách

# Khởi tạo 500 điểm xung quanh 3 cluster (2,2) (9,2) (4,9)
means = [[2, 2], [9, 2], [4, 9]] # 3 cluster đầu tiên
cov = [[2, 0], [0, 2]]
n_samples = 500 # chọn ngẫu nhiên 500 điểm
n_cluster = 3 # số cluster
X0 = np.random.multivariate_normal(means[0], cov, n_samples)
X1 = np.random.multivariate_normal(means[1], cov, n_samples)
X2 = np.random.multivariate_normal(means[2], cov, n_samples)
X = np.concatenate((X0, X1, X2), axis = 0)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(X[:, 0], X[:, 1], 'bo', markersize=5)
plt.plot()
plt.show()

# hàm khởi tạo n_cluster tâm cụm
# lấy ngẫu nhiên 3 cụm
def kmeans_init_centers(X, n_cluster):
  
  # ngẫu nhiên index k giữa 0 và shape(X), index không trùng
  # return về X[index] của cluster
  return X[np.random.choice(X.shape[0], n_cluster, replace=False)]
  
# Hàm xác định tâm cụm của từng điểm dữ liệu trong tập dữ liệu

def kmeans_predict_labels(X, centers):
  D = cdist(X, centers)
  # return index của cluster gần nhất
  return np.argmin(D, axis = 1)
# Hàm cập nhật lại vị trí của các tâm cụm
def kmeans_update_centers(X, labels, n_cluster):
  centers = np.zeros((n_cluster, X.shape[1]))
  for k in range(n_cluster): 
    # thu thập tất cả các điểm được gán cho cụm thứ k
    Xk = X[labels == k, :]
    # tính trung bình cộng
    centers[k,:] = np.mean(Xk, axis = 0)
  return centers

  #Kiểm tra xem đã tìm được lời giải chưa
def kmeans_has_converged(centers, new_centers):
  # return True nếu 2 bộ trung tâm giống nhau
  return (set([tuple(a) for a in centers]) == 
      set([tuple(a) for a in new_centers]))

# Hàm để thấy rõ cách hoạt động của thuật toán
# Hàm này dùng để vẽ dữ liệu lên đồ thị
# Random color chỉ làm việc với k <= 4
# (Chú ý)Nếu thay đổi k > 4, sửa lại phần random color
def kmeans_visualize(X, centers, labels, n_cluster, title):
  plt.xlabel('x') # label trục x
  plt.ylabel('y') # label trục y
  plt.title(title) # title của đồ thị
  plt_colors = ['b', 'g', 'r', 'm', 'c', 'y', 'k', 'w'] # danh sách các màu hỗ trợ
 
  for i in range(n_cluster):
    data = X[labels == i] # lấy dữ liệu của cụm i
    plt.plot(data[:, 0], data[:, 1], plt_colors[i] + '^', markersize = 4, label = 'cluster_' + str(i)) # Vẽ cụm i lên đồ thị
    plt.plot(centers[i][0], centers[i][1],  plt_colors[i+4] + 'o', markersize = 10, label = 'center_' + str(i)) # Vẽ tâm cụm i lên đồ thị
  plt.legend() # Hiện bảng chú thích
  plt.show()

 # Hàm chính thực hiện thuật toán k-means
def kmeans(init_centes, init_labels, X, n_cluster):
  centers = init_centes
  labels = init_labels
  times = 0
  while True:
    labels = kmeans_predict_labels(X, centers)
    kmeans_visualize(X, centers, labels, n_cluster, 'Nhãn được gán cho dữ liệu tại thời điểm = ' + str(times + 1))
    new_centers = kmeans_update_centers(X, labels, n_cluster)
    if kmeans_has_converged(centers, new_centers):
      break
    centers = new_centers
    kmeans_visualize(X, centers, labels, n_cluster, 'Cập nhật vị trí trung tâm tại thời điểm = ' + str(times + 1))
    times += 1
  return (centers, labels, times)


init_centers = kmeans_init_centers(X, n_cluster)
print('Tọa độ khởi tạo ban đầu của các tâm cụm \n', init_centers) # In ra tọa độ khởi tạo ban đầu của các tâm cụm
init_labels = np.zeros(X.shape[0])
kmeans_visualize(X, init_centers, init_labels, n_cluster, 'Các trung tâm trong lần chạy đầu tiên.')
centers, labels, times = kmeans(init_centers, init_labels, X, n_cluster)
print('Tọa độ của các tâm cụm sau khi thực hiện thuật toán K-mean\n', centers)
 
print('Làm xong! Kmeans đã phân cụm sau', times, 'vòng lặp')




