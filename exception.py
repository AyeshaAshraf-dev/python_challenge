class  BoardingException(Exception):
    pass
class SecurityException(BoardingException):
    pass
class TicketingException(BoardingException):
    pass
class ProhibitedItemException(SecurityException):
    pass
class NoSeatAssignedException(TicketingException):
    pass

class AirportGate:
    def boardPassenger(self,passenger):
        if passenger["has_weapon"]:
            raise ProhibitedItemException(f"ALERT: {passenger['name']} tried to bring a prohibited item!")
            
        # Check ticketing rule
        if passenger["seat"] is None:
            raise NoSeatAssignedException(f"NOTICE: {passenger['name']} does not have a seat assignment.")
            
        # If both checks pass
        print(f"Welcome aboard, {passenger['name']}! Enjoy your flight to seat {passenger['seat']}.")


gate = AirportGate()
passenger_with_knife = {"name": "Alice","has_weapon": True,"seat": "12B"}

try:
    gate.boardPassenger(passenger_with_knife)
except SecurityException as e:
    print("Call security right now")
except TicketingException as e:
    print("send passenger back to counter")
