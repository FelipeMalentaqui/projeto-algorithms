def study_schedule(permanence_period, target_time):
    total_alunos = 0
    # if target_time != int():
    #     return None
    for tempo1, tempo2 in permanence_period:
        # if tempo1 != int() or tempo2 != int():
        #     return None
        print(f'{tempo1}\n{tempo2}\n')
        if tempo1 == target_time or tempo2 == target_time:
            total_alunos += 1

    return total_alunos


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# permanence_period = [(9, 10), (3, 11)]
# target_time = 5
# print(study_schedule(permanence_period, target_time))
