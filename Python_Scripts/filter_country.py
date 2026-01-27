countries = ["8", 8,  "Republic of Ireland", "Federal Republic of Nigeria",
             "Federal Republic of Germany", "Federal Republic of Somalia"]

for item in countries:
  if type(item) == str:
    if item.startswith("Republic") or item.endswith("Nigeria"):
      print(item)