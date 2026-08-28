# 🎯 Test-Coverage Frontend – Team-Übersicht

**Stand:** Q1 2025 | **Zielwert:** 75-85%

---

## 📊 Schnell-Status

| Status | Bereiche | Coverage | Codezeilen ungetestet |
|:------:|---------|:--------:|:---------------------:|
| ✅ | Guards, Validierung, Interfaces | **89-97%** | ~30 |
| 🟡 | Search, UI-Components, Auth | **66-78%** | ~1.500 |
| 🔴 | **Experiment-Wizard, Services, Dashboard** | **45-58%** | **~5.000** |

---

## ⚠️ Top 3 Handlungsfelder

### 1. 🔴 Experiment-Wizard – **KRITISCH**
```
Coverage:     47,5% (2.830 von 5.959 Zeilen)
Ungetestet:   3.129 Zeilen
Risiko:       Fehlerhafte Berechnungen, Datenverlust
```
**→ Höchste Priorität:** Beam-Calc, Parameter-Validierung, Panel-Logik

---

### 2. 🔴 Services (Backend-API)
```
Coverage:     57,7% (806 von 1.397 Zeilen)
Ungetestet:   591 Zeilen
Risiko:       API-Fehler, fehlerhafte Datenübertragung
```
**→ Fokus:** ExperimentService, ParameterService, State-Services

---

### 3. 🔴 Experiment-Dashboard
```
Coverage:     44,9% (262 von 584 Zeilen)
Ungetestet:   322 Zeilen
Risiko:       Main-Entry-Point, erste User-Interaktion
```
**→ Fokus:** Grid-Config, Filter-Logik, Navigation

---

## ✅ Was läuft gut

| Bereich | Coverage | Status |
|---------|:--------:|--------|
| Shared (Validierung) | 94,7% | Sehr gut abgesichert |
| Guards (Zugriffsschutz) | 89,5% | Production-ready |
| Search-Strategie | 77,5% | Solide Basis, Feature komplett |

---

## 📋 Action Items

### Sprint-Planung

**Must-Have (nächste 2 Sprints):**
- [ ] Experiment-Wizard: Beam-Calculation-Tests (→ +15% Coverage)
- [ ] Experiment-Wizard: Setup-Page-Tests (→ +10% Coverage)
- [ ] Services: ExperimentService Unit-Tests (→ +8% Coverage)

**Should-Have (Quartal):**
- [ ] Dashboard: Grid-Config & Filter-Tests
- [ ] Wizard: Parameter-Table-Tests
- [ ] Services: Restliche Domain-Services

**Nice-to-Have:**
- [ ] Tools-Features auf 70% bringen
- [ ] Auth auf 75% erhöhen

---

## 📈 Fortschritts-Tracking

```
Ziel Q2 2025:  Experiment-Wizard von 47,5% → 75%
Sprint-Ziel:   +5-8% pro Sprint (ca. 300-500 Zeilen)
Dauer:         ~4-5 Sprints für kritische Bereiche
```

---

## 🔍 Details nach Bereich

<details>
<summary><b>Vollständige Liste</b> (Klick zum Aufklappen)</summary>

| Bereich | Coverage | Zeilen getestet | Zeilen gesamt | Status |
|---------|:--------:|:---------------:|:-------------:|:------:|
| Interfaces | 96,5% | 139 | 144 | ✅ |
| Shared (Validierung) | 94,7% | 54 | 57 | ✅ |
| Guards | 89,5% | 17 | 19 | ✅ |
| **Search-Strategie** | **77,5%** | 2.093 | 2.699 | 🟡 |
| UI-Components (common) | 75,3% | 1.049 | 1.394 | 🟡 |
| Report-Preview | 73,5% | 125 | 170 | 🟡 |
| Layout | 70,7% | 82 | 116 | 🟡 |
| Utilities | 68,1% | 126 | 185 | 🟡 |
| **Auth** | **65,6%** | 149 | 227 | 🟡 |
| **Services** | **57,7%** | 806 | 1.397 | 🔴 |
| Tools-Features | 53,9% | 292 | 542 | 🔴 |
| **Experiment-Wizard** | **47,5%** | 2.830 | 5.959 | 🔴 |
| **Dashboard** | **44,9%** | 262 | 584 | 🔴 |

</details>

---

## 💡 Unterstützung

**Testing-Guidelines:** `.github/copilot-instructions.md`  
**CI-Pipeline:** Läuft bei jedem PR (Vitest + Coverage-Report)  
**Coverage-Report:** `npm run test -- --coverage`

---

_Legende: ✅ Sehr gut (>85%) | 🟡 Akzeptabel (65-85%) | 🔴 Handlungsbedarf (<65%)_
