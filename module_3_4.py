def single_root_words(droot_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower() in droot_word.lower() or droot_word.lower() in i.lower():
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
