def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    
    most_permanence_period = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        else:
            most_permanence_period += 1 if period[0] <= target_time <= period[1] else 0
    return most_permanence_period
