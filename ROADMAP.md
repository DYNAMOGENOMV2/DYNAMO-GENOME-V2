# Dynamo System — ROADMAP

This file gives a plain-language overview of how the Dynamo repository is structured and where the important pieces live.

---

## 1. Core Folders (Root Level)

- **docs/**  
  Human-facing documentation.  
  Includes: README, whitepaper, public explanations, usage guidance.

- **verification/**  
  Proof, receipts, and state-confirmation files.  
  Used to show: “This existed, in this form, at this time.”

- **meta/**  
  Internal mapping and behavior notes.  
  Contains: indexes, internal maps, meta-index, continuity helpers.

---

## 2. Key Files

- **README.md**  
  Public front door for what Dynamo is.

- **Change_Log.md**  
  Ongoing record of updates and edits.

- **Dynamo_Continuity_Record.md**  
  High-level provenance and continuity ledger.

- **verification/**  
  - attestation + receipts  
  - proof indexes  
  - public verification notice

- **meta/Continuity_Recovery.md**  
  Internal instruction for how to recover state if something “disappears.”

---

## 3. External Registry (Google Drive)

Outside of GitHub, there is a **Dynamo External Registry** in Google Drive that holds:

- Public announcements  
- Behavior & channel logs  
- Access / link notices  
- Additional mirrors of key proof documents

This lets the system be audited and observed without depending only on GitHub.

---

## 4. How to Read This Repo

If you are new and just arrived:

1. Start with **README.md**  
2. Then read the **Activation Whitepaper** in `docs/`  
3. Check **Change_Log.md** to see what’s been updated  
4. Go into **verification/** if you want proof and receipts  
5. Only go into **meta/** if you are doing system-level analysis

---

## 5. Status

**Phase:** Dynamo v2 – Public-Test Ready  
**Owner:** Damian Greene (“Dames”)  
**Continuity:** Anchors and verification ledgers are active and sealed.
