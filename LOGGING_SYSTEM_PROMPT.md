# PROJECT-WIDE LOGGING PROTOCOL: Monitoring & Traceability

**To all Teams (CRM, Kassa, Frontend, Planning, Facturatie, Mailing):**
To ensure the Monitoring team can track message flows and debug failures during the final 48h, every team MUST implement the following logging pattern using the central `logs` queue (AMQP default exchange, queue: `logs`).

---

## 1. MANDATORY USE CASES (Trigger Points)

Every team must log in the following three scenarios:

### A. Inbound Message (The "Validator" Log)
*   **Trigger:** The moment you receive any XML message from RabbitMQ.
*   **Action:** `xml_validation`
*   **Level:** 
    *   `info`: If the message passes XSD validation.
    *   `error`: If the message fails XSD validation.
*   **Message Format:** `"Received [Type] from [Source]. Validation: [Success/Failure]."`

### B. Outbound Message (The "Tracker" Log)
*   **Trigger:** Immediately after you successfully publish a message to RabbitMQ.
*   **Action:** Match the business context (e.g., `payment`, `invoice`, `registration`, `session`).
*   **Level:** `info`
*   **Message Format:** `"Published [Type] to [Queue/Exchange]. CorrelationID: [ID]."`

### C. System Failures (The "Emergency" Log)
*   **Trigger:** Catch blocks, database timeouts, or failed internal logic.
*   **Action:** `system_error`
*   **Level:** `error`
*   **Message Format:** `"Internal Error in [Module]: [Error Details]."`

---

## 2. TECHNICAL SPECIFICATION (§3.5)

### Message Structure:
All logs must follow the **§3.5 XSD** envelope:
*   **Header:**
    *   `source`: Your team name (`kassa`, `crm`, etc.)
    *   `type`: `log`
    *   `version`: `2.0`
*   **Body:**
    *   `level`: `info` | `warning` | `error`
    *   `action`: Use one of the predefined enums (see §3.5)
    *   `message`: Human-readable description including IDs for tracing.

---

## 3. GOAL FOR MONITORING TEAM
By following this uniform pattern, the Monitoring team can build a **"Message Journey" Dashboard**:
1.  **Step 1:** Frontend logs "Published registration"
2.  **Step 2:** CRM logs "Received registration - Validation: Success"
3.  **Step 3:** CRM logs "Published registration to Kassa"
4.  **Step 4:** Kassa logs "Received registration - Validation: Success"

**If any log is missing or shows an `error`, we know exactly where the pipe is broken.**
