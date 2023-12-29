def IndoorTask(class_instance):
    while True:
        class_instance.observe()  # Step 1: Check for Observations
        if class_instance.pedestrian_observed() and not class_instance.chair_observed():  # Pedestrian_Observed is true and Chair is false
            class_instance.turn_left()  # Step 2: Turn Left
        elif not class_instance.pedestrian_observed() and class_instance.chair_observed():  # Chair is true and Pedestrian_Observed is false
            class_instance.turn_right()  # Step 3: Turn Right
        elif class_instance.pedestrian_observed() and class_instance.chair_observed():  # both Pedestrian_Observed and Chair are true
            class_instance.turn_left()  # Step 2: Turn Left
