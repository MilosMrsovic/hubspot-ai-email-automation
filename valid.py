import requests
import csv
import pandas as pd
import os

# --- Konfiguracija ---
HUBSPOT_TOKEN = "*******************************"  # MASKIRANO
HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_TOKEN}",
    "Content-Type": "application/json"
}

PROPERTIES_URL = "https://api.hubapi.com/crm/v3/properties/contacts"
CONTACTS_URL = "https://api.hubapi.com/crm/v3/objects/contacts"

# --- Apsolutni path za output u mountovani folder ---
OUTPUT_DIR = "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "hubspot_full_export.csv")

# --- Funkcije ---
def get_all_properties():
    print("Fetching all HubSpot contact properties...")
    resp = requests.get(PROPERTIES_URL, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    properties = [p["name"] for p in data["results"]]
    print(f"Found {len(properties)} properties.")
    return properties

def get_all_contacts(all_props):
    print("Fetching all contacts with full properties...")
    contacts = []
    after = None
    while True:
        params = {"limit": 100, "properties": all_props}
        if after:
            params["after"] = after
        resp = requests.get(CONTACTS_URL, headers=HEADERS, params=params)
        resp.raise_for_status()
        data = resp.json()
        for c in data["results"]:
            row = {"id": c["id"]}
            row.update(c.get("properties", {}))
            contacts.append(row)
        if "paging" in data:
            after = data["paging"]["next"]["after"]
        else:
            break
    print(f"Total contacts fetched: {len(contacts)}")
    return contacts

def save_to_csv(contacts, columns, filename=OUTPUT_FILE):
    print(f"Saving CSV to: {filename}")
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(contacts)
    print(f"Saved CSV → {filename}")

# --- Main ---
print("Current working directory:", os.getcwd())
all_properties = get_all_properties()
csv_columns = ["id"] + all_properties
contacts = get_all_contacts(all_properties)

save_to_csv(contacts, csv_columns)

# --- Pandas cleanup ---
df = pd.read_csv(OUTPUT_FILE, dtype=str)
df = df.replace(["", " ", "  ", "   "], pd.NA)
df = df.dropna(axis=1, how="all")
df = df.apply(lambda row: row.dropna(), axis=1)
df.to_csv(OUTPUT_FILE, index=False)

print("Data cleaned and saved successfully.")
print(f"Final CSV path: {OUTPUT_FILE}")
