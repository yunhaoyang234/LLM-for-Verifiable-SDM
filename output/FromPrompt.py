def FromPrompt(class_instance):
    # Observe the environment
    class_instance.observe()

    # Check if both pedestrian and chair are observed
    if class_instance.pedestrian_observed() and class_instance.chair_observed():
        class_instance.turn_left()
    # Check if only pedestrian is observed
    elif class_instance.pedestrian_observed():
        class_instance.turn_left()
    # Check if only chair is observed
    elif class_instance.chair_observed():
        class_instance.turn_right()
    else:
        # If nothing is observed, move forward
        class_instance.move_forward()
