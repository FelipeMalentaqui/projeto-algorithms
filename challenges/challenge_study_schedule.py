def study_schedule(permanence_period, target_time):
    total_alunos = 0
    if type(target_time) != int:
        return None

    # if permanence_period

    for tempo1, tempo2 in permanence_period:
        if type(tempo1) != int or type(tempo2) != int:
            return None
        # print(f"{tempo1}\n{tempo2}\n")
        if tempo1 <= target_time and tempo2 >= target_time:
            # if tempo1 <= target_time <= tempo2:
            # a comparação vai depender pra quem você esta olhando
            total_alunos += 1

    return total_alunos


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)]
target_time = 3
print(study_schedule(permanence_period, target_time))
