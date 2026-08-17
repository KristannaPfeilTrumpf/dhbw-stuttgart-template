---
name: skill-wissenschaftliche-arbeit-latex
description: 'Wissenschaftliche Projektarbeit LaTeX DHBW T2000 T3000. Use when: writing academic thesis, Projektarbeit, Bachelorarbeit; reviewing LaTeX documents for scientific writing style; checking DHBW formatting requirements; improving Einleitung, Grundlagen, Reflexion chapters; fixing citations BibLaTeX; correcting academic German style; validating figure/table references.'
argument-hint: 'Beschreibe was du brauchst: Kapitel schreiben, Text verbessern, Formatierung prüfen'
---

# Wissenschaftliche Projektarbeit (LaTeX) – DHBW

Dieser Skill unterstützt beim Erstellen wissenschaftlicher Arbeiten (T2000/T3000) für DHBW-Studierende in LaTeX.

## Wann diesen Skill verwenden

- Kapitel schreiben oder verbessern (Einleitung, Grundlagen, Reflexion)
- Text auf wissenschaftlichen Stil prüfen
- Formatierung und DHBW-Anforderungen validieren
- Zitierweise und BibLaTeX korrigieren
- Abbildungen/Tabellen korrekt einbinden

## Kernregeln (Kurzfassung)

### Formale Anforderungen
- **Umfang**: 25–35 Seiten (ohne Verzeichnisse/Anhänge)
- **Format**: DIN A4, einseitig, 1,5-zeilig, 12pt, mind. 2,5 cm Rand
- **Sprache**: Deutsch, gendergerecht, wissenschaftlicher Stil (kein "Ich habe...")

### Kapitelstruktur
1. Einleitung (Problemstellung, Ziel, Vorgehen) – 3-4 Seiten
2. Grundlagen (Stand der Technik) – 5-7 Seiten
3. Analyse/Anforderungen – 5-6 Seiten
4. Umsetzung – 7-9 Seiten
5. Test/Einführung – 4-5 Seiten
6. Reflexion & Ausblick – 1-1,5 Seiten

### Schreibstil
- **DO**: Passiv/unpersönlich ("Es wurde analysiert..."), Fachbegriffe, Belege
- **DON'T**: Erzählstil, Umgangssprache, unbelegte Aussagen

### LaTeX
- Querverweise: `\ref{}` + `\label{}`
- Abbildungen: `figure`-Umgebung mit `\caption` + `\label`
- Literatur: biblatex mit biber

## Detaillierte Guides

Für ausführliche Anleitungen siehe:
- [Schreibstil-Guide](./guides/schreibstil-guide.md) – Formulierungen, Textstruktur, häufige Fehler
- [Zitieren-Guide](./guides/zitieren-guide.md) – BibLaTeX, Quellenarten, Beispiele
- [LaTeX-Tipps](./guides/latex-tipps.md) – Abbildungen, Tabellen, Code-Listings, Kompilieren
- [Bewertung & Tipps](./guides/bewertung-und-tipps.md) – Bewertungskriterien, Prüfungsvorbereitung

## Beispiel

Siehe [Beispiel-Einleitung](./examples/beispiel_einleitung.tex) für ein ausgearbeitetes Kapitel.

## Workflow

1. **Thema definieren**: Problemstellung klar formulieren, Ziele SMART definieren
2. **Struktur anlegen**: Kapitel als separate .tex-Dateien
3. **Kapitelweise schreiben**: Quellen sofort eintragen, regelmäßig kompilieren
4. **Review**: Formale Vorgaben prüfen, alle Referenzen vollständig?
5. **Finalisieren**: Abstract am Ende schreiben, PDF prüfen

## Wichtige Hinweise

- Eigenanteil muss **eindeutig erkennbar** sein
- Grundlagen auf das **Nötigste beschränken**
- Jede Abbildung/Tabelle im Text **referenzieren und erklären**
- Ziele und Vorgehen **nicht vermischen**
- Reflexion: auch **Grenzen und Probleme** benennen
