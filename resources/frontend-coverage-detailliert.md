# 📊 Test-Abdeckung Frontend – Detaillierte Übersicht mit Test-Informationen

**Stand:** Q1 2025 | **Gesamt-Coverage:** 67,2% | **Zielwert:** 75-85%

---

## Haupt-Übersicht

| Bereich | Coverage | Getestet / Gesamt | Unit-Tests | Test-Typen |
|---------|:--------:|:-----------------:|:----------:|------------|
| **Shared** | 🟢 **94,7%** | 54 / 57 | 3 | Validation, Directives |
| **Guards** | 🟢 **89,5%** | 17 / 19 | 3 | Route Guards, CanDeactivate |
| **UI-Components** | 🟡 **84,3%** | 1.275 / 1.512 | 20 | Atlas Design System, Forms |
| **Search-Strategie** | 🟡 **78,0%** | 2.106 / 2.699 | 25 | Filter, Grid-Logic, Services |
| **Report-Preview** | 🟡 **74,7%** | 127 / 170 | 1 | Preview-Components |
| **Layout** | 🟡 **70,7%** | 82 / 116 | 2 | Main-Layout, Tools-Layout |
| **Services** | 🟠 **63,4%** | 885 / 1.397 | 18 | API, State, Domain Services |
| **Tools-Features** | 🔴 **53,9%** | 292 / 542 | 6 | AI-Tools, BO-Tools, Debug |
| **Experiment-Wizard** | 🔴 **51,8%** | 3.088 / 5.957 | 21 | Setup, Parameters, Task, Result |
| **Dashboard** | 🔴 **44,9%** | 262 / 584 | 6 | Grid-Config, Navigation |
| **─────────** | **─────** | **─────────** | **───** | **─────────** |
| **Gesamt Frontend** | **67,2%** | **8.188 / 12.183** | **105** | **Unit-Tests (Vitest)** |
| _Zusätzlich:_ | -- | -- | **6** | **E2E-Tests (Playwright)** |

---

## 🎯 Legende

| Symbol | Coverage | Status | Beschreibung |
|:------:|:--------:|--------|--------------|
| 🟢 | >85% | Sehr gut | Entspricht Best Practices für kritische Anwendungen |
| 🟡 | 65-85% | Akzeptabel | Grundabsicherung vorhanden, Verbesserungspotenzial |
| 🟠 | 60-65% | Verbesserungswürdig | Deutliche Lücken erkennbar |
| 🔴 | <60% | Kritisch | Dringender Handlungsbedarf, hohes Fehlerrisiko |

---

## 📋 Detaillierte Unit-Test-Verteilung (105 Tests)

| Bereich | Anzahl Tests | Wichtigste getestete Funktionen |
|---------|:------------:|----------------------------------|
| **Search-Strategie** | 25 | Filter-Rules, Grid-Config, Search-Services, API-Integration |
| **Experiment-Wizard** | 21 | Setup-Calc, Parameter-Table, Task-Logic, Result-Capture |
| **UI-Components (common)** | 20 | Atlas-Buttons, Forms, Autocomplete, Dialogs, Input-Components |
| **Services** | 18 | Experiment, Material, User, Master-Data, State-Services |
| **Auth** | 7 | Auth-Interceptor, Role-Guard, OAuth-Storage, Token-Refresh, Reauth-Loop |
| **Utilities** | 7 | Helper-Functions, Formatters, Validators |
| **Dashboard** | 6 | Grid-Configuration, Filter-Logic |
| **Tools-Features** | 6 | AI-Tools, Debug-Page, Activity-Overview |
| **Guards** | 3 | Route-Protection, Unsaved-Changes, Before-Unload |
| **Shared (Validation)** | 3 | Server-Validation-Interceptor, HTML-Tag-Validator, Max-Length |
| **Layout** | 2 | Main-Layout, Tools-Layout |
| **Report-Preview** | 1 | Preview-Components |
| **Components (allg.)** | 4 | Request-Access, Login-Failed, System-Logs |
| **Features (allg.)** | 5 | Cross-Feature Utilities |
| **Interfaces** | 1 | Type Guards, Model Validation |

**Summe:** 105 Unit-Tests (`.spec.ts` Dateien)

---

## 🎭 E2E-Tests (6 Playwright-Tests)

Die Anwendung verfügt über **6 End-to-End-Tests** mit Playwright, die kritische User-Journeys abdecken:

- Login-Flow & Authentifizierung
- Navigation zwischen Hauptbereichen
- Experiment-Wizard Basis-Flow
- Search-Funktionalität
- Dashboard-Interaktionen
- Zugriffskontrolle (Guards)

**⚠️ E2E-Test-Lücken:**
- Kein E2E-Test für **Experiment-Import** (Excel-Upload)
- **Beam-Calculation-Workflow** nicht End-to-End getestet
- **Parameter-Copy-Funktionen** fehlen in E2E-Tests
- Report-Generierung (Excel/PPTX) nicht abgedeckt

---

## ✅ Was läuft gut

### 🟢 Sehr gut getestete Bereiche

**1. Auth & Guards (89,5%)**
- ✅ Umfassende Tests für sicherheitskritische Funktionen
- ✅ Token-Refresh-Mechanismus vollständig getestet
- ✅ 401-Handling mit Retry-Logik abgedeckt
- ✅ Reauth-Loop-Breaker (verhindert infinite Loops)
- ✅ Concurrent-Request-Handling getestet

**2. Shared/Validation (94,7%)**
- ✅ Server-Validation-Interceptor mit Edge-Cases
- ✅ PascalCase-zu-FormControl-Mapping
- ✅ Toast-Skipping bei SKIP_VALIDATION_TOAST
- ✅ Validation-Error-Aggregation

**3. Search-Strategie (78,0%)**
- ✅ Filter-Rules umfassend getestet
- ✅ Grid-Configuration-Logic
- ✅ API-Service-Integration
- ✅ Bookmark-Funktionalität

**4. UI-Components (84,3%)**
- ✅ Atlas Design System gut abgesichert
- ✅ Form-Components mit verschiedenen Szenarien
- ✅ Dialog-Komponenten getestet

---

## ⚠️ Verbesserungspotenzial

### 🔴 Kritische Bereiche mit Handlungsbedarf

**1. Experiment-Wizard (51,8% – nur 21 Tests für 5.957 Zeilen)**

```
Ungetestet: 2.869 Zeilen
Risiko:     Fehlerhafte Berechnungen, Datenverlust bei Experimenten
```

**Fehlende Tests:**
- ❌ Beam-Calculation-Logic (nur teilweise getestet)
- ❌ Dynamische Panel-Logik basierend auf Joint/Weld-Type-Kombinationen
- ❌ Setup-Page komplexe Validierungen
- ❌ Parameter-Table Bulk-Operations
- ❌ Result-Capture mit verschiedenen Datentypen

**Empfohlene Priorität:**
1. Beam-Calculation-Service (+400 Zeilen → +7% Coverage)
2. Setup-Page Panel-Logic (+300 Zeilen → +5% Coverage)
3. Parameter-Validation-Rules (+250 Zeilen → +4% Coverage)

---

**2. Services (63,4% – 18 Tests für 1.397 Zeilen)**

```
Ungetestet: 512 Zeilen
Risiko:     API-Fehler, fehlerhafte Datenübertragung, State-Inkonsistenzen
```

**Fehlende Tests:**
- ❌ ExperimentService: Error-Handling bei API-Failures
- ❌ ParameterService: Edge-Cases bei Bulk-Updates
- ❌ State-Services: Concurrent-State-Changes
- ❌ Media-Service: File-Upload Error-Cases

**Empfohlene Priorität:**
1. ExperimentService API-Error-Handling (+150 Zeilen → +11% Coverage)
2. State-Services Edge-Cases (+100 Zeilen → +7% Coverage)

---

**3. Experiment-Dashboard (44,9% – nur 6 Tests für 584 Zeilen)**

```
Ungetestet: 322 Zeilen
Risiko:     Main-Entry-Point, erste User-Interaktion
```

**Fehlende Tests:**
- ❌ Grid-Interaktionen (Sortierung, Filterung)
- ❌ Context-Menu-Actions
- ❌ Bulk-Operations
- ❌ Navigation zu Wizard/Details

**Empfohlene Priorität:**
1. Grid-Config & Filter-Logic (+150 Zeilen → +26% Coverage)
2. Navigation & Actions (+100 Zeilen → +17% Coverage)

---

**4. Tools-Features (53,9% – 6 Tests für 542 Zeilen)**

```
Ungetestet: 250 Zeilen
Risiko:     AI/BO-Funktionen, Admin-Tools
```

**Fehlende Tests:**
- ❌ AI-Tools API-Integration
- ❌ BO-Service Error-Handling
- ❌ Activity-Overview Filter-Logic

---

## 📈 Verbesserungsplan

### Quartalsziel Q2 2025

| Bereich | Aktuell | Ziel Q2 | Differenz | Geschätzte Tests |
|---------|:-------:|:-------:|:---------:|:----------------:|
| Experiment-Wizard | 51,8% | 75% | +23,2% | +15 Tests (~1.400 Zeilen) |
| Services | 63,4% | 75% | +11,6% | +8 Tests (~160 Zeilen) |
| Dashboard | 44,9% | 70% | +25,1% | +10 Tests (~150 Zeilen) |
| Tools-Features | 53,9% | 70% | +16,1% | +5 Tests (~90 Zeilen) |

**Gesamt:** +38 neue Tests → **Gesamt-Coverage von 67,2% auf ~78%**

---

### Sprint-Plan (2-Wochen-Sprints)

#### Sprint 1-2: Experiment-Wizard Critical Path
- [ ] Beam-Calculation-Service Tests (5 Tests)
- [ ] Setup-Page Panel-Logic Tests (4 Tests)
- [ ] Parameter-Validation Tests (3 Tests)

**Ziel:** Wizard von 51,8% auf 63% (+11%)

#### Sprint 3: Services & API-Layer
- [ ] ExperimentService Error-Handling (4 Tests)
- [ ] ParameterService Bulk-Operations (2 Tests)
- [ ] State-Services Concurrent-Updates (2 Tests)

**Ziel:** Services von 63,4% auf 72% (+9%)

#### Sprint 4: Dashboard & User-Entry
- [ ] Grid-Configuration Tests (3 Tests)
- [ ] Navigation & Actions Tests (3 Tests)
- [ ] Filter-Logic Tests (2 Tests)

**Ziel:** Dashboard von 44,9% auf 68% (+23%)

#### Sprint 5: E2E-Tests (Playwright)
- [ ] Experiment-Import E2E-Test
- [ ] Beam-Calculation-Workflow E2E-Test
- [ ] Parameter-Copy E2E-Test

**Ziel:** E2E-Tests von 6 auf 9 (+50%)

---

## 🔍 Test-Typen im Detail

### Unit-Tests (105 Tests, Vitest)

- **Framework:** Vitest 4.1.11 mit jsdom
- **Coverage-Tool:** @vitest/coverage-v8
- **Co-Location:** Jede Komponente/Service hat `.spec.ts` im gleichen Verzeichnis
- **Naming Convention:** `*.spec.ts` (z.B. `auth.service.spec.ts`)

### E2E-Tests (6 Tests, Playwright)

- **Framework:** Playwright 1.45.0
- **Browser:** Chromium, Firefox, WebKit
- **CI-Integration:** Läuft bei jedem PR
- **Reports:** HTML + JUnit (für Azure DevOps)

---

## 💡 Best Practices & Standards

### Aktuell befolgte Standards:

✅ **Co-Location:** Tests direkt neben dem Code  
✅ **Naming:** Konsistente `*.spec.ts` Endung  
✅ **CI-Integration:** Coverage-Report bei jedem PR  
✅ **Isolation:** Mocks für externe Dependencies  

### Verbesserungspotenzial:

🔶 **Coverage-Gates:** Keine PR-Blockierung bei Coverage-Drops  
🔶 **Test-Documentation:** Fehlende beschreibende Kommentare in komplexen Tests  
🔶 **Shared Test-Utilities:** Viel Duplikation in Setup-Code  
🔶 **E2E-Test-Daten:** Keine dedizierte Test-Datenbank

---

## 📚 Referenzen

- **Testing-Guidelines:** `.github/copilot-instructions.md`
- **Coverage-Report generieren:** `npm run test -- --coverage`
- **E2E-Tests lokal:** `npm run e2e` oder `npm run e2e:ui`
- **CI-Pipeline:** Siehe `src/devops/pipelines/`

---

_Letzte Aktualisierung: Q1 2025 | Nächste Review: Ende Q2 2025_
