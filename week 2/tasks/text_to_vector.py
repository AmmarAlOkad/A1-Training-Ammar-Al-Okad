import numpy as np

print()
################

sen1 = "I am a student"
sen2 = "I am a teacher"

sen_split1 = sen1.split()
sen_split2 = sen2.split()
################

bag_of_word = set(sen_split1 + sen_split2)

print("bag_of_word", bag_of_word)

print()
################

def sen_to_vector(sen, bag_of_words):
    my_list = []
    for word in bag_of_words:
        if word in sen:
            my_list.append(1)
        else:
            my_list.append(0)
    return np.array(my_list)

vec1 = sen_to_vector(sen1, bag_of_word)
vec2 = sen_to_vector(sen2, bag_of_word)

print("vec1", vec1)
print("vec2", vec2)

print()
################

dot_product = np.dot(vec1, vec2)
print("dot_product", dot_product)
print()

norm1 = np.linalg.norm(vec1)
norm2 = np.linalg.norm(vec2)
print("norm1", norm1)
print("norm2", norm2)
print()

cosine_similarity = dot_product / (norm1 * norm2)
print("cosine_similarity", cosine_similarity)
print()
################

