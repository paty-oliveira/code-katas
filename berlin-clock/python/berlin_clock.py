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
        five_row = self.get_single_minutes_row(minutes)
        four_row = self.get_five_minutes_row(minutes)

        return first_row + two_row + three_row + four_row + five_row

    def get_seconds_row(self, seconds):
        first_row = ""
        if seconds % 2 == 0:
            first_row = "Y"
        else:
            first_row = "O"
        return first_row

    def get_five_hours_row(self, hours):
        two_row = ""
        lamps_on = hours // 5
        for i in range(1, self.NR_LAMPS_TWO_ROW + 1):
            if i <= lamps_on:
                two_row += self.RED_LAMP
            else:
                two_row += self.OFF_LAMP
        return two_row

    def get_single_hours_row(self, hours: int) -> str:
        single_hours = ""
        lamps_on = hours % 5
        for i in range(1, self.NR_LAMPS_THREE_ROW + 1):
            if i <= lamps_on:
                single_hours += self.RED_LAMP
            else:
                single_hours += self.OFF_LAMP
        return single_hours

    def get_single_minutes_row(self, minutes: int) -> str:
        single_minutes = ""
        lamps_on = minutes % 5
        for i in range(1, self.NR_LAMPS_FIVE_ROW + 1):
            if i <= lamps_on:
                single_minutes += self.YELLOW_LAMP
            else:
                single_minutes += self.OFF_LAMP
        return single_minutes

    def get_five_minutes_row(self, minutes: int) -> str:
        five_minutes = ""
        lamps_on = minutes // 5
        for i in range(1, self.NR_LAMPS_FOUR_ROW + 1):
            if i <= lamps_on:
                five_minutes += self.__red_or_yellow_lamp(i)
            else:
                five_minutes += self.OFF_LAMP

        return five_minutes

    def __red_or_yellow_lamp(self, lamp_number: int) -> str:
        return self.YELLOW_LAMP if lamp_number % 3 else self.RED_LAMP
