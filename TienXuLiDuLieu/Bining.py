from collections import Counter # Thư viện Counter trong python để đếm
import statistics
# Hàm tạo các giỏ với:
#dataset là bộ dữ liệu
# lower_bound là giá trị nhỏ nhất, bắt đầu các bin
# quantity là số lượng giỏ
def create_bins1(dataset,lower_bound, quantity):# Số giỏ biết trước
    bins = []
    width_long = round((max(dataset)-min(dataset))/quantity) #tính độ rộng cho giỏ
    for low in range(lower_bound, 
                     lower_bound + quantity*width_long + 1, width_long):
        bins.append((low, low+width_long))
    return bins

def create_bins2(dataset,lower_bound):# Số giỏ không biết trước
    bins = []
    width_long = round((max(dataset)-min(dataset))/len(dataset)) #tính độ rộng cho giỏ
    for low in range(lower_bound, 
                     lower_bound + quantity*width_long + 1, width_long):
        bins.append((low, low+width_long))
    return bins
#Hàm tìm  giỏ cho 1 giá trị trong bộ dữ liệu(dữ liệu đó thuộc giỏ nào)
def find_bin(value, bins):
    for i in range(0, len(bins)):
        if bins[i][0] <= value < bins[i][1]:
            return i
    return -1

dataset = [15,17,19,25,29,31,33,41,42,45,45,47,52,52,64]
bins = create_bins1(dataset=dataset,lower_bound=min(dataset),quantity=4) # khởi tạo các giỏ
#bins1 = create_bins_withdeep(dataset,4)
#print(bins1)
print(bins)
binned_weights = [] # Khởi tạo các giỏ đã chia dữ liệu
for value in dataset:
    bin_index = find_bin(value, bins)
    print(value, bin_index, bins[bin_index])
    binned_weights.append(bin_index)
frequencies = Counter(binned_weights) # đếm xem mỗi giỏ có bao nhiêu dữ liệu
print(frequencies)


