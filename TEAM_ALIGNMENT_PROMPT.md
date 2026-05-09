# MISSION BRIEFING: Unified Integration & Logging (Deadline - 48h)

**Context:** We are in the final integration phase. The central contract (v2.3) has been updated to support anonymous flows and unified validation. All teams MUST align with these rules immediately.

---

## 1. THE LOGGING MANDATE (Team Monitoring §3.5)
Every team must use the central `logs` queue (AMQP default exchange, queue name: `logs`) to track message flows.

### Use Cases:
1.  **Validation Log (Inbound):**
    *   **Action:** `xml_validation`
    *   **Logic:** Every time you receive a message, log the result. 
    *   **Level:** `info` if schema matches; `error` if it fails.
2.  **Flow Log (Outbound):**
    *   **Action:** Match the business context (`payment`, `invoice`, `registration`, etc.)
    *   **Logic:** Log when you successfully publish a message.
3.  **Error Log (Internal):**
    *   **Action:** `system_error`
    *   **Logic:** Log database timeouts, internal crashes, or 404s.

**XSD Requirement:** Use the standard `<message>` envelope with `<header>` (source/type="log"/version) and `<body>` (level/action/message).

---

## 2. PAYMENT_REGISTERED UPDATES (§6.6, §8.2, §11.5)
The schema for `payment_registered` is now **flexible** to support real-world festival scenarios.

*   **Anonymous Support:** `identity_uuid` and `invoice/id` are now **OPTIONAL** (`minOccurs="0"`). 
*   **Team Facturatie:** If `identity_uuid` is missing, map the payment to the **"Generic Bar Customer"** (Internal ID: 9999) for accounting.
*   **Unified Validation:** All `fixed` source constraints in headers are removed. Facturatie now uses ONE validator for all sources.

---

## 3. TEAM-SPECIFIC TASKS
*   **FRONTEND:** Implement `payment_registered` direct to `facturatie.incoming` (Issue #27). Do not wait for CRM.
*   **KASSA:** Ensure you can send payments without a badge scan (anonymous). Use `payment_context="consumption"`.
*   **CRM:** Do not block `payment_registered` messages if they are missing a UUID. Forward them as-is (Passthrough).
*   **FACTURATIE:** Update your consumer to handle null/missing `identity_uuid`. Link them to the generic customer.
*   **MONITORING:** Ensure Logstash is ready to map `action="xml_validation"` to a dedicated dashboard.

---

## 4. THE SIDECAR RULE
Do **NOT** implement heartbeat logic. The sidecar handles this. Focus 100% on your business logic and the `logs` queue.

**GOAL:** No message should move between teams without a corresponding `info` log in the monitoring system.
