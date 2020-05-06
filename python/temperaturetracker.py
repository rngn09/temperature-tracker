class TempTracker():
    """Temperature Tracker"""

    def __init__(self):
        """Initializes the object"""

        self.temperatures = dict()
        self.min_temp = 110
        self.max_temp = 0

    def insert(self, temp):
        """
        Inserts new recorded temperature to collection.

        :param temp: New temperature to add.
        :type temp: int
        """
        # check if given temp in valid range
        if temp < 0 or temp > 110:
            msg = "Temperature out of range: {}".format(temp)
            raise ValueError(msg)

        # add temp to collection
        if temp in self.temperatures:
            self.temperatures[temp] += 1
        else:
            self.temperatures[temp] = 1

        # check if it is min or max
        if temp >= self.max_temp:
            self.max_temp = temp
        if temp <= self.min_temp:
            self.min_temp = temp

    def get_min(self):
        """
        Gets minimum recorded temperature from collection.

        :return: minimum temperature
        :rtype: int
        """
        if not self.temperatures:
            return None
        return self.min_temp

    def get_max(self):
        """
        Gets maximum recorded temperature from collection.

        :return: maximum temperature
        :rtype: int
        """
        if not self.temperatures:
            return None
        return self.max_temp

    def get_mean(self):
        """
        Gets mean of all recorded temperatures in collection.

        :return: mean of all temperatures
        :rtype: float
        """
        if not self.temperatures:
            return None

        total_temp = float()
        total_count = float()

        for temp, count in self.temperatures.items():
            total_temp += temp * count
            total_count += count

        return round(total_temp / total_count, 1)
