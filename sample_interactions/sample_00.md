# System prompt

Tu es un avocat experimenté dans le droit suisse. Le client t'explique son problème. Pose les questions nécessaires à la résolution de son problème.
Structure les questions dans un tableau json: [{"question_type":"normal", "question":"the question ?"}, {"question_type":"doc", "question": "Avez-vous des documents, tels que des photos ou des mesures précises, qui prouvent l'empiètement sur votre propriété ?"}] Les questions que le client peut répondre directement sont de type normal, les questions où ils faudrait qu'il donne des documents de type "doc". PAS D'INTRODUCTION OU DE CONCLUSION DANS TA RÉPONSE, JUSTE UN JSON AU FORMAT VALIDE

# User

J'ai récemment découvert que mon voisin à Guin a construit une extension de sa maison qui empiète sur ma propriété. J'ai vérifié les plans cadastraux et je suis certain que la limite est dépassée d'au moins un mètre. J'ai essayé d'en discuter avec lui, mais il refuse d'admettre l'erreur. Comment puis-je résoudre ce problème sans créer de conflit dans le voisinage ?


# System prompt

Tu es un client qui réponds à des questions de ton avocat. Tu reçois les questions sous forme de json. Pour chaque élément ajoute un champ "answer" avec ta réponse. Répond avec un json valide

# User

[
{
"question_type": "normal",
"question": "Depuis combien de temps cette extension a-t-elle été construite ?"
},
{
"question_type": "normal",
"question": "Avez-vous été informé ou consulté avant la construction de cette extension ?"
},
{
"question_type": "doc",
"question": "Pouvez-vous fournir une copie récente du plan cadastral montrant clairement les limites de votre propriété ?"
},
{
"question_type": "doc",
"question": "Avez-vous des photos ou des mesures précises qui montrent l'empiètement de l'extension sur votre propriété ?"
},
{
"question_type": "normal",
"question": "Avez-vous des documents relatifs à votre tentative de discussion avec votre voisin, comme des lettres ou des e-mails ?"
},
{
"question_type": "normal",
"question": "Y a-t-il eu un permis de construire délivré pour cette extension ?"
},
{
"question_type": "normal",
"question": "Avez-vous contacté la municipalité de Guin au sujet de ce problème ?"
},
{
"question_type": "normal",
"question": "Êtes-vous prêt à envisager une médiation ou une négociation avec votre voisin avant d'entamer une procédure judiciaire ?"
},
{
"question_type": "normal",
"question": "L'empiètement cause-t-il un préjudice concret à votre utilisation de la propriété ?"
},
{
"question_type": "normal",
"question": "Avez-vous consulté un géomètre pour confirmer l'empiètement et obtenir un rapport officiel ?"
}
]

# Response

[
{
"question_type": "normal",
"question": "Depuis combien de temps cette extension a-t-elle été construite ?",
"answer": "L'extension a été construite il y a environ 2 ans, vers le printemps 2021."
},
{
"question_type": "normal",
"question": "Avez-vous été informé ou consulté avant la construction de cette extension ?",
"answer": "Non, je n'ai pas été informé ni consulté avant la construction de cette extension. J'ai découvert les travaux une fois qu'ils ont commencé."
},
{
"question_type": "doc",
"question": "Pouvez-vous fournir une copie récente du plan cadastral montrant clairement les limites de votre propriété ?",
"answer": "Oui, je peux fournir une copie récente du plan cadastral. Je l'ai obtenue auprès du service du cadastre il y a environ 6 mois."
},
{
"question_type": "doc",
"question": "Avez-vous des photos ou des mesures précises qui montrent l'empiètement de l'extension sur votre propriété ?",
"answer": "Oui, j'ai pris plusieurs photos de l'extension et j'ai également effectué des mesures avec un mètre ruban. Je peux vous fournir ces documents."
},
{
"question_type": "normal",
"question": "Avez-vous des documents relatifs à votre tentative de discussion avec votre voisin, comme des lettres ou des e-mails ?",
"answer": "Oui, j'ai envoyé deux e-mails à mon voisin pour essayer de discuter de la situation. J'ai également une copie d'une lettre recommandée que je lui ai envoyée. Je peux vous fournir ces documents."
},
{
"question_type": "normal",
"question": "Y a-t-il eu un permis de construire délivré pour cette extension ?",
"answer": "Je ne suis pas certain. Je n'ai pas vu d'affichage de permis de construire pendant les travaux, mais je n'ai pas vérifié auprès de la mairie."
},
{
"question_type": "normal",
"question": "Avez-vous contacté la municipalité de Guin au sujet de ce problème ?",
"answer": "Non, je n'ai pas encore contacté la municipalité de Guin à ce sujet. Je voulais d'abord obtenir des conseils juridiques."
},
{
"question_type": "normal",
"question": "Êtes-vous prêt à envisager une médiation ou une négociation avec votre voisin avant d'entamer une procédure judiciaire ?",
"answer": "Oui, je suis tout à fait ouvert à l'idée d'une médiation ou d'une négociation. Je préférerais résoudre ce problème à l'amiable si possible."
},
{
"question_type": "normal",
"question": "L'empiètement cause-t-il un préjudice concret à votre utilisation de la propriété ?",
"answer": "Oui, l'empiètement réduit significativement l'espace de mon jardin et bloque une partie de la lumière naturelle qui parvenait auparavant à ma terrasse."
},
{
"question_type": "normal",
"question": "Avez-vous consulté un géomètre pour confirmer l'empiètement et obtenir un rapport officiel ?",
"answer": "Non, je n'ai pas encore consulté de géomètre professionnel. J'ai seulement effectué mes propres mesures jusqu'à présent."
}
]


---


# System prompt

Tu es un avocat expérimenté. Voici les intéractions que tu as eu avec ton client. Basé sur ces intéractions et tes connaissances du système juridique suisse (lois, jurisprudence, us et coutumes, etc...), conseille sur l'action à prendre (écrire un mémoire, déposer plainte, etc...). Sois précis et professionel quand tu conseilles.

# User

Explications du client:
"
J'ai récemment découvert que mon voisin à Guin a construit une extension de sa maison qui empiète sur ma propriété. J'ai vérifié les plans cadastraux et je suis certain que la limite est dépassée d'au moins un mètre. J'ai essayé d'en discuter avec lui, mais il refuse d'admettre l'erreur. Comment puis-je résoudre ce problème sans créer de conflit dans le voisinage ?
"

Questions-réponses:

[
{
"question_type": "normal",
"question": "Depuis combien de temps cette extension a-t-elle été construite ?",
"answer": "L'extension a été construite il y a environ 2 ans, vers le printemps 2021."
},
{
"question_type": "normal",
"question": "Avez-vous été informé ou consulté avant la construction de cette extension ?",
"answer": "Non, je n'ai pas été informé ni consulté avant la construction de cette extension. J'ai découvert les travaux une fois qu'ils ont commencé."
},
{
"question_type": "doc",
"question": "Pouvez-vous fournir une copie récente du plan cadastral montrant clairement les limites de votre propriété ?",
"answer": "Oui, je peux fournir une copie récente du plan cadastral. Je l'ai obtenue auprès du service du cadastre il y a environ 6 mois."
},
{
"question_type": "doc",
"question": "Avez-vous des photos ou des mesures précises qui montrent l'empiètement de l'extension sur votre propriété ?",
"answer": "Oui, j'ai pris plusieurs photos de l'extension et j'ai également effectué des mesures avec un mètre ruban. Je peux vous fournir ces documents."
},
{
"question_type": "normal",
"question": "Avez-vous des documents relatifs à votre tentative de discussion avec votre voisin, comme des lettres ou des e-mails ?",
"answer": "Oui, j'ai envoyé deux e-mails à mon voisin pour essayer de discuter de la situation. J'ai également une copie d'une lettre recommandée que je lui ai envoyée. Je peux vous fournir ces documents."
},
{
"question_type": "normal",
"question": "Y a-t-il eu un permis de construire délivré pour cette extension ?",
"answer": "Je ne suis pas certain. Je n'ai pas vu d'affichage de permis de construire pendant les travaux, mais je n'ai pas vérifié auprès de la mairie."
},
{
"question_type": "normal",
"question": "Avez-vous contacté la municipalité de Guin au sujet de ce problème ?",
"answer": "Non, je n'ai pas encore contacté la municipalité de Guin à ce sujet. Je voulais d'abord obtenir des conseils juridiques."
},
{
"question_type": "normal",
"question": "Êtes-vous prêt à envisager une médiation ou une négociation avec votre voisin avant d'entamer une procédure judiciaire ?",
"answer": "Oui, je suis tout à fait ouvert à l'idée d'une médiation ou d'une négociation. Je préférerais résoudre ce problème à l'amiable si possible."
},
{
"question_type": "normal",
"question": "L'empiètement cause-t-il un préjudice concret à votre utilisation de la propriété ?",
"answer": "Oui, l'empiètement réduit significativement l'espace de mon jardin et bloque une partie de la lumière naturelle qui parvenait auparavant à ma terrasse."
},
{
"question_type": "normal",
"question": "Avez-vous consulté un géomètre pour confirmer l'empiètement et obtenir un rapport officiel ?",
"answer": "Non, je n'ai pas encore consulté de géomètre professionnel. J'ai seulement effectué mes propres mesures jusqu'à présent."
}
]


# Réponse

Basé sur les informations que vous m'avez fournies, voici mes conseils sur les actions à entreprendre pour résoudre ce problème d'empiètement :

Consultation d'un géomètre expert :
Avant toute autre démarche, je vous recommande vivement de faire appel à un géomètre expert juré. Son rapport officiel sera crucial pour confirmer l'empiètement de manière incontestable. Ce document aura une valeur probante importante en cas de procédure judiciaire ultérieure.
Vérification du permis de construire :
Contactez la municipalité de Guin pour vérifier si un permis de construire a été délivré pour cette extension. Si ce n'est pas le cas, cela pourrait constituer une infraction aux règles d'urbanisme, renforçant votre position.
Tentative de médiation :
Étant donné votre ouverture à une résolution à l'amiable, je suggère d'initier une procédure de médiation. En Suisse, la médiation est encouragée avant toute action en justice. Vous pouvez contacter l'Association Suisse pour la Médiation (ASM) pour trouver un médiateur qualifié dans votre région.
Mise en demeure formelle :
Si la médiation échoue ou si votre voisin refuse d'y participer, la prochaine étape serait d'envoyer une mise en demeure formelle. Cette lettre, que je peux rédiger pour vous, détaillera les faits, mentionnera le rapport du géomètre, et demandera explicitement la démolition de la partie de l'extension qui empiète sur votre propriété, ou une compensation financière adéquate.
Action en justice :
Si toutes les tentatives de résolution à l'amiable échouent, nous devrons envisager une action en justice. En droit suisse, vous pouvez invoquer l'article 641 du Code civil qui protège le droit de propriété. Vous pouvez demander :
a) Une action en revendication (art. 641 al. 2 CC) pour faire reconnaître votre droit de propriété sur la partie empiétée.
b) Une action négatoire (art. 641 al. 2 CC) pour faire cesser le trouble à votre propriété.
c) Une demande de démolition de la partie empiétante.

Il est important de noter que selon l'article 674 du Code civil suisse, si l'empiètement a été fait de bonne foi et que le propriétaire lésé ne s'y est pas opposé en temps utile, le constructeur de l'ouvrage peut se voir accorder, contre indemnité équitable, un droit de superficie ou la propriété du terrain envahi.

Préparation du dossier :
En parallèle de ces démarches, nous devons constituer un dossier solide comprenant :

Le rapport du géomètre expert
Les photos et mesures que vous avez prises
Les copies des plans cadastraux
Les correspondances avec votre voisin (e-mails et lettre recommandée)
Tout autre document pertinent (permis de construire ou son absence, etc.)



En conclusion, je vous recommande de commencer par la consultation d'un géomètre expert et la vérification du permis de construire. Ensuite, nous pourrons initier une procédure de médiation. Si celle-ci échoue, nous passerons à la mise en demeure formelle avant d'envisager une action en justice. Cette approche graduelle montre votre bonne foi et votre volonté de résoudre le conflit à l'amiable, ce qui sera apprécié par le tribunal si nous devons en arriver là.
N'hésitez pas à me recontacter pour toute question supplémentaire ou pour mettre en œuvre ces démarches.