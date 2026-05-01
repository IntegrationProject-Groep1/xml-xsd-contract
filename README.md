<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a7ea4,50:0b1f2a,100:6264a7&height=220&section=header&text=XML%2FXSD%20Contract%20Hub&fontSize=52&fontAlignY=38&fontColor=ffffff&desc=Source%20of%20Truth%20%E2%80%A2%20Integration%20Project%20Groep%201&descAlignY=62&descSize=18&animation=fadeIn" alt="XML/XSD Contract Hub banner" />

</div>

<p align="center">
  <a href="XML_XSD_Contract_v2.3_Centralized%201.md"><img alt="Contract" src="https://img.shields.io/badge/Contract-v2.3-0a7ea4?style=for-the-badge&logo=files&logoColor=white&labelColor=0b1f2a"></a>
  <a href="XML_XSD_Contract_v2.3_Centralized%201.md"><img alt="Source of Truth" src="https://img.shields.io/badge/Source%20of%20Truth-MD%20%E2%86%92%20XML%2FXSD-2f855a?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=0b1f2a"></a>
  <a href="instructions.md"><img alt="Governance" src="https://img.shields.io/badge/Governance-Maintainers%20Only-c53030?style=for-the-badge&logo=shield&logoColor=white&labelColor=0b1f2a"></a>
  <a href="#kernbestanden"><img alt="Taal" src="https://img.shields.io/badge/Taal-Nederlands-5b21b6?style=for-the-badge&logo=googletranslate&logoColor=white&labelColor=0b1f2a"></a>
</p>

<p align="center">
  <a href="https://github.com/IntegrationProject-Groep1/xml-xsd-contract/actions"><img alt="Build" src="https://img.shields.io/badge/Build-passing-2f855a?style=flat-square&logo=githubactions&logoColor=white&labelColor=0b1f2a"></a>
  <a href="changelog.md"><img alt="Version" src="https://img.shields.io/badge/Contract%20Version-v2.3-0a7ea4?style=flat-square&logo=semanticversioning&logoColor=white&labelColor=0b1f2a"></a>
  <a href="https://github.com/IntegrationProject-Groep1/xml-xsd-contract/actions/workflows/teams-notify.yml"><img alt="Teams Notify" src="https://img.shields.io/badge/Teams%20Notify-Actief-6264a7?style=flat-square&logo=microsoftteams&logoColor=white&labelColor=0b1f2a"></a>
  <a href="#maintainers"><img alt="Maintainers" src="https://img.shields.io/badge/Maintainers-Active-2f855a?style=flat-square&logo=githubsponsors&logoColor=white&labelColor=0b1f2a"></a>
  <a href="changelog.md"><img alt="Changelog" src="https://img.shields.io/badge/Changelog-Bijgewerkt-f59e0b?style=flat-square&logo=keepachangelog&logoColor=white&labelColor=0b1f2a"></a>
  <a href="https://github.com/IntegrationProject-Groep1/xml-xsd-contract/actions/workflows/enforce-maintainers.yml"><img alt="Enforcement" src="https://img.shields.io/badge/Enforcement-Actief-c53030?style=flat-square&logo=githubactions&logoColor=white&labelColor=0b1f2a"></a>
</p>

> **Wat is dit?**
> Deze repository is de **centrale Source of Truth** voor alle XML/XSD berichtafspraken binnen het Integration Project. Elke koppeling — CRM, Kassa, Frontend, Planning, Facturatie en meer — is gebonden aan de contractdefinities die hier beheerd worden. Afwijkingen worden hier gemeld, besproken en vastgelegd.

---

## Inhoudsopgave

**🧑‍💻 Voor developers (start hier)**
1. [Quickstart voor Developers](#quickstart-voor-developers)
2. [Probleem of vraag? Zo meld je het](#probleem-of-vraag-zo-meld-je-het)
3. [Berichtenstromen tussen teams](#berichtenstromen-tussen-teams)
4. [Hoe het XML/XSD contract in elkaar zit](#hoe-het-xmlxsd-contract-in-elkaar-zit)
5. [Kernbestanden](#kernbestanden)

**🛠️ Voor maintainers & beheer**

6. [Doelgroep en rechten](#doelgroep-en-rechten)
7. [Voor Maintainers: Wijzigingen Doorvoeren](#voor-maintainers-wijzigingen-doorvoeren)
8. [Governance & Regels](#governance--regels)
9. [Teams Notificaties (Automatisch)](#teams-notificaties-automatisch)
10. [Secrets Configuratie](#secrets-configuratie)
11. [Samenwerkingsafspraken](#samenwerkingsafspraken)

---

## 🧑‍💻 Voor Developers

## Quickstart voor Developers

> **Werk je aan CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing of Identity?** Dan ben je een **developer** van een integrerend team. Deze sectie is jouw startpunt.

| Wat wil je doen? | Ga naar |
|---|---|
| 📖 Het officiële XML/XSD contract lezen | [`XML_XSD_Contract_v2.3_Centralized 1.md`](XML_XSD_Contract_v2.3_Centralized%201.md) |
| 🐞 Een fout, onduidelijkheid of regressie melden | [Probleem of vraag? Zo meld je het](#probleem-of-vraag-zo-meld-je-het) |
| 🔁 Begrijpen welke berichten jouw team raken | [Berichtenstromen tussen teams](#berichtenstromen-tussen-teams) |
| 🧱 Zien hoe een bericht is opgebouwd | [Hoe het XML/XSD contract in elkaar zit](#hoe-het-xmlxsd-contract-in-elkaar-zit) |
| 📋 Het issue-template stap voor stap volgen | [`issue-guide.md`](issue-guide.md) |
| 📜 De recentste wijzigingen bekijken | [`changelog.md`](changelog.md) |

### Drie regels die altijd gelden voor developers

1. **Wijzig nooit zelf** een contractbestand of open een Pull Request — dit wordt technisch geblokkeerd door [`enforce-maintainers.yml`](.github/workflows/enforce-maintainers.yml).
2. **Open altijd een GitHub Issue** met het `[XML/XSD]` template wanneer je iets ziet dat niet klopt.
3. **Plaats daarna een bericht in Teams** in het kanaal **XML - XSD Channel** met de issue-URL, zodat de maintainers het direct zien.

---

## Probleem of vraag? Zo meld je het

> Je mag het contract **niet** zelf wijzigen of een Pull Request openen. Dit wordt technisch geblokkeerd.
> Volg onderstaand twee-stappen-proces wanneer je een fout, onduidelijkheid of gewenste wijziging tegenkomt.

```mermaid
flowchart LR
    A["❗ Probleem<br/>ontdekt"] --> B["📌 Stap 1<br/>Open GitHub Issue<br/>met [XML/XSD] template"]
    B --> C["💬 Stap 2<br/>Stuur Teams-bericht<br/>in XML - XSD Channel<br/>met issue-URL"]
    C --> D["🔧 Maintainer<br/>beoordeelt issue"]
    D --> E["✅ Fix + Changelog<br/>+ Push naar main"]
    E --> F["📣 Automatische<br/>Teams Notificatie"]

    style A fill:#c53030,color:#fff,stroke:#7f1d1d
    style B fill:#1e40af,color:#fff,stroke:#1e3a8a
    style C fill:#6264a7,color:#fff,stroke:#4a4880
    style D fill:#0b1f2a,color:#fff,stroke:#0a7ea4
    style E fill:#2f855a,color:#fff,stroke:#1a5738
    style F fill:#6264a7,color:#fff,stroke:#4a4880
```

### Wanneer open je een issue?

Open een issue als je een van deze situaties tegenkomt:

- XML komt niet overeen met het centrale contract.
- XSD validatie faalt.
- Message type, header of body wijkt af van de afgesproken structuur.
- Onzekerheid over interpretatie van een contractregel.
- Regressie na een wijziging.
- Een nieuwe flow of berichtveld dat in het contract zou moeten staan.

### Stap 1 — Open een formeel GitHub Issue

1. Ga naar **[Issues → New Issue](https://github.com/IntegrationProject-Groep1/xml-xsd-contract/issues/new/choose)**.
2. Kies het `[XML/XSD]` template.
3. Vul het template volledig in (zie [`issue-guide.md`](issue-guide.md) voor details):
   - Samenvatting van het probleem
   - Verwacht vs. huidig gedrag
   - Betrokken contractsectie (bv. `XML_XSD_Contract_v2.3 - sectie 11.1`)
   - Reproductiestappen
   - Voorbeeld XML/XSD of foutmelding
   - Impact op teams/flows
4. Label het issue correct: `xml`, `xsd`, `bug`, `contract`.
5. Submit het issue en **kopieer de issue-URL**.

### Stap 2 — Stuur direct daarna een bericht in Teams

Ga naar het Microsoft Teams kanaal: **XML - XSD Channel**

Stuur een bericht met:
- De issue-URL uit stap 1
- Een korte omschrijving van het probleem
- Welke flow/team er impact van ondervindt

> Dit zorgt ervoor dat maintainers **direct** op de hoogte zijn en de urgentie kunnen inschatten. Enkel een issue zonder Teams-bericht kan over het hoofd worden gezien.

### Tips voor sterke issues

- Voeg concrete voorbeelden toe (XML-snippets, foutmeldingen, log-lijnen).
- Vermeld exact het berichttype en de flow.
- Verwijs naar de juiste contractsectie.
- Vermijd vage omschrijvingen zoals *"werkt niet"* zonder context.

---

## Berichtenstromen tussen teams

> Deze diagrammen geven jou een **overzicht in één oogopslag** van hoe RabbitMQ berichten tussen teams reizen, en welke berichten jouw team raken.

### Interactieve Netwerk-Map

Deze kaart wordt automatisch gegenereerd op basis van de contractdefinities en toont alle live berichtstromen tussen teams.

<!-- NETWORK_MAP_START -->

<div align='center'>

![Integration Map](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=10B981&center=true&vCenter=true&width=600&lines=INTEGRATION+NETWORK+MAP;REAL-TIME+MESSAGE+FLOWS;CONTRACT+V2.3+SOURCE+OF+TRUTH;HUB-AND-SPOKE+ARCHITECTURE)

</div>

---

#### 🧭 System Integration Key
| Integration Flow | Architectural Path Description |
| :--- | :--- |
| ![](https://img.shields.io/badge/INBOUND-10b981?style=for-the-badge) | Functioneel bericht **NAAR** de CRM (Hub Entrance) |
| ![](https://img.shields.io/badge/OUTBOUND-3b82f6?style=for-the-badge) | Functioneel bericht **VANAF** de CRM (Hub Exit) |
| ![](https://img.shields.io/badge/PEER--TO--PEER-6366f1?style=for-the-badge) | Direct bericht **TUSSEN TEAMS** (Bypass Hub) |
| ![](https://img.shields.io/badge/SYSTEM-94a3b8?style=for-the-badge) | **HEARTBEATS** / Status updates naar Monitoring |

---

```mermaid
flowchart LR
    %% Style Definitions
    classDef core fill:#0b1f2a,color:#fff,stroke:#0a7ea4,stroke-width:4px;
    classDef ops fill:#1e3a8a,color:#fff,stroke:#0a7ea4,stroke-width:2px;
    classDef support fill:#2d3748,color:#fff,stroke:#718096,stroke-width:1px;

    subgraph CORE ["🔑 Core & Routing"]
        CRM(["CRM"])
        class CRM core;
        Identity(["Identity"])
        class Identity core;
        Requestor(["Requestor"])
        class Requestor core;
    end

    subgraph OPS ["⚙️ Operational Teams"]
        Facturatie(["Facturatie"])
        class Facturatie ops;
        Frontend(["Frontend"])
        class Frontend ops;
        Kassa(["Kassa"])
        class Kassa ops;
        Planning(["Planning"])
        class Planning ops;
    end

    subgraph SUPPORT ["📢 Support & Alerts"]
        Alle_teams(["Alle teams"])
        class Alle_teams support;
        Heartbeat(["Heartbeat"])
        class Heartbeat support;
        Mailing(["Mailing"])
        class Mailing support;
        Monitoring(["Monitoring"])
        class Monitoring support;
    end

    %% Functional Flows
    Alle_teams -. "heartbeat" .-> Monitoring
    CRM -- "invoice_request<br/>new_registration" --> Facturatie
    CRM -- "payment_registered" --> Frontend
    CRM -- "RPC request" --> Identity
    CRM -- "cancel_registration<br/>new_registration<br/>profile_update" --> Kassa
    CRM -- "send_mailing" --> Mailing
    CRM -. "heartbeat" .-> Monitoring
    CRM -- "cancel_registration" --> Planning
    Facturatie -- "invoice_created_notification<br/>invoice_status" --> CRM
    Facturatie -- "send_mailing" --> Mailing
    Facturatie -. "heartbeat" .-> Monitoring
    Frontend -- "new_registration<br/>user_checkin<br/>user_created<br/>user_deleted<br/>user_updated" --> CRM
    Frontend -- "RPC request" --> Identity
    Frontend -. "heartbeat" .-> Monitoring
    Frontend -- "calendar_invite<br/>session_create_request<br/>session_delete_request<br/>session_update_request" --> Planning
    Heartbeat -. "heartbeat" .-> Monitoring
    Identity -- "user_event" --> CRM
    Identity -- "identity_response" --> Requestor
    Kassa -- "payment_registered" --> CRM
    Kassa -- "payment_status<br/>wallet_balance_update" --> Frontend
    Kassa -. "heartbeat" .-> Monitoring
    Mailing -- "mailing_status" --> CRM
    Mailing -. "heartbeat" .-> Monitoring
    Monitoring -- "system_alert" --> Mailing
    Planning -- "session_created<br/>session_deleted<br/>session_updated" --> CRM
    Planning -- "Token Registration<br/>calendar_invite_confirmed<br/>session_created<br/>session_updated" --> Frontend
    Planning -. "heartbeat" .-> Monitoring

    %% Edge Styles
    linkStyle 0 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 1 stroke:#3b82f6,stroke-width:2px;
    linkStyle 2 stroke:#3b82f6,stroke-width:2px;
    linkStyle 3 stroke:#3b82f6,stroke-width:2px;
    linkStyle 4 stroke:#3b82f6,stroke-width:2px;
    linkStyle 5 stroke:#3b82f6,stroke-width:2px;
    linkStyle 6 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 7 stroke:#3b82f6,stroke-width:2px;
    linkStyle 8 stroke:#10b981,stroke-width:2px;
    linkStyle 9 stroke:#6366f1,stroke-width:2px;
    linkStyle 10 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 11 stroke:#10b981,stroke-width:2px;
    linkStyle 12 stroke:#6366f1,stroke-width:2px;
    linkStyle 13 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 14 stroke:#6366f1,stroke-width:2px;
    linkStyle 15 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 16 stroke:#10b981,stroke-width:2px;
    linkStyle 17 stroke:#6366f1,stroke-width:2px;
    linkStyle 18 stroke:#10b981,stroke-width:2px;
    linkStyle 19 stroke:#6366f1,stroke-width:2px;
    linkStyle 20 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 21 stroke:#10b981,stroke-width:2px;
    linkStyle 22 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
    linkStyle 23 stroke:#6366f1,stroke-width:2px;
    linkStyle 24 stroke:#10b981,stroke-width:2px;
    linkStyle 25 stroke:#6366f1,stroke-width:2px;
    linkStyle 26 stroke:#94a3b8,stroke-width:1px,stroke-dasharray:5;
```

<!-- NETWORK_MAP_END -->

Elke koppeling **implementeert** de XML/XSD structuur zoals gedefinieerd in het centrale MD-bestand. Wijzigingen gaan altijd via de maintainers en worden bijgehouden in `changelog.md`. Teams ontvangen automatisch een melding via Microsoft Teams bij elke update.

---

## Hoe het XML/XSD contract in elkaar zit

> Korte conceptuele blik op hoe een bericht is opgebouwd en hoe het zich verhoudt tot het centrale MD-document.

```mermaid
flowchart TB
    classDef truth   fill:#0b1f2a,color:#fff,stroke:#0a7ea4,stroke-width:3px;
    classDef msg     fill:#1e3a8a,color:#fff,stroke:#1e40af,stroke-width:2px;
    classDef field   fill:#2f855a,color:#fff,stroke:#1a5738,stroke-width:2px;
    classDef teamcl  fill:#6264a7,color:#fff,stroke:#4a4880,stroke-width:2px;

    SOT["📄 XML_XSD_Contract_v2.3<br/>(Source of Truth)"]:::truth

    subgraph BERICHT["📨 Eén XML bericht"]
        direction TB
        ENV["Envelope<br/>Message"]:::msg
        HDR["Header<br/>type · timestamp · sender · receiver"]:::field
        BODY["Body<br/>payload velden per message_type"]:::field
        ENV --> HDR
        ENV --> BODY
    end

    subgraph CONSUMERS["🧩 Implementaties per team"]
        direction LR
        CRM2["CRM"]:::teamcl
        KAS2["Kassa"]:::teamcl
        FE2["Frontend"]:::teamcl
        FAC2["Facturatie"]:::teamcl
        PL2["Planning"]:::teamcl
        ID2["Identity"]:::teamcl
        MAIL2["Mailing"]:::teamcl
        MON2["Monitoring"]:::teamcl
    end

    SOT --> BERICHT
    BERICHT --> CONSUMERS

    SOT -. "wijziging gemeld via issue" .-> ISSUE["GitHub Issue<br/>(door dev-team)"]:::field
    ISSUE -. "fix door maintainer" .-> SOT
```

**Belangrijk om te onthouden als developer:**

- Het centrale MD-bestand is de **enige** functionele waarheid — niet de implementaties van een individueel team.
- Header-velden zijn **identiek** in elk berichttype; alleen de body verschilt per `message_type`.
- Wijk je af van de structuur? **Dan is jouw implementatie fout, niet het contract.** Open een issue als je denkt dat het contract zelf moet wijzigen.

---

## Kernbestanden

| Bestand | Doel |
|---|---|
| [`XML_XSD_Contract_v2.3_Centralized 1.md`](XML_XSD_Contract_v2.3_Centralized%201.md) | Officieel, gecentraliseerd XML/XSD contract — de functionele waarheid |
| [`xml-expert.md`](xml-expert.md) | Agent-definitie en strikte werkmodus voor contractwijzigingen |
| [`instructions.md`](instructions.md) | Bindende werkinstructies voor alle bijdragers (mens en AI) |
| [`issue-guide.md`](issue-guide.md) | Stap-voor-stap handleiding voor het openen van XML/XSD issues |
| [`changelog.md`](changelog.md) | Volledige historiek van wijzigingen met datum, tijd en auteur |

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0a7ea4,100:6264a7&height=4&section=header" alt="divider" />
</div>

## 🛠️ Voor Maintainers & Beheer

> De volgende secties zijn relevant voor **maintainers, projectmanagers en mensen die governance bewaken**. Als developer hoef je dit niet te lezen om je werk te kunnen doen.

---

## Doelgroep en rechten

| Rol | Teams | Rechten |
|---|---|---|
| **Maintainer** | @tombomeke-ehb + aangewezen developer | Lezen · Wijzigen · Pushen naar `main` · PR mergen |
| **Niet-Admin User (developer)** | CRM · Kassa · Frontend · Planning · Facturatie · Monitoring · Mailing · Identity | Lezen · Issues openen · Teams-bericht sturen |

> ⚠️ **Niet-Admin Users mogen GEEN directe wijzigingen of Pull Requests doen aan de contractbestanden.**
> Dit is technisch afgedwongen via [`.github/workflows/enforce-maintainers.yml`](.github/workflows/enforce-maintainers.yml).
> Bij problemen of vragen volg je het proces onder [Probleem of vraag? Zo meld je het](#probleem-of-vraag-zo-meld-je-het).

### Source of Truth Architectuur

De contractdefinities in deze repository bepalen de structuur voor alle integrerende systemen:

```mermaid
flowchart TB
    subgraph HUB["🗂️  XML/XSD Contract Hub  —  deze repository"]
        direction TB
        CONTRACT["📄 XML_XSD_Contract_v2.3<br/>─────────────────<br/>Source of Truth"]
        INSTRUCTIONS["📋 instructions.md<br/>─────────────────<br/>Governance regels"]
        XMLEXPERT["🤖 xml-expert.md<br/>─────────────────<br/>Agent / AI kader"]
        CHANGELOG["📝 changelog.md<br/>─────────────────<br/>Wijzigingshistorie"]
        ISSUEGUIDE["🔖 issue-guide.md<br/>─────────────────<br/>Meldingsproces"]
    end

    subgraph INTTEAMS["⚙️  Integrerende Teams"]
        direction LR
        CRM["CRM"]
        KASSA["Kassa"]
        FRONTEND["Frontend"]
        PLANNING["Planning"]
        FACTURATIE["Facturatie"]
        OTHER["Monitoring · Mailing · Identity"]
    end

    CONTRACT  -->|"contractdefinities"| INTTEAMS
    INTTEAMS  -->|"📌 GitHub Issue"| ISSUEGUIDE
    INTTEAMS  -->|"💬 Teams: XML - XSD Channel"| HUB
```

---

<a name="maintainers"></a>

## Voor Maintainers: Wijzigingen Doorvoeren

**Actieve Maintainers:** @tombomeke-ehb · aangewezen developer

### Workflow bij elke wijziging

```mermaid
flowchart LR
    A["📖 Lees<br/>xml-expert.md<br/>+ instructions.md"] --> B["✏️ Wijziging<br/>uitvoeren<br/>(binnen scope)"]
    B --> C["📝 Changelog<br/>entry toevoegen<br/>vóór commit"]
    C --> D["💾 Commit & Push<br/>naar main"]
    D --> E["📣 Teams Notificatie<br/>verstuurd<br/>automatisch"]

    style A fill:#0b1f2a,color:#fff,stroke:#0a7ea4
    style B fill:#1e40af,color:#fff,stroke:#1e3a8a
    style C fill:#f59e0b,color:#0b1f2a,stroke:#b45309
    style D fill:#2f855a,color:#fff,stroke:#1a5738
    style E fill:#6264a7,color:#fff,stroke:#4a4880
```

1. Lees [`xml-expert.md`](xml-expert.md) en [`instructions.md`](instructions.md) — verplicht bij elke sessie.
2. Werk in kleine, begrijpelijke stappen; pas alleen aan wat binnen scope valt.
3. Vermijd brede bulk-wijzigingen zonder duidelijke motivatie.
4. Noteer impact op teams, flows en message types.
5. Schrijf duidelijke commit- en PR-beschrijvingen.
6. Update [`changelog.md`](changelog.md) **vóór** de commit.

### Enforcement

Toegang wordt gecontroleerd via:

- [`.github/workflows/enforce-maintainers.yml`](.github/workflows/enforce-maintainers.yml) — blokkeert contractwijzigingen van niet-maintainers.
- Secret `ALLOWED_CONTRACT_EDITORS` — komma-gescheiden lijst van toegestane GitHub usernames.

> Zonder deze secret faalt de enforcement workflow bewust.

---

## Governance & Regels

> De volgende regels zijn bindend voor iedereen die in of met deze repository werkt.
> Volledig kader: [`instructions.md`](instructions.md).

### Scope & Autoriteit

- Deze repository beheert de contract-documentatie en afspraken rond XML/XSD berichten.
- Het centrale contractbestand is de **functionele waarheid** voor structuur en validatieregels.
- Wijzigingen gebeuren bewust en gecontroleerd — nooit impulsief.
- **Alleen aangewezen maintainers** mogen wijzigingen uitvoeren.

### Kwaliteitsregels

- Consistentie gaat voor snelheid.
- Elke wijziging heeft een expliciete, gedocumenteerde reden.
- Berichtstructuren, naming en versies blijven uniform.
- Vermijd regressies door wijzigingen te toetsen aan bestaande afspraken.
- Twijfelgevallen worden eerst als issue gedocumenteerd.

### Verplichte Changelog-Entry

Na elke wijziging volgt **direct** een entry in `changelog.md` met dit formaat:

```md
## YYYY-MM-DD HH:MM (tijdzone)
- Auteur: ...
- Betrokken teams: ...
- Bestanden: ...
- Wijziging: ...
- Reden: ...
```

> Geen changelog-entry = geen complete wijziging.

### Definitie van Klaar

Een wijziging is pas klaar als:

1. De wijziging binnen scope is uitgevoerd.
2. De aanpassing duidelijk is beschreven.
3. `changelog.md` is bijgewerkt met datum en tijd.
4. Eventuele issue/PR context volledig is ingevuld.

---

## Teams Notificaties (Automatisch)

Bij elke push naar `main` of PR-event stuurt [`.github/workflows/teams-notify.yml`](.github/workflows/teams-notify.yml) automatisch een Adaptive Card naar het **XML - XSD Teams channel**.

```mermaid
flowchart TB
    subgraph TRIGGER["🚀 Trigger Events"]
        PUSH["Push naar main"]
        PR["Pull Request<br/>opened / sync / reopened / merged"]
    end

    subgraph WORKFLOW["⚙️  teams-notify.yml"]
        DETECT["🔍 Detecteer<br/>betrokken teams<br/>o.b.v. bestanden + changelog"]
        BUILD["🏗️  Bouw<br/>Adaptive Card payload"]
        SEND["📤 Verstuur<br/>webhook"]
    end

    subgraph CARD["📨 Adaptive Card in Teams"]
        TITLE["Titel: XML Update"]
        ACTOR["Actor + repository"]
        TEAMS_LIST["Betrokken teams"]
        CHANGELOG_ENTRY["Laatste changelog-entry"]
        FILES["Gewijzigde bestanden"]
        LINK["🔗 Link naar commit of PR"]
    end

    PUSH --> WORKFLOW
    PR   --> WORKFLOW
    DETECT --> BUILD --> SEND
    SEND --> CARD

    style TRIGGER  fill:#0b1f2a,color:#fff,stroke:#0a7ea4
    style WORKFLOW fill:#1e3a8a,color:#fff,stroke:#1e40af
    style CARD     fill:#6264a7,color:#fff,stroke:#4a4880
```

**Getriggerde events:**
- `push` naar `main`
- `pull_request` → opened, synchronize, reopened, merged

---

## Secrets Configuratie

Beide secrets zijn vereist voor volledige werking van de workflows.

### `TEAMS_WEBHOOK_URL`

Benodigd door: `teams-notify.yml`

1. Open GitHub repo **Settings**.
2. Ga naar **Secrets and variables → Actions**.
3. Klik **New repository secret**.
4. Naam: `TEAMS_WEBHOOK_URL`
5. Waarde: jouw Power Automate webhook URL.
6. Opslaan.

> Zonder deze secret draait de workflow wel, maar verstuurt ze **geen** webhook.

### `ALLOWED_CONTRACT_EDITORS`

Benodigd door: `enforce-maintainers.yml`

1. Open GitHub repo **Settings**.
2. Ga naar **Secrets and variables → Actions**.
3. Klik **New repository secret**.
4. Naam: `ALLOWED_CONTRACT_EDITORS`
5. Waarde: GitHub usernames, komma-gescheiden. Voorbeeld: `tombomeke-ehb,andereusername`
6. Opslaan.

> Zonder deze secret faalt de enforcement workflow bewust om ongeautoriseerde wijzigingen te blokkeren.

---

## Samenwerkingsafspraken

- Kleine, duidelijke wijzigingen werken beter dan grote bulk-edits.
- Elke wijziging is verklaarbaar: wat, waarom, impact.
- Geen wijziging zonder changelog-entry.
- Bij twijfel: issue openen en afstemmen vóór implementatie.
- PR's van niet-maintainers voor contractwijzigingen worden niet geaccepteerd.

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6264a7,50:0b1f2a,100:0a7ea4&height=120&section=footer" alt="footer" />

<sub><strong>XML/XSD Contract Hub</strong> · Integration Project Groep 1 · Centraal beheer van XML/XSD berichtafspraken</sub>
</div>
