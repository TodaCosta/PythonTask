def find_top_20(*args):

    dict_name_result = {}
    value_input_list = []
    scores_list = []
    extra_scores_list = []
    top_20_list = []

    for i in args:
        for j in i:
            for h in j.values():
                value_input_list.append(h)

    for i in range(0, len(value_input_list), 3):
        dict_name_result[value_input_list[i]] = 0

    for i in range(1, len(value_input_list), 3):
        sum_scores = sum(value_input_list[i].values())
        scores_list.append(sum_scores)

    for i in range(2, len(value_input_list), 3):
        extra_scores_list.append(value_input_list[i])

    sum_scores_and_extra = list(i + j for i, j in zip(scores_list, extra_scores_list))
    dict_name_result = dict(zip(dict_name_result, sum_scores_and_extra))

    dict_name_result = dict(sorted(dict_name_result.items(), reverse=True, key=lambda x: x[1]))
    for k, v in list(dict_name_result.items())[:20]:
        top_20_list.append(k)
    return top_20_list


print(find_top_20([{"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}]))