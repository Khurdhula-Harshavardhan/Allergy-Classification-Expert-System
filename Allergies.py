
class Allergy():
    """
    The class Allergy has simple on memory list of Allergies and their respective symptoms.
    It also has a method that can predict possible allergies.
    """
    __allergies = None
    __probabilities = None
    
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
        self.init_probablities()
        print("[RESULT] The default probabilities have been assigned.")

    def init_probablities(self):
        try:
            for allergy, symptom in self.__allergies.items():
                self.__probabilities[allergy] = 0.00
        except Exception as e:
            print("[ERR] The following error occured while initializing probabilities for Allergies: "+str(e))

    def diagnose(self, user_symptoms: list) -> list:
        """
        This method, accepts the user entered symptoms that will be used to determine most probable allergy.
        """
        try:
            pass
        except Exception as e:
            print("[ERR] The following error occured while trying to predict probable Allergies: "+str(e))









