class Night:
    def __init__(
        self,
        measurement_start,
        measurement_end,
        measurement_duration_in_s,
        sleep_quality,
        sleep_notes,
        wake_up_mood,
        heart_rate,
        nr_of_steps,
        sleep_regularity=None,
        alarm_mode=None,
        air_pressure_in_pa=None,
        city_name=None,
        nr_of_moves_per_h=None,
        time_asleep_in_s=None,
        time_before_sleep_in_s=None,
        window_start=None,
        window_end=None,
        did_snore=None,
        snore_time=None,
        weather_temp_in_c=None,
        weather_type=None,
    ):
        self.measurement_start = measurement_start
        self.measurement_end = measurement_end
        self.sleep_quality = sleep_quality
        self.sleep_regularity = sleep_regularity
        self.wake_up_mood = wake_up_mood
        self.heart_rate = heart_rate
        self.nr_of_steps = nr_of_steps
        self.alarm_mode = alarm_mode
        self.air_pressure_in_pa = air_pressure_in_pa
        self.city_name = city_name
        self.nr_of_moves_per_h = nr_of_moves_per_h
        self.measurement_duration_in_s = measurement_duration_in_s
        self.time_asleep_in_s = time_asleep_in_s
        self.time_before_sleep_in_s = time_before_sleep_in_s
        self.window_start = window_start
        self.window_end = window_end
        self.did_snore = did_snore
        self.snore_time = snore_time
        self.weather_temp_in_c = weather_temp_in_c
        self.weather_type = weather_type
        self.sleep_notes = sleep_notes
