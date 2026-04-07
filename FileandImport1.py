from mycomputation import AverageFloat


file_name = 'new_file'
compute_list=[]
# if exists(file_name):
#     remove('new_file')
with open("/Users/sandeep/PycharmProjects/FirstPythonProject/file_test", "r") as f:
     for line in f:
        compute_list.append(float(line.rstrip("\n")))

print(AverageFloat(compute_list))


