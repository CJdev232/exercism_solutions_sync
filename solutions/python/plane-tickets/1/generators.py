"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    count=0
    dict={0:'A',1:'B',2:'C',3:'D'}
    series_of_letters=''
    while (number-count>0):
        current_letter=dict[count%4]
        #series_of_letters.join(current_letter)
        yield current_letter
        count+=1
    
        
        


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    current=0
    dict={0:'A',1:'B',2:'C',3:'D'}
    num_rows=number//4+1
    row_index=current//4+1
    series_of_seats=''
    while (number-current>0):
        row_index=current//4+1
        if row_index>=13:
            row_index+=1
        current_letter=dict[current%4]
        seat=str(row_index)+current_letter
        #if row_index<13:
            #seat=row_index+current_letter
        #else:
            #seat=row_index+1+current_letter
        #series_of_seats.join(seat)
        yield seat
        current+=1
    

        
            
        
    
        
    

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    number=len(passengers)
    current=0
    dict={0:'A',1:'B',2:'C',3:'D'}
    num_rows=number//4+1
    row_index=current//4+1
    series_of_seats=''
    seat_assign={}
    #while (number-current>0):
    for current,passenger in enumerate(passengers):
        row_index=current//4+1
        if row_index>=13:
            row_index+=1
        current_letter=dict[current%4]
        current_passenger=passengers[current]
        #if row_index<13：
            #seat=row_index+current_letter
        #else:
            #seat=row_index+1+current_letter
        #seat_assign[current]=seat
        seat=str(row_index)+current_letter
        seat_assign[passenger]=seat
        current+=1
    return seat_assign
    
        
            

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    #flight_numbers=''
    for seat_number in seat_numbers:
        #flight_number=seat_number+flight_id
        #flight_numbers.join(flight_number)
        code=seat_number+flight_id
        code=code.ljust(12,'0')
        yield code
    
