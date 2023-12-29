def CrossRoad(class_instance):
    # Step 1: Check for Observations
    class_instance.observe()
    if class_instance.pedestrian_observed() and not class_instance.chair_observed():
        # Step 2: Turn Left
        class_instance.turn_left()
    elif not class_instance.pedestrian_observed() and class_instance.chair_observed():
        # Step 3: Turn Right
        class_instance.turn_right()
    elif class_instance.pedestrian_observed() and class_instance.chair_observed():
        # Step 2: Turn Left
        class_instance.turn_left()
