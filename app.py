import streamlit as st
import urllib.parse


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MIS Support Assistant",
    page_icon="💬",
    layout="centered"
)


# ============================================================
# BASIC CONFIG
# ============================================================

SUPPORT_EMAIL = "itbo@balenciaga.com"

LANGUAGE_OPTIONS = {
    "en": "English",
    "fr": "Français",
    "it": "Italiano"
}

APPLICATIONS = ["PLM", "BalChain", "BusinessMap", "Stealth"]


# ============================================================
# UI TEXTS
# ============================================================

UI_TEXTS = {
    "en": {
        "title": "MIS Support Assistant",
        "subtitle": "Select an application, describe your issue, and get the relevant support instruction.",
        "language": "Language",
        "application": "Application",
        "quick_topics": "Quick topics",
        "issue": "Describe your issue",
        "link": "Link to the concerned page / object",
        "link_help": "Please paste the link to the concerned style, collection, supplier, order, request, or page.",
        "screenshot": "A screenshot is available and can be attached if needed",
        "upload": "Optional: upload a screenshot for the demo",
        "submit": "Submit",
        "reset": "Reset",
        "answer_title": "Assistant answer",
        "matched_instruction": "Matched instruction",
        "no_match": "I could not find a matching instruction for this issue.",
        "missing_issue": "Please describe your issue or select a quick topic.",
        "missing_link": "Please add the concerned link.",
        "missing_screenshot": "Please confirm that a screenshot is available.",
        "contact": "Contact MIS Support",
        "provided_link": "Provided link",
        "screenshot_note": "Please also attach a screenshot if you contact support.",
        "helpful": "Was this helpful?",
        "support_note": "If not, you can contact MIS Support using the button below.",
        "email_preview": "Support email preview"
    },
    "fr": {
        "title": "Assistant MIS Support",
        "subtitle": "Sélectionnez une application, décrivez votre problème et obtenez l’instruction de support correspondante.",
        "language": "Langue",
        "application": "Application",
        "quick_topics": "Sujets rapides",
        "issue": "Décrivez votre problème",
        "link": "Lien vers la page / l’objet concerné",
        "link_help": "Veuillez coller le lien vers le style, la collection, le fournisseur, la commande, la demande ou la page concernée.",
        "screenshot": "Une capture d’écran est disponible et peut être ajoutée si nécessaire",
        "upload": "Optionnel : ajouter une capture d’écran pour la démo",
        "submit": "Envoyer",
        "reset": "Réinitialiser",
        "answer_title": "Réponse de l’assistant",
        "matched_instruction": "Instruction trouvée",
        "no_match": "Je n’ai pas trouvé d’instruction correspondant à cette demande.",
        "missing_issue": "Veuillez décrire votre problème ou sélectionner un sujet rapide.",
        "missing_link": "Veuillez ajouter le lien concerné.",
        "missing_screenshot": "Veuillez confirmer qu’une capture d’écran est disponible.",
        "contact": "Contacter MIS Support",
        "provided_link": "Lien fourni",
        "screenshot_note": "Merci de joindre également une capture d’écran si vous contactez le support.",
        "helpful": "Est-ce que cela vous a aidé ?",
        "support_note": "Si non, vous pouvez contacter MIS Support via le bouton ci-dessous.",
        "email_preview": "Aperçu de l’email au support"
    },
    "it": {
        "title": "Assistente MIS Support",
        "subtitle": "Seleziona un’applicazione, descrivi il problema e ricevi l’istruzione di supporto corrispondente.",
        "language": "Lingua",
        "application": "Applicazione",
        "quick_topics": "Argomenti rapidi",
        "issue": "Descrivi il problema",
        "link": "Link alla pagina / all’oggetto interessato",
        "link_help": "Incolla il link allo stile, alla collezione, al fornitore, all’ordine, alla richiesta o alla pagina interessata.",
        "screenshot": "Uno screenshot è disponibile e può essere allegato se necessario",
        "upload": "Opzionale: carica uno screenshot per la demo",
        "submit": "Invia",
        "reset": "Reset",
        "answer_title": "Risposta dell’assistente",
        "matched_instruction": "Istruzione trovata",
        "no_match": "Non ho trovato un’istruzione corrispondente a questa richiesta.",
        "missing_issue": "Descrivi il problema o seleziona un argomento rapido.",
        "missing_link": "Aggiungi il link interessato.",
        "missing_screenshot": "Conferma che uno screenshot è disponibile.",
        "contact": "Contatta MIS Support",
        "provided_link": "Link fornito",
        "screenshot_note": "Allega anche uno screenshot se contatti il supporto.",
        "helpful": "È stato utile?",
        "support_note": "In caso contrario, puoi contattare MIS Support tramite il pulsante qui sotto.",
        "email_preview": "Anteprima email al supporto"
    }
}


# ============================================================
# DEMO KNOWLEDGE BASE
# One instruction = one object with translations
# ============================================================

INSTRUCTIONS = [
    {
        "id": "plm_create_serie",
        "application": "PLM",
        "tags": ["serie", "series", "shape and serie", "plm", "create", "série", "créer", "creare"],
        "title": {
            "en": "Create a Serie",
            "fr": "Créer une série",
            "it": "Creare una serie"
        },
        "quick_topic": {
            "en": "How can I create a serie?",
            "fr": "Comment créer une série ?",
            "it": "Come posso creare una serie?"
        },
        "content": {
            "en": """Step 1. Open Shape and Serie.
Step 2. Open the Séries tab.
Step 3. Click New Série.
Step 4. Fill in Description.
Step 5. Click Save.
Step 6. Check that the Serie has been created.""",
            "fr": """Étape 1. Ouvrir Shape and Serie.
Étape 2. Ouvrir l’onglet Séries.
Étape 3. Cliquer sur New Série.
Étape 4. Renseigner la Description.
Étape 5. Cliquer sur Save.
Étape 6. Vérifier que la série a bien été créée.""",
            "it": """Passo 1. Aprire Shape and Serie.
Passo 2. Aprire la scheda Séries.
Passo 3. Cliccare su New Série.
Passo 4. Compilare il campo Description.
Passo 5. Cliccare su Save.
Passo 6. Verificare che la serie sia stata creata correttamente."""
        }
    },
    {
        "id": "plm_create_collection",
        "application": "PLM",
        "tags": ["collection", "plm", "create", "new collection", "créer", "collezione", "creare"],
        "title": {
            "en": "Create a Collection",
            "fr": "Créer une collection",
            "it": "Creare una collezione"
        },
        "quick_topic": {
            "en": "How can I create a collection?",
            "fr": "Comment créer une collection ?",
            "it": "Come posso creare una collezione?"
        },
        "content": {
            "en": """Step 1. Open the Collection section in PLM.
Step 2. Click New Collection.
Step 3. Fill in the required fields.
Step 4. Save the collection.
Step 5. Check that the collection has been created correctly.""",
            "fr": """Étape 1. Ouvrir la section Collection dans PLM.
Étape 2. Cliquer sur New Collection.
Étape 3. Renseigner les champs obligatoires.
Étape 4. Enregistrer la collection.
Étape 5. Vérifier que la collection a bien été créée.""",
            "it": """Passo 1. Aprire la sezione Collection in PLM.
Passo 2. Cliccare su New Collection.
Passo 3. Compilare i campi obbligatori.
Passo 4. Salvare la collezione.
Passo 5. Verificare che la collezione sia stata creata correttamente."""
        }
    },
    {
        "id": "plm_new_hierarchy",
        "application": "PLM",
        "tags": ["hierarchy", "new hierarchy", "plm", "create", "hiérarchie", "gerarchia"],
        "title": {
            "en": "Create a New Hierarchy",
            "fr": "Créer une nouvelle hiérarchie",
            "it": "Creare una nuova gerarchia"
        },
        "quick_topic": {
            "en": "How can I create a new hierarchy?",
            "fr": "Comment créer une nouvelle hiérarchie ?",
            "it": "Come posso creare una nuova gerarchia?"
        },
        "content": {
            "en": """Step 1. Open the hierarchy management section.
Step 2. Select the relevant category.
Step 3. Add the new hierarchy value.
Step 4. Save your changes.
Step 5. Check that the new value is available in PLM.""",
            "fr": """Étape 1. Ouvrir la section de gestion des hiérarchies.
Étape 2. Sélectionner la catégorie concernée.
Étape 3. Ajouter la nouvelle valeur de hiérarchie.
Étape 4. Enregistrer les modifications.
Étape 5. Vérifier que la nouvelle valeur est disponible dans PLM.""",
            "it": """Passo 1. Aprire la sezione di gestione delle gerarchie.
Passo 2. Selezionare la categoria interessata.
Passo 3. Aggiungere il nuovo valore di gerarchia.
Passo 4. Salvare le modifiche.
Passo 5. Verificare che il nuovo valore sia disponibile in PLM."""
        }
    },
    {
        "id": "plm_add_value_column",
        "application": "PLM",
        "tags": ["column", "value", "add value", "plm", "colonne", "valeur", "colonna", "valore"],
        "title": {
            "en": "Add a New Value to a Column",
            "fr": "Ajouter une nouvelle valeur dans une colonne",
            "it": "Aggiungere un nuovo valore a una colonna"
        },
        "quick_topic": {
            "en": "How can I add a new value to a column?",
            "fr": "Comment ajouter une nouvelle valeur dans une colonne ?",
            "it": "Come posso aggiungere un nuovo valore a una colonna?"
        },
        "content": {
            "en": """Step 1. Identify the column where the new value is needed.
Step 2. Check whether the value already exists.
Step 3. Add the new value in the relevant configuration table.
Step 4. Save the update.
Step 5. Ask the user to refresh PLM and check again.""",
            "fr": """Étape 1. Identifier la colonne dans laquelle la nouvelle valeur est nécessaire.
Étape 2. Vérifier que la valeur n’existe pas déjà.
Étape 3. Ajouter la nouvelle valeur dans la table de configuration concernée.
Étape 4. Enregistrer la mise à jour.
Étape 5. Demander à l’utilisateur de rafraîchir PLM et de vérifier à nouveau.""",
            "it": """Passo 1. Identificare la colonna in cui è necessario il nuovo valore.
Passo 2. Verificare che il valore non esista già.
Passo 3. Aggiungere il nuovo valore nella tabella di configurazione corrispondente.
Passo 4. Salvare l’aggiornamento.
Passo 5. Chiedere all’utente di aggiornare PLM e verificare di nuovo."""
        }
    },
    {
        "id": "plm_delete_color",
        "application": "PLM",
        "tags": ["color", "delete color", "plm", "couleur", "supprimer", "colore", "eliminare"],
        "title": {
            "en": "Delete a Color",
            "fr": "Supprimer une couleur",
            "it": "Eliminare un colore"
        },
        "quick_topic": {
            "en": "How can I delete a color?",
            "fr": "Comment supprimer une couleur ?",
            "it": "Come posso eliminare un colore?"
        },
        "content": {
            "en": """Step 1. Open the concerned style or product.
Step 2. Go to the color section.
Step 3. Check that the color is not used in any active flow.
Step 4. Delete the color if allowed.
Step 5. Save and ask the user to verify.""",
            "fr": """Étape 1. Ouvrir le style ou le produit concerné.
Étape 2. Aller dans la section des couleurs.
Étape 3. Vérifier que la couleur n’est pas utilisée dans un flux actif.
Étape 4. Supprimer la couleur si cela est autorisé.
Étape 5. Enregistrer et demander à l’utilisateur de vérifier.""",
            "it": """Passo 1. Aprire lo stile o il prodotto interessato.
Passo 2. Andare alla sezione dei colori.
Passo 3. Verificare che il colore non sia utilizzato in un flusso attivo.
Passo 4. Eliminare il colore se consentito.
Passo 5. Salvare e chiedere all’utente di verificare."""
        }
    },
    {
        "id": "businessmap_collection_not_visible",
        "application": "BusinessMap",
        "tags": ["collection", "not visible", "businessmap", "export", "business export", "collection non visible", "collezione non visibile"],
        "title": {
            "en": "Collection not visible in BusinessMap",
            "fr": "Collection non visible dans BusinessMap",
            "it": "Collezione non visibile in BusinessMap"
        },
        "quick_topic": {
            "en": "I cannot see my collection in BusinessMap",
            "fr": "Je ne vois pas ma collection dans BusinessMap",
            "it": "Non vedo la mia collezione in BusinessMap"
        },
        "content": {
            "en": """Step 1. Check that the Business Export flag is enabled in PLM.
Step 2. Check whether the collection has been exported.
Step 3. Verify that the collection belongs to the correct season.
Step 4. Ask the user to refresh BusinessMap.
Step 5. If the collection is still not visible, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que le flag Business Export est activé dans PLM.
Étape 2. Vérifier que la collection a bien été exportée.
Étape 3. Vérifier que la collection appartient à la bonne saison.
Étape 4. Demander à l’utilisateur de rafraîchir BusinessMap.
Étape 5. Si la collection n’est toujours pas visible, contacter MIS Support.""",
            "it": """Passo 1. Verificare che il flag Business Export sia attivo in PLM.
Passo 2. Verificare che la collezione sia stata esportata.
Passo 3. Verificare che la collezione appartenga alla stagione corretta.
Passo 4. Chiedere all’utente di aggiornare BusinessMap.
Passo 5. Se la collezione non è ancora visibile, contattare MIS Support."""
        }
    },
    {
        "id": "businessmap_style_not_visible",
        "application": "BusinessMap",
        "tags": ["style", "not visible", "businessmap", "export", "style non visible", "stile non visibile"],
        "title": {
            "en": "Style not visible in BusinessMap",
            "fr": "Style non visible dans BusinessMap",
            "it": "Stile non visibile in BusinessMap"
        },
        "quick_topic": {
            "en": "I cannot see my style in BusinessMap",
            "fr": "Je ne vois pas mon style dans BusinessMap",
            "it": "Non vedo il mio stile in BusinessMap"
        },
        "content": {
            "en": """Step 1. Check whether the style exists in PLM.
Step 2. Verify that the style is included in the correct collection.
Step 3. Check if the Business Export flag is enabled.
Step 4. Check whether the style has been exported.
Step 5. If the issue persists, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que le style existe dans PLM.
Étape 2. Vérifier que le style est inclus dans la bonne collection.
Étape 3. Vérifier que le flag Business Export est activé.
Étape 4. Vérifier que le style a bien été exporté.
Étape 5. Si le problème persiste, contacter MIS Support.""",
            "it": """Passo 1. Verificare che lo stile esista in PLM.
Passo 2. Verificare che lo stile sia incluso nella collezione corretta.
Passo 3. Verificare che il flag Business Export sia attivo.
Passo 4. Verificare che lo stile sia stato esportato.
Passo 5. Se il problema persiste, contattare MIS Support."""
        }
    },
    {
        "id": "businessmap_export_issue",
        "application": "BusinessMap",
        "tags": ["export", "businessmap", "business export", "issue", "problème export", "problema export"],
        "title": {
            "en": "BusinessMap Export Issue",
            "fr": "Problème d’export vers BusinessMap",
            "it": "Problema di export verso BusinessMap"
        },
        "quick_topic": {
            "en": "I have an export issue to BusinessMap",
            "fr": "J’ai un problème d’export vers BusinessMap",
            "it": "Ho un problema di export verso BusinessMap"
        },
        "content": {
            "en": """Step 1. Check whether the object is eligible for BusinessMap export.
Step 2. Verify the Business Export flag.
Step 3. Check mandatory fields in PLM.
Step 4. Ask the user to provide the object link and a screenshot.
Step 5. If the export still fails, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que l’objet est éligible à l’export vers BusinessMap.
Étape 2. Vérifier le flag Business Export.
Étape 3. Vérifier les champs obligatoires dans PLM.
Étape 4. Demander à l’utilisateur de fournir le lien de l’objet et une capture d’écran.
Étape 5. Si l’export échoue toujours, contacter MIS Support.""",
            "it": """Passo 1. Verificare che l’oggetto sia idoneo all’export verso BusinessMap.
Passo 2. Verificare il flag Business Export.
Passo 3. Verificare i campi obbligatori in PLM.
Passo 4. Chiedere all’utente di fornire il link dell’oggetto e uno screenshot.
Passo 5. Se l’export continua a fallire, contattare MIS Support."""
        }
    },
    {
        "id": "balchain_access",
        "application": "BalChain",
        "tags": ["balchain", "access", "login", "blank screen", "account", "connexion", "accès", "accesso", "schermata bianca"],
        "title": {
            "en": "BalChain Access Issue",
            "fr": "Problème d’accès à BalChain",
            "it": "Problema di accesso a BalChain"
        },
        "quick_topic": {
            "en": "The user cannot log in to BalChain",
            "fr": "L’utilisateur ne peut pas se connecter à BalChain",
            "it": "L’utente non riesce ad accedere a BalChain"
        },
        "content": {
            "en": """Step 1. Check whether the user already has a BalChain account.
Step 2. Ask the user to clear browser cache.
Step 3. Ask the user to try another browser.
Step 4. Check whether the user is using the correct link.
Step 5. If the issue persists, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que l’utilisateur dispose déjà d’un compte BalChain.
Étape 2. Demander à l’utilisateur de vider le cache du navigateur.
Étape 3. Demander à l’utilisateur d’essayer avec un autre navigateur.
Étape 4. Vérifier que l’utilisateur utilise le bon lien.
Étape 5. Si le problème persiste, contacter MIS Support.""",
            "it": """Passo 1. Verificare che l’utente abbia già un account BalChain.
Passo 2. Chiedere all’utente di cancellare la cache del browser.
Passo 3. Chiedere all’utente di provare con un altro browser.
Passo 4. Verificare che l’utente stia usando il link corretto.
Passo 5. Se il problema persiste, contattare MIS Support."""
        }
    },
    {
        "id": "balchain_blank_screen",
        "application": "BalChain",
        "tags": ["blank screen", "white screen", "balchain", "login", "access", "écran blanc", "schermata bianca"],
        "title": {
            "en": "Blank Screen in BalChain",
            "fr": "Écran blanc dans BalChain",
            "it": "Schermata bianca in BalChain"
        },
        "quick_topic": {
            "en": "The user sees a blank screen in BalChain",
            "fr": "L’utilisateur voit un écran blanc dans BalChain",
            "it": "L’utente vede una schermata bianca in BalChain"
        },
        "content": {
            "en": """Step 1. Ask the user to clear browser cache.
Step 2. Ask the user to try another browser.
Step 3. Check whether the issue happens only on the user's device.
Step 4. Ask the user to provide a screenshot.
Step 5. If the issue persists, contact MIS Support.""",
            "fr": """Étape 1. Demander à l’utilisateur de vider le cache du navigateur.
Étape 2. Demander à l’utilisateur d’essayer avec un autre navigateur.
Étape 3. Vérifier si le problème se produit uniquement sur le poste de l’utilisateur.
Étape 4. Demander à l’utilisateur de fournir une capture d’écran.
Étape 5. Si le problème persiste, contacter MIS Support.""",
            "it": """Passo 1. Chiedere all’utente di cancellare la cache del browser.
Passo 2. Chiedere all’utente di provare con un altro browser.
Passo 3. Verificare se il problema si verifica solo sul dispositivo dell’utente.
Passo 4. Chiedere all’utente di fornire uno screenshot.
Passo 5. Se il problema persiste, contattare MIS Support."""
        }
    },
    {
        "id": "stealth_export_issue",
        "application": "Stealth",
        "tags": ["stealth", "export", "style", "not exported", "error", "style non exporté", "stile non esportato"],
        "title": {
            "en": "Style not exported to Stealth",
            "fr": "Style non exporté vers Stealth",
            "it": "Stile non esportato verso Stealth"
        },
        "quick_topic": {
            "en": "The style was not exported to Stealth",
            "fr": "Le style n’a pas été exporté vers Stealth",
            "it": "Lo stile non è stato esportato verso Stealth"
        },
        "content": {
            "en": """Step 1. Check whether the style has the required export flag.
Step 2. Verify that all mandatory fields are completed.
Step 3. Check the export error message.
Step 4. Compare with a similar successfully exported style if needed.
Step 5. If the issue persists, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que le style possède le flag d’export requis.
Étape 2. Vérifier que tous les champs obligatoires sont renseignés.
Étape 3. Vérifier le message d’erreur d’export.
Étape 4. Comparer avec un style similaire exporté avec succès si nécessaire.
Étape 5. Si le problème persiste, contacter MIS Support.""",
            "it": """Passo 1. Verificare che lo stile abbia il flag di export richiesto.
Passo 2. Verificare che tutti i campi obbligatori siano compilati.
Passo 3. Controllare il messaggio di errore dell’export.
Passo 4. Confrontare con uno stile simile esportato correttamente, se necessario.
Passo 5. Se il problema persiste, contattare MIS Support."""
        }
    },
    {
        "id": "stealth_supplier_inactive",
        "application": "Stealth",
        "tags": ["supplier", "inactive", "stealth", "vendor", "fournisseur inactif", "fornitore inattivo"],
        "title": {
            "en": "Supplier inactive in Stealth",
            "fr": "Fournisseur inactif dans Stealth",
            "it": "Fornitore inattivo in Stealth"
        },
        "quick_topic": {
            "en": "The supplier is inactive in Stealth",
            "fr": "Le fournisseur est inactif dans Stealth",
            "it": "Il fornitore è inattivo in Stealth"
        },
        "content": {
            "en": """Step 1. Check whether the supplier exists in Stealth.
Step 2. Verify whether the supplier is active or inactive.
Step 3. If the supplier needs to be reactivated, contact the responsible team.
Step 4. Ask the user to provide the supplier code and screenshot.
Step 5. If needed, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que le fournisseur existe dans Stealth.
Étape 2. Vérifier si le fournisseur est actif ou inactif.
Étape 3. Si le fournisseur doit être réactivé, contacter l’équipe responsable.
Étape 4. Demander à l’utilisateur de fournir le code fournisseur et une capture d’écran.
Étape 5. Si nécessaire, contacter MIS Support.""",
            "it": """Passo 1. Verificare che il fornitore esista in Stealth.
Passo 2. Verificare se il fornitore è attivo o inattivo.
Passo 3. Se il fornitore deve essere riattivato, contattare il team responsabile.
Passo 4. Chiedere all’utente di fornire il codice fornitore e uno screenshot.
Passo 5. Se necessario, contattare MIS Support."""
        }
    },
    {
        "id": "stealth_currency_missing",
        "application": "Stealth",
        "tags": ["currency", "missing currency", "stealth", "error", "devise manquante", "valuta mancante"],
        "title": {
            "en": "Missing currency error in Stealth",
            "fr": "Erreur de devise manquante dans Stealth",
            "it": "Errore di valuta mancante in Stealth"
        },
        "quick_topic": {
            "en": "There is a missing currency error in Stealth",
            "fr": "Il y a une erreur de devise manquante dans Stealth",
            "it": "C’è un errore di valuta mancante in Stealth"
        },
        "content": {
            "en": """Step 1. Check the currency assigned to the supplier or material.
Step 2. Verify whether the currency is correctly maintained in Stealth.
Step 3. Check if the same error appears on similar objects.
Step 4. Ask the user to provide the object link and screenshot.
Step 5. If the issue persists, contact MIS Support.""",
            "fr": """Étape 1. Vérifier la devise associée au fournisseur ou au matériel.
Étape 2. Vérifier que la devise est correctement maintenue dans Stealth.
Étape 3. Vérifier si la même erreur apparaît sur des objets similaires.
Étape 4. Demander à l’utilisateur de fournir le lien de l’objet et une capture d’écran.
Étape 5. Si le problème persiste, contacter MIS Support.""",
            "it": """Passo 1. Verificare la valuta associata al fornitore o al materiale.
Passo 2. Verificare che la valuta sia correttamente mantenuta in Stealth.
Passo 3. Verificare se lo stesso errore appare su oggetti simili.
Passo 4. Chiedere all’utente di fornire il link dell’oggetto e uno screenshot.
Passo 5. Se il problema persiste, contattare MIS Support."""
        }
    },
    {
        "id": "stealth_sap_order_blocked",
        "application": "Stealth",
        "tags": ["sap", "order", "blocked", "stealth", "pni", "commande sap bloquée", "ordine sap bloccato"],
        "title": {
            "en": "SAP order blocked",
            "fr": "Commande SAP bloquée",
            "it": "Ordine SAP bloccato"
        },
        "quick_topic": {
            "en": "The SAP order is blocked",
            "fr": "La commande SAP est bloquée",
            "it": "L’ordine SAP è bloccato"
        },
        "content": {
            "en": """Step 1. Check whether the order exists in Stealth.
Step 2. Verify the associated request code.
Step 3. Check whether an SAP order number exists.
Step 4. Ask the user to provide the request code, object link, and screenshot.
Step 5. If the SAP order is blocked, contact MIS Support.""",
            "fr": """Étape 1. Vérifier que la commande existe dans Stealth.
Étape 2. Vérifier le request code associé.
Étape 3. Vérifier qu’un numéro de commande SAP existe.
Étape 4. Demander à l’utilisateur de fournir le request code, le lien de l’objet et une capture d’écran.
Étape 5. Si la commande SAP est bloquée, contacter MIS Support.""",
            "it": """Passo 1. Verificare che l’ordine esista in Stealth.
Passo 2. Verificare il request code associato.
Passo 3. Verificare che esista un numero d’ordine SAP.
Passo 4. Chiedere all’utente di fornire il request code, il link dell’oggetto e uno screenshot.
Passo 5. Se l’ordine SAP è bloccato, contattare MIS Support."""
        }
    }
]


# ============================================================
# HELPERS
# ============================================================

def initialize_session_state():
    if "issue" not in st.session_state:
        st.session_state.issue = ""
    if "link" not in st.session_state:
        st.session_state.link = ""
    if "screenshot_ready" not in st.session_state:
        st.session_state.screenshot_ready = False


def set_issue_from_topic(topic: str):
    st.session_state.issue = topic


def reset_form():
    st.session_state.issue = ""
    st.session_state.link = ""
    st.session_state.screenshot_ready = False


def find_instruction(question: str, application: str):
    question = question.lower()
    best_item = None
    best_score = 0

    for item in INSTRUCTIONS:
        if item["application"] != application:
            continue

        searchable_text = " ".join([
            item["title"]["en"],
            item["title"]["fr"],
            item["title"]["it"],
            item["quick_topic"]["en"],
            item["quick_topic"]["fr"],
            item["quick_topic"]["it"],
            " ".join(item["tags"]),
        ]).lower()

        score = sum(
            1
            for word in question.split()
            if len(word) > 2 and word in searchable_text
        )

        if score > best_score:
            best_score = score
            best_item = item

    return best_item if best_score > 0 else None


def build_mailto(language, application, issue, link, instruction):
    instruction_title = (
        instruction["title"][language]
        if instruction
        else "No matching instruction found"
    )

    subject = f"MIS Support Request - {application}"

    if language == "fr":
        body = f"""Bonjour,

Je rencontre un problème avec l'application suivante : {application}.

Problème :
{issue}

Lien concerné :
{link}

Capture d'écran :
Une capture d'écran est disponible et peut être ajoutée à la demande.

Instruction proposée par l'assistant :
{instruction_title}

Pouvez-vous m'aider, s'il vous plaît ?

Merci d'avance."""
    elif language == "it":
        body = f"""Buongiorno,

Ho un problema con la seguente applicazione: {application}.

Problema:
{issue}

Link interessato:
{link}

Screenshot:
Uno screenshot è disponibile e può essere allegato alla richiesta.

Istruzione proposta dall'assistente:
{instruction_title}

Potreste aiutarmi, per favore?

Grazie in anticipo."""
    else:
        body = f"""Hello,

I have an issue with the following application: {application}.

Issue:
{issue}

Concerned link:
{link}

Screenshot:
A screenshot is available and can be attached to the request.

Instruction suggested by the assistant:
{instruction_title}

Could you please help with this issue?

Thank you in advance."""

    return (
        f"mailto:{SUPPORT_EMAIL}"
        f"?subject={urllib.parse.quote(subject)}"
        f"&body={urllib.parse.quote(body)}"
    )


def render_mailto_button(mailto_link: str, label: str):
    st.markdown(
        f"""
        <a href="{mailto_link}" target="_blank"
           style="
              display: inline-block;
              padding: 10px 16px;
              background-color: #111111;
              color: white;
              text-decoration: none;
              border-radius: 6px;
              font-weight: bold;
              font-family: Arial, sans-serif;
           ">
           {label}
        </a>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# APP
# ============================================================

initialize_session_state()

language = st.radio(
    "Language / Langue / Lingua",
    options=list(LANGUAGE_OPTIONS.keys()),
    format_func=lambda code: LANGUAGE_OPTIONS[code],
    horizontal=True,
)

texts = UI_TEXTS[language]

st.title(texts["title"])
st.caption(texts["subtitle"])

application = st.radio(
    texts["application"],
    options=APPLICATIONS,
    horizontal=True,
)

st.subheader(texts["quick_topics"])

available_topics = [
    item["quick_topic"][language]
    for item in INSTRUCTIONS
    if item["application"] == application
]

if available_topics:
    topic_columns = st.columns(2)

    for index, topic in enumerate(available_topics):
        with topic_columns[index % 2]:
            st.button(
                topic,
                key=f"topic_{language}_{application}_{index}",
                on_click=set_issue_from_topic,
                args=(topic,),
            )

st.divider()

issue = st.text_area(
    texts["issue"],
    key="issue",
    height=120,
)

link = st.text_input(
    texts["link"],
    key="link",
    help=texts["link_help"],
)

screenshot_ready = st.checkbox(
    texts["screenshot"],
    key="screenshot_ready",
)

uploaded_file = st.file_uploader(
    texts["upload"],
    type=["png", "jpg", "jpeg"],
)

submit_col, reset_col = st.columns([1, 1])

with submit_col:
    submitted = st.button(texts["submit"], type="primary")

with reset_col:
    st.button(texts["reset"], on_click=reset_form)

if submitted:
    if not issue.strip():
        st.warning(texts["missing_issue"])
        st.stop()

    if not link.strip():
        st.warning(texts["missing_link"])
        st.stop()

    if not screenshot_ready and uploaded_file is None:
        st.warning(texts["missing_screenshot"])
        st.stop()

    instruction = find_instruction(issue, application)

    st.divider()
    st.subheader(texts["answer_title"])

    if instruction:
        st.success(texts["matched_instruction"])
        st.markdown(f"**{instruction['title'][language]}**")
        st.text(instruction["content"][language])
    else:
        st.warning(texts["no_match"])

    st.markdown(f"**{texts['provided_link']}:** {link}")
    st.info(texts["screenshot_note"])
    st.markdown(f"**{texts['helpful']}**")
    st.write(texts["support_note"])

    mailto_link = build_mailto(
        language=language,
        application=application,
        issue=issue,
        link=link,
        instruction=instruction,
    )

    render_mailto_button(mailto_link, texts["contact"])

    with st.expander(texts["email_preview"]):
        instruction_title = (
            instruction["title"][language]
            if instruction
            else "No matching instruction found"
        )

        st.write(f"To: {SUPPORT_EMAIL}")
        st.write(f"Subject: MIS Support Request - {application}")
        st.write("Instruction:", instruction_title)
        st.write("Issue:", issue)
        st.write("Link:", link)
