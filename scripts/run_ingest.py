from src.ingestion import fetch, sources
import json
from datetime import datetime
from src.storage import db

fetch_solarWind = fetch.fetch_solarWind(sources.PLASMA_URL)
fetch_mag = fetch.fetch_mag(sources.MAG_URL)
fetch_kp = fetch.fetch_kp(sources.KP_URL)

db.init_db()
db.insert_plasma(fetch_solarWind)
db.insert_mag(fetch_mag)
db.insert_kp(fetch_kp)

print(db.get_latest_n_mag(5))

# with open (f"data/raw/solarWind_{datetime.now().strftime('%Y-%m-%d')}.json", "w") as f:
#     json.dump(fetch_solarWind, f, indent=2)

# with open (f"data/raw/mag_{datetime.now().strftime('%Y-%m-%d')}.json", "w") as f:
#     json.dump(fetch_mag, f, indent=2)

# with open (f"data/raw/kp_{datetime.now().strftime('%Y-%m-%d')}.json", "w") as f:
#     json.dump(fetch_kp, f, indent=2)

print("\nData fetched and saved successfully!")
print(f"\nLengths: solarWind={len(fetch_solarWind)}, mag={len(fetch_mag)}, kp={len(fetch_kp)}")

print(f"Sample solarWind: {fetch_solarWind[0] if fetch_solarWind else 'No data'}")
print(f"Sample mag: {fetch_mag[0] if fetch_mag else 'No data'}")
print(f"Sample kp: {fetch_kp[0] if fetch_kp else 'No data'}")