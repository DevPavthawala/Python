words_stats = {}

with open("E://2k23//data scientist//practice problem program//practice problelm week1-2//13_read_write_files//poem.txt","r") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            if word in words_stats:
                words_stats[word] += 1
            else:
                words_stats[word] = 1

print(words_stats)

word_occurance = list(words_stats.values())
max_count = max(word_occurance)
print("max occurance of any word is ",max_count)

print("Word with max occurance are :")
for word,count in words_stats.items():
    if count == max_count:
        print(f'the "{word}" word is maximun and repeat upto "{count}" times')
