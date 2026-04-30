# XML/XSD Contract Hub

[![Contract Version](https://img.shields.io/badge/Contract-v2.3-0a7ea4?style=for-the-badge&logo=files&logoColor=white&labelColor=0b1f2a)](XML_XSD_Contract_v2.3_Centralized%201.md)
[![Source of Truth](https://img.shields.io/badge/Source_of_Truth-XML_/_XSD-2f855a?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=0b1f2a)](XML_XSD_Contract_v2.3_Centralized%201.md)
[![Governance](https://img.shields.io/badge/Governance-Maintainers_Only-c53030?style=for-the-badge&logo=shield&logoColor=white&labelColor=0b1f2a)](instructions.md)
[![Language](https://img.shields.io/badge/Language-Dutch-5b21b6?style=for-the-badge&logo=googletranslate&logoColor=white&labelColor=0b1f2a)](#kernbestanden)

---

## Status & Operational Metrics

De onderstaande metrics bieden realtime inzicht in de integriteit en operationele status van de contractdefinities binnen het ecosysteem.

[![Build Status](https://img.shields.io/badge/Build_Process-Passing-2f855a?style=flat-square&logo=githubactions&logoColor=white&labelColor=0b1f2a)](../../actions)
[![Teams Notify](https://img.shields.io/badge/Teams_Integration-Active-6264a7?style=flat-square&logo=microsoftteams&logoColor=white&labelColor=0b1f2a)](../../actions/workflows/teams-notify.yml)
[![Enforcement](https://img.shields.io/badge/Access_Control-Active-c53030?style=flat-square&logo=githubactions&logoColor=white&labelColor=0b1f2a)](../../actions/workflows/enforce-maintainers.yml)
[![Changelog Status](https://img.shields.io/badge/Audit_Trail-Verified-f59e0b?style=flat-square&logo=keepachangelog&logoColor=white&labelColor=0b1f2a)](changelog.md)
[![Contract Update](https://img.shields.io/badge/Contract_Sync-April_2026-0a7ea4?style=flat-square&logo=semanticversioning&logoColor=white&labelColor=0b1f2a)](changelog.md)

> **Architecturaal Kader**  
> Deze repository fungeert als de **Gecentraliseerde Source of Truth** voor alle XML/XSD berichtafspraken binnen het Integration Project. Elke systeemkoppeling — waaronder CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing en Identity — is strikt gebonden aan de contractdefinities die in dit platform worden beheerd.

---

## Inhoudsopgave

1. [Doelgroep & Rechtenbeheer](#doelgroep--rechtenbeheer)
2. [Operationele Startgids](#operationele-startgids)
3. [Systeemarchitectuur](#systeemarchitectuur)
4. [Interactieve Netwerk-Map (Message Flow)](#interactieve-netwerk-map-message-flow)
5. [Technische Berichtenstroom (Topologie)](#technische-berichtenstroom-topologie)
6. [Kernbestanden & Documentatie](#kernbestanden)
7. [Governance & Kwaliteitsstandaarden](#governance--kwaliteitsstandaarden)
8. [Incident & Change Reporting](#incident--change-reporting)
9. [Maintainer Operations](#maintainer-operations)
10. [Automatisering & Notificaties](#automatisering--notificaties)
11. [Systeemconfiguratie (Secrets)](#systeemconfiguratie-secrets)
12. [Samenwerkingsprotocollen](#samenwerkingsprotocollen)

---

## Doelgroep & Rechtenbeheer

Toegang tot de contractdefinities is gebaseerd op een strikt rollenmodel om de integriteit van de Source of Truth te waarborgen.

| Classificatie | Geassocieerde Teams | Autorisatieniveau |
|:---|:---|:---|
| **Maintainer** | Architectuurbeheer & Kern-ontwikkelaars | Read/Write · Push naar `main` · PR Approval |
| **Developer** | CRM · Kassa · Frontend · Planning · Facturatie · e.a. | Read-only · Issue Management |

> **Handhaving:** Gebruikers zonder beheerrechten kunnen geen directe modificaties of Pull Requests doorvoeren. Dit beleid wordt technisch afgedwongen via de `enforce-maintainers.yml` workflow.

---

## Operationele Startgids

### Voor Developers (Integratie-teams)

1. **Specificatie-analyse:** Bestudeer het officiële contract: [`XML_XSD_Contract_v2.3_Centralized 1.md`](XML_XSD_Contract_v2.3_Centralized%201.md).
2. **Procesbeheer:** Raadpleeg de [`issue-guide.md`](issue-guide.md) voor de correcte afhandeling van inconsistenties.
3. **Communicatie:** Participeer in het Microsoft Teams kanaal **XML - XSD Channel** voor directe afstemming.
4. **Beperking:** Voer onder geen beding directe wijzigingen door in de contractbestanden.

### Voor Maintainers (Beheerders)

1. **Context-validatie:** Lees voorafgaand aan elke sessie [`xml-expert.md`](xml-expert.md) en [`instructions.md`](instructions.md).
2. **Methodiek:** Werk uitsluitend in geisoleerde, traceerbare stappen.
3. **Auditering:** Elke modificatie vereist een onmiddellijke registratie in [`changelog.md`](changelog.md) voorafgaand aan de commit.
4. **Configuratie:** Verifieer de aanwezigheid van de vereiste repository secrets.

---

## Systeemarchitectuur

De onderstaande visualisatie beschrijft de hiërarchische structuur van de repository en de interactie met de externe integratie-ecosystemen:

```mermaid
flowchart TB
    subgraph HUB["XML/XSD Contract Hub"]
        direction TB
        CONTRACT["XML_XSD_Contract_v2.3\n(Source of Truth)"]
        INSTRUCTIONS["instructions.md\n(Governance)"]
        XMLEXPERT["xml-expert.md\n(AI Context Framework)"]
        CHANGELOG["changelog.md\n(Audit Trail)"]
        ISSUEGUIDE["issue-guide.md\n(SOP)"]
    end

    subgraph TEAMS["Integration Ecosystem"]
        direction LR
        CRM["CRM"]
        KASSA["Kassa"]
        FRONTEND["Frontend"]
        PLANNING["Planning"]
        FACTURATIE["Facturatie"]
        OTHER["Services"]
    end

    CONTRACT  -->|"Contractdefinities"| TEAMS
    TEAMS  -->|"GitHub Issue"| ISSUEGUIDE
    TEAMS  -->|"Teams Communication"| HUB
```

---

## Interactieve Netwerk-Map (Message Flow)

Deze kaart wordt automatisch gegenereerd op basis van de contractdefinities en toont alle live berichtstromen tussen teams.

### ![https://img.shields.io/badge/Source_of_Truth-Live_Integration_Map-2f855a?style=for-the-badge&logo=gitbook&logoColor=white&labelColor=0b1f2a](https://img.shields.io/badge/Source_of_Truth-Live_Integration_Map-2f855a?style=for-the-badge&logo=gitbook&logoColor=white&labelColor=0b1f2a)

#### Legende
| Kleur / Stijl | Richting & Betekenis |
| :--- | :--- |
| ![](https://img.shields.io/badge/-%20-10b981?style=flat-square) **Groen** | Bericht **NAAR** de CRM (Inbound Hub) |
| ![](https://img.shields.io/badge/-%20-3b82f6?style=flat-square) **Blauw** | Bericht **VANAF** de CRM (Outbound Hub) |
| ![](https://img.shields.io/badge/-%20-6366f1?style=flat-square) **Indigo** | Direct bericht tussen teams (Peer-to-peer) |
| ![](https://img.shields.io/badge/-%20-94a3b8?style=flat-square) **Grijs** | Heartbeat / Status naar Monitoring (stippellijn) |

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

---

## Technische Berichtenstroom (Topologie)

Dit diagram biedt inzicht in de RabbitMQ-topologie en de informatiestromen tussen de diverse exchanges en systemen:

```mermaid
flowchart TB
    subgraph EXCHANGES["RabbitMQ Exchanges"]
        direction LR
        CRM_EX["crm.exchange\n(Direct)"]
        KASSA_EX["kassa.exchange\n(Topic)"]
        PLAN_EX["planning.exchange\n(Topic)"]
        IDENT_EX["user.events\n(Fanout)"]
    end

    subgraph NODES["System Nodes"]
        direction TB
        CRM["CRM (Salesforce)"]
        KASSA["Kassa"]
        FRONT["Frontend"]
        PLAN["Planning (O365)"]
        FACT["Facturatie"]
        MAIL["Mailing"]
        MONI["Monitoring (ELK)"]
    end

    %% Flows
    FRONT -- "user_created" --> CRM_EX --> CRM
    CRM -- "new_registration" --> KASSA_EX --> KASSA
    KASSA -- "payment_registered" --> CRM_EX --> CRM
    CRM -- "invoice_request" --> FACT
    PLAN -- "session_created" --> CRM_EX --> CRM
    CRM -- "send_mailing" --> MAIL
    CRM -- "user_events" --> IDENT_EX --> CRM & KASSA & FACT
    NODES -- "heartbeat" --> MONI

    style EXCHANGES fill:#f8f9fa,stroke:#1e3a8a
    style NODES fill:#f8f9fa,stroke:#2f855a
```

---

## Kernbestanden

| Bestand | Functionele Beschrijving |
|:---|:---|
| [`XML_XSD_Contract_v2.3_Centralized 1.md`](XML_XSD_Contract_v2.3_Centralized%201.md) | Gecentraliseerd XML/XSD contract — de functionele en technische waarheid. |
| [`xml-expert.md`](xml-expert.md) | Agent-definitie en strikt operationeel kader voor contractwijzigingen. |
| [`instructions.md`](instructions.md) | Bindende werkinstructies voor alle geautoriseerde bijdragers. |
| [`issue-guide.md`](issue-guide.md) | Standard Operating Procedure voor het rapporteren van inconsistenties. |
| [`changelog.md`](changelog.md) | Volledige audit-historiek van wijzigingen inclusief metadata en rationalisatie. |

---

## Governance & Kwaliteitsstandaarden

Alle werkzaamheden binnen deze repository zijn onderworpen aan de volgende kwaliteitsnormen:

### Operationele Kaders
- Consistentie prevaleert boven snelheid in alle omstandigheden.
- Elke wijziging dient een expliciete, gedocumenteerde rationalisatie te hebben.
- Berichtstructuren, naamgevingsconventies en versienummers blijven uniform.
- Regressie-vrij werken door proactieve validatie tegen bestaande afspraken.

### Audit Verplichting
Na elke modificatie volgt direct een registratie in `changelog.md` conform onderstaande ISO-standaard:

```md
## YYYY-MM-DD HH:MM (tijdzone)
- Auteur: ...
- Betrokken teams: ...
- Bestanden: ...
- Wijziging: ...
- Reden: ...
```

---

## Incident & Change Reporting

Bij detectie van afwijkingen dient onderstaand proces strikt te worden nageleefd door niet-bevoegde gebruikers:

```mermaid
flowchart LR
    A["Inconsistentie\ndetectie"] --> B["Stap 1:\nOpen GitHub Issue\n(XML/XSD Template)"]
    B --> C["Stap 2:\nTeams Bericht\ninclusief Issue-URL"]
    C --> D["Evaluatie door\nMaintainer"]
    D --> E["Fix + Audit Log\nPush naar main"]
    E --> F["Geautomatiseerde\nTeams Notificatie"]

    style A fill:#f8f9fa,stroke:#c53030
    style B fill:#f8f9fa,stroke:#1e40af
    style C fill:#f8f9fa,stroke:#6264a7
    style D fill:#f8f9fa,stroke:#0b1f2a
    style E fill:#f8f9fa,stroke:#2f855a
    style F fill:#f8f9fa,stroke:#6264a7
```

---

## Maintainer Operations

Beheerders maken gebruik van gestandaardiseerde processen en hulpmiddelen om de operationele continuïteit te waarborgen.

### Standaard Workflow
1. Analyseer `xml-expert.md` en `instructions.md` bij aanvang van elke sessie.
2. Voer wijzigingen uitsluitend uit binnen de vastgestelde scope.
3. Vermijd bulk-modificaties zonder expliciete motivatie.
4. Update `changelog.md` **voorafgaand** aan de commit.

### Quality of Life Tooling
Ter ondersteuning van de audit-verplichting is het volgende hulmiddel beschikbaar:

#### Changelog Automator
Automatiseert de generatie van changelog-entries inclusief automatische tijdsstempel en Git-identificatie.
- **Commando:** `node scripts/log-change.js`
- **Functionaliteit:** Vraagt om teams, bestanden en rationalisatie via interactieve prompts.

---

## Automatisering & Notificaties

Bij elke push naar `main` of Pull Request-event verzendt de `.github/workflows/teams-notify.yml` workflow automatisch een Adaptive Card naar het geconfigureerde Microsoft Teams kanaal. Dit waarborgt de onmiddellijke distributie van architecturale wijzigingen binnen de organisatie.

---

## Systeemconfiguratie (Secrets)

De onderstaande geheimen zijn vereist voor de volledige functionaliteit van de CI/CD-pijplijnen:

- **`TEAMS_WEBHOOK_URL`**: De Power Automate webhook URL voor systeemnotificaties.
- **`ALLOWED_CONTRACT_EDITORS`**: Whitelist van geautoriseerde GitHub-identiteiten (komma-gescheiden).

---

## Samenwerkingsprotocollen

- Modificaties moeten altijd verklaarbaar en traceerbaar zijn: wat, waarom en de impact.
- Bij onduidelijkheden wordt eerst een issue geopend ter afstemming.
- Pull Requests van niet-maintainers voor contractwijzigingen worden principieel afgewezen.

---

*XML/XSD Contract Hub — Integration Project Groep 1*  
*Centraal beheer van architecturale berichtafspraken.*
