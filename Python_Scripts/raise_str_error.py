countries = ["8", 8,  "Republic of Ireland", "Federal Republic of Nigeria",
             "Federal Republic of Germany", "Federal Republic of Somalia"]

for item in countries:
  if type(item) == str:
    raise TypeError(f"String '{item}' found in list {countries}")
  else:
    print(item)
    