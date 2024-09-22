# 1

def create_sentence(*words):
    return ' '.join(words[:7])

sentence = create_sentence('This', 'is', 'a', 'sentence', 'with', 'multiple', 'words', 'included')
print(sentence)

# 2

def filter_bad_words(sentence):
    bad_words = ['lazy', 'don’t feel like it']
    
    filtered_sentence = ' '.join([word for word in sentence.split() if word not in bad_words])
    return filtered_sentence

filtered_sentence = filter_bad_words('I don’t feel like working today because I am lazy')
print(filtered_sentence)

# 3

def add_squares(list1, list2):
    return list(map(lambda x, y: x + y**2, list1, list2))

list1 = [1, 2, 3]
list2 = [4, 5]
result = add_squares(list1, list2)
print(result)

# 4

def add_one_to_each(lst):
    return list(map(lambda x: x + 1, lst))

my_list = [3, 5, 7, 9]
new_list = add_one_to_each(my_list)
print(new_list)
