# XML/XSD Contract Hub

![Contract Version](https://img.shields.io/badge/Contract-v2.3-0a7ea4?style=for-the-badge&labelColor=0b1f2a)
![Source of Truth](https://img.shields.io/badge/Source%20of%20Truth-XML%2FXSD-2f855a?style=for-the-badge&labelColor=0b1f2a)
![Workflow](https://img.shields.io/badge/Workflow-Instructions%20%2B%20Changelog-f59e0b?style=for-the-badge&labelColor=0b1f2a)
![Language](https://img.shields.io/badge/Docs-Nederlands-1f2937?style=for-the-badge&labelColor=0b1f2a)

Deze repository bevat het gecentraliseerde XML/XSD contract voor het Integration Project.
Het doel is dat alle teams dezelfde berichtenstructuur gebruiken en afwijkingen snel zichtbaar zijn.

## Waarom Deze Repo Bestaat

- Een centrale plek voor het officiële XML/XSD contract.
- Duidelijke afspraken tussen teams over message-structuren.
- Minder regressies en snellere troubleshooting bij integratieproblemen.
- Volledige traceerbaarheid van wijzigingen via changelog.

## Kernbestanden

- `XML_XSD_Contract_v2.3_Centralized 1.md`: het officiële en gecentraliseerde contract.
- `xml-expert.md`: agent-definitie en strikte werkmodus voor contractwijzigingen.
- `instructions.md`: verplichte werkinstructies voor bijdragen in deze repo.
- `issue-guide.md`: handleiding om XML/XSD issues op GitHub te openen.
- `changelog.md`: historiek van alle wijzigingen met datum en tijd.

## Verplichte Workflow

Bij elke prompt of wijziging in deze repo:

1. Lees `xml-expert.md`.
2. Lees `instructions.md`.
3. Werk volgens de xml-expert werkwijze (scope en stappen respecteren).
4. Voeg na elke wijziging een entry toe in `changelog.md`.

## Wijzigingsrechten (Belangrijk)

**Alleen aangewezen maintainers mogen wijzigingen doen in deze repository.**

Andere teams mogen:

- Issues openen (zie `issue-guide.md`)
- Vragen stellen
- Contractnoden melden

Andere teams mogen niet:

- Contractbestanden wijzigen
- Push naar main
- Pull requests openen

Dit voorkomt fouten en drift. Alle wijzigingen gaan via centrale maintainers.

Deze regel wordt afgedwongen door:

- `.github/workflows/enforce-maintainers.yml`

### Secret voor maintainer lijst (verplicht)

1. Open GitHub repo `Settings`.
2. Ga naar `Secrets and variables` > `Actions`.
3. Klik `New repository secret`.
4. Naam: `ALLOWED_CONTRACT_EDITORS`
5. Waarde: GitHub usernames, komma-gescheiden. Voorbeeld: `jouwusername,andereusername`
6. Opslaan.

Zonder deze secret faalt de enforcement workflow bewust.

## Issue Melden op GitHub

Voor XML/XSD problemen gebruik je de handleiding in:

- `issue-guide.md`

Kort samengevat:

1. Open een nieuwe issue in GitHub.
2. Gebruik titelprefix `[XML/XSD]`.
3. Voeg contractsectie, reproduceerstappen en voorbeeld XML/XSD toe.
4. Label correct (`xml`, `xsd`, `bug`, `contract`).

## Teams Notificaties (Automatisch)

Deze repo heeft een GitHub Actions workflow die een webhook-bericht stuurt naar het XML - XSD Teams channel bij:

1. Push naar `main`
2. Pull request events naar `main` (open, update, reopen, merge)

Bestand:

- `.github/workflows/teams-notify.yml`

De melding bevat:

- Vaste tekst: `XML is geupdate`
- Laatste entry uit `changelog.md`
- Gedetecteerde betrokken teams (best effort)
- Event context (push of PR)

### Secret instellen (verplicht)

1. Open GitHub repo `Settings`.
2. Ga naar `Secrets and variables` > `Actions`.
3. Klik `New repository secret`.
4. Naam: `TEAMS_WEBHOOK_URL`
5. Waarde: jouw Power Automate webhook URL.
6. Opslaan.

Zonder deze secret draait de workflow wel, maar verstuurt ze geen webhook.

## Samenwerkingsafspraken

- Kleine, duidelijke wijzigingen werken beter dan grote bulk-edits.
- Elke wijziging moet verklaarbaar zijn: wat, waarom, impact.
- Geen wijziging zonder changelog-entry.
- Bij twijfel: issue openen en afstemmen voor implementatie.

## Snelle Start

1. Lees `XML_XSD_Contract_v2.3_Centralized 1.md`.
2. Lees `xml-expert.md` en `instructions.md`.
3. Werk je wijziging uit.
4. Log de wijziging in `changelog.md` met datum en tijd.

## Status

Actieve beheerrepo voor contractbeheer en afstemming tussen teams.
