def OutdoorTask(class_instance):
    # Step 1
    if class_instance.stop_sign_observed():
        class_instance.stop()
    # Step 2
    elif not class_instance.pedestrian_observed() and not class_instance.car_observed():
        class_instance.turn_right()
        # Step 3
        class_instance.move_forward()
