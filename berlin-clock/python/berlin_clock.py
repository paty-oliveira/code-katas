class BerlinClock:
    RED_LAMP = "R"
    YELLOW_LAMP = "Y"
    OFF_LAMP = "O"
    NR_LAMPS_TWO_ROW = 4
    NR_LAMPS_THREE_ROW = 4
    NR_LAMPS_FOUR_ROW = 11
    NR_LAMPS_FIVE_ROW = 4

    def convert(self, time: str) -> str:
        parsed_time = time.split(":")
        minutes = int(parsed_time[1])
        hours = int(parsed_time[0])
        seconds = int(parsed_time[2])
        first_row = self.get_seconds_row(seconds)
        two_row = self.get_five_hours_row(hours)
        three_row = self.get_single_hours_row(hours)
        four_row = self.get_five_minutes_row(minutes)
        five_row = self.get_single_minutes_row(minutes)

        return first_row + two_row + three_row + four_row + five_row

    def get_seconds_row(self, seconds):
        return self.YELLOW_LAMP if seconds % 2 == 0 else self.OFF_LAMP

    def get_five_hours_row(self, hours):
        lamps_on = hours // 5
        return self.__on_or_off(self.NR_LAMPS_TWO_ROW, lamps_on, self.RED_LAMP)

    def get_single_hours_row(self, hours: int) -> str:
        lamps_on = hours % 5
        return self.__on_or_off(self.NR_LAMPS_THREE_ROW, lamps_on, self.RED_LAMP)

    def get_five_minutes_row(self, minutes: int) -> str:
        five_minutes = ""
        lamps_on = minutes // 5
        for i in range(1, self.NR_LAMPS_FOUR_ROW + 1):
            if i <= lamps_on:
                five_minutes += self.__red_or_yellow_lamp(i)
            else:
                five_minutes += self.OFF_LAMP

        return five_minutes

    def get_single_minutes_row(self, minutes: int) -> str:
        lamps_on = minutes % 5
        return self.__on_or_off(self.NR_LAMPS_FIVE_ROW, lamps_on, self.YELLOW_LAMP)
   
    def __on_or_off(self, total_lamps, nr_lamps_on, lamp_on_symbol):
        time_format = ""
        for i in range(1, total_lamps + 1):
            if i <= nr_lamps_on:
                time_format += lamp_on_symbol
            else:
                time_format += self.OFF_LAMP
        return time_format

    def __red_or_yellow_lamp(self, lamp_number: int) -> str:
        return self.YELLOW_LAMP if lamp_number % 3 else self.RED_LAMP
