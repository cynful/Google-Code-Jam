def consider_words(words, index):
    count = 0
    word_map = {}
    for word in words:
        if index > len(word):
            continue
        last_char = word[-1*index]
        if last_char in word_map:
            word_map[last_char].append(word)
        else:
            word_map[last_char] = [word]
    
    for last_char in word_map.keys():
        lengt = len(word_map[last_char])
        if lengt > 2:
            res = consider_words(word_map[last_char], index+1)
            if lengt - res >= 2:
                count += 2
            count += res
            
        elif lengt == 2:
            count += 2
    
    return count

def solution():
  numwords = eval(input())
  words = [input() for j in range(numwords)]

  return consider_words(words, 1)

for i in range(eval(input())):
    print("Case #%d: %d" % (i+1, solution()))