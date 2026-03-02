import pandas as pd
import google.generativeai as genai

genai.configure(api_key="xxxxxxxxxxxxxxxxxxx")
model_name = "gemini-2.5-flash"

form_data = pd.read_csv("Responses.csv", encoding="utf-8")
row = form_data.iloc[1]

prompt = (
    f"Suggest a {row['season']} {row['travelstyle'].lower()} trip for a {row['pfstatus'].lower()} "
    f"aged {row['age']} living in {row['city']}. They travel {row['traveltime'].lower()}, "
    f"enjoy {row['destination'].lower()} destinations, and their typical budget is {row['travelbudjet'].lower()}. "
    "Give a 3‑day travel itinerary, top 3 attractions, and a small packing list."
)

model = genai.GenerativeModel(model_name)
response = model.generate_content(prompt)
print(response.text)

