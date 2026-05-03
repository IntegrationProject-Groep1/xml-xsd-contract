# Implementatieplan: Synchronisatie Centraal Contract v2.3

## 1. Probleemanalyse
De Kassa-specifieke XSD's en het centrale contract (`XML_XSD_Contract_v2.3_Centralized 1.md`) vertonen kleine inconsistenties op het gebied van velden (phone), validatiestriktheid (currency, regex) en verplichte koppelingen (correlation_id).

## 2. Voorgestelde Wijzigingen

### Fase A: Lean Architectuur Pivot (Veld: Phone)
*   **Locatie:** §1 (Globale Regels - `ContactType`) en álle inline `<contact>` definities.
*   **Status:** **GEREVERTEERD** (Besluit 03/05/2026).
*   **Rationale:** Na feedback van Team Kassa is het veld geschrapt om "schema bloat" te voorkomen. Het contract blijft beperkt tot velden met bevestigde stakeholder-behoeften.

### Fase B: Striktheid Financiële Velden (Currency)
*   **Locatie:** §6 (Kassa) - `CurrencyAmountType`.
*   **Wijziging:** Wijzig `type="xs:string"` naar `fixed="eur"` voor het `currency` attribuut waar dit nog niet het geval is.
*   **Impact:** Dwingt het gebruik van Euro af op de Kassa-interfaces zoals afgesproken.

### Fase C: Target Architecture (Header Regex)
*   **Locatie:** §1 (Globale Regels - `HeaderType`).
*   **Wijziging:** Voeg een duidelijke commentaar/markering toe dat de `UUIDType` (met Regex) de **Target Architecture** is voor alle teams.
*   **Impact:** Moedigt teams aan om van simpele strings naar strikte validatie te migreren zonder bestaande flows direct te breken.

### Fase D: Verplichte Koppelingen (Correlation ID)
*   **Locatie:** §6.5 (`invoice_request`) en §6.4 (`refund_processed`).
*   **Wijziging:** Verwijder `minOccurs="0"` bij `correlation_id` in de XSD definities.
*   **Impact:** Garandeert dat de business logica (koppelen order aan factuur/refund) altijd over de juiste ID's beschikt.

## 3. Validatiestappen
1.  Controleer of alle 9+ `contact` blokken in het document zijn bijgewerkt.
2.  Verifieer dat `correlation_id` in §6.5 nu verplicht is.
3.  Check of `fixed="eur"` overal in de Kassa-sectie consistent is toegepast.

## 4. Rollback Plan
Indien de wijzigingen te veel conflicten veroorzaken, kunnen we terugvallen op de git-staat van voor deze wijzigingen.
