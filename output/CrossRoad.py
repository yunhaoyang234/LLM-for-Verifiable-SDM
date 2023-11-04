def CrossRoad(vehicle):
    vehicle.observe()  # observe the environment first
    if vehicle.pedestrian_observed():  # Step 1
        vehicle.stop()  # stop if pedestrian is observed
    elif vehicle.car_observed():  # Step 2
        vehicle.stop()  # stop if car is observed
    else:  # Step 3
        vehicle.move_forward()  # move forward if neither pedestrian nor car is observed
