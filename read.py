data = []
count = 0
length = 0
new = []
good = []

with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        length += len(data[count])
        count += 1
        if count % 1000 == 0:
            print(len(data))
                      
    for line in data:
        if len(line) < 100:
            new.append(line)
            
    for line in data:
        if "good" in line:
            good.append(line)
        
               
            
print(f"檔案讀取完了,總共有{len(data)}筆資料")            
average = length/len(data)            
print("留言的平均長度=", average)

print(f"一共有{len(new)}筆留言長度小於100")
print(f"留言包含good有{len(good)}筆")


wc = { } #word_count

with open("reviews.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
        
print(len(wc))

while True:
    word = input("請問您想查什麼字(輸入q離開):")
    if word == "q":
        break
    if word in wc:
        print(word, "出現過的次數為:", wc[word])
    else:
        print("這個字沒有在留言裡哦!")
print("感謝使用此功能")
