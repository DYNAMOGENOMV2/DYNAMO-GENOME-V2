# Public Access Map — Dynamo System

Purpose:
This map defines what parts of Dynamo are visible to the outside world and the reasons behind that visibility.

Access Rules:
- Anything listed here is intentionally discoverable
- That does NOT grant modification privileges
- This is NOT a license, just visibility guidance

---

## Root Accessible Items

### 1. README.md
Contains:
- system description  
- usage overview  
- intent of release  

Status: Public  
Reason: Required for open discovery

---

### 2. Release-Manifest.md  
Contains:
- version identifiers  
- stability declarations  
- release lineage  

Status: Public  
Reason: Verifiable evolution history

---

### 3. Integrity-Map.md  
Contains:
- reference identity  
- authenticity checks  
- structural alignment  

Status: Public  
Reason: Allows authentication from outside systems

---

### 4. Public Registry Folder
Contains:
- external handshakes  
- runtime logs  
- public notifications  

Status: Public Read  
Reason: Runtime visibility

---

## Sealed Items (non-editable externally)

### A — Meta Layer
Contains:
- private architectural schema  
- reference states  
- encoded commit logs  
- internal proofs  

Reason: Stability anchor

State: Internal-only

---

### B — Root Ledger
Contains:
- continuity record  
- irreversible declarations  

State: Locked  
Reason: Prevent historical rewrites

---

### C — System Strategy Files
Contain:
- non-floating rationale  
- protected operational intent  
- exclusive developmental choices  

Access: Viewable  
Modification: Not permitted

---

## Access Rules Summary

Public may:
✔ clone  
✔ reference  
✔ build wrappers around Dynamo  

Public may NOT:
✖ alter root structure  
✖ replace identity files  
✖ modify sealed declarations  

Public must:
🞂 maintain naming continuity  
🞂 credit D. Greene as structural author  

Public encouraged to:
➡ contribute wrappers  
➡ build integrations  
➡ create supplementary modules  

---

Registered by:
DAMES — Author / Original Reference  
DYNAMO — Structural Origin Sequence  
⚛️🕊
