# Changelog

Alle wijzigingen aan deze repository worden hier chronologisch bijgehouden.

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