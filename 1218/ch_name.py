import os

os.chdir(r'C:\Users\student\Desktop\TIL\1218\dummy')
print(os.getcwd()) # 현재 작업 폴더를 알려줌
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG", "SSAFY"))
    