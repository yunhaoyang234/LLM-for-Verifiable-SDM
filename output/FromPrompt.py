def FromPrompt(class_instance):
    # observe the environment
    class_instance.observe()

    # check if pedestrian is observed
    if class_instance.pedestrian_observed():
        # turn left
        class_instance.turn_left()
    # check if chair is observed
    elif class_instance.chair_observed():
        # turn right
        class_instance.turn_right()
    # check if both pedestrian and chair are observed
    elif class_instance.pedestrian_observed() and class_instance.chair_observed():
        # turn left
        class_instance.turn_left()
