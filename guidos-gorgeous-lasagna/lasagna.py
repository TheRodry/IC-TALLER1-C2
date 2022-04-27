EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time: int):
    """
    Calculate the bake time remaining.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time;
# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_layers: int):
    '''
    Return preparation time based on numbers of layers 
    '''
    return PREPARATION_TIME * number_layers;
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_layers: int, elapsedTime: int):
    '''
    Return elapsed time
    '''
    return preparation_time_in_minutes(number_layers) + elapsedTime;