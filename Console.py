from Allergies import Allergy


class Console():
    """
    This module acts as a interface between our user and our Expert System.
    It prompts user to enter their symptoms and based on that the input is communicated to Expert System.
    These results are then returned.
    """
    __expert_system = None
    def __init__(self) -> None:
        print("[CONSOLE] Initializing the Expert System...")
        self.__expert_system = Allergy()
        print("[CONSOLE] Expert System has been initialized successfuly!")

    def run(self) -> None:
        try:
            symptoms = input("Enter symptoms you have: ")
            symptoms = symptoms.lower()
            symptoms = symptoms.replace(" ", '')
            symptoms = symptoms.strip("\n")
            symptoms =symptoms.split(" ")

        except Exception as e:
            print("[ERR] The following error occured while trying to run the user console: "+str(e))