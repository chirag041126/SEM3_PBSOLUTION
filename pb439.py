list=["lessonplan", "lesson","ees", "length"]
list.sort(reverse=True)
ans=""
for i in range(len(list[-1])):
    if list[0][i]==list[-1][i]:
        ans+=list[-1][i]
        continue
    else:
        print(-1)
        break
print(ans)    
