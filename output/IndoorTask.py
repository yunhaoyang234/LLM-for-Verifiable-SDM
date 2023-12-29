def OutdoorTask(class_instance):
    while True:
        class_instance.observe()  # Step 1: Check for Observations
        if class_instance.pedestrian_observed() and not class_instance.chair_observed():  # If Pedestrian_Observed is true
            class_instance.turn_left()  # Step 2: Turn Left
        elif class_instance.chair_observed() and not class_instance.pedestrian_observed():  # If Chair is true
            class_instance.turn_right()  # Step 3: Turn Right
        elif class_instance.pedestrian_observed() and class_instance.chair_observed():  # If both are true
            class_instance.turn_left()  # Step 2: Turn Left
