
def is_failing(grade):
    if grade >= 60:
        return False
    else:
        return True


def can_ski_today(is_sunny, is_snowing):
    if is_sunny == True and is_snowing == False:
        return True
    else:
        return False


def is_in_zone(x, left_edge, right_edge):
    if x > left_edge:
        if x < right_edge:
            return True
        else:
            return False
    else:
        return False


def is_milan_event(venue_name):
    """Checking if venue is in the city of Milan"""
    if venue_name == 'Milan Speed Skating Area':
        return True
    elif venue_name == 'Milan Hockey Forum':
        return True
    elif venue_name == 'Olympic Stadium of Milan':
        return True
    else:
        return False
