def CrossRoad(class_instance):
    # Step 1: Check for Obstacles
    if class_instance.pedestrian_observed() or class_instance.car_observed():
        class_instance.stop()
    # Step 2: Check for Stop Sign
    elif class_instance.stop_sign_observed():
        class_instance.approach_stop_sign()
    # Step 3: Move Forward
    elif not class_instance.pedestrian_observed() and not class_instance.car_observed() and not class_instance.stop_sign_observed():
        class_instance.move_forward()
