class BerlinClock:
    RED_LAMP = "R"
    YELLOW_LAMP = "Y"
    OFF_LAMP = "O"
    NR_LAMPS_SINGLE_ROW = 4
    NR_LAMPS_FIVE_ROW = 11

    def convert(self, time: str) -> str:
        parsed_time = time.split(":")
        minutes = self.__extract_minutes(parsed_time)
        five_row = self.get_single_minutes_row(minutes)
        four_row = self.get_five_minutes_row(minutes)

        berlin_format = four_row + five_row

        return berlin_format

    def get_single_minutes_row(self, minutes: int) -> str:
        single_minutes = ""
        lamps_on = minutes % 5
        for i in range(1, self.NR_LAMPS_SINGLE_ROW + 1):
            if i <= lamps_on:
                single_minutes += self.YELLOW_LAMP
            else:
                single_minutes += self.OFF_LAMP
        return single_minutes

    def get_five_minutes_row(self, minutes: int) -> str:
        five_minutes = ""
        lamps_on = minutes // 5
        for i in range(1, self.NR_LAMPS_FIVE_ROW + 1):
            if i <= lamps_on:
                five_minutes += self.__red_or_yellow_lamp(i)
            else:
                five_minutes += self.OFF_LAMP

        return five_minutes

    def __extract_minutes(self, parsed_time: list) -> int:
        return int(parsed_time[1])

    def __red_or_yellow_lamp(self, lamp_number: int) -> str:
        return self.YELLOW_LAMP if lamp_number % 3 else self.RED_LAMP
