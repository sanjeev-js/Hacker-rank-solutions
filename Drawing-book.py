num_pages = int(input())
page_no = int(input())

list_of_pages = []
i = 1
while i<num_pages+1:
    if i == 1:
        list_of_pages.append([i])
        i = i + 1
    elif num_pages % 2 == 0:
        if i < num_pages:
            list_of_pages.append([i,i+1])
            i = i + 2 
        else:
            list_of_pages.append([i])
            break
    else:
        list_of_pages.append([i,i+1])
        i = i + 2
count_start = 0
count_end = 0
if (page_no in list_of_pages[0]) or (page_no in list_of_pages[-1]):
    print(0)
    exit()
i = 0
while page_no not in list_of_pages[i]:
    count_start = count_start + 1
    i = i + 1
i = len(list_of_pages)-1
while page_no not in list_of_pages[i]:
    count_end = count_end + 1
    i = i - 1
if count_start<count_end:
    print(count_start)
elif count_start>count_end:
    print(count_end)
else:
    print(count_start)
