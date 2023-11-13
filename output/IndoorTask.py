def IndoorTask(class_instance):
    # Step 1
    if not class_instance.chair_observed():
        class_instance.move_forward()
    # Step 2
    if class_instance.pedestrian_observed():
        class_instance.turn_left()
    # Step 3
    if class_instance.chair_observed():
        class_instance.stop()
