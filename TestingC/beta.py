import openpyxl


workbook = openpyxl.load_workbook('ListofPersonalities.xlsx')
sheet = workbook['Objects']
Personalities = []
for personality_row in sheet.iter_rows(values_only=True, min_row=2):
    personality = personality_row[0]
    Personalities.append(personality)

for personality in Personalities:
    print(personality)