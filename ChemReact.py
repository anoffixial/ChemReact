#Codes for Chemical Reaction results.

print()
print("Welcome to ChemReact")
print("These are the listed chemicals which are available to use :")
print()

chemicals=['1) Oxygen[O2]','2) Carbon[C]','3) Hydrogen[H]','4) Chlorine[Cl]']
chemicals2=['Oxygen','Carbon','Hydrogen','Chlorine']

for i in chemicals:
    print(i)
    
print()
print("Enter the exact chemical name as shown in the list.")
print()
selection1=input("Enter the first element : ")
selection2=input("Enter the second element : ")
sol=selection1+selection2
print()

if selection1 and selection2 in chemicals2:
    d1={'OxygenOxygen':'Oxygen[O2]','OxygenCarbon':'Carbon Dioxide[CO2]','OxygenHydogen':'Water[H20]','OxygenChlorine':'Chlorine Heptoxide[Cl2O7]','CarbonCarbon':'Carbon-Carbon','CarbonOxygen':'Carbon Dioxide[CO2]','CarbonHydrogen':'Methane[CH4]','CarbonChlorine':'Carbon Tetrachloride[C Cl4]','HydrogenOxygen':'Water[H20]','HydrogenCarbon':'Methane[CH4]','HydrogenHydrogen':'Hydrogen[H2]','HydrogenChlorine':'Hydrogen Chlorine[HCl]','ChlorineOxygen':'Chlorine Heptoxide[Cl2O7]','ChlorineCarbon':'Carbon Tetrachloride[C Cl4]','ChlorineHydrogen':'Hydrogen Chloride[HCl]','ChlorineChlorine':'Dichloride[Cl2]'}
    if sol in d1:
        print("This reaction will give out :")
        print(d1[sol])

else:
    print("Sorry, Wrong input.")

print()
print("Thank You for using ChemReact")
print("-AN")



