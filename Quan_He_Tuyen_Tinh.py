import numpy as np
from scipy.optimize import linprog

# Nhập số biến và số ràng buộc
num_variables = int(input("Nhập số biến: "))
num_constraints = int(input("Nhập số ràng buộc: "))

# Nhập hệ số của hàm mục tiêu
print("Nhập hệ số của hàm mục tiêu (c):")
c = np.array([float(input(f"c[{i+1}]: ")) for i in range(num_variables)])
a = input("Nhập đích hàm mục tiêu (max hoặc min):")
if a == "min":
    c = c
else:
   c *= -1
# Khởi tạo ma trận hệ số A và vector b cho các ràng buộc
A = np.zeros((num_constraints, num_variables))
b = np.zeros(num_constraints)

# Nhập ma trận hệ số A và vector b
print("Nhập ma trận hệ số A:")
for i in range(num_constraints):
    A[i] = [float(x) for x in input().split()]

print("Nhập vector b:")
b = np.array([float(x) for x in input().split()])

# Đưa hàm mục tiêu về dạng tối ưu hóa

# Giải bài toán LP
result = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)] * num_variables, method='highs')

# In kết quả
print("Biến tối ưu x:", result.x)
print("Giá trị tối ưu z:", result.fun)
