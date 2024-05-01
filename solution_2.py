class AirTicket:
    """
     Represents an air ticket and provides methods for creating and formatting tickets.

    Attributes:
        passenger_name (list): A list containing passenger names.
        _from (list): A list containing departure locations.
        to (list): A list containing destination locations.
        date_time (list): A list containing departure date and time.
        flight (list): A list containing flight numbers.
        seat (list): A list containing seat numbers.
        _class (list): A list containing ticket classes.
        gate (list): A list containing gate numbers.

    Methods:
        __init__: Initializes an AirTicket object with data from a given string.
        __str__: Returns a formatted string representation of the AirTicket object.
    """
    passenger_name = []
    _from = []
    to = []
    date_time = []
    flight = []
    seat = []
    _class = []
    gate = []

    def __init__(self, data):
        """
        Initializes an AirTicket object with data from a given string.

        Args:
            data (str): A string containing ticket information separated by ';'.
        """
        person_data = data.split(';')
        self.name = person_data[0]
        AirTicket.passenger_name.append(person_data[0])
        AirTicket._from.append(person_data[1])
        AirTicket.to.append(person_data[2])
        AirTicket.date_time.append(person_data[3])
        AirTicket.flight.append(person_data[4])
        AirTicket.seat.append(person_data[5])
        AirTicket._class.append(person_data[6])
        if person_data[7][-1] == '\n':
            AirTicket.gate.append(person_data[7][:-1])
        else:
            AirTicket.gate.append(person_data[7])

    def __str__(self):
        """
        Returns a formatted string representation of the AirTicket object.

        Returns:
            str: The formatted ticket information.
        """
        ind = AirTicket.passenger_name.index(self.name)
        return ('|' + AirTicket.passenger_name[ind] + ' ' * (16 - len(AirTicket.passenger_name[ind])) + '|'
                + AirTicket._from[ind] + ' ' * (4 - len(AirTicket._from[ind])) + '|' + AirTicket.to[ind] +
                ' ' * (3 - len(AirTicket.to[ind])) + '|' + AirTicket.date_time[ind] +
                ' ' * (16 - len(AirTicket.date_time[ind])) + '|' + AirTicket.flight[ind] +
                ' ' * (20 - len(AirTicket.flight[ind])) + '|' + AirTicket.seat[ind] +
                ' ' * (4 - len(AirTicket.seat[ind])) + '|' + AirTicket._class[ind] +
                ' ' * (3 - len(AirTicket._class[ind])) + '|' + AirTicket.gate[ind] +
                ' ' * (4 - len(AirTicket.gate[ind])) + '|')


class Load:
    """
    Represents a data loader for AirTicket objects.

    Attributes:
        data (list): A list containing loaded AirTicket objects.

    Methods:
        write: Reads ticket data from a file and creates AirTicket objects.
    """
    data = []

    @classmethod
    def write(cls, file):
        """
        Reads ticket data from a file and creates AirTicket objects.

        Args:
            file (str): The path to the file containing ticket data.
        """
        with open(file) as f:
            tickets = f.readlines()
            for n in range(1, len(tickets)):
                tick = AirTicket(tickets[n])
                Load.data.append(tick)
