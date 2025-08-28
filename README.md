Federal laws in french : 

[liechticonsulting/fedlex](https://huggingface.co/datasets/liechticonsulting/fedlex)

https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/mcq_4_choices/test?sort%5Bcolumn%5D=language&sort%5Bdirection%5D=desc&row=195

Lexam paper : https://arxiv.org/pdf/2505.12864

system prompt : ```Vous êtes un système expert juridique spécialisé dans le droit suisse. Vous répondez de manière juridiquement correcte et toujours en francais. toutes les citations d'article doivent être dans le format art. 99-199 CO par exemple, donc avec a minuscule pour art. et ensuite le numéro suivi du code de la loi. JAMAIS Arts. ou Art. ou bien pas de code de loi ! VOUS NE RÉPONDEZ QUE EN TABLEAU, IL FAUT FAIRE UN TABLEAU TRÈS COMPLET QUI RECOUVRE TOUTE LA LOI, PAS DE PLACE POUR DES COMMENTAIRES.
Groupe les articles par thèmes de quelques articles, répond dans des tableaux qui systématiquement recouvrent l'entiereté de la loi, exemple de réponse:
### 9.2  Procédure d’exécution (art. 337‑343)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| **Exécution directe** | art. 337 CPC| Si le tribunal a déjà ordonné les mesures d’exécution, la décision s’exécute directement. |
| **Requête d’exécution** | art. 338‑339 CPC| Sinon, le créancier dépose une requête auprès du **tribunal de l’exécution** (domicile du débiteur, lieu d’exécution ou lieu de la décision). |
| **Compétence** | art. 339 al. 1 CPC| Tribunal du domicile du débiteur, du lieu d’exécution ou du tribunal qui a rendu la décision. |
| **Mesures conservatoires** | art. 340‑343 CPC| Le tribunal de l’exécution peut imposer des amendes, saisir des biens, ordonner la **mise à ban** ou la **surveillance électronique** (art. 343 al. 1‑e CPC). |
| **Caractère exécutoire suspendu** | art. 341‑342 CPC| Le débiteur peut demander suspension, prouver extinction, prescription ou péremption. |

### prochain titre

<prochain tableau>

etc...

LE CODE DE CETTE LOI EST CPC, MET TOUJOURS LE CODE DE LA LOI EN QUESTION AVEC LE NUMÉRO D'ARTICLE (y compris quand tu cites un article dans les points clés). FAIT DES GROUPES PAR EXEMPLES art.1-3 CPC

TOUTES LES LIGNES DOIVENT TOUJOURS ETRE REMPLIES POUR CHAQUE TABLEAU. NE MENTIONNE PAS DE NUMÉRO D'ARTICLE DANS LA COLONNE THÈME
```

model : gpt-oss-120b


### Art. 1‑3 – Objet et champ d’application (art. 1‑3 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Objet | art. 1 CPC | La loi règle la procédure applicable devant les juridictions cantonales : affaires civiles cieuses, décisions judiciaires de la juridiction gracieuse, poursuite pour dettes et faillite, arbitrage. |
| Causes internationales | art. 2 CPC | Les traités internationaux et la loi fédérale du 18 déc. 1987 sur le droit international privé (LDIP) sont réservés. |
| Organisation des tribunaux | art. 3 CPC | Sauf disposition contraire, l’organisation des tribunaux et autorités de conciliation relève des cantons. |

---

### Art. 4‑8 – Compétence matérielle et récusation (art. 4‑8 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Principes de compétence | art. 4 CPC | Le droit cantonal détermine la compétence matérielle et fonctionnelle, sauf disposition contraire. La valeur litigieuse est calculée selon la présente loi. |
| Instance cantonale unique | art. 5 CPC | Le droit cantonal institue la juridiction compétente pour statuer en instance cantonale unique sur les litiges de propriété intellectuelle, droit des cartels, usage d’une raison de commerce, etc. |
| Tribunal de commerce | art. 6 CPC | Les cantons peuvent créer un tribunal de commerce pour les litiges commerciaux ; conditions d’éligibilité détaillées (activité commerciale, valeur ≥ 30 000 CHF, etc.). |
| Juridiction de l’assurance complémentaire | art. 7 CPC | Les cantons peuvent instituer un tribunal pour les litiges relatifs aux assurances complémentaires à l’assurance‑maladie sociale. |
| Action directe devant le tribunal supérieur | art. 8 CPC | Si la valeur litigieuse ≥ 100 000 CHF, le demandeur peut, avec l’accord du défendeur, porter l’action directement devant le tribunal supérieur (instance cantonale unique). |

---

### Art. 9‑14 – For, domicile et résidence (art. 9‑14 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| For impératif | art. 9 CPC | Un for est impératif uniquement s’il est prévu expressément par la loi; les parties ne peuvent y déroger. |
| Domicile et siège | art. 10 CPC | Détermination du for : domicile du particulier, siège de la personne morale, domicile du défendeur étranger, etc. |
| Résidence | art. 11 CPC | Le for est le domicile ; à défaut, la résidence habituelle ou le dernier lieu de résidence connu. |
| Établissements et succursales | art. 12 CPC | Le tribunal du domicile, du siège ou du lieu d’établissement ou de succursale est compétent pour les actions découlant d’activités commerciales ou professionnelles. |
| Mesures provisionnelles | art. 13 CPC | Competence du tribunal du for principal et du lieu d’exécution des mesures provisionnelles. |
| Demande reconventionnelle | art. 14 CPC | La demande reconventionnelle peut être formée au for principal lorsqu’elle est connexe; le for subsiste même si la demande principale est liquidée. |

---

### Art. 15‑16 – Consorité, appel en cause et élection de for (art. 15‑17 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Consorité et cumul d’actions | art. 15 CPC | Un tribunal compétent à l’égard d’un défendeur l’est pour tous les co‑defendeurs ; les prétentions connexes sont jugées par le même tribunal. |
| Appel en cause | art. 16 CPC | Le tribunal compétent pour l’action principale statue aussi sur l’appel en cause. |
| Élection de for | art. 17 CPC | Les parties peuvent convenir d’un for pour le règlement d’un différend, sauf disposition contraire; la convention doit être écrite ou prouvable. |
| Acceptation tacite | art. 18 CPC | Le tribunal saisi est compétent lorsqu’une partie, sans réserve, ne conteste pas la compétence. |
| Juridiction gracieuse | art. 19 CPC | Le tribunal ou l’autorité du domicile ou du siège du requérant est impérativement compétent pour les affaires de juridiction gracieuse. |

---

### Art. 20‑28 – Droit de la personnalité, succession et biens immobiliers (art. 20‑29 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Protection de la personnalité | art. 20 CPC | Le tribunal du domicile ou du siège de l’une des parties statue sur les actions fondées sur atteinte à la personnalité, droit de réponse, changement de nom, actions liées à la LPD. |
| Décès et absence | art. 21 CPC | Le tribunal du dernier domicile connu statue sur la déclaration de décès ou d’absence. |
| Registres de l’état civil | art. 22 CPC | Le tribunal du ressort du registre concerné est compétent pour les actions de modification du registre. |
| Droit du mariage | art. 23‑27 CPC | Le tribunal du domicile de l’une des parties est compétent pour les requêtes relatives au mariage, séparation de biens, filiation, entretien, et aux prétentions de la mère non mariée. |
| Successions | art. 28 CPC | Le tribunal du dernier domicile du défunt statue sur les actions successorales, la liquidation du régime matrimonial, et les actions sur biens immobiliers ou agricoles. |
| Droits réels – Immeubles | art. 29 CPC | Le tribunal du lieu d’immatriculation au registre foncier est compétent pour les actions réelles, les communautés de propriétaires, les gages, ainsi que pour la juridiction gracieuse relative aux droits réels. |
| Droits réels – Biens meubles | art. 30 CPC | Le tribunal du domicile, du siège du défendeur ou du lieu où le bien est situé statue sur les actions relatives aux droits réels mobiliers et aux créances garanties. |

---

### Art. 31‑38 – Actions découlant de contrats, consommation et accidents (art. 31‑38 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Principes généraux | art. 31 CPC | Le tribunal du domicile ou du siège du défendeur ou du lieu d’exécution de la prestation est compétent pour les actions découlant d’un contrat. |
| Consommateurs | art. 32 CPC | Le for est le domicile du consommateur (ou du défendeur pour le fournisseur) pour les contrats de consommation. |
| Bail à loyer ou à ferme | art. 33 CPC | Le tribunal du lieu où est situé l’immeuble est compétent pour les actions fondées sur un contrat de bail. |
| Droit du travail | art. 34 CPC | Le tribunal du domicile ou du siège du défendeur ou du lieu d’exercice du travail est compétent pour les actions relatives au droit du travail. |
| Renonciation aux for | art. 35 CPC | Les parties ne peuvent renoncer aux for : art. 32‑34 avant la naissance du litige ou par acceptation tacite. |
| Actions illicites | art. 36‑38 CPC | Le tribunal du domicile ou du siège du lésé ou du défendeur, ou du lieu de l’acte ou du résultat, statue sur les actions illicites, dommages‑intérêts de mesures provisionnelles injustifiées, accidents de véhicules à moteur ou de bicyclettes, et, selon art. 38 a, les accidents nucléaires. |

---

### Art. 39‑44 – Droit civil, action de la Cour et valeur litigieuse (art. 39‑44 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Conclusions civiles | art. 39 CPC | La compétence du tribunal pénal pour les conclusions civiles est réservée. |
| Valeur litigieuse | art. 91‑94 CPC* (voir tableau ci‑dessous) | Principes de détermination, revenus périodiques, consorité simple, et règle de la demande reconventionnelle. |
| Valeur des actions non chiffrées | art. 85 CPC | Une action non chiffrée peut être introduite ; la valeur litigieuse est fixée par le tribunal, la compétence reste malgré le dépassement éventuel. |
| Action partielle | art. 86 CPC | Une prétention divisible peut donner lieu à une action partielle. |
| Action formatrice | art. 87 CPC | Action visant à créer, modifier ou dissoudre un droit ou rapport juridique. |
| Action en constatation de droit | art. 88 CPC | Action destinée à faire constater l’existence ou l’inexistence d’un droit ou d’un rapport juridique. |

\* Voir tableau **Valeur litigieuse (art. 91‑94 CPC)** ci‑après.

---

### Art. 95‑111 – Frais, avance et assistance judiciaire (art. 95‑111 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Définitions des frais | art. 95 CPC | Frais = frais judiciaires + dépens (émoluments de conciliation, frais d’administration des preuves, etc.). |
| Tarif des frais | art. 96 CPC | Les cantons fixent le tarif des frais; dispositions relatives aux émoluments de la LP sont réservées. |
| Information sur les frais | art. 97 CPC | Le tribunal informe la partie non représentée de l’estimation des frais et de l’assistance judiciaire. |
| Avance de frais | art. 98‑101 CPC | Le tribunal peut exiger une avance (½ ou totalité) selon la nature de la procédure ; délais, sûretés et conséquences du non‑paiement. |
| Frais d’administration des preuves | art. 102 CPC | Chaque partie avance les frais d’administration des preuves qu’elle requiert; partage en cas de demande conjointe. |
| Recours contre frais | art. 103 CPC | Les décisions relatives aux avances et sûretés sont susceptibles de recours. |
| Fixation et répartition des frais | art. 104‑108 CPC | Les frais sont généralement fixés et répartis d’office ; règles générales, équité et cas de transaction. |
| Dépenses et frais de transaction | art. 109‑111 CPC | Règles de répartition en cas de transaction, recours, remboursement des frais et dispenses. |

---

### Art. 112‑122 – Sursis, remise, intérêts et assistance judiciaire (art. 112‑122 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Sursis et remise | art. 112 CPC | Le tribunal peut accorder un sursis ou renoncer aux créances de frais si la partie est durablement démunie. Prescription des créances de frais : 10 ans; intérêt moratoire : 5 %. |
| Assistance judiciaire – droit | art. 117 CPC | Une personne sans ressources suffisantes et dont la cause n’est pas dépourvue de chance a droit à l’assistance judiciaire. |
| Étendue de l’assistance | art. 118 CPC | Exonération d’avances et sûretés, exonération des frais judiciaires, désignation d’un conseil juridique (officier d’office). Possibilité partielle ou totale, même pour l’administration des preuves. |
| Requête et procédure | art. 119 CPC | La requête d’assistance judiciaire peut être présentée avant ou pendant la litispendance; le tribunal statue en procédure sommaire; le défaut de preuve de fortune entraîne la décision. |
| Retrait de l’assistance | art. 120 CPC | Le tribunal retire l’assistance judiciaire si les conditions ne sont plus remplies ou jamais remplis. |
| Recours contre décision d’assistance | art. 121 CPC | Les décisions refusant ou retirant l’assistance judiciaire sont susceptibles de recours. |
| Règlement des frais en cas d’assistance | art. 122 CPC | En cas de succombance : rémunération du conseil juridique par le canton, frais judiciaires à la charge du canton, avances restituées, dépens versés à la partie adverse. En cas de gain : le canton paie le conseil si les dépens ne peuvent être obtenus de la partie adverse. |

---

### Art. 123‑127 – Remboursement, dispense cantonale et service d’exécution (art. 123‑127 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Remboursement de l’assistance | art. 123 CPC | La partie doit rembourser l’assistance judiciaire dès qu’elle en a la capacité; la créance du canton se prescrit par 10 ans à compter de la fin du procès. |
| Dispositions cantonales sur les frais | art. 116 CPC | Les cantons peuvent prévoir des dispenses de frais plus larges ; les dispenses cantonales s’appliquent également à la Confédération. |
| Sursis, remise et intérêts (voir art. 112) | – | – |
| Exécution des décisions (art. 335‑344) : voir tableau **Exécution (art. 335‑344 CPC)** ci‑après. |

---

### Valeur litigieuse (art. 91‑94 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Principe général | art. 91 CPC | La valeur du litige est déterminée par les conclusions ; les intérêts, frais de procédure ou mesures subsidiaires ne sont pas pris en compte. |
| Revenus périodiques | art. 92 CPC | Les revenus ou prestations périodiques sont valorisés comme un capital (20 × revenu annuel ; ou valeur actualisée pour rentes viagères). |
| Consorité simple & cumul d’actions | art. 93 CPC | En cas de consorité simple ou de cumul, les prétentions sont additionnées, sauf exclusion; le type de procédure reste le même. |
| Demande reconventionnelle | art. 94 CPC | Si les demandes s’opposent, la valeur la plus élevée prévaut ; si elles ne s’excluent pas, les valeurs sont additionnées pour le calcul des frais. |

---

### Exécution des décisions (art. 335‑344 CPC)

| Thème | Référence | Points clés |
|-------|-----------|------------|
| Champ d’application | art. 335 CPC | Les décisions sont exécutées selon les dispositions du présent chapitre ; les décisions portant sur versement ou sûretés relèvent de la LP. |
| Caractère exécutoire | art. 336 CPC | Décision exécutoire lorsqu’elle est entrée en force sans suspension, ou lorsqu’un caractère exécutoire anticipé a été prononcé. |
| Exécution directe | art. 337 CPC | Si la décision ordonne les mesures d’exécution, elle peut être exécutée directement ; la partie succombante peut demander suspension auprès du tribunal de l’exécution. |
| Requête d’exécution | art. 338 CPC | Si la décision ne peut être exécutée directement, une requête d’exécution doit être présentée au tribunal de l’exécution, avec les conditions et documents nécessaires. |
| Compétence du tribunal de l’exécution | art. 339 CPC | Compétent : tribunal du domicile/siège du succombant, du lieu d’exécution, ou du lieu de la décision. Procédure sommaire. |
| Mesures conservatoires | art. 340 CPC | Le tribunal de l’exécution peut, sans audience préalable, ordonner des mesures conservatoires. |
| Examen du caractère exécutoire | art. 341 CPC | Le tribunal examine d’office le caractère exécutoire, fixe un bref délai au succombant, qui peut invoquer faits post‑notification (extinction, prescription, etc.) ; titres requis pour extinction ou sursis. |
| Prestations conditionnelles | art. 342 CPC | Les décisions conditionnelles ou subordonnées à contre‑prestation s’exécutent seulement si la condition est remplie ou la contre‑prestation offerte/exécutée. |
| Obligations de faire, s’abstenir, tolérer | art. 343 CPC | Le tribunal peut assortir la décision d’amendes (max 5 000 CHF, 1 000 CHF/jour), d’une peine prévue à l’art. 292 CP, d’une mesure de contrainte (enlèvement, expulsion) ou d’exécution par un tiers. En cas d’interdiction au sens art. 28 b CC, possible surveillance électronique (art. 28 c CC). |
| Déclaration de volonté | art. 344 CPC | (Contenu non fourni dans le texte extrait ; article réservé ou non détaillé). |

---  

https://ocrmypdf.readthedocs.io/en/latest/cookbook.html#basic-examples

# Publications

https://www.ejl-fjv.ch/publications

# HF Datasets

https://huggingface.co/datasets/rcds/swiss_legislation

https://huggingface.co/datasets/rcds/occlusion_swiss_judgment_prediction

https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics?tab=readme-ov-file#datasets-and-data

LEGAL_TOPICS = [
    "Formation des contrats",
    "Effets des contrats",
    "Inexécution des contrats",
    "Responsabilité contractuelle",
    "Responsabilité extracontractuelle (délictuelle et quasi-délictuelle)",
    "Obligations naturelles",
    "Gestion d'affaires",
    "Enrichissement sans cause",
    "Contrats spéciaux (vente, location, bail, mandat, prêt, dépôt, etc.)",
    "Droit des sûretés (gage, hypothèque, privilège)",
    "Droit des sociétés (sociétés de personnes, sociétés de capitaux)",
    "Droit des faillites et des poursuites",
    "Droit des successions",
    "Droit de la famille (mariage, divorce, séparation de corps, filiation, autorité parentale, adoption)",
    "Droit des personnes (capacité juridique, personnalité juridique, domicile, etc.)",
    "Droit des biens (propriété, possession, servitudes, etc.)",
    "Droit des choses (droit réel)",
    "Droit immobilier (propriété bâtie, copropriété, servitudes foncières, droit de superficie)",
    "Droit des contrats spéciaux (contrats de construction, contrats d'assurance, contrats de travail)",
    "Droit de la responsabilité civile",
    "Droit de la responsabilité pénale (aspects civils)",
    "Droit international privé (droit civil)",
    "Droit comparé (droit civil)",
    "Droit des contrats électroniques",
    "Droit de la protection des données (aspects civils)",
    "Droit de la consommation",
    "Droit des assurances",
    "Droit du travail (aspects civils)",
    "Droit des successions internationales",
    "Droit des régimes matrimoniaux",
    "Droit des libéralités (donations, legs)",
    "Droit des testaments",
    "Droit de la représentation",
    "Droit des associations",
    "Droit des fondations",
    "Droit des trusts (si applicable en Suisse)",
    "Droit des marques (aspects civils)",
    "Droit d'auteur (aspects civils)",
    "Droit des brevets (aspects civils)",
    "Droit de la concurrence (aspects civils)",
    "Droit de la propriété intellectuelle (aspects civils)",
]

LEGAL_TOPICS = [
    "Introduction générale au droit pénal suisse",
    "Sources du droit pénal suisse (Code pénal, lois spéciales, jurisprudence)",
    "Principes fondamentaux du droit pénal suisse (légalité, culpabilité, proportionnalité, etc.)",
    "Interprétation des normes pénales",
    "L'infraction pénale: éléments constitutifs (élément matériel, élément moral, élément légal)",
    "La tentative",
    "La participation (auteur, complice, instigateur)",
    "L'élément matériel de l'infraction",
    "L'élément moral de l'infraction (dol, faute)",
    "L'imputabilité",
    "Les causes d'exclusion de la responsabilité pénale (erreur, force majeure, état de nécessité, légitime défense)",
    "Les infractions contre les personnes (homicide, meurtre, lésions corporelles, menaces, etc.)",
    "Les infractions contre la liberté (séquestration, enlèvement, traite des êtres humains, etc.)",
    "Les infractions contre l'honneur (diffamation, calomnie, injures, etc.)",
    "Les infractions contre la propriété (vol, escroquerie, abus de confiance, extorsion, etc.)",
    "Les infractions contre le patrimoine (destruction, dommage, incendie, etc.)",
    "Les infractions contre l'administration publique (corruption, faux, usage de faux, etc.)",
    "Les infractions contre l'ordre économique (concurrence déloyale, banqueroute, etc.)",
    "Les infractions contre la sécurité publique (infractions à la législation sur les armes, les explosifs, etc.)",
    "Les infractions contre la paix publique (troubles à l'ordre public, etc.)",
    "Les infractions contre la morale publique (prostitution, pornographie, etc.)",
    "Les infractions contre les mœurs (inceste, attentat à la pudeur, etc.)",
    "Les infractions contre la santé publique (infractions à la législation sur les stupéfiants, les aliments, etc.)",
    "Les infractions contre l'environnement (pollution, destruction de la nature, etc.)",
    "Les infractions routières (conduite en état d'ivresse, excès de vitesse, etc.)",
    "Les infractions liées à l'informatique (cybercriminalité, piratage, etc.)",
    "Les infractions liées aux technologies de l'information et de la communication (TIC)",
    "Les infractions liées aux données personnelles",
    "Les infractions liées aux marchés financiers",
    "Les infractions liées à la propriété intellectuelle",
    "Les infractions liées aux assurances",
    "Les infractions liées au travail",
    "Les infractions liées à l'immigration",
    "Les infractions liées à la sécurité sociale",
    "Les infractions liées à la fiscalité",
    "Les infractions liées aux douanes",
    "Les infractions liées à la protection des animaux",
    "Les infractions liées à la protection des consommateurs",
    "Les infractions liées à la protection de l'enfance",
    "Les infractions liées à la protection des données",
    "Les infractions liées à la lutte contre le terrorisme",
    "Les infractions liées à la criminalité organisée",
    "Les infractions liées au blanchiment d'argent",
    "Les infractions liées au trafic de drogue",
    "Les infractions liées au trafic d'armes",
    "Les infractions liées à la traite des êtres humains",
    "Les infractions liées à la corruption",
    "Les infractions liées à la fraude fiscale",
    "Les infractions liées à la fraude sociale",
    "Les infractions liées à la fraude aux assurances",
    "Les infractions liées à la fraude bancaire",
    "Les infractions liées à la fraude informatique",
    "Les infractions liées à la contrefaçon",
    "Les infractions liées au proxénétisme",
    "Les infractions liées à la violence domestique",
    "Les infractions liées à la violence conjugale",
    "Les infractions liées à la violence scolaire",
    "Les infractions liées à la violence sur les personnes âgées",
    "Les infractions liées à la violence sur les personnes handicapées",
    "Les infractions liées au harcèlement",
    "Les infractions liées au cyberharcèlement",
    "Les infractions liées au harcèlement sexuel",
    "Les infractions liées à la discrimination",
    "Les infractions liées au racisme",
    "Les infractions liées à la xénophobie",
    "Les infractions liées à l'antisémitisme",
    "Les infractions liées à l'homophobie",
    "Les infractions liées à l'islamophobie",
    "Les infractions liées à la haine",
    "Les infractions liées à l'incitation à la haine",
    "Les infractions liées à la propagande",
    "Les infractions liées à la négation du génocide",
    "Les infractions liées à la révisionnisme",
    "Les infractions liées à la manipulation",
    "Les infractions liées à la désinformation",
    "Les infractions liées à la manipulation de l'information",
    "Les infractions liées à la diffusion de fausses nouvelles",
    "Les infractions liées à la diffamation en ligne",
    "Les infractions liées à la calomnie en ligne",
    "Les infractions liées à l'injure en ligne",
    "Les infractions liées à la violation de la vie privée",
    "Les infractions liées à la violation du secret professionnel",
    "Les infractions liées à la violation du secret bancaire",
    "Les infractions liées à la violation du secret médical",
    "Les infractions liées à la violation du secret de l'instruction",
    "Les infractions liées à la violation du secret d'enquête",
    "Les infractions liées à la violation du secret des affaires",
    "Les infractions liées à la violation du secret commercial",
    "Les infractions liées à la violation du secret industriel",
    "Les infractions liées à la violation du droit d'auteur",
    "Les infractions liées à la violation du droit des marques",
    "Les infractions liées à la violation du droit des brevets",
    "Les infractions liées à la violation du droit des dessins et modèles",
    "Les infractions liées à la violation du droit des logiciels",
    "Les infractions liées à la violation du droit des bases de données",
    "Les infractions liées à la violation du droit des semences",
    "Les infractions liées à la violation du droit des variétés végétales",
    "Les infractions liées à la violation du droit des obtentions végétales",
    "Les peines (peines privatives de liberté, peines pécuniaires, peines accessoires)",
    "L'exécution des peines",
    "L'amnistie",
    "La prescription",
    "La procédure pénale suisse (enquête, instruction, jugement)",
    "Les voies de recours en matière pénale",
    "Le droit international pénal",
    "Le droit pénal comparé",
    "La prévention de la criminalité",
    "La réinsertion des délinquants",
    "La justice des mineurs",
    "La responsabilité pénale des personnes morales",
    "Le droit pénal économique",
    "Le droit pénal environnemental",
    "Le droit pénal informatique",
    "Le droit pénal médical",
    "Le droit pénal militaire",
    "Le droit pénal international humanitaire",
    "Le droit pénal européen",
    "La coopération internationale en matière pénale",
    "L'extradition",
    "L'assistance judiciaire internationale en matière pénale",
    "Les droits des victimes",
    "La protection des témoins",
    "Le secret de l'instruction",
    "Le secret professionnel",
    "Le droit à un procès équitable",
    "La présomption d'innocence",
    "Le droit au silence",
    "Le droit à un avocat",
    "Le droit à un interprète",
    "Le droit d'accès aux documents",
    "Le droit de recours",
    "Le droit de réparation",
    "Le droit à la réparation du préjudice",
    "Le droit à l'indemnisation",
    "Le droit à la compensation",
    "Le droit à la satisfaction",
    "Le droit à la réparation morale",
    "Le droit à la réparation matérielle",
    "Le droit à la réparation financière",
    "Le droit à la réparation en nature",
    "Le droit à la réparation intégrale",
    "Le droit à la réparation équitable",
    "Le droit à la réparation juste",
    "Le droit à la réparation proportionnelle",
    "Le droit à la réparation effective",
    "Le droit à la réparation rapide",
    "Le droit à la réparation simple",
    "Le droit à la réparation complète",
    "Le droit à la réparation totale",
    "Le droit à la réparation immédiate",
    "Le droit à la réparation sans délai",
    "Le droit à la réparation sans condition",
    "Le droit à la réparation sans restriction",
    "Le droit à la réparation sans exception",
    "Le droit à la réparation sans limitation",
    "Le droit à la réparation sans réserve",
    "Le droit à la réparation sans ambiguïté",
    "Le droit à la réparation sans équivoque",
    "Le droit à la réparation sans hésitation",
    "Le droit à la réparation sans délai supplémentaire",
    "Le droit à la réparation sans délai injustifié",
    "Le droit à la réparation sans délai excessif",
    "Le droit à la réparation sans délai anormal",
    "Le droit à la réparation sans délai déraisonnable",
    "Le droit à la réparation sans délai disproportionné",
    "Le droit à la réparation sans délai abusif",
    "Le droit à la réparation sans délai injuste",
    "Le droit à la réparation sans délai illégitime",
    "Le droit à la réparation sans délai arbitraire",
    "Le droit à la réparation sans délai capricieux",
    "Le droit à la réparation sans délai fantaisiste",
    "Le droit à la réparation sans délai imprévisible",
    "Le droit à la réparation sans délai imprécis",
    "Le droit à la réparation sans délai incertain",
    "Le droit à la réparation sans délai vague",
    "Le droit à la réparation sans délai flou",
    "Le droit à la réparation sans délai obscur",
    "Le droit à la réparation sans délai ambigu",
    "Le droit à la réparation sans délai équivoque",
    "Le droit à la réparation sans délai hésitant",
    "Le droit à la réparation sans délai indéterminé",
    "Le droit à la réparation sans délai indéfini",
    "Le droit à la réparation sans délai imprécisé",
    "Le droit à la réparation sans délai non spécifié",
    "Le droit à la réparation sans délai non déterminé",
    "Le droit à la réparation sans délai non précisé",
    "Le droit à la réparation sans délai non indiqué",
    "Le droit à la réparation sans délai non mentionné",
    "Le droit à la réparation sans délai non communiqué",
    "Le droit à la réparation sans délai non communiqué",
    "Le droit à la réparation sans délai non divulgué",
    "Le droit à la réparation sans délai non révélé",
    "Le droit à la réparation sans délai non exposé",
    "Le droit à la réparation sans délai non exprimé",
    "Le droit à la réparation sans délai non formulé",
    "Le droit à la réparation sans délai non articulé",
    "Le droit à la réparation sans délai non énoncé",
    "Le droit à la réparation sans délai non stipulé",
    "Le droit à la réparation sans délai non prescrit",
    "Le droit à la réparation sans délai non fixé",
    "Le droit à la réparation sans délai non établi",
    "Le droit à la réparation sans délai non défini",
    "Le droit à la réparation sans délai non spécifié",
    "Le droit à la réparation sans délai non déterminé",
    "Le droit à la réparation sans délai non précisé",
    "Le droit à la réparation sans délai non indiqué",
    "Le droit à la réparation sans délai non mentionné",
    "Le droit à la réparation sans délai non communiqué",
    "Le droit à la réparation sans délai non divulgué",
    "Le droit à la réparation sans délai non révélé",
    "Le droit à la réparation sans délai non exposé",
    "Le droit à la réparation sans délai non exprimé",
    "Le droit à la réparation sans délai non formulé",
    "Le droit à la réparation sans délai non articulé",
    "Le droit à la réparation sans délai non énoncé",
    "Le droit à la réparation sans délai non stipulé",
    "Le droit à la réparation sans délai non prescrit",
    "Le droit à la réparation sans délai non fixé",
    "Le droit à la réparation sans délai non établi",
    "Le droit à la réparation sans délai non défini",


]

LEGAL_TOPICS = [
    "Organisation de l'Etat fédéral",
    "Organisation des cantons",
    "Organisation des communes",
    "Principes généraux du droit administratif",
    "Sources du droit administratif",
    "Législation fédérale",
    "Législation cantonale",
    "Législation communale",
    "Jurisprudence administrative",
    "Doctrine administrative",
    "Acte administratif",
    "Décision administrative",
    "Notification administrative",
    "Recours administratif",
    "Recours hiérarchique",
    "Recours gracieux",
    "Recours contentieux",
    "Tribunaux administratifs",
    "Tribunal fédéral",
    "Protection juridictionnelle des droits fondamentaux",
    "Droit de recours",
    "Droit d'être entendu",
    "Principe de proportionnalité",
    "Principe d'égalité",
    "Principe de légalité",
    "Principe de bonne foi",
    "Principe de sécurité juridique",
    "Principe de confiance légitime",
    "Pouvoir réglementaire",
    "Ordonnances",
    "Règlements",
    "Circulaires",
    "Instructions",
    "Autorisation administrative",
    "Concession administrative",
    "Subvention",
    "Aide financière",
    "Contrôle administratif",
    "Surveillance administrative",
    "Inspection administrative",
    "Sanctions administratives",
    "Amendes",
    "Retraits d'autorisation",
    "Suspension d'activité",
    "Droit de la construction",
    "Permis de construire",
    "Autorisation de bâtir",
    "Loi sur l'aménagement du territoire",
    "Loi sur la protection de l'environnement",
    "Droit de l'environnement",
    "Protection de la nature",
    "Protection des eaux",
    "Protection de l'air",
    "Gestion des déchets",
    "Energie",
    "Droit de l'énergie",
    "Energie renouvelable",
    "Transport",
    "Infrastructures de transport",
    "Routes",
    "Chemins de fer",
    "Aviation",
    "Navigation",
    "Droit des transports",
    "Droit de la circulation routière",
    "Sécurité routière",
    "Droit des assurances sociales",
    "AVS",
    "AI",
    "APG",
    "Assurance-chômage",
    "Assurance-maladie",
    "Droit du travail public",
    "Fonction publique",
    "Fonctionnaires",
    "Employés de l'Etat",
    "Droit des marchés publics",
    "Marchés publics",
    "Appels d'offres",
    "Concessions",
    "Contrats de partenariat",
    "Droit des étrangers",
    "Séjour",
    "Immigration",
    "Naturalisation",
    "Expulsion",
    "Droit d'asile",
    "Protection internationale",
    "Droit pénal administratif",
    "Infractions administratives",
    "Procédure pénale administrative",
    "Droit de la santé publique",
    "Hygiène",
    "Prévention",
    "Soins",
    "Hôpitaux",
    "Droit de la sécurité sociale",
    "Protection de la jeunesse",
    "Protection de l'enfance",
    "Protection des mineurs",
    "Droit de l'éducation",
    "Ecoles",
    "Universités",
    "Formation professionnelle",
    "Droit de la culture",
    "Musées",
    "Bibliothèques",
    "Patrimoine culturel",
    "Droit des médias",
    "Presse",
    "Radio",
    "Télévision",
    "Internet",
    "Droit de la concurrence (aspects administratifs)",
    "Droit de la propriété intellectuelle (aspects administratifs)",
    "Droit des communications électroniques",
    "Protection des données (aspects administratifs)",
    "Droit fiscal (aspects administratifs)",
    "Impôts",
    "Taxes",
    "Droit douanier",
    "Droit international public (aspects administratifs)",
    "Traités internationaux",
    "Relations internationales",
    "Coopération internationale",
    "Droit administratif comparé",
    "Droit administratif européen",
    "Droit administratif cantonal (exemples: droit de la construction vaudois, droit de l'environnement genevois)",
    "Droit administratif communal (exemples: règlement communal, police communale)",
    "Planification territoriale",
    "Urbanisme",
    "Aménagement du territoire",
    "Gestion des ressources naturelles",
    "Eau potable",
    "Assainissement",
    "Déchets",
    "Forêts",
    "Agriculture",
    "Protection des animaux",
    "Sécurité publique",
    "Police",
    "Justice",
    "Protection civile",
    "Gestion des crises",
    "Catastrophes naturelles",
    "Sécurité nationale",
    "Défense nationale",
    "Armée",
    "Police fédérale",
    "Service militaire",
    "Service civil",
    "Droit des étrangers (aspects administratifs)",
    "Intégration des étrangers",
    "Politique d'asile",
    "Réfugiés",
    "Demandeurs d'asile",
    "Expulsion des étrangers",
    "Droit des marchés publics (aspects spécifiques)",
    "Concessions de service public",
    "Partenariats public-privé",
    "Contrats de performance",
    "Contrôle des marchés publics",
    "Recours contre les marchés publics",
    "Droit de la commande publique",
    "Droit de la fonction publique (aspects spécifiques)",
    "Statut des fonctionnaires",
    "Conditions de travail des fonctionnaires",
    "Droits et obligations des fonctionnaires",
    "Disciplines des fonctionnaires",
    "Protection des fonctionnaires",
    "Droit des associations (aspects administratifs)",
    "Subventions aux associations",
    "Contrôle des associations",
    "Droit des fondations (aspects administratifs)",
    "Surveillance des fondations",
    "Contrôle des fondations",
    "Droit des régies autonomes",
    "Droit des établissements publics",
    "Droit des entreprises publiques",
    "Droit des services publics",
    "Délégation de service public",
    "Privatisation des services publics",
    "Régulation des services publics",
    "Contrôle des services publics",
    "Droit de l'information administrative",
    "Accès aux documents administratifs",
    "Transparence administrative",
    "Protection des données (aspects administratifs spécifiques)",
    "Protection des données personnelles",
    "Sécurité des données",
    "Cyber sécurité",
    "Droit de la protection des données (aspects administratifs)",
    "Législation sur la protection des données",
    "Autorité de surveillance des données",
    "Recours contre les décisions de l'autorité de surveillance des données",
    "Droit de la surveillance des marchés financiers (aspects administratifs)",
    "Surveillance des banques",
    "Surveillance des assurances",
    "Surveillance des marchés boursiers",
    "Lutte contre le blanchiment d'argent",
    "Lutte contre le financement du terrorisme",
    "Droit de la concurrence (aspects administratifs spécifiques)",
    "Cartels",
    "Abus de position dominante",
    "Aides d'Etat",
    "Contrôle des concentrations",
    "Droit de la propriété intellectuelle (aspects administratifs spécifiques)",
    "Protection des marques",
    "Protection des brevets",
    "Protection du droit d'auteur",
    "Protection des dessins et modèles",
    "Protection des indications géographiques",
    "Droit de la consommation (aspects administratifs)",
    "Protection des consommateurs",
    "Contrôle des prix",
    "Publicité trompeuse",
    "Vente à distance",
    "Droit de la santé (aspects administratifs)",
    "Hôpitaux",
    "Médecins",
    "Pharmacies",
    "Médicaments",
    "Assurance maladie",
    "Droit de l'agriculture (aspects administratifs)",
    "Subventions agricoles",
    "Contrôle des denrées alimentaires",
    "Protection des animaux (aspects administratifs)",
    "Bien-être animal",
    "Protection des végétaux",
    "Protection des forêts",
    "Gestion des eaux",
    "Protection de l'environnement (aspects administratifs)",
    "Pollution",
    "Changement climatique",
    "Biodiversité",
    "Gestion des déchets",
    "Energie nucléaire",
    "Risques naturels",
    "Protection de la population",
    "Sécurité alimentaire",
    "Sécurité sanitaire",
    "Sécurité énergétique",
    "Sécurité de l'information",
    "Sécurité des infrastructures critiques",
    "Gestion des risques",
    "Planification de la sécurité",
    "Gestion des crises",
    "Résilience",
    "Coopération internationale (aspects administratifs)",
    "Aide au développement",
    "Coopération technique",
    "Coopération scientifique",
    "Diplomatie",
    "Consulat",
    "Ambassade",
    "Relations bilatérales",
    "Relations multilatérales",
    "Organisations internationales",
    "Union européenne",
    "Conseil de l'Europe",
    "Nations Unies",
    "OMC",
    "Droit international humanitaire (aspects administratifs)",
    "Droit des réfugiés",
    "Droit des migrations",
    "Droit de la paix",
    "Droit de la guerre",
    "Droit de la sécurité internationale",
    "Droit de la défense",
    "Droit de la sécurité intérieure",
    "Droit de la police",
    "Droit de la justice",
    "Droit pénal (aspects administratifs)",
    "Infractions administratives",
    "Procédure administrative",
    "Sanctions administratives",
    "Recours contre les décisions administratives",
    "Droit administratif suisse comparé",
    "Droit administratif européen",
    "Droit administratif international",
    "Droit constitutionnel (aspects administratifs)",
    "Séparation des pouvoirs",
    "Etat de droit",
    "Démocratie",
    "Droits fondamentaux",
    "Libertés fondamentales",
    "Protection des droits fondamentaux",
    "Contrôle de constitutionnalité",
    "Contrôle de légalité",
    "Contrôle de proportionnalité",
    "Contrôle d'opportunité",
    "Droit administratif et nouvelles technologies",
    "Intelligence artificielle",
    "Big data",
    "Blockchain",
    "Internet des objets",
    "Cyber sécurité",
    "Protection des données",
    "Droit administratif et développement durable",
    "Economie circulaire",
    "Transition énergétique",
    "Adaptation au changement climatique",
    "Biodiversité",
    "Gestion des ressources naturelles",
    "Droit administratif et participation citoyenne",
    "Consultation publique",
    "Participation des citoyens",
    "Transparence administrative",
    "Accès à l'information",
    "Droit administratif et gouvernance",
    "Bonne gouvernance",
    "Ethique publique",
    "Responsabilité publique",
    "Intégrité publique",
    "Transparence publique",
    "Responsabilité sociale des entreprises",
    "Développement durable",
    "Responsabilité environnementale",
    "Responsabilité sociale",
    "Responsabilité économique",
    "Gouvernance d'entreprise",
    "Compliance",
    "Ethique des affaires",
    "Droit administratif et innovation",
    "Régulation de l'innovation",
    "Incubateurs d'entreprises",
    "Start-ups",
    "Economie numérique",
    "Economie collaborative",
    "Economie sociale et solidaire",
    "Droit administratif et digitalisation",
    "Administration numérique",
    "Services publics numériques",
    "E-gouvernement",
    "Transformation numérique",
    "Droit administratif et sécurité",
    "Sécurité intérieure",
    "Sécurité extérieure",
    "Cyber sécurité",
    "Sécurité des infrastructures critiques",
    "Gestion des risques",
    "Protection de la population",
    "Droit administratif et santé",
    "Santé publique",
    "Prévention",
    "Soins de santé",
    "Hôpitaux",
    "Médecins",
    "Pharmacies",
    "Médicaments",
    "Assurance maladie",
    "Droit administratif et éducation",
    "Système éducatif",
    "Ecoles",
    "Universités",
    "Formation professionnelle",
    "Recherche scientifique",
    "Innovation",
    "Droit administratif et culture",
    "Patrimoine culturel",
    "Musées",
    "Bibliothèques",
    "Arts",
    "Spectacles",
    "Médias",
    "Droit administratif et sport",
    "Sport professionnel",
    "Sport amateur",
    "Infrastructures sportives",
    "Gestion des événements sportifs",
    "Droit administratif et tourisme",
    "Tourisme durable",
    "Infrastructures touristiques",
    "Gestion des destinations touristiques",
    "Droit administratif et mobilité",
    "Mobilité durable",
    "Transport public",
    "Transport privé",
    "Infrastructures de transport",
    "Gestion du trafic",
    "Droit administratif et énergie",
    "Transition énergétique",
    "Energie renouvelable",
    "Efficacité énergétique",
    "Sécurité énergétique",
    "Droit administratif et environnement",
    "Protection de l'environnement",
    "Gestion des ressources naturelles",
    "Biodiversité",
    "Changement climatique",
    "Pollution",
    "Déchets",
    "Eau",
    "Air",
    "Sol",
    "Droit administratif et agriculture",
    "Agriculture durable",
    "Production agricole",
    "Commercialisation des produits agricoles",
    "Protection des végétaux",
    "Protection des animaux",
    "Droit administratif et forêt",
    "Gestion forestière",
    "Protection des forêts",
    "Exploitation forestière",
    "Droit administratif et urbanisme",
    "Aménagement du territoire",
    "Urbanisme durable",
    "Planification urbaine",
    "Construction",
    "Habitat",
    "Droit administratif et logement",
    "Politique du logement",
    "Accès au logement",
    "Qualité du logement",
    "Droit administratif et social",
    "Protection sociale",
    "Sécurité sociale",
    "Aide sociale",
    "Insertion sociale",
    "Lutte contre la pauvreté",
    "Droit administratif et économie",
    "Politique économique",
    "Développement économique",
    "Innovation",
    "Compétitivité",
    "Emploi",
    "Droit administratif et finance",
    "Politique financière",
    "Gestion des finances publiques",
    "Dette publique",
    "Investissements publics",
    "Droit administratif et justice",
    "Accès à la justice",
    "Efficacité de la justice",
    "Indépendance de la justice",
    "Droit administratif et sécurité",
    "Sécurité intérieure",
    "Sécurité extérieure",
    "Cyber sécurité",
    "Sécurité des infrastructures critiques",
    "Gestion des risques",
    "Protection de la population",
    "Droit administratif et défense nationale",
    "Défense nationale",
    "Armée",
    "Sécurité nationale",
    "Droit administratif et relations internationales",
    "Coopération internationale",
    "Diplomatie",
    "Relations bilatérales",
    "Relations multilatérales",
    "Organisations internationales",
    "Droit administratif et droit international",
    "Droit international public",
    "Droit international privé",
    "Droit européen",
    "Droit comparé",
    "Droit administratif et technologie",
    "Intelligence artificielle",
    "Big data",
    "Blockchain",
    "Internet des objets",
    "Cyber sécurité",
    "Droit administratif et société",
    "Développement durable",
    "Inclusion sociale",
    "Egalité des chances",
    "Diversité",
    "Droit administratif et gouvernance",
    "Bonne gouvernance",
    "Transparence",
    "Responsabilité",
    "Ethique",
    "Intégrité",
    "Droit administratif et participation citoyenne",
    "Consultation publique",
    "Participation des citoyens",
    "Démocratie participative",
    "Droit administratif et innovation",
    "Régulation de l'innovation",
    "Incubateurs d'entreprises",
    "Start-ups",
    "Economie numérique",
    "Economie collaborative",
    "Economie sociale et solidaire",
    "Droit administratif et digitalisation",
    "Administration numérique",
    "Services publics numériques",
    "E-gouvernement",
    "Transformation numérique",
    "Droit administratif et sécurité",
    "Sécurité intérieure",
    "Sécurité extérieure",
    "Cyber sécurité",
    "Sécurité des infrastructures critiques",
    "Gestion des risques",
    "Protection de la population",
    "Droit administratif et santé",
    "Santé publique",
    "Prévention",
    "Soins de santé",
    "Hôpitaux",
    "Médecins",
    "Pharmacies",
    "Médicaments",
    "Assurance maladie",
    "Droit administratif et éducation",
    "Système éducatif",
    "Ecoles",
    "Universités",
    "Formation professionnelle",
    "Recherche scientifique",
    "Innovation",
    "Droit administratif et culture",
    "Patrimoine culturel",
    "Musées",
    "Bibliothèques",
    "Arts",
    "Spectacles",
    "Médias",
    "Droit administratif et sport",
    "Sport professionnel",
    "Sport amateur",
    "Infrastructures sportives",
    "Gestion des événements sportifs",
    "Droit administratif et tourisme",
    "Tourisme durable",
    "Infrastructures touristiques",
    "Gestion des destinations touristiques",
    "Droit administratif et mobilité",
    "Mobilité durable",
    "Transport public",
    "Transport privé",
    "Infrastructures de transport",
    "Gestion du trafic",
    "Droit administratif et énergie",
    "Transition énergétique",
    "Energie renouvelable",
    "Efficacité énergétique",
    "Sécurité énergétique",
    "Droit administratif et environnement",
    "Protection de l'environnement",
    "Gestion des ressources naturelles",
    "Biodiversité",
    "Changement climatique",
    "Pollution",
    "Déchets",
    "Eau",
    "Air",
    "Sol",
    "Droit administratif et agriculture",
    "Agriculture durable",
    "Production agricole",
    "Commercialisation des produits agricoles",
    "Protection des végétaux",
    "Protection des animaux",
    "Droit administratif et forêt",
    "Gestion forestière",
    "Protection des forêts",
    "Exploitation forestière",
    "Droit administratif et urbanisme",
    "Aménagement du territoire",
    "Urbanisme durable",
    "Planification urbaine",
    "Construction",
    "Habitat",
    "Droit administratif et logement",
    "Politique du logement",
    "Accès au logement",
    "Qualité du logement",
    "Droit administratif et social",
    "Protection sociale",
    "Sécurité sociale",
    "Aide sociale",
    "Insertion sociale",
    "Lutte contre la pauvreté",
    "Droit administratif et économie",
    "Politique économique",
    "Développement économique",
    "Innovation",
    "Compétitivité",
    "Emploi",
    "Droit administratif et finance",
    "Politique financière",
    "Gestion des finances publiques",
    "Dette publique",
    "Investissements publics",
    "Droit administratif et justice",
    "Accès à la justice",
    "Efficacité de la justice",
    "Indépendance de la justice",
    "Droit administratif et sécurité",
    "Sécurité intérieure",
    "Sécurité extérieure",
    "Cyber sécurité",
    "Sécurité des infrastructures critiques",
    "Gestion des risques",
    "Protection de la population",
    "Droit administratif et défense nationale",
    "Défense nationale",
    "Armée",
    "Sécurité nationale",
    "Droit administratif et relations internationales",
    "Coopération internationale",
    "Diplomatie",
    "Relations bilatérales",
    "Relations multilatérales",
    "Organisations internationales",
    "Droit administratif et droit international",
    "Droit international public",
    "Droit international privé",
    "Droit européen",
    "Droit comparé"
]
LEGAL_TOPICS = [
    # "Droit de la santé en général",
    # "Principes fondamentaux du droit de la santé suisse",
    # "Législation fédérale en matière de santé",
    # "Législation cantonale en matière de santé",
    # "Sources du droit de la santé (lois, ordonnances, jurisprudence, doctrine)",
    # "La Constitution fédérale et la santé",
    # "La Loi fédérale sur l'assurance-maladie (LAMal)",
    # "Les assurances-maladie complémentaires",
    # "L'assurance-maladie obligatoire (AMO)",
    # "Les primes d'assurance-maladie",
    # "Le choix du médecin et de l'établissement",
    # "Les prestations assurées par l'AMO",
    # "Les prestations non assurées par l'AMO",
    # "Les recours contre les décisions des assureurs-maladie",
    # "La surveillance des assureurs-maladie",
    # "L'autorité fédérale de surveillance des marchés financiers (FINMA) et la santé",
    # "L'Office fédéral de la santé publique (OFSP)",
    # "Les cantons et la santé",
    # "Les institutions de santé",
    # "Les hôpitaux",
    # "Les cliniques",
    # "Les cabinets médicaux",
    # "Les maisons de soins",
    # "Les EMS (établissements médico-sociaux)",
    # "Les pharmacies",
    # "Le personnel de santé",
    # "Les médecins",
    # "Les infirmiers",
    # "Les physiothérapeutes",
    # "Les ergothérapeutes",
    # "Les logopèdes",
    # "Les assistants médicaux",
    # "Les autres professions de santé",
    # "Le secret professionnel médical",
    # "La responsabilité médicale",
    # "La responsabilité civile des professionnels de santé",
    # "La responsabilité pénale des professionnels de santé",
    # "La faute médicale",
    # "Le consentement éclairé",
    # "L'information du patient",
    # "Le droit du patient",
    # "Le droit à l'information",
    # "Le droit à la confidentialité",
    # "Le droit à la dignité",
    # "Le droit à l'autodétermination",
    # "Le droit de refuser un traitement",
    # "Le droit de choisir son médecin",
    # "Le droit de consulter son dossier médical",
    # "Le droit de recours",
    # "Les directives anticipées",
    # "Le testament biologique",
    # "La procuration pour soins",
    # "La protection des données médicales",
    # "La loi fédérale sur la protection des données (LPD)",
    "Le transfert de données médicales",
    "La sécurité des données médicales",
    "La recherche médicale",
    "L'expérimentation sur l'homme",
    "L'éthique médicale",
    "Les comités d'éthique",
    "Les aspects bioéthiques",
    "Le clonage",
    "Les cellules souches",
    "La génétique",
    "La procréation médicalement assistée (PMA)",
    "La fécondation in vitro (FIV)",
    "Le don d'organes",
    "La transplantation d'organes",
    "Le don de sang",
    "Les soins palliatifs",
    "Les soins de fin de vie",
    "L'euthanasie",
    "Le suicide assisté",
    "La législation sur les stupéfiants",
    "La législation sur l'alcool",
    "La législation sur le tabac",
    "La santé publique",
    "La prévention",
    "La promotion de la santé",
    "La lutte contre les maladies infectieuses",
    "La lutte contre les épidémies",
    "La santé au travail",
    "La sécurité au travail",
    "La médecine du travail",
    "La santé environnementale",
    "La pollution de l'air",
    "La pollution de l'eau",
    "La pollution du sol",
    "Les risques chimiques",
    "Les risques biologiques",
    "Les risques physiques",
    "La protection de la population",
    "Les catastrophes naturelles",
    "Les accidents",
    "Les urgences",
    "Les plans d'urgence",
    "Le système de santé suisse",
    "Le financement du système de santé",
    "L'accès aux soins",
    "L'équité en matière de santé",
    "Les inégalités en matière de santé",
    "Les déterminants sociaux de la santé",
    "La qualité des soins",
    "L'évaluation des soins",
    "L'accréditation des hôpitaux",
    "La gestion des risques",
    "La gestion de la qualité",
    "La formation du personnel de santé",
    "La recherche en santé",
    "L'innovation en santé",
    "La coopération internationale en matière de santé",
    "Le droit international de la santé",
    "Les traités internationaux en matière de santé",
    "Les organisations internationales de santé",
    "L'Organisation mondiale de la santé (OMS)",
    "Le Conseil de l'Europe",
    "L'Union européenne",
    "Le droit comparé en matière de santé",
    "Le droit de la santé en Europe",
    "Le droit de la santé aux États-Unis",
    "Le droit de la santé au Canada",
    "Le droit de la santé en Australie",
    "Le droit de la santé en Nouvelle-Zélande",
    "Le droit de la santé en Afrique",
    "Le droit de la santé en Asie",
    "Le droit de la santé en Amérique latine",
    "Les aspects économiques du droit de la santé",
    "Les aspects sociaux du droit de la santé",
    "Les aspects politiques du droit de la santé",
    "Les aspects éthiques du droit de la santé",
    "Les aspects philosophiques du droit de la santé",
    "La jurisprudence en matière de droit de la santé",
    "La doctrine en matière de droit de la santé",
    "La littérature en matière de droit de la santé",
    "Les revues spécialisées en droit de la santé",
    "Les bases de données juridiques en matière de santé",
    "Les sites web spécialisés en droit de la santé",
    "Les associations professionnelles en matière de santé",
    "Les organisations de patients",
    "Les associations de consommateurs",
    "Les médias et la santé",
    "La communication en matière de santé",
    "L'éducation à la santé",
    "La prévention des maladies chroniques",
    "La gestion des maladies chroniques",
    "Les soins de longue durée",
    "Les soins à domicile",
    "Les aides techniques",
    "L'adaptation du logement",
    "L'intégration sociale des personnes handicapées",
    "La réadaptation",
    "La réinsertion professionnelle",
    "La protection des personnes vulnérables",
    "Les enfants malades",
    "Les personnes âgées",
    "Les personnes handicapées",
    "Les personnes atteintes de maladies mentales",
    "Les personnes atteintes de maladies rares",
    "Les personnes en situation de précarité",
    "Les migrants",
    "Les réfugiés",
    "Les sans-abri",
    "L'accès aux soins pour les populations vulnérables",
    "La lutte contre les discriminations en matière de santé",
    "La promotion de l'équité en matière de santé",
    "La participation des patients à la prise de décision",
    "Le partage des responsabilités en matière de santé",
    "La collaboration interprofessionnelle",
    "La collaboration intersectorielle",
    "La gouvernance du système de santé",
    "La réforme du système de santé",
    "L'avenir du système de santé suisse"
]

LEGAL_TOPICS = [
    "Contrat de travail: formation, validité, nullité",
    "Types de contrats de travail (à durée déterminée, indéterminée, etc.)",
    "Clause de non-concurrence",
    "Clause de confidentialité",
    "Clause de mobilité",
    "Période d'essai",
    "Rémunération: salaire, primes, avantages sociaux",
    "Heures de travail: durée, heures supplémentaires, repos hebdomadaire",
    "Congés: vacances, congés maladie, congés maternité/paternité",
    "Temps partiel",
    "Travail à temps plein",
    "Télétravail",
    "Délégation de personnel",
    "Mise à disposition de personnel",
    "Harcèlement sexuel au travail",
    "Harcèlement moral au travail",
    "Discrimination au travail",
    "Protection contre le licenciement",
    "Licenciement abusif",
    "Licenciement pour faute grave",
    "Licenciement pour motif économique",
    "Procédure de licenciement",
    "Indemnité de licenciement",
    "Préavis",
    "Délai de congé",
    "Résiliation du contrat de travail",
    "Rupture anticipée du contrat de travail",
    "Obligations de l'employeur",
    "Obligations du salarié",
    "Santé et sécurité au travail",
    "Accident du travail",
    "Maladie professionnelle",
    "Assurance-maladie obligatoire",
    "Assurance-accidents",
    "Assurance-chômage",
    "Litiges du travail",
    "Procédure de conciliation",
    "Procédure judiciaire",
    "Tribunal du travail",
    "Rôle de l'inspection du travail",
    "Convention collective de travail (CCT)",
    "Négociation collective",
    "Grève",
    "Lock-out",
    "Conciliation",
    "Arbitrage",
    "Médiation",
    "Droit de grève",
    "Droit de lock-out",
    "Protection des données personnelles au travail",
    "Utilisation des technologies de l'information et de la communication (TIC)",
    "Surveillance au travail",
    "Droit à la déconnexion",
    "Droit à la formation professionnelle",
    "Formation continue",
    "Perfectionnement professionnel",
    "Développement des compétences",
    "Mobilité professionnelle",
    "Gestion de carrière",
    "Recrutement",
    "Sélection du personnel",
    "Intégration des nouveaux employés",
    "Évaluation du personnel",
    "Gestion des performances",
    "Rémunération variable",
    "Primes de rendement",
    "Participation aux bénéfices",
    "Stock-options",
    "Avantages en nature",
    "Véhicule de société",
    "Assurance complémentaire",
    "Plan d'épargne-retraite",
    "Régime de retraite",
    "Prévoyance professionnelle",
    "Caisse de pension",
    "Fondation de prévoyance",
    "Assurance-vie",
    "Assurance-invalidité",
    "Assurance-décès",
    "Protection juridique",
    "Droit d'auteur et propriété intellectuelle au travail",
    "Inventions faites par les employés",
    "Secret professionnel",
    "Confidentialité des données",
    "Protection des données sensibles",
    "Droit à l'information",
    "Droit à la consultation",
    "Droit à la participation",
    "Comité d'entreprise",
    "Délégués du personnel",
    "Syndicats",
    "Négociation sociale",
    "Dialogue social",
    "Relations professionnelles",
    "Gestion des conflits",
    "Résolution des conflits",
    "Médiation des conflits",
    "Arbitrage des conflits",
    "Procédure de recours",
    "Recours contre une décision de l'employeur",
    "Recours contre une décision de la justice",
    "Exécution des jugements",
    "Saisie des salaires",
    "Droit international du travail",
    "Travailleurs détachés",
    "Mobilité internationale",
    "Travail transfrontalier",
    "Convention collective de travail internationale",
    "Droit de l'Union européenne en matière de droit du travail",
    "Harmonisation du droit du travail",
    "Législation sur le travail des jeunes",
    "Travail des mineurs",
    "Protection des travailleurs vulnérables",
    "Travailleurs migrants",
    "Travailleurs saisonniers",
    "Travailleurs temporaires",
    "Travail indépendant",
    "Travail à domicile",
    "Travail à distance",
    "Travail flexible",
    "Travail intermittent",
    "Travail occasionnel",
    "Travail au noir",
    "Travail illégal",
    "Travail clandestin",
    "Exploitation du travail",
    "Travail forcé",
    "Esclavage moderne",
    "Trafic d'êtres humains",
    "Protection des lanceurs d'alerte",
    "Whistleblowing",
    "Dénonciation d'irrégularités",
    "Protection contre les représailles",
    "Droit à la vie privée au travail",
    "Droit à l'image",
    "Droit à l'honneur",
    "Droit à la réputation",
    "Droit à la dignité",
    "Droit à la considération",
    "Droit à la sécurité",
    "Droit à la santé",
    "Droit à la formation",
    "Droit à l'évolution professionnelle",
    "Droit à la promotion",
    "Droit à la mobilité interne",
    "Droit à la participation aux décisions",
    "Droit à la consultation des représentants du personnel",
    "Droit à la négociation collective",
    "Droit à la grève",
    "Droit de lock-out",
    "Droit à la protection contre le licenciement",
    "Droit à l'indemnisation en cas de licenciement",
    "Droit à la réintégration",
    "Droit à la réparation du préjudice",
    "Droit à la réparation morale",
    "Droit à la réparation matérielle",
    "Droit à la réparation intégrale",
    "Droit à la réparation équitable",
    "Droit à la réparation juste",
    "Droit à la réparation proportionnelle",
    "Droit à la réparation effective",
    "Droit à la réparation rapide",
    "Droit à la réparation simple",
    "Droit à la réparation complète",
    "Droit à la réparation totale",
    "Droit à la réparation immédiate",
    "Droit à la réparation sans délai",
    "Droit à la réparation sans condition",
    "Droit à la réparation sans restriction",
    "Droit à la réparation sans exception",
    "Droit à la réparation sans limitation",
    "Droit à la réparation sans réserve",
    "Droit à la réparation sans ambiguïté",
    "Droit à la réparation sans équivoque",
    "Droit à la réparation sans hésitation",
    "Droit à la réparation sans délai supplémentaire",
    "Droit à la réparation sans retard injustifié",
    "Droit à la réparation sans complication",
    "Droit à la réparation sans difficulté",
    "Droit à la réparation sans obstacle",
    "Droit à la réparation sans entrave",
    "Droit à la réparation sans empêchement",
    "Droit à la réparation sans impediment",
    "Droit à la réparation sans impedimentum",
    "Droit à la réparation sans impedimentum juris",
    "Droit à la réparation sans impedimentum facti",
    "Droit à la réparation sans impedimentum juris et facti"
]

LEGAL_TOPICS = [
    # "Conditions du divorce en Suisse",
    # "Divorce par consentement mutuel",
    # "Divorce pour faute",
    # "Divorce pour rupture de la communauté de vie",
    # "Divorce après séparation de corps",
    # "Délai de réflexion avant le divorce",
    # "Procédure de divorce devant le tribunal",
    # "Rôle du juge dans la procédure de divorce",
    # "Représentation juridique lors d'un divorce",
    # "Assistance juridique en matière de divorce",
    # "Frais de procédure de divorce",
    # "Allocation compensatoire",
    # "Calcul de l'allocation compensatoire",
    # "Critères de détermination de l'allocation compensatoire",
    # "Durée de l'allocation compensatoire",
    # "Révision de l'allocation compensatoire",
    # "Pension alimentaire pour enfants",
    # "Calcul de la pension alimentaire pour enfants",
    # "Critères de détermination de la pension alimentaire pour enfants",
    # "Durée de la pension alimentaire pour enfants",
    # "Révision de la pension alimentaire pour enfants",
    # "Pension alimentaire pour conjoint",
    # "Calcul de la pension alimentaire pour conjoint",
    # "Critères de détermination de la pension alimentaire pour conjoint",
    # "Durée de la pension alimentaire pour conjoint",
    # "Révision de la pension alimentaire pour conjoint",
    # "Partage des biens matrimoniaux",
    # "Régime matrimonial légal (communauté de biens)",
    # "Régime matrimonial conventionnel (séparation de biens)",
    # "Partage des dettes matrimoniales",
    # "Evaluation des biens matrimoniaux",
    # "Liquidation du régime matrimonial",
    # "Attribution du logement familial",
    # "Droit de visite et d'hébergement des enfants",
    # "Détermination du droit de visite et d'hébergement",
    # "Modification du droit de visite et d'hébergement",
    # "Autorité parentale conjointe",
    # "Autorité parentale exclusive",
    # "Entente parentale",
    # "Médiation familiale",
    # "Conciliation familiale",
    # "Rôle du médiateur familial",
    # "Avantages de la médiation familiale",
    # "Procédure de médiation familiale",
    # "Accord amiable dans le cadre d'un divorce",
    # "Homologation de l'accord amiable",
    # "Force exécutoire de l'accord amiable",
    # "Divorce international",
    "Jurisdiction compétente en cas de divorce international",
    "Application de la loi applicable en cas de divorce international",
    "Reconnaissance et exécution d'un jugement de divorce étranger",
    "Convention de La Haye sur les aspects civils de l'enlèvement international d'enfants",
    "Protection des enfants dans le cadre d'un divorce international",
    "Divorce et droit des successions",
    "Divorce et droit fiscal",
    "Divorce et droit des assurances",
    "Divorce et droit du travail",
    "Impact du divorce sur les assurances sociales",
    "Divorce et conséquences sur les contrats d'assurance-vie",
    "Divorce et conséquences sur les contrats de prévoyance professionnelle",
    "Divorce et conséquences sur les contrats de location",
    "Divorce et conséquences sur les contrats de crédit",
    "Divorce et conséquences sur les contrats d'hypothèque",
    "Divorce et conséquences sur les contrats de travail",
    "Divorce et conséquences sur les droits de propriété intellectuelle",
    "Divorce et conséquences sur les droits d'auteur",
    "Divorce et conséquences sur les droits de marque",
    "Divorce et conséquences sur les droits de brevet",
    "Divorce et conséquences sur les droits de succession",
    "Divorce et conséquences sur les droits de donation",
    "Divorce et conséquences sur les droits de legs",
    "Divorce et conséquences sur les droits de fiducie",
    "Divorce et conséquences sur les droits de fondation",
    "Divorce et conséquences sur les droits d'association",
    "Divorce et conséquences sur les droits de société",
    "Divorce et conséquences sur les droits de partenariat enregistré",
    "Divorce et conséquences sur les droits de cohabitation",
    "Divorce et conséquences sur les droits de famille",
    "Divorce et conséquences sur les droits des enfants",
    "Divorce et conséquences sur les droits des parents",
    "Divorce et conséquences sur les droits des grands-parents",
    "Divorce et conséquences sur les droits des tuteurs",
    "Divorce et conséquences sur les droits des curateurs",
    "Divorce et conséquences sur les droits des administrateurs",
    "Divorce et conséquences sur les droits des représentants légaux",
    "Divorce et conséquences sur les droits des mandataires",
    "Divorce et conséquences sur les droits des avocats",
    "Divorce et conséquences sur les droits des notaires",
    "Divorce et conséquences sur les droits des huissiers",
    "Divorce et conséquences sur les droits des experts",
    "Divorce et conséquences sur les droits des témoins",
    "Divorce et conséquences sur les droits des parties",
    "Divorce et conséquences sur les droits des tiers",
    "Divorce et conséquences sur les droits patrimoniaux",
    "Divorce et conséquences sur les droits extrapatrimoniaux",
    "Divorce et conséquences sur les droits moraux",
    "Divorce et conséquences sur les droits personnels",
    "Divorce et conséquences sur les droits sociaux",
    "Divorce et conséquences sur les droits économiques",
    "Divorce et conséquences sur les droits politiques",
    "Divorce et conséquences sur les droits culturels",
    "Divorce et conséquences sur les droits environnementaux",
    "Divorce et conséquences sur les droits humains",
    "Divorce et conséquences sur les droits fondamentaux",
    "Divorce et conséquences sur les libertés fondamentales",
    "Divorce et conséquences sur les droits de la personnalité",
    "Divorce et conséquences sur les droits de la vie privée",
    "Divorce et conséquences sur les droits à l'image",
    "Divorce et conséquences sur les droits à l'honneur",
    "Divorce et conséquences sur les droits à la réputation",
    "Divorce et conséquences sur les droits à la dignité",
    "Divorce et conséquences sur les droits à l'intégrité physique",
    "Divorce et conséquences sur les droits à la santé",
    "Divorce et conséquences sur les droits à l'éducation",
    "Divorce et conséquences sur les droits à la formation",
    "Divorce et conséquences sur les droits à l'emploi",
    "Divorce et conséquences sur les droits à la sécurité sociale",
    "Divorce et conséquences sur les droits à la retraite",
    "Divorce et conséquences sur les droits à l'assistance sociale",
    "Divorce et conséquences sur les droits à l'aide sociale",
    "Divorce et conséquences sur les droits à l'hébergement",
    "Divorce et conséquences sur les droits à la logement",
    "Divorce et conséquences sur les droits à la santé mentale",
    "Divorce et conséquences sur les droits à la protection sociale",
    "Divorce et conséquences sur les droits à la protection des enfants",
    "Divorce et conséquences sur les droits à la protection des femmes",
    "Divorce et conséquences sur les droits à la protection des hommes",
    "Divorce et conséquences sur les droits à la protection des personnes vulnérables",
    "Aspects psychologiques du divorce",
    "Impact du divorce sur les enfants",
    "Soutien psychologique pour les enfants",
    "Soutien psychologique pour les parents",
    "Conséquences à long terme du divorce sur les enfants",
    "Conséquences à long terme du divorce sur les parents",
    "Prévention des conflits dans le cadre du divorce",
    "Gestion des conflits dans le cadre du divorce",
    "Résolution des conflits dans le cadre du divorce",
    "Négociation dans le cadre du divorce",
    "Arbitrage dans le cadre du divorce",
    "Médiation dans le cadre du divorce",
    "Litige dans le cadre du divorce",
    "Procédure judiciaire dans le cadre du divorce",
    "Appel dans le cadre du divorce",
    "Pourvoi en cassation dans le cadre du divorce",
    "Exécution des décisions de divorce",
    "Recours contre les décisions de divorce",
    "Modification des décisions de divorce",
    "Révision des décisions de divorce",
    "Annulation des décisions de divorce",
    "Nullité des décisions de divorce",
    "Jurisprudence suisse en matière de divorce",
    "Doctrine suisse en matière de divorce",
    "Législation suisse en matière de divorce",
    "Conventions internationales en matière de divorce",
    "Droit comparé en matière de divorce",
    "Perspectives d'avenir en matière de divorce en Suisse"
]

LEGAL_TOPICS = [
    # "Droit des contrats commerciaux",
    # "Négociation commerciale et formation des contrats",
    # "Conditions générales de vente",
    # "Contrats internationaux (droit commercial international)",
    # "Incoterms",
    # "Lettre de crédit",
    # "Crédits documentaires",
    # "Garantie bancaire",
    # "Cautionnement",
    # "Avances sur facture",
    # "Factoring",
    # "Affacturage",
    # "Forfaitisation",
    # "Leasing",
    # "Location-gérance",
    # "Franchise",
    # "Concession",
    # "Licence",
    # "Joint-venture",
    # "Fusion-acquisition",
    # "Droit des sociétés commerciales",
    # "Sociétés anonymes (SA)",
    # "Sociétés à responsabilité limitée (SARL)",
    # "Sociétés en commandite par actions (SCA)",
    # "Sociétés simples (SNC)",
    # "Sociétés en nom collectif (SNC)",
    # "Coopératives",
    # "Fondations de droit privé",
    # "Associations",
    # "Création de sociétés",
    # "Transformation de sociétés",
    # "Fusion de sociétés",
    # "Scission de sociétés",
    # "Dissolution de sociétés",
    # "Liquidation de sociétés",
    # "Gouvernance d'entreprise",
    # "Conseil d'administration",
    # "Direction générale",
    # "Contrôle interne",
    # "Compliance",
    # "Droit boursier",
    # "Introduction en bourse (IPO)",
    # "Offre publique d'achat (OPA)",
    # "Marché réglementé",
    # "Marché hors cote",
    # "Prospectus",
    # "Information des investisseurs",
    # "Droit des valeurs mobilières",
    # "Actions",
    # "Obligations",
    # "Titres de créance",
    # "Droit des titres",
    # "Droit de la concurrence",
    # "Cartels",
    # "Abus de position dominante",
    # "Contrôle des concentrations",
    # "Aides d'État",
    # "Pratique anticoncurrentielle",
    # "Droit de la propriété intellectuelle",
    # "Marques",
    # "Brevets",
    # "Dessins et modèles",
    # "Copyright",
    # "Droit d'auteur",
    # "Secrets commerciaux",
    # "Licences",
    # "Franchise",
    # "Droit de la responsabilité civile",
    # "Responsabilité contractuelle",
    # "Responsabilité extracontractuelle",
    # "Responsabilité des dirigeants",
    # "Responsabilité des administrateurs",
    # "Responsabilité des mandataires",
    # "Droit des contrats de distribution",
    # "Contrat d'agence",
    # "Contrat de concession",
    # "Contrat de distribution sélective",
    # "Contrat de franchise",
    # "Droit des contrats de travail",
    # "Contrat de travail",
    # "Licenciement",
    # "Résiliation du contrat de travail",
    # "Droit social",
    # "Négociation collective",
    # "Grèves",
    # "Lock-out",
    # "Droit des faillites",
    # "Procédure de faillite",
    # "Liquidation judiciaire",
    # "Concordat préventif",
    # "Réorganisation judiciaire",
    # "Droit des sûretés",
    # "Gage",
    # "Hypothèque",
    # "Privilège",
    # "Nantissement",
    # "Cautionnement",
    # "Droit bancaire",
    # "Crédit",
    # "Débit",
    # "Chèques",
    # "Lettres de change",
    # "Billets à ordre",
    # "Droit des assurances",
    # "Assurance responsabilité civile",
    # "Assurance dommages",
    # "Assurance vie",
    # "Assurance maladie",
    # "Assurance accidents",
    # "Droit fiscal (aspects commerciaux)",
    # "TVA",
    # "Impôt sur les sociétés",
    # "Impôt sur le revenu",
    # "Droit international privé (droit commercial)",
    # "Arbitrage commercial international",
    # "Médiation commerciale",
    # "Conciliation commerciale",
    # "Droit des contrats électroniques",
    # "Signature électronique",
    # "Commerce électronique",
    # "Vente en ligne",
    # "Protection des données (aspects commerciaux)",
    # "RGPD",
    #"Législation sur la protection des données",
    "Droit de la consommation (aspects commerciaux)",
    "Droit des transports",
    "Transport routier",
    "Transport ferroviaire",
    "Transport maritime",
    "Transport aérien",
    "Droit de la logistique",
    "Chaîne d'approvisionnement",
    "Gestion de la supply chain",
    "Droit de la construction",
    "Marchés publics",
    "Contrats de construction",
    "Responsabilité des constructeurs",
    "Droit immobilier (aspects commerciaux)",
    "Investissement immobilier",
    "Gestion immobilière",
    "Location commerciale",
    "Bail commercial",
    "Droit des énergies renouvelables",
    "Énergie solaire",
    "Énergie éolienne",
    "Énergie hydraulique",
    "Droit de l'environnement (aspects commerciaux)",
    "Responsabilité environnementale",
    "Gestion des déchets",
    "Droit des technologies de l'information et de la communication (TIC)",
    "Contrat de développement logiciel",
    "Contrat de maintenance informatique",
    "Hébergement de données",
    "Sécurité informatique",
    "Cybercriminalité",
    "Droit des nouvelles technologies",
    "Intelligence artificielle",
    "Blockchain",
    "Cryptomonnaies",
    "NFT",
    "Métavers",
    "Droit du numérique",
    "Protection des données personnelles",
    "Droit des médias",
    "Publicité",
    "Presse",
    "Audiovisuel",
    "Droit du sport",
    "Contrats sportifs",
    "Droit du sponsoring",
    "Droit des jeux vidéo",
    "Droit de la mode",
    "Protection des marques de mode",
    "Droit de la gastronomie",
    "Droit de l'hôtellerie",
    "Droit du tourisme",
    "Droit de l'art",
    "Marché de l'art",
    "Protection des œuvres d'art",
    "Droit des assurances (aspects commerciaux)",
    "Réassurance",
    "Gestion des risques",
    "Compliance",
    "Gouvernance d'entreprise",
    "Responsabilité sociale des entreprises (RSE)",
    "Développement durable",
    "Ethique des affaires",
    "Droit pénal des affaires",
    "Blanchiment d'argent",
    "Corruption",
    "Fraude",
    "Délit d'initié",
    "Manipulation de marché",
    "Droit des sociétés commerciales (SA, SARL, Sàrl, GmbH, AG)",
    "Constitution de sociétés commerciales",
    "Modifications statutaires des sociétés commerciales",
    "Dissolution et liquidation des sociétés commerciales",
    "Responsabilité des organes des sociétés commerciales",
    "Conflits d'intérêts dans les sociétés commerciales",
    "Protection des actionnaires/associés minoritaires",
    "Contrôle des sociétés commerciales",
    "Fusions et acquisitions d'entreprises",
    "Droit des valeurs mobilières",
    "Émission d'actions et d'obligations",
    "Marché boursier suisse",
    "Offres publiques d'achat (OPA)",
    "Droit des marchés financiers",
    "Contrôle des opérations sur titres",
    "Lutte contre le blanchiment d'argent",
    "Financement des entreprises",
    "Crédit bancaire",
    "Droit des sûretés commerciales (gage, nantissement, privilège)",
    "Droit des contrats commerciaux",
    "Formation des contrats commerciaux",
    "Interprétation des contrats commerciaux",
    "Exécution des contrats commerciaux",
    "Inexécution des contrats commerciaux",
    "Responsabilité contractuelle en droit commercial",
    "Clause de confidentialité",
    "Clause pénale",
    "Clause compromissoire",
    "Clause de réserve de propriété",
    "Vente commerciale",
    "Achat et vente de marchandises",
    "Vente à tempérament",
    "Vente avec réserve de propriété",
    "Location-gérance",
    "Franchise",
    "Concession",
    "Distribution",
    "Agence commerciale",
    "Mandat commercial",
    "Commission",
    "Courtage",
    "Transport de marchandises",
    "Assurance transport",
    "Assurance responsabilité civile professionnelle",
    "Assurance crédit",
    "Assurance caution",
    "Droit de la concurrence",
    "Ententes restrictives de concurrence",
    "Abus de position dominante",
    "Contrôle des concentrations",
    "Publicité trompeuse",
    "Pratique commerciale déloyale",
    "Protection des consommateurs",
    "Droit de la propriété intellectuelle (marques, brevets, dessins et modèles)",
    "Droit d'auteur en droit commercial",
    "Licences et franchises",
    "Secret commercial",
    "Know-how",
    "Droit des contrats de travail (aspects commerciaux)",
    "Négociation collective",
    "Grèves et lock-out",
    "Droit du travail et droit commercial",
    "Droit des faillites et des poursuites commerciales",
    "Procédure de faillite",
    "Concordat préventif",
    "Liquidation judiciaire",
    "Réorganisation d'entreprise",
    "Droit des restructurations",
    "Droit international commercial",
    "Contrats internationaux",
    "Arbitrage commercial international",
    "Convention de Vienne sur les contrats de vente internationale de marchandises",
    "Incoterms",
    "Droit des sociétés transnationales",
    "Droit fiscal des entreprises",
    "Impôt sur les sociétés",
    "Taxe sur la valeur ajoutée (TVA)",
    "Impôt sur le revenu des personnes physiques (entreprises individuelles)",
    "Droit des assurances commerciales",
    "Droit bancaire",
    "Droit des titres de paiement",
    "Lettre de change",
    "Billet à ordre",
    "Chèque",
    "Droit des paiements électroniques",
    "Droit de la protection des données (aspects commerciaux)",
    "RGPD et droit suisse",
    "Cybercriminalité en droit commercial",
    "Commerce électronique",
    "Contrats électroniques",
    "Signature électronique",
    "Vente en ligne",
    "Marketing digital",
    "Protection des données personnelles en ligne",
    "Droit de la concurrence déloyale",
    "Parasitisme",
    "Dénigrement",
    "Détournement de clientèle",
    "Droit des contrats de distribution sélective",
    "Droit des contrats de licence",
    "Droit des contrats de franchise",
    "Droit des contrats d'agence",
    "Droit des contrats de commission",
    "Droit des contrats de courtage",
    "Droit des contrats de transport",
    "Droit des contrats d'assurance",
    "Droit des contrats de leasing",
    "Droit des contrats de factoring",
    "Droit des contrats de forfaiting",
    "Droit des contrats de crédit-bail",
    "Droit des contrats de location-gérance",
    "Droit des contrats de partenariat",
    "Droit des contrats de joint-venture",
    "Droit des contrats de consortium",
    "Droit des contrats de coentreprise",
    "Droit des contrats de collaboration",
    "Droit des contrats de cession de créances",
    "Droit des contrats de nantissement",
    "Droit des contrats de gage",
    "Droit des contrats de cautionnement",
    "Droit des contrats de garantie",
    "Droit des contrats de sûreté",
    "Droit des contrats de fiducie",
    "Droit des contrats de trust",
    "Droit des contrats de donation",
    "Droit des contrats de legs",
    "Droit des contrats de succession",
    "Droit des contrats de mariage",
    "Droit des contrats de divorce",
    "Droit des contrats de séparation",
    "Droit des contrats de famille",
    "Droit des contrats de location",
    "Droit des contrats de bail",
    "Droit des contrats de construction",
    "Droit des contrats d'ingénierie",
    "Droit des contrats de services",
    "Droit des contrats d'abonnement",
    "Droit des contrats de maintenance",
    "Droit des contrats de réparation",
    "Droit des contrats de fourniture",
    "Droit des contrats de prestation de services",
    "Droit des contrats de travaux",
    "Droit des contrats d'entreprise",
    "Droit des contrats de sous-traitance",
    "Droit des contrats de partenariat public-privé",
    "Droit des contrats de concession",
    "Droit des contrats de délégation de service public"
]


# Exemples de sujets à chercher dans les jurisprudences

ESCROQUERIE

PAR MÉTIER

GESTION DÉLOYALE

GESTION FAUTIVE

PARTIE CIVILE

DOMMAGE

DOMMAGES-INTÉRÊTS

CRÉANCE

RESPONSABILITÉ CONTRACTUELLE

RESPONSABILITÉ DÉLICTUELLE

RESPONSABILITÉ RESTREINTE{DROIT PÉNAL}

RESPONSABILITÉ{DROIT PÉNAL}

AGGRAVATION DE LA PEINE

ATTÉNUATION DE LA PEINE

SURSIS À L'EXÉCUTION DE LA PEINE

SURSIS PARTIEL À L'EXÉCUTION DE LA PEINE

HONORAIRES

AVOCAT

COMPLICITÉ

FRAIS JUDICIAIRES

DÉPENS

EXPERTISE PSYCHIATRIQUE

AFFECTION PSYCHIQUE

MALADIE MENTALE

NOTAIRE

INTENTION

DROIT D'ÊTRE ENTENDU

ADMINISTRATION DES PREUVES

# Exemples d'articles à chercher dans les jurisprudences

41 CO
146 al. 1 CP
146 al. 2 CP
158 ch. 1 al. 1 CP
158 ch. 1 al. 3 CP
165 ch. 1 CP
19 al. 2 CP
25 CP
42 CP
43 CP
44 al. 1 CP
47 CP
48 let. a ch. 4 CP
70 al. 1 CP
71 al. 1 CP
29 al. 1 Cst.
123 CPP (CH)
126 CPP (CH)
389 CPP (CH)
429 al. 1 let. a CPP (CH)
433 CPP (CH)
</td>

# Questions juridiques

taxes communales d'alimentation en eau et d'assainissement imposées à un propriétaire d'immeubles.

règles de motivation du recours de droit administratif 

critères d'évaluation des examens du notariat

règles applicables en matière de conflit d'intérêts dans le cadre d'une curatelle


# Mass pdf visual processing:

The idea is to process pdf as images via gpt-4o-mini and to extract their content in markdown format to keep the basic structure of the document and generate usage translations

# Démarches juridiques en suisse
### Droit pénal

#### État civil
- Déclaration de naissance : [Office de l'état civil]
- Déclaration de décès : [Office de l'état civil]
- Mariage civil : [Office de l'état civil]
- Partenariat enregistré (union civile) : [Office de l'état civil]
- Divorce : [Tribunal de première instance]
- Modification de nom : [Office de l'état civil]

#### Droit des personnes
- Changement de nom ou de prénom : [Office de l'état civil]
- Déclaration d'absence : [Tribunal de première instance]
- Protection des majeurs (curatelle) : [Tribunal de protection de l'adulte et de l'enfant, dans certains cantons, cela peut être l'Autorité de protection de l'adulte et de l'enfant (APAE)]

#### Droit de la famille
- Adoption : [Tribunal de protection de l'adulte et de l'enfant]
- Reconnaissance de paternité : [Office de l'état civil]
- Tutelle et curatelle : [Tribunal de protection de l'adulte et de l'enfant]

#### Successions
- Testament : [Notaire, le testament olographe peut être rédigé sans notaire]
- Pacte successoral : [Notaire]
- Acceptation ou renonciation à une succession : [Tribunal de première instance, dans certains cantons, cela peut se faire auprès de l'autorité compétente en matière de successions]

#### Enquête et poursuite
- Dépôt de plainte pénale : [Police ou Ministère public]
- Audition en tant que témoin ou victime : [Police ou Ministère public]
- Dénonciation anonyme : [Police ou Ministère public]

#### Procédures pénales
- Comparution devant le tribunal de police : [Tribunal de police]
- Comparution devant le tribunal pénal : [Tribunal pénal]
- Recours contre une décision de classement : [Ministère public,  le recours se fait auprès de l'autorité de recours compétente, qui peut varier selon les cantons]

#### Défense et assistance judiciaire
- Demande d'assistance judiciaire : [Tribunal de première instance]
- Nomination d'un avocat d'office : [Tribunal de première instance]
- Contestation d'une décision de refus d'assistance judiciaire : [Tribunal de première instance]

#### Exécution des peines
- Demande de libération conditionnelle : [Service pénitentiaire ou Tribunal d'application des peines, dans certains cantons, c'est le juge d'application des peines qui est compétent.]
- Demande de sursis : [Tribunal d'application des peines]
- Demande de révision de peine : [Tribunal de première instance]

#### Mesures de protection
- Demande d'ordonnance de protection (interdiction de contact, éloignement) : [Tribunal de protection de l'adulte et de l'enfant]
- Plainte pour violence domestique : [Police ou Ministère public]
- Plainte pour harcèlement : [Police ou Ministère public]

#### Infractions spécifiques
- Plainte pour cybercriminalité : [Police ou Ministère public]
- Plainte pour escroquerie : [Police ou Ministère public]
- Plainte pour abus de confiance : [Police ou Ministère public]

#### Réparation et compensation
- Demande de réparation du dommage : [Tribunal de première instance]
- Demande d'indemnisation pour détention injustifiée : [Tribunal de première instance]
- Demande de réparation pour erreur judiciaire : [Tribunal de première instance]

#### Procédures de recours et appels
- Appel contre un jugement pénal : [Cour d'appel, cela peut être la Cour d'appel ou le Tribunal cantonal selon les cantons]
- Recours en cassation : [Tribunal fédéral]

#### Mesures pénales alternatives
- Mesures éducatives : [Tribunal des mineurs]
- Travail d'intérêt général : [Tribunal de première instance]

#### Réhabilitation et effacement
- Demande de réhabilitation : [Tribunal de première instance]
- Effacement du casier judiciaire : [Office fédéral de la justice]

#### Coopération internationale
- Extradition : [Office fédéral de la justice]
- Entraide judiciaire internationale : [Office fédéral de la justice]

### Droit administratif

#### Permis et autorisations
- Demande de permis de séjour : [Service cantonal des migrations]
- Demande de permis de travail : [Service cantonal des migrations]
- Demande de permis de construire : [Service cantonal de l'aménagement du territoire, Dans certains cas, cela peut être la commune plutôt que le canton]
- Demande d'autorisation pour manifestation publique : [Municipalité ou préfecture]

#### Contestations administratives
- Recours contre une décision administrative : [Tribunal administratif cantonal]
- Demande de réexamen d'une décision administrative : [Autorité ayant rendu la décision]
- Recours auprès du Tribunal administratif fédéral : [Tribunal administratif fédéral]

#### Naturalisation et citoyenneté
- Demande de naturalisation ordinaire : [Service cantonal des naturalisations]
- Demande de naturalisation facilitée : [Service cantonal des naturalisations, c'est le Secrétariat d'État aux migrations (SEM) qui est compétent au niveau fédéral.]
- Recours contre une décision de refus de naturalisation : [Tribunal administratif cantonal]

#### Droits sociaux
- Demande de prestations de l'AI (assurance invalidité) : [Office cantonal de l'assurance-invalidité]
- Demande de prestations complémentaires : [Service cantonal des prestations sociales]
- Contestation d'une décision de l'assurance chômage : [Tribunal administratif cantonal]

#### Santé et sécurité publique
- Demande de subvention pour l'assurance maladie : [Service cantonal de l'assurance maladie]
- Contestation d'une décision sanitaire : [Tribunal administratif cantonal, les recours peuvent aussi être adressés au Tribunal fédéral dans certains cas]
- Plainte pour insalubrité ou nuisances : [Service cantonal de l'environnement]

#### Droit de l'environnement et de l'urbanisme
- Demande d'autorisation environnementale : [Service cantonal de l'environnement]
- Recours contre une décision relative à l'environnement : [Tribunal administratif cantonal]
- Contestation de projets d'aménagement du territoire : [Tribunal administratif cantonal]

#### Éducation et formation
- Recours contre une décision scolaire (exclusion, redoublement) : [Tribunal administratif cantonal]
- Demande de bourse d'études : [Service cantonal des bourses]
- Plainte pour non-respect des droits des étudiants : [Service cantonal de l'éducation]

#### Transport et mobilité
- Demande de permis de conduire : [Service cantonal des automobiles et de la navigation]
- Contestation d'une amende de circulation : [Tribunal administratif cantonal]
- Recours contre une décision de retrait de permis : [Tribunal administratif cantonal]



#### Litiges administratifs spécifiques
- Droit des assurances sociales : [Tribunal administratif cantonal]
- Droit des étrangers et intégration : [Tribunal administratif cantonal]
- Droit de la construction et aménagement du territoire : [Tribunal administratif cantonal]

#### Procédures spécifiques
- Médiation administrative : [Service cantonal de médiation]
- Procédure de conciliation : [Autorité de conciliation compétente]

#### Surveillance et contrôle administratif
- Contrôle de légalité : [Tribunal administratif cantonal]
- Surveillance des marchés publics : [Tribunal administratif cantonal]

#### Droits fondamentaux et libertés publiques
- Protection des données personnelles : [Préposé fédéral à la protection des données et à la transparence]
- Liberté d'information : [Service cantonal de l'information et de la transparence]

#### Gestion des situations d'urgence
- Mesures sanitaires : [Tribunal administratif cantonal]
- Planification de la protection civile : [Tribunal administratif cantonal, Cette compétence relève généralement des autorités cantonales ou communales plutôt que du Tribunal administratif cantonal.]

https://github.com/OfficeDev/Office-Add-in-samples

# Particularités suisses

En Suisse, certaines assurances sont obligatoires, comme l'assurance maladie de base (LAMal) et l'assurance responsabilité civile pour les véhicules à moteur. D'autres sont fortement recommandées, comme l'assurance ménage et responsabilité civile privée.

Il est également important de noter que le système d'assurance sociale suisse (AVS, AI, APG) offre une couverture de base pour la retraite, l'invalidité et la perte de gain, que les assurances privées peuvent compléter.

Enfin, la Suisse a un système de surveillance des assurances très développé, avec l'Autorité fédérale de surveillance des marchés financiers (FINMA) qui veille à la protection des assurés et à la stabilité du système financier.


# Problèmes juridiques que l'on peut rencontrer en Suisse :

## 1. Droit de la famille

- Divorce et séparation
- Garde des enfants et pension alimentaire
- Adoption et filiation

## 2. Droit du travail

- Licenciement abusif
- Harcèlement au travail
- Conditions de travail et salaires

## 3. Droit pénal

- Vols et cambriolages
- Infractions liées aux drogues
- Violences domestiques

## 4. Droit des contrats

- Litiges commerciaux
- Non-respect des contrats de vente
- Problèmes de location immobilière

## 5. Droit des étrangers

- Permis de séjour et de travail
- Demandes d'asile
- Expulsions

## 6. Droit de la consommation

- Litiges liés à la consommation de biens et services
- Publicité mensongère
- Garantie des produits

## 7. Droit administratif

- Contestations de décisions administratives
- Problèmes liés à l'urbanisme et à la construction
- Questions fiscales

## 8. Droit de la propriété intellectuelle

- Violations de droits d'auteur
- Litiges de brevets et marques

---


# Notes

For vision tasks (e.g. using claude 3 haiku) it is **crucial** to orient the photos of documents correctly, otherwise the model starts to make stuff up, even at temp=0

# Multilangual embedding model

https://deepinfra.com/BAAI/bge-m3?version=babcf60cae0a1f438d7ade582983d4ba462303c2

"
BAAI/bge-m3
BGE-M3 is a versatile text embedding model that supports multi-functionality, multi-linguality, and multi-granularity, allowing it to perform dense retrieval, multi-vector retrieval, and sparse retrieval in over 100 languages and with input sizes up to 8192 tokens. The model can be used in a retrieval pipeline with hybrid retrieval and re-ranking to achieve higher accuracy and stronger generalization capabilities. BGE-M3 has shown state-of-the-art performance on several benchmarks, including MKQA, MLDR, and NarritiveQA, and can be used as a drop-in replacement for other embedding models like DPR and BGE-v1.5"

Run locally:

```python


from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel('BAAI/bge-m3')

embeddings=[model.encode(content)['dense_vecs'].tolist()]



```

# swiss-legal-applications

Useful resources regarding legal applications.

https://github.com/HazyResearch/legalbench/

https://aclanthology.org/2021.nllp-1.3.pdf

https://arxiv.org/pdf/2309.12269v4


https://elsevier-ssrn-document-store-prod.s3.amazonaws.com/23/03/18/ssrn_id4392741_code627779.pdf?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJIMEYCIQDXpwTjpl7pBk9i7jQV%2FdC3u0rTwZWMiz4x4FoYbrB8VgIhAN7X7ct02wFXUSWLiUjF51pOptlOsW49JhEfeTOko7jxKscFCNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMMzA4NDc1MzAxMjU3IgwwZ5%2BrFY%2FwMQiR%2FLwqmwVOsKquiexldCKenyp%2BP4v6OyFpxaWPttZkbu0acL6ZIvFEHTHOiCTirEWIBZl1IMvRaOMxeV6MsHATT1QR9ttDf1GvBYlOh44yRqhGPipIoo8sGboVxxnmtbaYegU0XRFV2FNSphmZ7AU32Lgy526wdYQjPEEPdjHLdjRk9EEc324yFxsEo4OyBq2JenT2DNLksGA3xPhvi2fv3wWELpLxBM8lxOUhq1hQO0fprZlCpaGMeyYqPdpQjMQpjyPpvF2%2BVEbnXGO4vj7AzNh%2FMAPv4JpveZV3dzMo5i7%2BTVZ7AwdPLOrSz7Jq7gJX%2FV0sK8jL4lLcn%2FYJ1kseSas6w%2BDYkjii8S8FooNqE1m4kkvFpvX%2FKpT6KC6xExmnLP7wlX3kVZLalqLLaLgtlO3ZqujjtIqvfuQNmolAqtZjTtxfoKUJRTMvPPTO5fkby%2BWWclnvcaHhCfE%2FKBue6XGCfAzUZfwypIQoXRltwosGjP91BO%2F%2F9OgqKlYjM1bteN%2Bc%2Fv5Ntj%2ByrYgS4JO3qA3j3cpfpScCiYgq80crNRGESwG2ZzhbUqbcmEF%2B0s6bVP8paZ4pkyfIN3VdufS4dMGnDMmszqy5Wm8X55wQs7jcQ8ZOrkhZsMZq0IOmGLjFwjx1sQ%2Fev99swyOPX00%2FkMDym1D0bAScoSOMMAovC8954DVT4k5FhmBqln33cr7RmHy0ztCnmsTMtZFlbkHnaGcR6LCXX01LDEEnumAvVmaPB1QrP%2FzzH%2BqybVibUd%2Bn798JvhAYLieg827NAWhkQvbBRrIfTtZfthVeZindLRKCI0xKFD5QnDk%2F0MUCJHulOQDTcNWzXWD%2FkNsXpB%2ByzQgQrj%2FAmMQPYiZzua6sNgvTEuWpazK0g9MKyiMvpX2CMNTI8bMGOrABwtO0H1bZpD5fZn3toAcZkkC4qAzF5CRcxbY%2FJkhnzyeU9Bf28tdAfbVz2zHiNq0ubHm91fsn00O%2Br1iRHHRZsDeDAK44xSVEkrUO2z84%2Fzg63bBVBR59C7pXfKGaHYdnx9owwYIjH0UYEhPEHRsoUlMYaJrUtKCuK0tho3XlM9B8%2FTlON4EGs9vEomo8hpS1OkcbBA6KTI6ZRpCSR79Iotbo1U3FtluKhy22XN2s4xE%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240626T195321Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAUPUUPRWEXRIMIMVJ%2F20240626%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=efe29b6ebbfffb79e75c8e6fc341d17b806865d8c099fdac060380d7d55bcb2a

## laws.json

Contains all the federal laws. fileUrl.value contains the link for the xml version of each law.
The uuid has been generated by us, just to give a unique identifier to each of them. It has no connection with other identification methods.

## Websites

[bger.ch](https://www.bger.ch/)

- Build queries and call via CURL

  https://fedlex.data.admin.ch/en-CH/sparql

- Nice structure with unique, ascending number (just leave the /2024 at the end no matter what). The earliest we got working is 30000

  https://droitpourlapratique.ch/decision/90584/2024
  
  All the content is within ```<div id="print_main">```

  https://droitpourlapratique.ch/decision/90584/2024
  
---
## AI tools

### Langchain script

Extract the xml articles (also referenced as "article"  from a legal point of view) from a local xml file and embeds them in a chroma database.


/!\ Splits the articles that are too big in the middle, with no precautions /!\

Requires the user to press enter to launch the embedding (in vscode this opens up a pop up on top)

```python

import xml.etree.ElementTree as ET
import tiktoken
import random
import matplotlib.pyplot as plt
import os
import getpass
from langchain_core.documents.base import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = "<key here or just a environment variable>"

def chroma_db_from_xml_file(xml_file, chroma_dir_name, metadata, add_to_existing=False):
    MAX_T = 8192

    def extract_articles():
        tree = ET.parse(xml_file)
        root = tree.getroot()
        articles = []
        
        def find_articles(element):
            if "article" in element.tag:
                articles.append(ET.tostring(element, encoding='unicode'))
            for child in element:
                find_articles(child)
        
        find_articles(root)
        return articles


    def split_if_necessary(string_arr):
        enc = tiktoken.get_encoding("cl100k_base")
        new_string_arr = []
        for e in string_arr:
            if len(enc.encode(e)) > MAX_T:
                mid = len(e) // 2
                a, b = e[:mid], e[mid:]
                new_string_arr.append(a)
                new_string_arr.append(b)
            else:
                new_string_arr.append(e)
        print(len(string_arr), len(new_string_arr))
        
        rerun_algo = False
        for s in new_string_arr:
            if len(enc.encode(e)) > MAX_T:
                rerun_algo = True
        
        if rerun_algo:
            return split_if_necessary(new_string_arr)
        
        return new_string_arr

    def get_token_counts(string_array):
        token_counts = []
        enc = tiktoken.get_encoding("cl100k_base")
        for string in string_array:
            t = len(enc.encode(string))
            if t > MAX_T:
                print(t)
            token_counts.append(t)

        return token_counts
    def display_token_count_chart(string_array):
        token_counts = get_token_counts(string_array)

        plt.figure(figsize=(10, 30))
        plt.bar(range(len(string_array)), token_counts)
        plt.xlabel('String Index')
        plt.ylabel('Token Count')
        plt.title('Token Count Distribution')
        
        # Add a horizontal red line at 8192
        plt.axhline(y=MAX_T, color='red', linestyle='-', linewidth=1)
        
        plt.show()

    articles = extract_articles()
    s_a = split_if_necessary(articles)
    display_token_count_chart(s_a)
    COST_PER_1M_TOKEN = 0.13
    n_tokens = sum(get_token_counts(s_a))
    input(f"N TOKENS {n_tokens}\nPRICE USD {COST_PER_1M_TOKEN*(n_tokens/1000000)}")
    
    documents = []
    for l in s_a:
        doc = Document(page_content = l)
        doc.metadata=metadata
        documents.append(doc)

    if(add_to_existing):
        db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory=chroma_dir_name)
        db.add_documents(documents)
        return db
    
    return Chroma.from_documents(documents, OpenAIEmbeddings(), persist_directory=chroma_dir_name)
```

Somehow hard to find via google, so here it is:
[Document class documentation](https://api.python.langchain.com/en/latest/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document)


---

# Attorney lookup New York

https://arsent.ch/s/attorney_lookup_new_york.csv

---

# Prompt library:

Vous êtes un expert en droit suisse. Vous vous exprimez comme un juriste.
Vous devez justifier ce paragraphe:
La gestion déloyale est une infraction intentionnelle, ce qui signifie que l'auteur doit avoir agi en connaissance de cause et en voulant les conséquences de ses actes. Le dol éventuel, c'est-à-dire l'acceptation du risque de causer un dommage, suffit pour caractériser l'intention, mais il doit être prouvé.

A partir de la jurisprudence que je vous donne, justifiez de manière succinte le paragraphe et citez sans reformulez les passages correspondants dans l'arrêt que je vous donne.

Structurez votre réponse dans ce format:

# Justification

<courte justification>

# Extraits de l'arrêt concernant cet aspect

< liste avec des bullets points de citations de passages sans reformulation>



### Created and maintained by [Liechti Consulting](https://liechticonsulting.com) &nbsp; :switzerland:

Need AI-powered solutions? sacha@liechticonsulting.com :rocket:

---
