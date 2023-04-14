from Allergies import Allergy


class Console():
    """
    This module acts as a interface between our user and our Expert System.
    It prompts user to enter their symptoms and based on that the input is communicated to Expert System.
    These results are then returned.
    """
    __expert_system = None
    __lowest_possible_option = None
    __highest_possible_option = None

    def display_options(self) -> None:
        try:
            option = 1
            self.__lowest_possible_option = option
            for symptom in self.__expert_system.get_symptoms():
                print("[OPTION] %d. %s."%(option, symptom))
                option = option + 1
            self.__highest_possible_option = option
        except Exception as e:
            print("[ERR] The following error occured while trying to display symptom options to user: "+str(e))

    def run(self) -> None:
        try:
            print("*"*50)
            print("[CONSOLE] Initializing the Expert System...")
            self.__expert_system = Allergy()
            print("[CONSOLE] Expert System has been initialized successfuly!")
            self.display_options()
            symptoms = input("[INPUT] Enter symptoms you have: ")
            symptoms = symptoms.lower()
            symptoms = symptoms.replace(" ", '')
            symptoms = symptoms.strip("\n")
            symptoms =symptoms.split(",")
            
            results = self.__expert_system.diagnose(symptoms)
            print("\n\n")
            print("*"*50)
            if len(results) == 0:
                print("[RESULT] You do not have any significant Allergy.")
            else:
                print("[RESULT] You possibly have allergy here are a list of triggers with probabilities please consult a medical professional if you have interacted/consumed/touched any of the following:")
                for allergy, probability in results.items():
                    print("[TRIGGER] %s, probability: %f"%(allergy, probability))
        except Exception as e:
            print("[ERR] The following error occured while trying to run the user console: "+str(e))


Console().run()