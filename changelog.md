# Changelog

Alle wijzigingen aan deze repository worden hier chronologisch bijgehouden.

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