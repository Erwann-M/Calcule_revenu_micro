revenu_base = input("Quel est le montant perçu en revenu de micro-entreprise ? ")
revenu_are = input("Quel est le montant de l'ARE ? ")
# Calcule de l'abatement forfaitaire en libérale
revenu_base = float(revenu_base)
revenu_are = float(revenu_are)

abatement = revenu_base * 0.34
revenu_de_reference = revenu_base - abatement

# Calcule allocation partielle
revenu_ref_moins_retenu = revenu_de_reference * 0.70
alloc_partielle = revenu_are - revenu_ref_moins_retenu

# Calcule total net chomage + revenu micro entreprise
cotisations = revenu_base * 0.233
total_net_revenu_base = revenu_base - cotisations
total_net = total_net_revenu_base + alloc_partielle

print("-------------------------------- RÉSULTAT --------------------------------")
print("| Montant allocation partielle : " + str(alloc_partielle) + ".")
print("| Montant des cotisations : " + str(cotisations) + ".")
print("| Montant revenu Micro entreprise moins les cotisations (net) : " + str(total_net_revenu_base) + ".")
print("--------------------------------------------------------------------------")
print("| Montant TOTAL revenu micro + chomage : " + str(total_net) + ".")
print("--------------------------------------------------------------------------")
