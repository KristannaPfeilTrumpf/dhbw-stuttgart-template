# Zitier-Guide: LaTeX mit BibLaTeX (DHBW-konform)

## Grundprinzipien

1. **Alles was nicht von dir ist → Quelle angeben**
2. **Jede Quelle im Literaturverzeichnis muss im Text zitiert sein**
3. **Jedes Zitat im Text muss im Literaturverzeichnis stehen**
4. **Einheitlich bleiben** – ein Stil für die gesamte Arbeit

## Zitierweise in LaTeX (numeric-Stil)

### Sinngemäßes Zitat (häufigster Fall!)
```latex
Die Low-Code-Entwicklung ermöglicht es, Anwendungen mit minimalem 
Programmieraufwand zu erstellen \cite[vgl.][S.~15]{mueller2024}.
```
→ Ergebnis: "... zu erstellen [vgl. 1, S. 15]."

### Direktes Zitat (selten verwenden!)
```latex
Laut Schmidt ist \enquote{die Datenqualität der entscheidende 
Erfolgsfaktor für digitale Prozesse} \cite[S.~42]{schmidt2023}.
```
→ Ergebnis: "... „die Datenqualität der entscheidende Erfolgsfaktor für digitale Prozesse" [2, S. 42]."

### Mehrere Quellen
```latex
Verschiedene Autoren bestätigen diesen Ansatz 
\cite{mueller2024, schmidt2023, weber2025}.
```
→ Ergebnis: "... diesen Ansatz [1, 2, 3]."

### Quelle ohne Seitenangabe (z.B. Webseite)
```latex
Microsoft beschreibt Power Apps als eine Low-Code-Plattform 
\cite{microsoft_powerapps}.
```

## BibLaTeX Entry-Typen

### Buch (@book)
```bibtex
@book{balzert2011,
    author    = {Balzert, Helmut},
    title     = {Lehrbuch der Softwaretechnik},
    subtitle  = {Entwurf, Implementierung, Installation und Betrieb},
    edition   = {3},
    publisher = {Spektrum Akademischer Verlag},
    address   = {Heidelberg},
    year      = {2011}
}
```

### Webseite (@online)
```bibtex
@online{microsoft_powerapps,
    author    = {{Microsoft Corporation}},
    title     = {What is Power Apps?},
    url       = {https://learn.microsoft.com/en-us/power-apps/powerapps-overview},
    urldate   = {2026-03-15},
    year      = {2025}
}
```
**Wichtig**: `urldate` = Datum der Einsichtnahme (Pflicht bei Internetquellen!)

### Zeitschriftenartikel (@article)
```bibtex
@article{weber2025,
    author  = {Weber, Anna and Fischer, Thomas},
    title   = {Automatisierung von Geschäftsprozessen mit Power Automate},
    journal = {Wirtschaftsinformatik \& Management},
    volume  = {17},
    number  = {2},
    pages   = {34--41},
    year    = {2025}
}
```

### Firmeninterne Quelle (@misc)
```bibtex
@misc{trumpf_prozess2024,
    author       = {{TRUMPF SE + Co. KG}},
    title        = {Prozessbeschreibung Stundenbuchung},
    howpublished = {Internes Dokument},
    year         = {2024},
    note         = {Nicht öffentlich zugänglich}
}
```

### Konferenzbeitrag (@inproceedings)
```bibtex
@inproceedings{chen2024,
    author    = {Chen, Li and Park, James},
    title     = {Low-Code Development in Enterprise Environments},
    booktitle = {Proceedings of the International Conference on Software Engineering},
    pages     = {112--120},
    year      = {2024},
    address   = {Lisbon}
}
```

## Seitenangaben – Regeln

| Situation | LaTeX-Code | Ergebnis |
|-----------|-----------|----------|
| Eine Seite | `\cite[S.~20]{quelle}` | [1, S. 20] |
| Folgeseite | `\cite[S.~20\,f.]{quelle}` | [1, S. 20 f.] |
| Mehrere Seiten | `\cite[S.~20\,ff.]{quelle}` | [1, S. 20 ff.] |
| Seitenbereich | `\cite[S.~20--25]{quelle}` | [1, S. 20–25] |
| Sinngemäß | `\cite[vgl.][S.~20]{quelle}` | [vgl. 1, S. 20] |

## Wann muss ich zitieren?

### MUSS zitiert werden:
- Definitionen von Fachbegriffen
- Aussagen über den Stand der Technik
- Statistische Daten und Zahlen
- Methoden/Frameworks die man verwendet
- Theoretische Konzepte
- Alle übernommenen Abbildungen/Tabellen

### Muss NICHT zitiert werden:
- Allgemeinwissen ("Das Internet verbindet Computer weltweit")
- Eigene Ergebnisse und Schlussfolgerungen
- Triviale Formeln (z.B. a² + b² = c²)
- Selbst erstellte Abbildungen (aber: "Eigene Darstellung" angeben!)

## Qualität der Quellen

### Gute Quellen (bevorzugen!)
- Fachbücher und Lehrbücher
- Peer-reviewed Zeitschriftenartikel
- Konferenzbeiträge
- Offizielle Dokumentationen (Microsoft Docs etc.)
- Normen und Standards

### Akzeptable Quellen (mit Vorsicht)
- Fachzeitschriften ohne Peer-Review
- Whitepapers von Unternehmen
- Hochschulschriften (Bachelor-/Masterarbeiten)
- Offizielle Firmen-Webseiten

### Schlechte Quellen (vermeiden!)
- Wikipedia (höchstens als Einstieg, nie als Beleg)
- Blogposts ohne erkennbare Autorenschaft
- Foren-Beiträge (Stack Overflow etc.)
- Social Media
- Nicht nachprüfbare Quellen

## Typische Fehler

1. **Quelle am Satzende ohne "vgl."**
   - ❌ `Datenqualität ist wichtig \cite{mueller2024}.`
   - ✅ `Datenqualität ist wichtig \cite[vgl.][S.~12]{mueller2024}.`

2. **Wikipedia als einzige Quelle für eine Definition**
   - ❌ Besser: Fachbuch oder Standardwerk verwenden

3. **Internetquelle ohne Zugriffsdatum**
   - ❌ Immer `urldate` angeben!

4. **Zu wenige Quellen**
   - Richtwert: mindestens 15–20 Quellen für 30 Seiten
   - Grundlagen-Kapitel sollte die meisten Quellen haben

5. **Nur Internetquellen**
   - Mix aus Büchern, Artikeln und Online-Quellen anstreben
