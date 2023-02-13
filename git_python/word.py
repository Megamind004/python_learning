a = input("random string: ")
word = input("Wanted word: ")    

def count_word(string,word):
    cnt = 0 
    for i in range(len(a)-len(word)+1):
        if a[i:i+len(word)] == word:
            cnt += 1

    print(cnt)

wc = count_word(a,word)

