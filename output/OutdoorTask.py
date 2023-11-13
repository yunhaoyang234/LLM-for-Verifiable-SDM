def OutdoorTask(vehicle):
    # Step 1
    if vehicle.stop_sign_observed():
        vehicle.approach_stop_sign()

    # Step 2
    vehicle.stop()

    # Step 3
    if not vehicle.pedestrian_observed() and not vehicle.car_observed():
        vehicle.turn_right()
