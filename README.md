# week1-assignment
1. DataAugmentation.py 是图像增强模块，包含类DataAugmentation
2. test.py 是测试文件
   调用方法： 
   from DataAugmentation import DataAugmentation
   data_aug = DataAugmentation()
   data_aug.read_file('timg.jpg') # 可支持中文路径
   
   # 然后调用data_aug对象的成员函数即可
   ...
