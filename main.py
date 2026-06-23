print("Laboratoire Numérique Convertisseur & Mole\n[1] Les volumes\n[2] Les moles")
Choix_Utilisateur = int(input("Ton choix: "))

if Choix_Utilisateur == 1:
    v_ml = float(input("Entrer une valeur en millilitres (mL) "))
    v_l = v_ml/1000
    print(f"{v_ml}mL est égale à {v_l}L")
elif Choix_Utilisateur == 2:
    m_grammes = float(input("Entrer la masse en grammes (g) "))
    M_gmol = float(input("Entrer la masse molaire en (g/mol) "))
    n_moles = m_grammes/M_gmol
    print(f"Pour une masse de {m_grammes}g ton échantillon contient {n_moles}mol.")
else:
    print("Choix invalide.")
