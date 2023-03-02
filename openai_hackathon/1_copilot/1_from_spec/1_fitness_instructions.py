"""
Add type hints to all your functionality and use mypi to test for correctness.

Compute the total intensity of repetitions of a workout.
"""
def intensity(reps: int, weight: int) -> int:
    return reps * weight


def routine_intensity(routine: list) -> int:
    """
    Compute the total intensity of a routine for any number of workouts.
    """

    return sum([intensity(reps, weight) for reps, weight in routine])

"""
Compute the total intensity for any number of days that has any number routines. 
"""
def total_intensity(days: list) -> int:
    intensity = 0
    for routine in days:
       intensity+=sum([routine_intensity(routine)])
    return intensity

"""
Plan a week of workouts based on the different parts of the body
and return the total intensity.
"""

planning = { 
    "lower": {
        "days": ["Monday", "Wednesday", "Friday"],
        "routine": [[[10,100],[10,100],[10,100]], 
                    [[10,100],[10,100],[10,100]], 
                    [[10,100],[10,100],[10,100]]]
    },
    "upper": {
        "days": ["Tuesday", "Thursday", "Saturday"],
        "routine": [[[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]]]
    },
    "core": {
        "days": ["Monday", "Wednesday", "Friday"],
        "routine": [[[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]]]
    }
}
def total_intensity_plan(planning):
    """
    Plan a week of workouts based on the different parts of the body.
    """
    intensity = 0
    for part in planning:
        intensity+=total_intensity(planning[part]["routine"])
    return intensity
    

"""
Define a minimum and maximum weekly intensity and select a plan on intensity and 
balance across the parts of the body and days of the week. 
"""
planning1 = { 
    "lower": {
        "days": ["Monday", "Wednesday", "Friday"],
        "routine": [[[10,100],[10,100],[10,100]], 
                    [[10,100],[10,100],[10,100]], 
                    [[10,100],[10,100],[10,100]]]
    },
    "upper": {
        "days": ["Tuesday", "Thursday", "Saturday"],
        "routine": [[[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]]]
    },
    "core": {
        "days": ["Monday", "Wednesday", "Friday"],
        "routine": [[[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]],
                    [[10,100],[10,100],[10,100]]]
    }
}
planning2 = { 
    "lower": {
        "days": ["Monday", "Wednesday", "Friday"],
        "routine": [[[5,100],[5,100],[5,100]], 
                    [[5,100],[5,100],[5,100]], 
                    [[5,100],[5,100],[5,100]]]
    },
    "upper": {
        "days": ["Tuesday", "Thursday", "Saturday"],
        "routine": [[[4,100],[10,100],[3,100]],
                    [[10,100],[4,100],[10,100]],
                    [[3,100],[10,100],[4,100]]]
    },
    "core": {
        "days": ["Monday", "Wednesday", "Friday"],
        "routine": [[[5,100],[10,100],[4,100]],
                    [[10,100],[5,100],[10,100]],
                    [[9,100],[10,100],[10,100]]]
    }
}


def select_plan(plans: list, min_intensity: int, max_intensity: int) -> list:
    """
    Define a minimum and maximum weekly intensity and select a plan on intensity and 
    balance across the parts of the body and days of the week. 
    """
    for plan in plans:
        intensity = total_intensity_plan(plan)
        if min_intensity <= intensity <= max_intensity:
            return plan
    return "Could not find a plan within the given intensity range."

if __name__ == "__main__":
    print(select_plan([planning1, planning2], 0, 30000))
    print(select_plan([planning1, planning2], 0, 20000))
    print(select_plan([planning1, planning2], 0, 10000))