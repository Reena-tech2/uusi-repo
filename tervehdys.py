def tervehdys(nimi, ika):
    print(f"\nHei, {nimi}! Hauska tavata.")
    print(f"Olet {ika} vuotta vanha.")
    
    if ika < 18:
        print("Olet vielä nuori! 😊")
    elif ika < 65:
        print("Olet parhaassa iässä! 💪")
    else:
        print("Hienoa kokemusta takana! 👏")