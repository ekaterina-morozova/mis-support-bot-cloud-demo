import streamlit as st
import urllib.parse
import re

st.set_page_config(
    page_title="MIS Support Assistant",
    page_icon="💬",
    layout="centered"
)

SUPPORT_EMAIL = "itbo@balenciaga.com"

LANGUAGE_OPTIONS = {
    "en": "English",
    "fr": "Français",
    "it": "Italiano"
}

APPLICATIONS = ["PLM", "BalChain", "BusinessMap", "Stealth"]

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
        "upload": "Upload a screenshot if no link is available",
        "submit": "Submit",
        "reset": "Reset",
        "answer_title": "Assistant answer",
        "matched_instruction": "Matched instruction",
        "no_match": "I could not find a matching instruction for this issue.",
        "missing_issue": "Please describe your issue or select a quick topic.",
        "missing_link_or_screenshot": "Please add a concerned link or upload a screenshot.",
        "contact": "Contact MIS Support",
        "provided_link": "Provided link",
        "no_link": "No link provided",
        "screenshot_uploaded": "Screenshot uploaded",
        "screenshot_not_uploaded": "No screenshot uploaded",
        "screenshot_note": "If you contact support, please include the link and/or screenshot.",
        "helpful": "Was this helpful?",
        "support_note": "If not, you can contact MIS Support using the button below.",
        "email_preview": "Support email preview",
        "ticket_metadata": "Suggested ticket metadata",
        "labels": "Labels",
        "priority": "Priority",
        "medium": "Medium",
        "high": "High"
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
        "upload": "Ajoutez une capture d’écran si aucun lien n’est disponible",
        "submit": "Envoyer",
        "reset": "Réinitialiser",
        "answer_title": "Réponse de l’assistant",
        "matched_instruction": "Instruction trouvée",
        "no_match": "Je n’ai pas trouvé d’instruction correspondant à cette demande.",
        "missing_issue": "Veuillez décrire votre problème ou sélectionner un sujet rapide.",
        "missing_link_or_screenshot": "Veuillez ajouter un lien concerné ou télécharger une capture d’écran.",
        "contact": "Contacter MIS Support",
        "provided_link": "Lien fourni",
        "no_link": "Aucun lien fourni",
        "screenshot_uploaded": "Capture d’écran ajoutée",
        "screenshot_not_uploaded": "Aucune capture d’écran ajoutée",
        "screenshot_note": "Si vous contactez le support, veuillez inclure le lien et/ou la capture d’écran.",
        "helpful": "Est-ce que cela vous a aidé ?",
        "support_note": "Si non, vous pouvez contacter MIS Support via le bouton ci-dessous.",
        "email_preview": "Aperçu de l’email au support",
        "ticket_metadata": "Métadonnées suggérées pour le ticket",
        "labels": "Labels",
        "priority": "Priorité",
        "medium": "Medium",
        "high": "High"
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
        "upload": "Carica uno screenshot se non è disponibile un link",
        "submit": "Invia",
        "reset": "Reset",
        "answer_title": "Risposta dell’assistente",
        "matched_instruction": "Istruzione trovata",
        "no_match": "Non ho trovato un’istruzione corrispondente a questa richiesta.",
        "missing_issue": "Descrivi il problema o seleziona un argomento rapido.",
        "missing_link_or_screenshot": "Aggiungi un link interessato oppure carica uno screenshot.",
        "contact": "Contatta MIS Support",
        "provided_link": "Link fornito",
        "no_link": "Nessun link fornito",
        "screenshot_uploaded": "Screenshot caricato",
        "screenshot_not_uploaded": "Nessuno screenshot caricato",
        "screenshot_note": "Se contatti il supporto, includi il link e/o lo screenshot.",
        "helpful": "È stato utile?",
        "support_note": "In caso contrario, puoi contattare MIS Support tramite il pulsante qui sotto.",
        "email_preview": "Anteprima email al supporto",
        "ticket_metadata": "Metadati suggeriti per il ticket",
        "labels": "Labels",
        "priority": "Priorità",
        "medium": "Medium",
        "high": "High"
    }
}


# ============================================================
# DEMO KNOWLEDGE BASE
# ============================================================

INSTRUCTIONS = [
    {
        "id": "plm_create_serie",
        "application": "PLM",
        "request_type": "service_request",
        "priority": "Medium",
        "tags": [
            "serie", "series", "shape", "shape and serie", "plm", "create",
            "new serie", "série", "créer", "creare", "nuova serie"
        ],
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
        "request_type": "service_request",
        "priority": "Medium",
        "tags": [
            "collection", "plm", "create", "new collection",
            "collection creation", "créer collection", "nouvelle collection",
            "collezione", "creare collezione", "nuova collezione"
        ],
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
            "en": """Please indicate the name of the new collection you would like to create using this form.

Once we receive the collection name, we will create it within the day.""",
            "fr": """Veuillez indiquer le nom de la nouvelle collection que vous souhaitez créer via ce formulaire.

Une fois le nom de la collection reçu, nous la créerons dans la journée.""",
            "it": """Indica il nome della nuova collezione che desideri creare tramite questo modulo.

Una volta ricevuto il nome della collezione, la creeremo entro la giornata."""
        }
    },
    {
        "id": "plm_new_hierarchy",
        "application": "PLM",
        "request_type": "service_request",
        "priority": "Medium",
        "tags": [
            "hierarchy", "new hierarchy", "plm", "create",
            "hiérarchie", "nouvelle hiérarchie", "gerarchia", "nuova gerarchia"
        ],
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
            "en": """Please send us the validated hierarchy that needs to be created.

Once we receive the validated hierarchy, we will create it within the day.""",
            "fr": """Veuillez nous envoyer la hiérarchie validée qui doit être créée.

Une fois la hiérarchie validée reçue, nous la créerons dans la journée.""",
            "it": """Inviaci la gerarchia validata che deve essere creata.

Una volta ricevuta la gerarchia validata, la creeremo entro la giornata."""
        }
    },
    {
        "id": "plm_add_value_column",
        "application": "PLM",
        "request_type": "service_request",
        "priority": "Medium",
        "tags": [
            "column", "value", "add value", "new value", "plm",
            "colonne", "valeur", "ajouter valeur", "nouvelle valeur",
            "colonna", "valore", "nuovo valore"
        ],
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
            "en": """Please indicate the value that needs to be created.

Please also provide:
- a screenshot of the concerned column;
- the link to the concerned column or object.

We will create the new value within 1–2 days.""",
            "fr": """Veuillez indiquer la valeur qui doit être créée.

Merci de fournir également :
- une capture d’écran de la colonne concernée ;
- le lien vers la colonne ou l’objet concerné.

Nous créerons la nouvelle valeur sous 1 à 2 jours.""",
            "it": """Indica il valore che deve essere creato.

Fornisci anche:
- uno screenshot della colonna interessata;
- il link alla colonna o all’oggetto interessato.

Creeremo il nuovo valore entro 1–2 giorni."""
        }
    },
    {
        "id": "plm_delete_color",
        "application": "PLM",
        "request_type": "service_request",
        "priority": "Medium",
        "tags": [
            "color", "delete color", "remove color", "plm",
            "couleur", "supprimer couleur", "colore", "eliminare colore"
        ],
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
            "en": """Please send us the link and a screenshot of the color that needs to be deleted.

Once we receive the required information, we will delete it within the day.""",
            "fr": """Veuillez nous envoyer le lien et une capture d’écran de la couleur qui doit être supprimée.

Une fois les informations nécessaires reçues, nous la supprimerons dans la journée.""",
            "it": """Inviaci il link e uno screenshot del colore che deve essere eliminato.

Una volta ricevute le informazioni necessarie, lo elimineremo entro la giornata."""
        }
    },
    {
        "id": "businessmap_collection_not_visible",
        "application": "BusinessMap",
        "request_type": "bug",
        "priority": "High",
        "tags": [
            "collection", "not visible", "cannot see", "missing collection",
            "businessmap", "business map", "export", "business export",
            "collection non visible", "je ne vois pas", "collezione non visibile",
            "non vedo"
        ],
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
            "en": """Please describe what you cannot find in BusinessMap.

Please also provide:
- the link to the concerned object, if available;
- a screenshot showing the issue.

We will investigate your request as soon as possible.""",
            "fr": """Veuillez décrire ce que vous ne trouvez pas dans BusinessMap.

Merci de fournir également :
- le lien vers l’objet concerné, si disponible ;
- une capture d’écran montrant le problème.

Nous analyserons votre demande dans les plus brefs délais.""",
            "it": """Descrivi cosa non riesci a trovare in BusinessMap.

Fornisci anche:
- il link all’oggetto interessato, se disponibile;
- uno screenshot che mostri il problema.

Analizzeremo la tua richiesta nel più breve tempo possibile."""
        }
    },
    {
        "id": "businessmap_style_not_visible",
        "application": "BusinessMap",
        "request_type": "bug",
        "priority": "High",
        "tags": [
            "style", "not visible", "cannot see", "missing style",
            "businessmap", "business map", "export",
            "style non visible", "stile non visibile", "je ne vois pas", "non vedo"
        ],
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
            "en": """Please describe what you cannot find in BusinessMap.

Please also provide:
- the link to the concerned object, if available;
- a screenshot showing the issue.

We will investigate your request as soon as possible.""",
            "fr": """Veuillez décrire ce que vous ne trouvez pas dans BusinessMap.

Merci de fournir également :
- le lien vers l’objet concerné, si disponible ;
- une capture d’écran montrant le problème.

Nous analyserons votre demande dans les plus brefs délais.""",
            "it": """Descrivi cosa non riesci a trovare in BusinessMap.

Fornisci anche:
- il link all’oggetto interessato, se disponibile;
- uno screenshot che mostri il problema.

Analizzeremo la tua richiesta nel più breve tempo possibile."""
        }
    },
    {
        "id": "businessmap_export_issue",
        "application": "BusinessMap",
        "request_type": "bug",
        "priority": "High",
        "tags": [
            "export", "businessmap", "business map", "business export", "issue",
            "problem", "error", "blocked", "cannot export",
            "problème export", "erreur", "bloqué", "problema export", "errore"
        ],
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
            "en": """Please describe what you cannot find or export in BusinessMap.

Please also provide:
- the link to the concerned object, if available;
- a screenshot showing the issue.

We will investigate your request as soon as possible.""",
            "fr": """Veuillez décrire ce que vous ne trouvez pas ou ne parvenez pas à exporter dans BusinessMap.

Merci de fournir également :
- le lien vers l’objet concerné, si disponible ;
- une capture d’écran montrant le problème.

Nous analyserons votre demande dans les plus brefs délais.""",
            "it": """Descrivi cosa non riesci a trovare o esportare in BusinessMap.

Fornisci anche:
- il link all’oggetto interessato, se disponibile;
- uno screenshot che mostri il problema.

Analizzeremo la tua richiesta nel più breve tempo possibile."""
        }
    },
    {
        "id": "balchain_access",
        "application": "BalChain",
        "request_type": "bug",
        "priority": "High",
        "tags": [
            "balchain", "access", "login", "log in", "cannot login", "cannot log in",
            "blank screen", "account", "supplier", "password", "button",
            "connexion", "accès", "fournisseur", "mot de passe",
            "accesso", "schermata bianca", "fornitore", "password"
        ],
        "title": {
            "en": "BalChain Login or Access Issue",
            "fr": "Problème de connexion ou d’accès à BalChain",
            "it": "Problema di login o accesso a BalChain"
        },
        "quick_topic": {
            "en": "The user or supplier cannot log in to BalChain",
            "fr": "L’utilisateur ou le fournisseur ne peut pas se connecter à BalChain",
            "it": "L’utente o il fornitore non riesce ad accedere a BalChain"
        },
        "content": {
            "en": """Please first check the following points:

Step 1. Make sure that a BalChain account already exists for the user or supplier.
Step 2. Clear the browser cache and try again.
Step 3. Try using another browser.
Step 4. If the issue concerns a supplier, make sure the supplier clicks the BalChain button, not the Balenciaga button.
Step 5. If the issue persists, please contact MIS Support through this form and provide a link and/or screenshot.""",
            "fr": """Veuillez d’abord vérifier les points suivants :

Étape 1. Assurez-vous qu’un compte BalChain existe déjà pour l’utilisateur ou le fournisseur.
Étape 2. Videz le cache du navigateur et réessayez.
Étape 3. Essayez avec un autre navigateur.
Étape 4. Si le problème concerne un fournisseur, assurez-vous qu’il clique sur le bouton BalChain, et non sur le bouton Balenciaga.
Étape 5. Si le problème persiste, veuillez contacter MIS Support via ce formulaire et fournir un lien et/ou une capture d’écran.""",
            "it": """Verifica prima i seguenti punti:

Passo 1. Assicurati che esista già un account BalChain per l’utente o il fornitore.
Passo 2. Cancella la cache del browser e riprova.
Passo 3. Prova a utilizzare un altro browser.
Passo 4. Se il problema riguarda un fornitore, assicurati che clicchi sul pulsante BalChain e non sul pulsante Balenciaga.
Passo 5. Se il problema persiste, contatta MIS Support tramite questo modulo e fornisci un link e/o uno screenshot."""
        }
    },
    {
        "id": "stealth_style_export",
        "application": "Stealth",
        "request_type": "bug",
        "priority": "High",
        "tags": [
            "stealth", "export", "style", "not exported", "cannot export style",
            "error", "blocked", "style non exporté", "stile non esportato",
            "erreur", "errore"
        ],
        "title": {
            "en": "Cannot export a style to Stealth",
            "fr": "Impossible d’exporter un style vers Stealth",
            "it": "Impossibile esportare uno stile verso Stealth"
        },
        "quick_topic": {
            "en": "I cannot export a style to Stealth",
            "fr": "Je ne peux pas exporter un style vers Stealth",
            "it": "Non riesco a esportare uno stile verso Stealth"
        },
        "content": {
            "en": """Please provide:
- the link to the concerned style;
- a screenshot showing the export issue or error message.

We will investigate your request as soon as possible.""",
            "fr": """Veuillez fournir :
- le lien vers le style concerné ;
- une capture d’écran montrant le problème d’export ou le message d’erreur.

Nous analyserons votre demande dans les plus brefs délais.""",
            "it": """Fornisci:
- il link allo stile interessato;
- uno screenshot che mostri il problema di export o il messaggio di errore.

Analizzeremo la tua richiesta nel più breve tempo possibile."""
        }
    },
    {
        "id": "stealth_material_quote_style_code_export",
        "application": "Stealth",
        "request_type": "bug",
        "priority": "High",
        "tags": [
            "stealth", "export", "material quote", "style quote", "cannot export",
            "material quote export", "style quote export", "error", "blocked",
            "erreur", "errore"
        ],
        "title": {
            "en": "Cannot export a material quote or style quote to Stealth",
            "fr": "Impossible d’exporter un Material Quote ou un style quote vers Stealth",
            "it": "Impossibile esportare un Material Quote o uno style quote verso Stealth"
        },
        "quick_topic": {
            "en": "I cannot export a material quote or style quote to Stealth",
            "fr": "Je ne peux pas exporter un Material Quote ou un style quote vers Stealth",
            "it": "Non riesco a esportare un Material Quote o uno style quote verso Stealth"
        },
        "content": {
            "en": """Please provide:
- the link to the concerned material quote or style quote;
- a screenshot showing the export issue or error message.

We will investigate your request as soon as possible.""",
            "fr": """Veuillez fournir :
- le lien vers le Material Quote ou le style quote concerné ;
- une capture d’écran montrant le problème d’export ou le message d’erreur.

Nous analyserons votre demande dans les plus brefs délais.""",
            "it": """Fornisci:
- il link al Material Quote o allo style quote interessato;
- uno screenshot che mostri il problema di export o il messaggio di errore.

Analizzeremo la tua richiesta nel più breve tempo possibile."""
        }
    }
]

def initialize_session_state():
    if "issue" not in st.session_state:
        st.session_state.issue = ""
    if "link" not in st.session_state:
        st.session_state.link = ""


def set_issue_from_topic(topic: str):
    st.session_state.issue = topic


def reset_form():
    st.session_state.issue = ""
    st.session_state.link = ""


def normalize_text(text: str) -> str:
    text = text.lower()
    text = text.replace("business map", "businessmap")
    text = text.replace("log in", "login")
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9]+", " ", text)
    return text.strip()


def tokenize(text: str):
    stop_words = {
        "the", "and", "for", "with", "this", "that", "from", "into", "onto",
        "can", "cannot", "cant", "can't", "could", "would", "should", "please",
        "how", "what", "where", "when", "why", "issue", "problem", "problems",
        "je", "j", "ne", "pas", "un", "une", "le", "la", "les", "des", "de",
        "du", "dans", "sur", "pour", "avec", "comment", "veuillez",
        "non", "un", "una", "il", "lo", "la", "gli", "le", "di", "da",
        "per", "con", "come", "posso", "riesco"
    }

    normalized = normalize_text(text)
    words = normalized.split()

    return [
        word
        for word in words
        if len(word) > 2 and word not in stop_words
    ]


def find_instruction(question: str, application: str):
    question_tokens = tokenize(question)
    best_item = None
    best_score = 0

    for item in INSTRUCTIONS:
        if item["application"] != application:
            continue

        searchable_text = " ".join([
            item["id"],
            item["title"]["en"],
            item["title"]["fr"],
            item["title"]["it"],
            item["quick_topic"]["en"],
            item["quick_topic"]["fr"],
            item["quick_topic"]["it"],
            " ".join(item["tags"]),
        ])

        searchable_normalized = normalize_text(searchable_text)
        searchable_tokens = tokenize(searchable_text)

        score = 0

        for token in question_tokens:
            if token in searchable_tokens:
                score += 3
            elif token in searchable_normalized:
                score += 1

        for tag in item["tags"]:
            if normalize_text(tag) in normalize_text(question):
                score += 4

        if score > best_score:
            best_score = score
            best_item = item

    return best_item if best_score > 0 else None


def suggest_labels(application: str):
    return ["L1", application]


def suggest_priority(issue: str, instruction):
    if instruction and instruction.get("priority"):
        return instruction["priority"]

    high_priority_keywords = [
        "bug", "error", "blocked", "cannot work", "not working",
        "cannot login", "cannot log in", "access issue", "export issue",
        "not visible", "missing", "blank screen",
        "erreur", "bloqué", "ne fonctionne pas", "impossible",
        "errore", "bloccato", "non funziona"
    ]

    issue_normalized = normalize_text(issue)

    for keyword in high_priority_keywords:
        if normalize_text(keyword) in issue_normalized:
            return "High"

    return "Medium"


def build_mailto(language, application, issue, link, instruction, uploaded_file, labels, priority):
    instruction_title = (
        instruction["title"][language]
        if instruction
        else "No matching instruction found"
    )

    subject = f"MIS Support Request - {application}"

    link_text = link if link.strip() else "No link provided"
    labels_text = ", ".join(labels)

    screenshot_text = (
        "A screenshot is available and can be attached to the request."
        if uploaded_file is not None
        else "No screenshot was uploaded."
    )

    if language == "fr":
        link_text = link if link.strip() else "Aucun lien fourni"
        screenshot_text = (
            "Une capture d’écran est disponible et peut être ajoutée à la demande."
            if uploaded_file is not None
            else "Aucune capture d’écran n’a été ajoutée."
        )

        body = f"""Bonjour,

Je rencontre un problème avec l'application suivante : {application}.

Problème :
{issue}

Lien concerné :
{link_text}

Capture d'écran :
{screenshot_text}

Instruction proposée par l'assistant :
{instruction_title}

Métadonnées suggérées :
Application : {application}
Labels : {labels_text}
Priority : {priority}

Pouvez-vous m'aider, s'il vous plaît ?

Merci d'avance."""
    elif language == "it":
        link_text = link if link.strip() else "Nessun link fornito"
        screenshot_text = (
            "Uno screenshot è disponibile e può essere allegato alla richiesta."
            if uploaded_file is not None
            else "Nessuno screenshot è stato caricato."
        )

        body = f"""Buongiorno,

Ho un problema con la seguente applicazione: {application}.

Problema:
{issue}

Link interessato:
{link_text}

Screenshot:
{screenshot_text}

Istruzione proposta dall'assistente:
{instruction_title}

Metadati suggeriti:
Applicazione: {application}
Labels: {labels_text}
Priority: {priority}

Potreste aiutarmi, per favore?

Grazie in anticipo."""
    else:
        body = f"""Hello,

I have an issue with the following application: {application}.

Issue:
{issue}

Concerned link:
{link_text}

Screenshot:
{screenshot_text}

Instruction suggested by the assistant:
{instruction_title}

Suggested ticket metadata:
Application: {application}
Labels: {labels_text}
Priority: {priority}

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

    if not link.strip() and uploaded_file is None:
        st.warning(texts["missing_link_or_screenshot"])
        st.stop()

    instruction = find_instruction(issue, application)
    labels = suggest_labels(application)
    priority = suggest_priority(issue, instruction)

    st.divider()
    st.subheader(texts["answer_title"])

    if instruction:
        st.success(texts["matched_instruction"])
        st.markdown(f"**{instruction['title'][language]}**")
        st.text(instruction["content"][language])
    else:
        st.warning(texts["no_match"])

    st.subheader(texts["ticket_metadata"])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**{texts['labels']}:** {', '.join(labels)}")

    with col2:
        if priority == "High":
            st.error(f"**{texts['priority']}:** {texts['high']}")
        else:
            st.info(f"**{texts['priority']}:** {texts['medium']}")

    if link.strip():
        st.markdown(f"**{texts['provided_link']}:** {link}")
    else:
        st.markdown(f"**{texts['provided_link']}:** {texts['no_link']}")

    if uploaded_file is not None:
        st.info(texts["screenshot_uploaded"])
    else:
        st.info(texts["screenshot_not_uploaded"])

    st.info(texts["screenshot_note"])
    st.markdown(f"**{texts['helpful']}**")
    st.write(texts["support_note"])

    mailto_link = build_mailto(
        language=language,
        application=application,
        issue=issue,
        link=link,
        instruction=instruction,
        uploaded_file=uploaded_file,
        labels=labels,
        priority=priority,
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
        st.write("Application:", application)
        st.write("Labels:", ", ".join(labels))
        st.write("Priority:", priority)
        st.write("Instruction:", instruction_title)
        st.write("Issue:", issue)
        st.write("Link:", link if link.strip() else texts["no_link"])

        if uploaded_file is not None:
            st.write("Screenshot:", uploaded_file.name)
        else:
            st.write("Screenshot:", texts["screenshot_not_uploaded"])
