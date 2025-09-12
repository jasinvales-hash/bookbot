def get_num_words(filepath):
    with open(filepath) as f:
        str_f = f.read()
        all_words = str_f.split()
        for num_words in range(len(all_words)):
            num_words = num_words + 1
    return num_words

def get_count_char(filepath):
    with open(filepath) as f:
        str_f = f.read()
        all_words = str_f.split()
        str_all_words = str(all_words)
        str_all_words = str_all_words.lower()
        char = list(str_all_words)
#        list_num_char = []
        dict_num_char = {}
        for all_char in char:
#            num = dict_num_char[all_char]
            if all_char not in dict_num_char and all_char.isalpha() == True:
#                dict_num_char["char"] = all_char
                dict_num_char[all_char] = 1
#                list_num_char.append({"char": dict_num_char, "num": dict_num_char[all_char]})
            elif all_char in dict_num_char and all_char.isalpha() == True:
                dict_num_char[all_char] += 1
#                list_num_char.append({"char": dict_num_char, "num": dict_num_char[all_char] + 1})
#                list_num_char.append({"char": dict_num_char, "num": all_char})
        return dict_num_char

#        return list_num_char


def sort_on(items):
    return items["num"]

def sorted_dict(filepath):
    count_dict = get_count_char(filepath)
#    new_list = get_count_char(filepath)
    new_list = []
    for i in range(len(count_dict)):
         new_list.append({"char": list(count_dict)[i], "num": list(count_dict.values())[i]})
#    new_dict = {"char": list(count_dict.keys()), "num": list(count_dict.values())}
#   new_list[
#    for i in range(len(list(new_dict))):
#        new_list.append({"char": {new_dict}, "num": {new_dict[i]}})
    new_list.sort(reverse=True, key=sort_on)
#    final_list = []
#    for i in range(len(new_list)):
#        final_list.append({
#    return sorted_new_list
    return new_list
#   with open(filepath) as f:
#        str_f = f.read()
#        all_words = str_f.split()
#        str_all_words = str(all_words)
#        str_all_words = str_all_words.lower()
#        char = list(str_all_words)
#        dict_num_char = {}
#        for all_char in char:
#            if all_char not in dict_num_char:
#                dict_num_char[all_char] = 1
#            else:
#                dict_num_char[all_char} += 1
#        print(f"

#    dict_num_char = get_count_char("bookbot/frankenstein.txt")
#    return dict_num_char[all_char]
#    sorted_dict_num_char = dict_num_char.sorted(reverse=True, key=)

