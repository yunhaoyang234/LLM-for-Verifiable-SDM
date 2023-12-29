def FromPrompt(class_instance):
    # First, the vehicle observes the environment
    class_instance.observe()

    # If both a pedestrian and a chair are observed, the vehicle turns left
    if class_instance.pedestrian_observed() and class_instance.chair_observed():
        class_instance.turn_left()
    # If only a pedestrian is observed, the vehicle also turns left
    elif class_instance.pedestrian_observed():
        class_instance.turn_left()
    # If only a chair is observed, the vehicle turns right
    elif class_instance.chair_observed():
        class_instance.turn_right()
    # If neither a pedestrian nor a chair is observed, the vehicle moves forward
    else:
        class_instance.move_forward()
