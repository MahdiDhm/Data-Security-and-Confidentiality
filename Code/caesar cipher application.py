"""
Chiffrement César - Application 
Application graphique pour chiffrer et déchiffrer du texte avec le chiffrement César.
Le chiffrement César décale chaque lettre d'un nombre fixe de positions dans l'alphabet.

"""

import tkinter as tk
from tkinter import ttk, messagebox


def cesar_chiffrement(texte, decalage):
    """Chiffre un texte en utilisant le chiffrement César."""

    texte_chiffre = ""
    
    # Parcourir chaque caractère du texte
    for caractere in texte:
        # Traiter les lettres majuscules (A-Z)
        if 'A' <= caractere <= 'Z':
            # Appliquer le décalage modulo 26 pour rester dans l'alphabet
            texte_chiffre += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
        
        # Traiter les lettres minuscules (a-z)
        elif 'a' <= caractere <= 'z':
            # Appliquer le décalage modulo 26 pour rester dans l'alphabet
            texte_chiffre += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        
        # Conserver les caractères non-alphabétiques (chiffres, espaces, ponctuation)
        else:
            texte_chiffre += caractere
    
    return texte_chiffre


def cesar_dechiffrement(texte, decalage):
    """
    Déchiffre un texte chiffré avec le chiffrement César.
    """
    # Inverser le décalage pour retrouver le texte original
    return cesar_chiffrement(texte, -decalage)


def chiffrer_action():
    """Gère l'action du bouton 'Chiffrer'."""
    
    # Récupérer le texte saisi par l'utilisateur
    texte = entree_texte.get()
    
    # Récupérer et valider le décalage
    try:
        decalage = int(entree_decalage.get())
    except ValueError:
        # Afficher un message d'erreur si le décalage n'est pas un nombre
        messagebox.showerror("Erreur", "Le décalage doit être un nombre entier.")
        return
    
    # Appliquer le chiffrement
    texte_chiffre = cesar_chiffrement(texte, decalage)
    
    # Afficher le résultat dans le champ de sortie
    sortie_chiffre.config(state="normal")  # Activer l'édition temporairement
    sortie_chiffre.delete(0, tk.END)  # Effacer le contenu précédent
    sortie_chiffre.insert(0, texte_chiffre)  # Insérer le nouveau texte
    sortie_chiffre.config(state="readonly")  # Rendre le champ en lecture seule


def dechiffrer_action():
    """Gère l'action du bouton 'Déchiffrer'."""
    
    # Récupérer le texte saisi par l'utilisateur
    texte = entree_texte.get()
    
    # Récupérer et valider le décalage
    try:
        decalage = int(entree_decalage.get())
    except ValueError:
        # Afficher un message d'erreur si le décalage n'est pas un nombre
        messagebox.showerror("Erreur", "Le décalage doit être un nombre entier.")
        return
    
    # Appliquer le déchiffrement
    texte_dechiffre = cesar_dechiffrement(texte, decalage)
    
    # Afficher le résultat dans le champ de sortie
    sortie_dechiffre.config(state="normal")  # Activer l'édition temporairement
    sortie_dechiffre.delete(0, tk.END)  # Effacer le contenu précédent
    sortie_dechiffre.insert(0, texte_dechiffre)  # Insérer le nouveau texte
    sortie_dechiffre.config(state="readonly")  # Rendre le champ en lecture seule



# INTERFACE GRAPHIQUE

# Creer la fenetre principale
fenetre = tk.Tk()
fenetre.title("Chiffrement César")
fenetre.geometry("450x300")
fenetre.config(bg="#2C3E50")  # Couleur de fond sombre

# Configurer le style de l'application
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#2C3E50", foreground="white")
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12))

# Creer un frame principal avec du padding
frame = ttk.Frame(fenetre, padding=20)
frame.pack(expand=True)

# Champ d'entree du texte
label_texte = ttk.Label(frame, text="Texte :")
label_texte.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entree_texte = ttk.Entry(frame, width=40)
entree_texte.grid(row=0, column=1, padx=5, pady=5)

# Champ d'entree du decalage
label_decalage = ttk.Label(frame, text="Décalage :")
label_decalage.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entree_decalage = ttk.Entry(frame, width=10)
entree_decalage.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Les deux Boutons d'acttion (chiffrer et dechiffrer)
bouton_chiffrer = ttk.Button(frame, text=" Chiffrer", command=chiffrer_action)
bouton_chiffrer.grid(row=2, column=0, pady=10, padx=5)

bouton_dechiffrer = ttk.Button(frame, text=" Déchiffrer", command=dechiffrer_action)
bouton_dechiffrer.grid(row=2, column=1, pady=10, padx=5)

#  Champ d'affichage du texte chiffre
label_chiffre = ttk.Label(frame, text="Texte chiffré :")
label_chiffre.grid(row=3, column=0, padx=5, pady=5, sticky="w")
sortie_chiffre = ttk.Entry(frame, width=40, state="readonly")
sortie_chiffre.grid(row=3, column=1, padx=5, pady=5)

# Champ d'affichage du texte dechiffre
label_dechiffre = ttk.Label(frame, text="Texte déchiffré :")
label_dechiffre.grid(row=4, column=0, padx=5, pady=5, sticky="w")
sortie_dechiffre = ttk.Entry(frame, width=40, state="readonly")
sortie_dechiffre.grid(row=4, column=1, padx=5, pady=5)

# Lancer l'application
fenetre.mainloop()
