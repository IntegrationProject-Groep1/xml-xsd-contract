# Instructions voor Werken in Deze Repo

Dit document is bindend voor iedereen die in deze repository werkt:

- Menselijke bijdragers
- AI-assistenten
- Specialized agents (zoals de xml-expert)

Doel: de XML/XSD contracten consistent, controleerbaar en traceerbaar houden.

## 1. Scope en Autoriteit

1. Deze repository beheert de contract-documentatie en afspraken rond XML/XSD berichten.
2. Het centrale contractbestand is de functionele waarheid voor structuur en validatieregels.
3. Wijzigingen gebeuren bewust en gecontroleerd, nooit impulsief.
4. Alleen aangewezen maintainers mogen wijzigingen in deze repository uitvoeren.
5. Andere teams gebruiken issues om fouten, ontbrekende XML of contractvragen te melden.

## 2. Verplichte Start bij Elke Prompt of Taak

Bij het itereren van een prompt in deze repo moet je altijd eerst:

1. `xml-expert.md` lezen.
2. `instructions.md` lezen.
3. De werkwijze en beperkingen uit `xml-expert.md` toepassen.

Als deze volgorde niet gevolgd wordt, is het werkproces onvolledig.

## 3. Werkwijze Voor Mensen

1. Werk in kleine, begrijpelijke stappen.
2. Pas alleen aan wat binnen de scope van je taak valt.
3. Vermijd brede bulk-wijzigingen zonder duidelijke motivatie.
4. Noteer impact op teams, flows en message types.
5. Gebruik duidelijke commit- en PR-beschrijvingen.
6. Als je geen maintainer bent: maak een issue, wijzig het contract niet zelf.

## 4. Werkwijze Voor AI-assistenten en Agents

1. Lees altijd eerst de contextbestanden uit sectie 2.
2. Respecteer scopebeperkingen van de actieve agent.
3. Voer geen speculatieve wijzigingen uit.
4. Bewaar technische nauwkeurigheid in XML/XSD terminologie.
5. Vermeld aannames expliciet wanneer iets onzeker is.
6. Registreer elke gemaakte wijziging in `changelog.md`.

## 5. Kwaliteitsregels voor XML/XSD Contractwerk

1. Consistentie gaat voor snelheid.
2. Elke wijziging moet een duidelijke reden hebben.
3. Berichtstructuren, naming en versies moeten uniform blijven.
4. Vermijd regressies door wijzigingen lokaal te toetsen aan bestaande afspraken.
5. Twijfelgevallen worden eerst als issue gedocumenteerd.

## 6. Verplichte Changelog-Registratie

Na elke verandering in deze repo moet je onmiddellijk een entry toevoegen in `changelog.md`.

Elke entry bevat minimaal:

- Datum
- Tijd
- Auteur (naam, team of agent)
- Betrokken teams
- Gewijzigde bestanden
- Wat er precies veranderd is
- Waarom dit nodig was

Gebruik dit vaste formaat:

```md
## YYYY-MM-DD HH:MM (tijdzone)
- Auteur: ...
- Betrokken teams: ...
- Bestanden: ...
- Wijziging: ...
- Reden: ...
```

Regel: geen changelog-entry betekent geen complete wijziging.

## 7. Issue en PR Discipline

1. Problemen of onduidelijkheden worden via GitHub Issues gemeld.
2. Gebruik het XML/XSD issue-template voor volledige context.
3. Pull requests volgen de PR-template en moeten changelog-updates bevestigen.
4. Een PR zonder duidelijke impactbeschrijving is niet review-klaar.
5. PR's van niet-maintainers voor contractwijzigingen worden niet geaccepteerd.
6. Niet-maintainers openen alleen issues en doen geen push of PR voor contractwijzigingen.

## 8. Definitie van Klaar

Een wijziging is pas klaar als:

1. De wijziging binnen scope is uitgevoerd.
2. De aanpassing duidelijk beschreven is.
3. `changelog.md` is bijgewerkt met datum en tijd.
4. Eventuele issue/PR context volledig is ingevuld.

## 9. Praktische Verwijzingen

- Hoofdcontract: `XML_XSD_Contract_v2.3_Centralized 1.md`
- Agentkader: `xml-expert.md`
- Issue-handleiding: `issue-guide.md`
- Changelog: `changelog.md`

## 10. Kernprincipe

Deze repository is een gedeelde Source of Truth.
Elke bijdrage moet de betrouwbaarheid, leesbaarheid en teamafstemming versterken.