
class Allergy():
    """
    The class Allergy has simple on memory list of Allergies and their respective symptoms.
    It also has a method that can predict possible allergies.
    """
    __allergies = None
    __probabilities = None
    __THRESHOLD = None
    __result = None
    __symptoms = None
    def __init__(self) -> None:
        """
        This is the constructor of Allery, that initializes the python dictionary data structure,
        Which holds the <key>: <value> pairs of the <possible allergy>: <symptoms>.
        """
        print("[DATA] Initializing local data pertaining to Allergies and their symptoms.")

        self.__allergies = {
                "pollen": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "pet_dander": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "certain_foods": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "dust_mites": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "mold": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "insect_stings": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "latex": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "nickel": ["rashes", "itching", "swelling", "blisters"],
                "medications": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "cockroach_droppings": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "soy": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "egg": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "peanuts": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "tree_nuts": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "fish": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "shellfish": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "wheat": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "milk": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "dairy": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "sesame": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "perfumes": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "cosmetics": ["rashes", "itching", "swelling"],
                "cleaning_products": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "paints": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "smoke": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "chemicals": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "plants": ["itching", "rashes", "watery_eyes", "nasal_congestion"],
                "animal_hair": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "feathers": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "pollution": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "grass": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "aspirin": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "penicillin": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "sulfonamides": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "antibiotics": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "vinegar": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "alcohol": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "acetaminophen": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "ibuprofen": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "naproxen": ["rashes", "itching", "swelling", "difficulty_breathing"],
                "cigarette_smoke": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "vehicle_emissions": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "formaldehyde": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "isocyanates": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "chlorine": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "ammonia": ["sneezing", "itching", "rashes", "watery_eyes", "nasal_congestion"],
                "hair_dyes": ["rashes", "itching", "swelling"],
                "fabric_softeners": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "detergents": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "pesticides": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "insecticides": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "herbicides": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
                "fungicides": ["sneezing", "itching", "watery_eyes", "nasal_congestion"],
        }
        print("[RESULT] The Allergy data has been Initialized successfully!")

        print("[PROBA] Initializing Probabilities for each allergy.")
        self.__probabilities = dict()
        self.init_probablities()
        print("[RESULT] The default probabilities have been assigned.")
        self.__THRESHOLD = 0.5
        print("[THRESHOLD] Initialized Decision making threshold to %f."%(self.__THRESHOLD))
        self.__result = dict()
        self.__symptoms = list()
        self.init_symptoms()

    def init_symptoms(self) -> None:
        try:
            print("[SYMPTOM] Defining list of symptoms")
            for allergy, symptoms in self.__allergies.items():
                for symptom in symptoms:
                    if symptom in self.__symptoms:
                        continue
                    else:
                        self.__symptoms.append(symptom)
            print("[SYMPTOM] Defined list of symptoms")
        except Exception as e:
            print("[ERR] The following error occured while trying to create a distinct list of symptoms: "+str(e))

    def get_symptoms(self) -> list():
        """
        Returns a list of distinct symptoms..
        """
        return self.__symptoms
    
    def init_probablities(self):
        try:
            for allergy, symptom in self.__allergies.items():
                self.__probabilities[allergy] = 0.00
        except Exception as e:
            print("[ERR] The following error occured while initializing probabilities for Allergies: "+str(e))

    def update_probability(self, allergy: str, probability: float) -> None:
        """
        Updates the probability for the possible allergy. 
        """
        try:
            #print("[PROBA] Updating probability of '%s' with %f."%(allergy, probability))
            self.__probabilities[allergy] = probability
        except Exception as e:
            print("[ERR] The following error occured while trying to update probability for an allergy: "+str(e))
    
    def get_probabilites(self) -> dict:
        """
        Returns the probabilities of each allergy.
        """
        return self.__probabilities

    def determine_allergies(self) -> None:
        try:
            print("[DIAGNOSIS] Determining the possible allergies...")

            for allergy, probability in self.__probabilities.items():
                if probability>= self.__THRESHOLD:
                    self.__result[allergy] = probability
            
            print("[DIAGNOSIS] Possible Allergies have been computed!")
        except Exception as e:
            print("[ERR] The following error occured while trying to determine probable allergies: "+str(e))

    def diagnose(self, user_symptoms: list) -> list:
        """
        This method, accepts the user entered symptoms that will be used to determine most probable allergy.
        """
        try:
            print("[DIAGNOSIS] Please wait while the diagnosis is performed.")
            for allergy, symptoms in self.__allergies.items():
                matched_symptoms = 0
                total_symptoms = len(symptoms)
                for symptom in user_symptoms:
                    if symptom in symptoms:
                        matched_symptoms = matched_symptoms + 1
                
                self.update_probability(allergy= allergy, probability= (matched_symptoms / total_symptoms))
            print("[DIAGNOSIS] Probabilities have been computed for possible allergies.")

            self.determine_allergies()
            return self.__result
        except Exception as e:
            print("[ERR] The following error occured while trying to predict probable Allergies: "+str(e))









