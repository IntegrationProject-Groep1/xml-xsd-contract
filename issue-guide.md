# Issue Guide: XML/XSD Probleem Melden op GitHub

Dit document legt stap voor stap uit hoe je op GitHub een duidelijke issue opent voor XML/XSD problemen.

## Wanneer Open Je Een Issue?

Open een issue als je een van deze situaties ziet:

- XML komt niet overeen met het centrale contract.
- XSD validatie faalt.
- Message type, header of body wijkt af van de afgesproken structuur.
- Onzekerheid over interpretatie van een contractregel.
- Regressie na een wijziging.

## Stap-voor-Stap op GitHub

1. Ga naar de repository op GitHub.
2. Klik op het tabblad **Issues**.
3. Klik op **New issue**.
4. Gebruik als titel: `[XML/XSD] Korte beschrijving van het probleem`.
5. Vul de beschrijving in volgens het sjabloon hieronder.
6. Voeg labels toe (bijvoorbeeld `xml`, `xsd`, `bug`, `contract`).
7. Wijs een verantwoord teamlid toe als dat kan.
8. Klik op **Submit new issue**.

## Aanbevolen Issue Sjabloon

```md
## Samenvatting
Beschrijf kort het probleem.

## Verwacht gedrag
Wat zou volgens het contract moeten gebeuren?

## Huidig gedrag
Wat gebeurt er nu effectief?

## Betrokken contractsectie
Bijv. XML_XSD_Contract_v2.3_Centralized 1.md - sectie 11.1

## Reproductiestappen
1. ...
2. ...
3. ...

## Voorbeeld XML/XSD of foutmelding
Plak relevante snippets of validatiefouten.

## Impact
Welke teams/flows worden geraakt?

## Voorstel tot oplossing (optioneel)
Eventuele suggestie of eerste analyse.
```

## Tips Voor Sterke Issues

- Voeg concrete voorbeelden toe.
- Vermeld exact berichttype en flow.
- Verwijs naar de juiste contractsectie.
- Vermijd vage omschrijvingen zoals "werkt niet" zonder context.
- Update na oplossing ook de `changelog.md` in deze repo.