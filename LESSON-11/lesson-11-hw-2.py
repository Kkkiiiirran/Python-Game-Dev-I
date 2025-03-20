import heapq

file = open('LESSON-11\para.txt', 'r')

para = []
for content in file:
    line = content.split()
    para.extend(line)

file.close()
print(para)


word_map ={}
for word in para:
    if word in word_map:
        word_map[word]+=1
    else:
        word_map[word] = 1

print(word_map)

heap = []
# heapq.heapify(heap)
words = []
print("Initial heap:", heap)
for word, count in word_map.items():
    if len(heap) < 5:
        heapq.heappush(heap, (count, word))  # Push as (count, word)
    else:
        heapq.heappushpop(heap, (count, word))

while heap:
    x = heapq.heappop(heap)
    print(x)


    
    
