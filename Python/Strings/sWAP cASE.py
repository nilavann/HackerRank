def swap_case(s):
    return "".join( [ word.upper() if( word.islower()) else word.lower() for word in s])