from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Kuku Afya is live!"})

# Disease data mapping symptoms to the most relevant disease
disease_data = {
    "coughing&sneezing": "Newcastle Disease",
    "dischargefromthenostrils": "Newcastle Disease",
    "scabbylessions": "Fowl Pox",
    "swollenwattles": "Fowl Cholera",
    "suddendeath": "Fowl Cholera",
    "paralysisoflegs": "Marek’s Disease",
    "whitediarrhea": "Gumboro",
    "yellowdiarrhea": "Fowl Typhoid",
    "greendiarrhea": "Fowl Typhoid",
    "bloodydiarrhea": "Coccidiosis",
    "visibleparasites": "External Parasites",
    "excessivescratching": "External Parasites",
    "wormsinfeces": "Internal Parasites"
}

# Detailed disease descriptions (trun

disease_details = {
    "Newcastle Disease": """✅ **What is it?** 
A highly contagious viral disease affecting chickens, causing respiratory, dige>

✅ **How is it spread?**  
- Direct contact with infected birds  
- Contaminated feed, water, and equipment  
- Airborne (especially in crowded farms)  

✅ **Mortality Rate:**  
- Up to 100% in severe cases  

✅ **Commonly Affected Age:**  
- All ages, but young birds are more susceptible  

✅ **Effect on Egg Production:**  
- Drastic reduction in egg production  
- Eggs may have thin shells or be misshapen  

✅ **Symptoms/Signs:**  
- Difficulty breathing (gasping, wheezing)  
- Greenish diarrhea  
- Twisted neck (nervous signs)  
- Loss of appetite and lethargy  
- Swollen eyes and head  
- Sudden death in severe cases  
- Decreased egg production  

✅ **Control Measures:**  
**Prevention:**  
- Regular vaccination  
- Strict biosecurity (limit farm visitors, disinfect equipment)  
- Quarantine new birds  

**Treatment:**  
- No direct cure; only supportive care (electrolytes, vitamins)  
- Antibiotics for secondary bacterial infections  

🚨 **Consult a Vet for Proper Diagnosis & Advice**  
""",
    "Fowl Pox": """✅ **What is it?** 
A slow-spreading viral disease causing lesions on the skin and inside the mouth>

✅ **How is it spread?**  
- Mosquito bites (main vector)  
- Direct contact with infected birds  
- Contaminated feed and water  

✅ **Mortality Rate:**  
- Low (1-10%) but higher if respiratory tract is affected  

✅ **Commonly Affected Age:**  
- All ages, but more common in young and stressed birds  

✅ **Effect on Egg Production:**  
- Moderate drop in egg production                                        ✅ **Symptoms/Signs:**  
- Wart-like scabs on comb, wattles, and eyelids  
- Yellowish-white ulcers in the mouth/throat  
- Labored breathing if respiratory tract is involved  
- Weight loss  
- Depression and reduced activity  
- Swelling around the eyes  
- Loss of appetite  

✅ **Control Measures:**  
**Prevention:**  
- Vaccinate birds (especially in mosquito-prone areas)  
- Control mosquitoes  
- Isolate sick birds  

**Treatment:**  
- No cure, but iodine or antiseptic ointment can help scabs heal  
- Vitamin A supplements to aid recovery  
- Antibiotics to prevent secondary infections  

🚨 **Consult a Vet for Further Guidance**  
""",
    "Fowl Cholera": """✅ **What is it?** 
A bacterial infection (caused by Pasteurella multocida) that affects chickens' >

✅ **How is it spread?**  
- Contaminated feed, water, or bedding  
- Direct contact with sick birds  
- Rodents and wild birds  

✅ **Mortality Rate:**  
- Acute form: Up to 100%  
- Chronic form: Lower but still dangerous  

✅ **Commonly Affected Age:**  
- Mostly affects mature birds (over 16 weeks)  

✅ **Effect on Egg Production:**  
- Severe drop in egg laying  

✅ **Symptoms/Signs:**  
- Swollen wattles and face  
- Green or yellow diarrhea  
- Difficulty breathing  
- Sudden death in severe cases  
- Dark red/purple discoloration of comb and wattles  
- Lameness and swollen joints  
- Loss of appetite and dehydration  

✅ **Control Measures:**  
**Prevention:**  
- Good sanitation and rodent control  
- Vaccination in high-risk areas  
- Quarantine new birds  

**Treatment:**  
- Antibiotics (sulfadimethoxine, tetracyclines, penicillin)  
- Isolate and treat sick birds immediately  

🚨 **Consult a Vet for Proper Antibiotic Treatment**  
""",
    "Marek’s Disease": """✅ **What is it?** 
A highly contagious viral disease affecting the nervous system, skin, and organ>

✅ **How is it spread?**  
- Airborne transmission (from infected dust and dander)  
- Direct contact with infected birds  

✅ **Mortality Rate:**  
- High (Up to 50%) in unvaccinated flocks  

✅ **Commonly Affected Age:**  
- Young birds (3-25 weeks old)  

✅ **Effect on Egg Production:**  
- Infected hens may never lay eggs if affected early                                                           ✅ **Symptoms/Signs:**  
- Paralysis of legs, wings, or neck  
- Greyish eyes (blindness)  
- Weight loss and paleness  
- Swollen feather follicles  
- Tumors in organs (in severe cases)  
- Ruffled feathers and depression  
- Death after progressive weakness  

✅ **Control Measures:**  
**Prevention:**  
- Vaccinate chicks at hatch  
- Maintain a clean, dust-free environment  

**Treatment:**  
- No cure. Supportive care only.  
- Euthanize severely affected birds to prevent spread.  

🚨 **Consult a Vet for Prevention Strategies**  
""",
    "Gumboro": """✅ **What is it?** 
A viral disease affecting young chickens’ immune systems, leading to high morta>

✅ **How is it spread?**  
- Contaminated feed, water, and droppings  
- Direct contact with infected birds  

✅ **Mortality Rate:**  
- 20-100% depending on the strain  

✅ **Commonly Affected Age:**  
- 3-6 week-old chicks  

✅ **Effect on Egg Production:**  
- Not directly affected, but survivors may become weak layers  

✅ **Symptoms/Signs:**  
- Ruffled feathers and depression  
- Watery, white diarrhea  
- Swollen, bleeding bursa (internal organ)  
- Trembling and weakness  
- Dehydration (birds refuse to drink)  
- Sudden death in young birds  
- Reduced immune function (making birds vulnerable to other diseases)  

✅ **Control Measures:**  
**Prevention:**  
- Vaccination of chicks  
- Strict farm hygiene  

**Treatment:**  
- No cure. Only electrolytes and vitamins to support recovery.  

🚨 **Consult a Vet for Vaccination Schedule**  
""",
    "Fowl Typhoid": """✅ **What is it?** 
A bacterial infection (Salmonella gallinarum) causing blood poisoning in chickens .                                      ✅ **How is it spread?**  
- Contaminated water, feed, or droppings  
- Passed from hen to eggs (vertical transmission)  

✅ **Mortality Rate:**  
- Up to 90% if untreated  

✅ **Commonly Affected Age:**  
- Mostly mature birds (above 8 weeks)  

✅ **Effect on Egg Production:**  
- Drop in egg production  
- Eggs may have poor shell quality  

✅ **Symptoms/Signs:**  
- Pale comb and wattles  
- Greenish-yellow diarrhea  
- Swollen liver and spleen  
- Decreased appetite and weakness  
- Sudden death in severe cases  
- Low egg production  
- High fever  

✅ **Control Measures:**  
**Prevention:**  
- Vaccination  
- Proper sanitation  

**Treatment:**  
- Antibiotics (Sulfa drugs, Tetracyclines)  

🚨 **Consult a Vet for Diagnosis & Antibiotic Use**  
""",
    "Coccidiosis": """✅ **What is it?** 
A parasitic disease caused by Eimeria protozoa that affects the intestinal tract of chicken>

✅ **How is it spread?**  
- Ingestion of contaminated droppings, feed, or water  
- Moist and dirty bedding provides ideal conditions for parasite survival  

✅ **Mortality Rate:**  
- 10-80% depending on the severity and intervention  

✅ **Commonly Affected Age:**  
- Mainly young chicks (3-8 weeks old)  
- Older birds develop some resistance but can still be affected  

✅ **Effect on Egg Production:**  
- Reduced egg production due to poor nutrient absorption  
- Soft or thin-shelled eggs in chronic cases  

✅ **Symptoms/Signs:**  
- Bloody or watery diarrhea (red-stained droppings)  
- Droopy and weak birds  
- Weight loss and reduced appetite  
- Ruffled feathers and dehydration  
- Pale comb and wattles  
- Hunched posture  
- Sudden death in severe cases  

✅ **Control Measures:**  
**Prevention:**  
- Keep litter dry (use proper ventilation and clean bedding)  
- Use medicated chick feed containing coccidiostats  
- Regularly clean and disinfect drinking systems  

**Treatment:**  
- Coccidiostats (e.g., Amprolium, Sulfaquinoxaline) added to drinking water  
- Provide electrolytes and vitamins to aid recovery  
     🚨 **Consult a Vet for Proper Drug Administration**  
""",
    "External Parasites": """✅ **What is it?** 
External parasites such as mites, lice, fleas, and ticks feed on chickens' blood, causing i>

✅ **How is it spread?**  
- Direct contact with infected birds  
- Infestation from wild birds, rodents, and dirty bedding  

✅ **Mortality Rate:**  
- Low, but can be fatal if severe infestations lead to anemia and weakness  

✅ **Commonly Affected Age:**  
- All ages can be affected  

✅ **Effect on Egg Production:**  
- Decreased egg production due to stress and anemia  

✅ **Symptoms/Signs:**  
- Itching and excessive preening  
- Red, irritated skin on vent, face, and under wings  
- Feather loss  
- Scaly, crusty legs (scaly leg mites)  
- Pale comb and wattles (anemia)  
- Weakness and weight loss  
- Black or red specks on feathers (visible mites or lice)  

✅ **Control Measures:**  
**Prevention:**  
- Regular dust bathing areas with diatomaceous earth or wood ash  
- Keep the chicken house dry and clean  
- Inspect and treat new birds before adding them to the flock  

**Treatment:**  
- Use poultry-safe insecticides (e.g., permethrin powder, ivermectin drops)  
- Clean and disinfect coops using lime wash or diatomaceous earth  
- Repeat treatment every 7-10 days to kill newly hatched parasites  

🚨 **Consult a Vet for Severe Infestations & Proper Treatment Options**  
""",
    "Internal Parasites": """✅ **What is it?** 
Internal parasites, such as roundworms, tapeworms, and cecal worms, infect the digestive tr>

✅ **How is it spread?**  
- Ingestion of contaminated feed, water, or droppings  
- Intermediate hosts (e.g., earthworms, beetles, snails)  

✅ **Mortality Rate:**  
- Low to moderate, but severe infestations can lead to death  

✅ **Commonly Affected Age:**  
- All ages, but young birds are more susceptible  

✅ **Effect on Egg Production:**  
- Reduced egg production due to poor nutrient absorption  
- Thin-shelled or misshapen eggs  

✅ **Symptoms/Signs:**  
- Visible worms in feces  
- Ruffled feathers and lethargy  
- Weight loss despite normal appetite  
- Pale comb and wattles (anemia)  
- Diarrhea (sometimes bloody if intestinal lining is damaged)  
- Reduced growth rate in young birds  
- Weakness and dehydration  

✅ **Control Measures:**  
**Prevention:**  
- Regular deworming (e.g., every 3-6 months)  
- Keep feed and water clean and free from contamination  
- Rotate pastures to reduce parasite load  

**Treatment:**  
- Dewormers (e.g., fenbendazole, levamisole, piperazine)  
- Provide electrolytes and vitamins to support recovery  
- Clean and disinfect the coop to prevent reinfection  

🚨 **Consult a Vet for Proper Deworming Schedule & Medication**  
"""                                                    }

@app.route("/predict", methods=["GET", "POST"])
def predict_disease():
    # Get symptoms from the request
    if request.method == "POST":
        data = request.get_json()
        symptoms = data.get("symptoms", "")
    else:  # Handle GET requests
        symptoms = request.args.get("symptoms", "")

    # Normalize the symptoms (remove spaces and convert to lowercase)
    symptoms = symptoms.replace(" ", "").lower()

    print("Received symptoms:", symptoms)  # Debugging

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    # Check if the symptoms match any disease in disease_data
    matched_disease = disease_data.get(symptoms)

    if not matched_disease:
        return jsonify({"message": "No matching disease found. Consult a vet!"})

    # Get the disease details
    disease_info = disease_details.get(matched_disease, "Details not available")

    # Return the disease details
    return jsonify({
        "disease": matched_disease,
        "details": disease_info
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000
