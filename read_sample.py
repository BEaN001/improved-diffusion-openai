import numpy as np
from PIL import Image
# arr0 = np.array([0,1,2,3])
# arr1 = np.array([4,5,6,7,8])

# np.savez('openai-', a = arr0, b = arr1)

# datas = np.load('openai-2022-07-15-12-22-11-400658/samples_32x64x64x3.npz')
# print(datas.files)
# # print(datas['a'])
# # print(datas['b'])
# i = 0
# for data in datas['arr_0']:
#     print(data.shape)
#     Image.fromarray(data).save(f'sample_{i}.png')
#     i += 1

# datas = np.load('/tmp/openai-2022-07-15-18-50-40-805570/samples_16x256x256x3.npz')
# print(datas.files)
# # print(datas['a'])
# # print(datas['b'])
# i = 100
# for data in datas['arr_0']:
#     print(data.shape)
#     Image.fromarray(data).save(f'sample_{i}.png')
#     i += 1

datas = np.load('/tmp/openai-2022-07-18-14-25-23-820326/samples_16x256x256x3.npz')
print(datas.files)
# print(datas['a'])
# print(datas['b'])
i = 200
for data in datas['arr_0']:
    print(data.shape)
    Image.fromarray(data).save(f'sample_{i}.png')
    i += 1