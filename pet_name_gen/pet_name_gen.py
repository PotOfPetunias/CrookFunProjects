from math import nan
import random
from sounds import consonant_list
from sounds import vowel_list
from sounds import Sound

def gen_archie_like():
    print(random.choice(vowel_list))
    print(random.choice(consonant_list))
    print(random.choice(consonant_list))
    print(vowel_list[1]) # ee

def gen_sammie_like():
    print(random.choice(consonant_list))
    print(random.choice(vowel_list))
    print(random.choice(consonant_list))
    print(vowel_list[1]) # ee

def gen_smart_name():
    done = False
    name = []
    while not done:
        if len(name) == 0:
            name.append(random.choice(consonant_list+vowel_list))
        elif not name[-1].is_consonant():
            name.append(random.choice(consonant_list))
        else: # The last sounds was a consonant
            if len(name) == 1:
                name.append(random.choice(consonant_list+vowel_list))
            elif name[-2].is_consonant(): # There are two consonants in a row
                if any(not s.is_consonant() for s in name): # is there already a vowel?
                    # One vowel already exists
                    name.append(vowel_list[1])
                    done = True
                else:
                    name.append(random.choice(vowel_list))
            else:
                assert any(not s.is_consonant() for s in name)
                if random.randint(0,1) % 2 == 0:
                    name.append(random.choice(consonant_list))
                name.append(vowel_list[1])
                done = True
    return name


if __name__ == "__main__":
    print("A random name is :")
    name = gen_smart_name()
    [print(a) for a in name]
    print("A random Archie like name is :")
    gen_archie_like()
    print("A random Sammie like name is :")
    gen_sammie_like()