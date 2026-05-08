# Changelog

Alle wijzigingen aan deze repository worden hier chronologisch bijgehouden.

## 2026-05-08 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — GJeremy64)
- Betrokken teams: Kassa, CRM, Frontend
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: QR-code ondersteuning als alternatief voor badge-scan aan de kassa:
  - **§6.3 `badge_scanned`**: `scan_type` (badge|qr_code) toegevoegd als verplicht discriminator-veld. `badge_id` en `identity_uuid` zijn nu optioneel (minOccurs="0") — bij badge-scan aanwezig, bij QR-scan alleen `identity_uuid`. Tweede voorbeeldblok toegevoegd voor QR-scenario.
  - **§26.1 `wallet_lease_request`**: `badge_id` optioneel gemaakt (minOccurs="0") zodat QR-scan (enkel `identity_uuid`) geldig is. Tweede voorbeeldblok toegevoegd.
  - **Overzichtstabel (§Kassa)**: bron `badge_scanned` uitgebreid met "of Kassa (QR)".
- Reden: QR-code op de frontend toont de `master_uuid`; de Odoo POS-camera scant die, waarna de klant direct geselecteerd is en de wallet lease flow start zonder fysieke badge.

## 2026-05-07 (middag) (+02:00)
- Auteur: Gemini CLI (Integratie Orchestrator)
- Betrokken teams: CRM, Facturatie, Mailing
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Redundante `<template_id>` verwijderd uit `send_mailing` contract (Sectie 12.1 & 13.1):
  - **Sectie 12.1 (XSD)**: `<xs:element name="template_id" type="xs:string"/>` verwijderd.
  - **Sectie 12.1 & 13.1 (Voorbeelden)**: `<template_id>` tags verwijderd uit de XML voorbeelden.
- Reden: Versimpeling van het contract. Het veld `<template_id>` (specifiek voor Sendgrid) is redundant omdat de Mailing-service de `<mail_type>` intern kan vertalen naar het juiste template-ID. Dit vermindert koppeling tussen zendende teams en de specifieke mailing-provider configuratie.

## 2026-05-07 (avond) (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — GJeremy64)
- Betrokken teams: Alle teams, Monitoring, Heartbeat, Mailing
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Contract-afstemming met Monitoring-repo + logging XSD geformaliseerd:
  - **Sectie 3.5 (nieuw)**: Log-bericht XSD toegevoegd (Alle teams excl. Monitoring → `logs` queue). Bevat `level` (info/warning/error), `action` (13 waarden), `message`. Source-enum incl. `iot_gateway`.
  - **Sectie 3 (Heartbeat XSD)**: `<uptime type="xs:nonNegativeInteger">` toegevoegd als verplicht body-veld — Logstash quarantineert berichten zonder dit veld.
  - **Sectie 4 (system_alert)**: Formaat teruggebracht naar de werkende implementatie: platte `<alert>` root (`type`, `system`, `message`, `timestamp`), queue `to_mailing`, default exchange. Gedocumenteerd als geoorloofde uitzondering op Regel 1 voor intern Monitoring↔Mailing verkeer.
  - **Globale SourceType (§2)**: `identity-service` en `iot_gateway` toegevoegd aan de enum.
  - **Heartbeat-note (§3)**: `iot_gateway` toegevoegd aan de toegestane source-waarden voor Monitoring-team.
  - **TOC**: Sectie 3.5 toegevoegd.
  - **Audit-sectie Monitoring**: Status bijgewerkt naar "nagenoeg conform", overbodige actiepunten verwijderd. Enige openstaande actie: `iot_gateway` toevoegen aan Logstash logs-whitelist.
  - **Audit-sectie Heartbeat service**: `degraded` verwijderd uit body-beschrijving; `uptime` gemarkeerd als verplicht.
  - **Routing-tabellen en per-team secties**: `monitoring.alerts` → `to_mailing` gecorrigeerd; Mailing-actiepunten bijgewerkt.
  - **AUTHORITATIVE REFERENCE block verwijderd**: Kassa's `schema_log.xsd` was ten onrechte aangeduid als Gold Standard — contract is nu de enige bron van waarheid.
- Reden: Vier concrete mismatches gevonden tussen contract en Monitoring-repo na analyse van commit e52044a en directe repo-inspectie. Contract aangepast zodat het de werkende implementatie correct beschrijft en teams een betrouwbare referentie hebben.

## 2026-05-07 10:47 (+02:00)
- Auteur: Gemini CLI (Integratie Orchestrator)
- Betrokken teams: Frontend, CRM, Facturatie
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: XSD en Voorbeeld XML voor `event_ended` in sectie 11.6 (Frontend → Facturatie) exact gelijkgetrokken met sectie 5.7 (Frontend → CRM).
- Reden: Voldoen aan globale regel 3 ("Berichtstructuren, naming en versies moeten uniform blijven") en regel 1 ("Consistentie gaat voor snelheid"). De definitie was al structureel correct, maar bevatte opmaak-inconsistenties (tags op meerdere regels versus gecomprimeerd en optionele XML-headers).

## 2026-05-07 10:45 (+02:00)
- Auteur: Gemini CLI (Integratie Orchestrator)
- Betrokken teams: Frontend, Facturatie
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Nieuw berichttype `event_ended` (Frontend → Facturatie) toegevoegd — Issue #34:
  - **Quick Reference (§0)**: `event_ended` bij Frontend bijgewerkt met extra bestemming (Facturatie).
  - **Quick Reference (§0)**: `event_ended` bij Facturatie toegevoegd als ONTVANGT bericht.
  - **Sectie 11.6** toegevoegd met volledige XSD en XML-voorbeeld (source: `frontend`, queue: `facturatie.incoming`).
  - **Kritieke fixes**: Actiepunten toegevoegd voor Frontend (extra publicatie naar Facturatie) en Facturatie (nieuwe consumer voor mailing trigger).
- Reden: Issue #34 — Facturatie heeft het `event_ended` bericht nodig om factuur-mailings te triggeren; Frontend stuurde dit voorheen alleen naar CRM.

## 2026-05-06 20:55 (+02:00)
- Auteur: Gemini CLI (Integratie Orchestrator)
- Betrokken teams: Frontend, Facturatie
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Consistentie-verbeteringen Issue #27:
  - **Quick Reference (§0)**: Status `payment_registered` bij Frontend hersteld naar `v2.0`.
  - **Sectie 11.5 (XSD)**: `UUIDType` toegevoegd en toegepast op `message_id` en `correlation_id`.
  - **Sectie 24 (Interface Analyse)**: `Frontend → Facturatie` flow toegevoegd aan de samenvattingstabel.
- Reden: Puntjes op de i voor Issue #27; wegwerken van kleine inconsistenties in het contract.

## 2026-05-06 20:55 (+02:00)
- Auteur: Gemini CLI (Integratie Orchestrator)
- Betrokken teams: Frontend, Facturatie, Monitoring
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `README.md`, `changelog.md`
- Wijziging: Contract-verfijning op basis van kwaliteitsaudit:
  - **Sectie 11.5 (payment_registered)**: XSD versterkt met `SourceType` en `UUIDType`. XML voorbeeld gecorrigeerd naar online betalingscontext (`online_invoice` + `online`).
  - **Netwerk-Map**: Monitoring-headers gecorrigeerd (`### **Team Monitoring**`) zodat heartbeats en alerts correct worden toegewezen in het diagram.
  - **Opschoning**: Dubbele footers en loze regels aan het einde van het contract-document verwijderd.
- Reden: Consistentie-verbetering en technische correctheid van de schema's en het visuele overzicht.

## 2026-05-06 20:45 (+02:00)
- Auteur: Gemini CLI (Integratie Orchestrator)
- Betrokken teams: Frontend, Facturatie
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Contract-structuur hersteld en actiepunten aangevuld — Issue #27 vervolg:
  - **Sectie 17 (Team Facturatie)**: Header en tabel-opmaak hersteld (was vermangeld in vorige update).
  - **Quick Reference (§0)**: Status voor `payment_registered` bij Frontend en Facturatie bijgewerkt (nu gemarkeerd als "NIEUW — nog niet geïmplementeerd").
  - **Sectie 17 (Team Frontend)**: Actiepunt toegevoegd voor de implementatie van `PaymentRegisteredSender.php`.
- Reden: De vorige update had per abuis de Team Facturatie header overschreven en de tabel-opmaak gebroken. Tevens actiepunten verduidelijkt voor de teams op basis van Issue #27.

## 2026-05-06 20:32 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Frontend, Facturatie
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `README.md`, `changelog.md`
- Wijziging: Nieuw berichttype `payment_registered` (Frontend → Facturatie) toegevoegd — Issue #27:
  - **Sectie 11.5** toegevoegd met volledige XSD en XML-voorbeeld (source: `frontend`, queue: `facturatie.incoming`)
  - **Quick Reference** (§0 Frontend + Facturatie): nieuwe VERZENDT/ONTVANGT rijen toegevoegd
  - **§16 Queue-overzicht**: `Frontend | Facturatie | facturatie.incoming` rij toegevoegd
  - **§17 Per-Team Samenvatting**: Frontend en Facturatie tabellen en actiepuntenlijsten bijgewerkt
  - **README.md Mermaid diagram**: `Frontend -- "payment_registered" --> Facturatie` pijl toegevoegd
  - **ToC** bijgewerkt: `11.5` vermeld in de Inhoudsopgave onder CRM → Facturatie
  - Source-waarde gecorrigeerd van `"Frontend"` (uppercase) naar `"frontend"` (lowercase) conform SourceType enum in §2
- Reden: Issue #27 — Frontend stuurde het bericht al niet naar Facturatie; de flow ontbrak ook volledig uit het contract. Toegevoegd conform het XML/XSD-voorbeeld uit het issue.

## 2026-05-06 10:00 (+02:00)
- Auteur: Gemini CLI (Lead Integratie Agent)
- Betrokken teams: Alle teams, Monitoring, Facturatie, CRM, Frontend
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Diverse contract-correcties op basis van code review: `SourceType` hersteld (o.a. `iot_gateway`), header-structuur gestandaardiseerd (`UUIDType`), `invoice_available` en `invoice_id` (string) gefixed, monitoring tabel-markdown hersteld, `facturatie.to.frontend` toegevoegd aan §16, logging-referenties verwijderd, en optionele `uptime` aan heartbeat body toegevoegd.
- Reden: Oplossen van inconsistenties, XSD-validatiefouten en Markdown-fouten in het contract v2.3.

## 2026-05-04 15:45 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Alle teams, Monitoring, Heartbeat (sidecar)
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Heartbeat routing definitief gecorrigeerd in §3, §3.2 en §16: exchange = `""` (AMQP default), routing_key = `"heartbeat"`, direct naar queue. Eerdere vermeldingen van `kassa.exchange` en `heartbeat` exchange verwijderd. Geverifieerd aan de hand van `test/producer.py` op `hotfix/logging-pipeline` (`exchange=""`, `routing_key=HEARTBEAT_QUEUE`) en logstash config (luistert direct op queue `heartbeat`).
- Reden: Monitoring-implementatie gebruikt de AMQP default exchange — geen named exchange. Contract was incorrect en inconsistent met de werkende implementatie.

## 2026-05-04 15:15 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Alle teams
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: `message_id` type gecorrigeerd van `xs:string` naar `UUIDType` in §3 (heartbeat), §3.5 (logging) en §2.6 (system_error). UUIDType-definitie toegevoegd aan §3.5 logging XSD (ontbrak). Routing heartbeat (§3.2: kassa.exchange + routing key) was al correct in contract — geen wijziging nodig.
- Reden: Inconsistentie gesignaleerd door implementerende agent: globale HeaderType (§2) gebruikt al UUIDType, maar standalone per-sectie XSDs gebruikten nog xs:string. Resterende ~34 standalone XSDs in het contract hebben hetzelfde patroon — bulk-fix beschikbaar op aanvraag.

## 2026-05-04 15:00 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Monitoring, Heartbeat (sidecar)
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Heartbeat XSD (§3) aangepast: `degraded` verwijderd uit `status`-enum, `<uptime>` (xs:integer, seconden) toegevoegd aan body. Voorbeeldxml bijgewerkt. Toelichting toegevoegd dat interne fouten via `log` (level=error, action=system_error) gerapporteerd worden — niet via heartbeat status.
- Reden: `degraded` is overbodig nu het logging-systeem (§3.5) beschikbaar is. Interne problemen horen thuis als error-log, niet als heartbeat-status. `uptime` geeft Monitoring nuttige runtime-info zonder extra berichten.

## 2026-05-04 14:45 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Alle teams
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Waarschuwingstekst boven de action-voorbeelden in §3.5 uitgebreid. Verduidelijkt dat `{placeholder}`-syntax geen voorgeschreven formaat is maar een aanduiding — teams gebruiken de string-opmaak van hun eigen taal (f-string, template literal, sprintf, String.format). Taalspecifieke codepatronen toegevoegd als richtlijn. Vermeld dat de exacte berichttekst per team mag verschillen.
- Reden: Risico dat teams de placeholder-notatie letterlijk interpreteren of de voorbeeldteksten hardcoderen.

## 2026-05-04 14:30 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Alle teams
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Sectie 3.5 uitgebreid met voorbeelden per action-categorie (alle 13 actions, meerdere levels). Elk voorbeeld bevat XML-comments die expliciet aangeven welke velden runtime gegenereerd moeten worden (`message_id`, `timestamp`, `message`-inhoud). Prominente waarschuwing toegevoegd dat voorbeeldwaarden nooit hardcoded mogen worden.
- Reden: Teams hebben concrete voorbeelden nodig per action om te weten welke runtime-informatie in het `<message>`-veld thuishoort.

## 2026-05-03 (+02:00)
- Auteur: Gemini CLI (AI-assistent)
- Betrokken teams: Kassa, CRM, Facturatie, Frontend, Planning
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`
- Wijzigingen:
    - **Lean Architecture (Phone):** Alle sporen van het `<phone>` veld (XSD en XML voorbeelden) verwijderd uit het hele document (o.a. §5.1 en §5.2).
    - **Strikte Valuta-validatie:** Alle `currency` attributen in het hele document voorzien van `fixed="eur"` conform de globale regel in §1.
    - **Target Architecture Markering:** `UUIDType` geactiveerd en toegepast op `message_id` en `correlation_id` in de gedeelde header. Standalone schema-blokken (§6.4, §6.5, §10.2, §10.3) nu technisch valide door inclusie van benodigde types.
    - **Verplichte Correlation ID:** `correlation_id` verplicht gemaakt (`minOccurs="1"`) in kritieke business flows: `invoice_request` en `refund_processed`.
    - **Adres-harmonisatie:** Nieuwe regel 6 toegevoegd voor verplichte splitsing van straat en huisnummer, inclusief gedocumenteerd splitting-algoritme voor legacy integraties (Odoo).
    - **Profile Update Verbeteringen (§10.2):** Veld `<type>` toegevoegd (private/company) en `<date_of_birth>` optioneel gemaakt om de update-flow te optimaliseren.
    - **Cleanup:** `PLAN_CONTRACT_SYNC.md` verwijderd na succesvolle synchronisatie. Dubbele tekstfragmenten en opmaakfouten in de XSD-blokken gecorrigeerd.
- Reden: Volledige synchronisatie van het centraal contract met de technische realiteit en stakeholder-behoeften (Kassa, CRM, Frontend). Verhoging van de globale consistentie en betrouwbaarheid van het contract.
## 2026-05-04 14:15 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Identity
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: `identity-service` toegevoegd aan `source`-enum in §3.5 logging XSD. Quick Reference Identity-team bijgewerkt met `VERZENDT log` rij. Queue-overzicht §16 bijgewerkt.
- Reden: Identity-service voert acties uit (UUID aanmaken, lookups) die gelogd moeten worden. Monitoring ontvangt alleen logs en verstuurt ze niet.

## 2026-05-04 14:00 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: CRM, Kassa, Facturatie, Frontend, Planning, Mailing, Monitoring
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Nieuw berichttype `log` toegevoegd — sectie 3.5 "Logging — Alle teams → Monitoring":
  - Queue `logs` (durable, geen exchange, geen team-prefix) — conform implementatie op `origin/hotfix/logging-pipeline` in Monitoring-repo.
  - XSD met `source` enum (crm/kassa/facturatie/frontend/planning/mailing), `type=log`, `body`: `level` (info/warning/error), `action` (13 categorieën), vrij tekstveld `message`.
  - ToC bijgewerkt (sectie 3.5 toegevoegd).
  - Queue-overzicht (§16) bijgewerkt met `logs`-rij.
  - Quick Reference bovenaan bijgewerkt: VERZENDT `log` rij toegevoegd aan Kassa, CRM, Frontend, Planning, Facturatie en Mailing.
  - Quick Reference Monitoring bijgewerkt: ONTVANGT `log` toegevoegd.
  - §17 Monitoring-samenvatting bijgewerkt: `log`-queue toegevoegd + actiepunt voor Logstash `logs`-pipeline.
- Reden: Voorstel van team Planning/Monitoring om gestructureerde logging via RabbitMQ te standardiseren. Implementatie al aanwezig op `hotfix/logging-pipeline` in de Monitoring-repo — contract was nog niet bijgewerkt.

## 2026-05-02 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Geen (interne workflow)
- Bestanden: `.github/workflows/teams-notify.yml`
- Wijziging: `awk`-commando gecorrigeerd dat de laatste changelog-entry uitlaast. Het script itereerde het volledige bestand en pakte de onderste sectie — maar de nieuwste entries staan bovenaan. Fix: stop bij de tweede `## `-header zodat alleen de eerste (nieuwste) entry wordt gepakt.
- Reden: Teams-notificaties toonden altijd de oudste changelog-entry in plaats van de recentste.

## 2026-05-02 (+02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: Geen (interne workflow)
- Bestanden: `.github/workflows/update-network-map.yml`
- Wijziging: Workflow aangepast zodat hij een PR opent in plaats van rechtstreeks naar `main` te pushen. Gebruikt nu `peter-evans/create-pull-request@v6` op branch `chore/auto-update-network-map`.
- Reden: De directe `git push` naar `main` werd geblokkeerd door de branch protection rule (wijzigingen moeten via een PR). De workflow crashte daardoor bij elke contractwijziging.

## 2026-05-01 (lokale tijd +02:00)
- Auteur: Claude Sonnet 4.6 (AI-assistent — tombomeke-ehb)
- Betrokken teams: CRM, Frontend, Kassa, Facturatie, Mailing, Planning, Monitoring, Identity
- Bestanden: `XML_XSD_Contract_v2.3_Centralized 1.md`, `changelog.md`
- Wijziging: Volledige sweep en audit van het contract — 10 fouten gevonden en gefixed:
  1. **§2 SourceType**: `iot_gateway` toegevoegd aan globale source enum (was inconsistent met §6.3 `badge_scanned`).
  2. **§6.1 consumption_order header XSD**: `source` en `version` kregen `fixed=` constraints (waren plain `xs:string`).
  3. **§6.3 badge_scanned XSD**: `kassa` toegevoegd als geldige source-waarde naast `iot_gateway` (conform §0.5.2).
  4. **§8.1 invoice_status header XSD**: `source`, `type`, `version` kregen `fixed=` constraints (waren plain `xs:string` zonder validatie).
  5. **§10.2 profile_update**: `payment_due.status` enum gecorrigeerd van `pending|paid` naar `unpaid|paid` (inconsistentie met §10.1).
  6. **§12.1 send_mailing XSD**: `facturatie` toegevoegd aan source enum (Facturatie stuurt ook `send_mailing` maar stond niet in de enum — zou XSD-validatie breken bij Mailing).
  7. **§13 Facturatie → Mailing**: Queue gecorrigeerd van `crm.to.mailing` naar `facturatie.to.mailing` (inconsistentie met §16 en §17).
  8. **§17.1 session_view_response**: `speaker.user_id` gemarkeerd als `minOccurs="0"` (was verplicht, maar §7.1/7.2 maken het optioneel — sessies zonder speaker-UUID konden niet via RPC worden teruggegeven).
  9. **§5.6 Nieuw**: XSD toegevoegd voor `cancel_registration` (Frontend → CRM) — stond vermeld in §17 team-tabel maar miste volledig een XSD-sectie.
  10. **Sectie-nummering**: Subsecties in §19 hernummerd van 17.x naar 19.x; §20 subsectie hernummerd van 18.1 naar 20.1.
- Reden: Volledige contractaudit op verzoek van maintainer. Alle gevonden contract-inconsistenties en XSD-fouten worden door dit team (contract-maintainers) gefixed — andere teams passen hun code aan op basis van dit bijgewerkte contract.

## 2026-04-30 14:27 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Bestanden: README.md, instructions.md, issue-guide.md, changelog.md
- Wijziging: Nieuwe werkinstructies toegevoegd, issue-handleiding toegevoegd, README uitgebreid met projectuitleg/workflow/badges en changelog-systeem opgestart.
- Reden: Betere samenwerking, traceerbaarheid en duidelijke procedure voor XML/XSD contractbeheer.

## 2026-04-30 14:28 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Bestanden: instructions.md, changelog.md
- Wijziging: Typefout gecorrigeerd ("ittereren" naar "itereren") in de instructies.
- Reden: Documentkwaliteit en duidelijke communicatie verbeteren.

## 2026-04-30 14:29 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Bestanden: instructions.md, .github/ISSUE_TEMPLATE/xml-xsd-probleem.md, .github/ISSUE_TEMPLATE/config.yml, .github/PULL_REQUEST_TEMPLATE.md, changelog.md
- Wijziging: Uitgebreide instructies toegevoegd voor mensen en AI-agents, GitHub issue-template toegevoegd voor XML/XSD problemen, issue-config geactiveerd en PR-template toegevoegd met verplichte changelog-check.
- Reden: Sterkere governance, betere standaardisatie van samenwerking en volledige traceerbaarheid van contractwijzigingen.

## 2026-04-30 14:35 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Betrokken teams: CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing, Identity
- Bestanden: .github/workflows/teams-notify.yml, README.md, instructions.md, changelog.md
- Wijziging: GitHub Actions workflow toegevoegd voor Teams webhooknotificaties bij push naar main en PR-events, README uitgebreid met secret-setup instructies, en instructies aangescherpt met verplicht veld "Betrokken teams" in changelog-entries.
- Reden: Automatische teamcommunicatie opzetten en de kwaliteit van betrokken-teamdetectie in notificaties verbeteren.

## 2026-04-30 14:42 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Betrokken teams: CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing, Identity
- Bestanden: .github/workflows/enforce-maintainers.yml, .github/workflows/teams-notify.yml, README.md, instructions.md, changelog.md
- Wijziging: Nieuwe maintainer-enforcement workflow toegevoegd op push/PR naar main, Teams webhookworkflow verbeterd met compatibele velden (`text`, `title`, `summary`) en duidelijke HTTP response-logging, en repo-instructies aangescherpt zodat alleen maintainers mogen wijzigen en andere teams issues moeten gebruiken.
- Reden: Contractwijzigingen strikt centraliseren en webhookproblemen sneller kunnen diagnosticeren wanneer Teams-berichten uitblijven.

## 2026-04-30 14:45 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Betrokken teams: CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing, Identity
- Bestanden: instructions.md, README.md, .github/PULL_REQUEST_TEMPLATE.md, changelog.md
- Wijziging: Governance explicieter gemaakt: niet-maintainers openen alleen issues en doen geen push/PR voor contractwijzigingen; PR-template verduidelijkt dat het voor maintainers is.
- Reden: Rollen strikt afbakenen zodat uitsluitend de centrale beheerders contractwijzigingen uitvoeren en andere teams via issues werken.

## 2026-04-30 14:47 (+02:00)
- Auteur: GitHub Copilot (GPT-5.3-Codex)
- Betrokken teams: Geen (verwijdering van template)
- Bestanden: .github/PULL_REQUEST_TEMPLATE.md (verwijderd), changelog.md
- Wijziging: PR-template verwijderd om verwarring te voorkomen en duidelijk te maken dat PR's uitsluitend voorbehouden zijn aan maintainers.
- Reden: Maximale duidelijkheid en voorkoming van false positives - andere teams mogen geen PR's openen en hoeven geen template te zien.

## 2026-04-30 15:15 (+02:00)
- Auteur: Gemini CLI (Lead Integratie Agent)
- Betrokken teams: CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing, Identity
- Bestanden: .github/workflows/teams-notify.yml, README.md, changelog.md
- Wijziging: Teams notificatie workflow hersteld naar Adaptive Card formaat (v1.2), changelog extractie gefixed naar laatste entry, README aangescherpt met governance (alleen maintainers) en communicatiekanalen (XML - XSD Channel).
- Reden: Betrouwbare teamcommunicatie garanderen en contractintegriteit beschermen via strikte beheersregels.

## 2026-04-30 16:55 (+02:00)
- Auteur: Gemini CLI (Lead Integratie Agent)
- Betrokken teams: CRM, Kassa, Frontend, Planning, Facturatie, Monitoring, Mailing, Identity
- Bestanden: scripts/generate_network_map.py, README.md, changelog.md
- Wijziging: Netwerk-map script volledig herschreven met subgraph-architectuur, logische teamcategorisering (Core/Ops/Support) en verbeterde Mermaid node-styling.
- Reden: Verbetering van de visuele structuur en leesbaarheid van het centrale integratieoverzicht.