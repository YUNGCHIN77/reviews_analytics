data = []
count = 0
length = 0

with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        length += len(data[count])
        count += 1
        if count % 1000 == 0:
            print(len(data))
            
print(f"檔案讀取完了,總共有{len(data)}筆資料")            
average = length/len(data)            
print("留言的平均長度=", average)


