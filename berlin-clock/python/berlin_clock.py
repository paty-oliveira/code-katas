class BerlinClock:

    def convert(self, time: str) -> str:
        parsed_time = time.split(":")
        minutes = self.extract_minutes(parsed_time)
        berlin_format = self.get_single_minutes_row(minutes)

        return berlin_format

    def get_single_minutes_row(self, minutes: int) -> str:
        total_lamps = 4
        nr_lamps_on = minutes % 5
        single_minutes_row_format = "Y" * nr_lamps_on

        time = self.fill_with_off_lamps(single_minutes_row_format, total_lamps)

        return time

    def fill_with_off_lamps(self, time_format: str, total_lamps: int) -> str:
        if len(time_format) < total_lamps:
            nr_off_lamps = total_lamps - len(time_format)
            time_format += "O" * nr_off_lamps
        return time_format

    def extract_minutes(self, parsed_time: list) -> int:
        minutes = int(parsed_time[1])
        return minutes
