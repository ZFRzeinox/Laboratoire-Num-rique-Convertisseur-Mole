import math

print("Laboratoire Numérique\n[1] Les volumes\n[2] Les moles\n[3] Calculer le pH avec la masse")
Choix_Utilisateur = int(input("Ton choix: "))

if Choix_Utilisateur == 1:
    v_ml = float(input("Entrer une valeur en millilitres (mL) "))
    v_l = v_ml / 1000
    print(f"{v_ml}mL est égale à {v_l}L")

elif Choix_Utilisateur == 2:
    m_grammes = float(input("Entrer la masse en grammes (g) "))
    M_gmol = float(input("Entrer la masse molaire en (g/mol) "))
    n_moles = m_grammes / M_gmol
    print(f"Pour une masse de {m_grammes}g ton échantillon contient {n_moles}mol.")

elif Choix_Utilisateur == 3:
    m_grammes = float(input("Entrer la masse en grammes (g) "))
    M_gmol = float(input("Entrer la masse molaire en (g/mol) "))
    n_moles = m_grammes / M_gmol
    volume_l = float(input("Entrer le volume de la solution en Litres (L):"))
    concentration = n_moles / volume_l
    nature = input("Est-ce un [A] Acide ou une [B] Base ? (A/B) : ").upper()
    calcul_log = -math.log10(concentration)

    if nature == "B":
        ph = 14 - calcul_log
    else:
        ph = calcul_log

    if ph > 7:
        print(f"La solution est basique car le ph de la solution est de: {ph}")
    elif ph == 7:
        print(f"La solution est neutre car le ph de la solution est de: {ph}")
    elif ph < 7:
        print(f"La solution est acide car le ph de la solution est de: {ph}")

else:
    print("Choix invalide.")
