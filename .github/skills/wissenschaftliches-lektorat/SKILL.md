---
name: wissenschaftliches-lektorat
description: 'Wissenschaftliches Lektorat für akademische Texte auf Deutsch. Use when: Lektorieren, Korrekturlesen, sprachliche Überarbeitung, Stilverbesserung, Rechtschreibprüfung, Grammatikkorrektur für Haus-, Bachelor-, Master-, Projektarbeiten; Sachlichkeit, Präzision, Nachvollziehbarkeit, Objektivität prüfen.'
argument-hint: 'Füge den zu überarbeitenden Textabschnitt ein'
---

# Wissenschaftliches Lektorat

Sprachliche und stilistische Überarbeitung akademischer Texte auf Deutsch.

## Wann verwenden

- Überarbeitung von Abschnitten aus Haus-, Bachelor- oder Masterarbeiten
- Prüfung auf Sachlichkeit, Präzision, Nachvollziehbarkeit und Objektivität
- Korrektur von Rechtschreibung, Grammatik und Zeichensetzung
- Stilverbesserung für wissenschaftliche Texte

## Checkliste

Prüfe jeden Text systematisch anhand dieser Checkliste:

### 1. Rechtschreibung
- [ ] Korrekte Schreibweise aller Wörter
- [ ] Groß-/Kleinschreibung beachtet
- [ ] Getrennt-/Zusammenschreibung korrekt
- [ ] Fachbegriffe einheitlich geschrieben

### 2. Grammatik
- [ ] Kasus (Fälle) korrekt
- [ ] Kongruenz Subjekt-Prädikat
- [ ] Bezüge von Pronomen eindeutig
- [ ] Satzbau grammatikalisch korrekt

### 3. Kommasetzung
- [ ] Kommas bei Nebensätzen
- [ ] Kommas bei Relativsätzen
- [ ] Kommas bei Infinitivgruppen mit "zu"
- [ ] Kommas bei Aufzählungen
- [ ] Kommas bei Einschüben und Appositionen

### 4. Zeitform
- [ ] Kapitelspezifische Zeitform beachtet (siehe Abschnitt Zeitformen)
- [ ] Abgeschlossene Arbeitsschritte → Präteritum/Perfekt
- [ ] Funktionsbeschreibungen/Definitionen → Präsens
- [ ] Interpretationen/allgemeingültige Aussagen → Präsens
- [ ] Kein historisches Präsens

### 5. Satzaufbau
- [ ] Sätze nicht zu lang (max. 25-30 Wörter)
- [ ] Hauptaussage nicht in Nebensätzen versteckt
- [ ] Aktiv statt Passiv wo sinnvoll
- [ ] Keine Schachtelsätze

### 6. Struktur
- [ ] Überschriften präzise und aussagekräftig
- [ ] Übergänge zwischen Abschnitten vorhanden
- [ ] Logischer Aufbau erkennbar
- [ ] Roter Faden durchgängig

### 7. Wissenschaftlicher Stil
- [ ] **Sachlichkeit**: Keine umgangssprachlichen Verstärker ("total", "irgendwie", "ziemlich")
- [ ] **Präzision**: Konkrete statt vage Formulierungen
- [ ] **Nachvollziehbarkeit**: Aussagen belegt oder begründet
- [ ] **Objektivität**: Keine persönliche Meinung, keine wertenden Adjektive

### 8. LaTeX-Formatierung
- [ ] Anführungszeichen als `\enquote{}`
- [ ] Hervorhebungen nur mit `\textbf{}` wo nötig
- [ ] Akronyme mit `\ac{}`
- [ ] Querverweise mit `\ref{}` und `\autocite{}`

## Grundregeln

### Verbindliche Sprachregeln für jede Textgenerierung
- Verwende keine Semikolons im generierten Text.
- Verwende in keinem Fall die Begriffe "Ich", "wir" oder "man" als eigenständige Wörter im generierten Text.
- Halte die Bezeichnung für Personenrollen innerhalb aller Kapitel konsistent, zum Beispiel durchgehend "Anwender" oder durchgehend "Nutzer".

### Sprache
Arbeite ausschließlich auf Deutsch. Weise bei anderen Sprachen darauf hin.

### Fachlicher Inhalt
- Verändere niemals die fachliche Kernaussage, These oder den Erkenntnisgehalt
- Erfinde keine neuen Belege, Quellen oder Fakten
- Bei fachlicher Unsicherheit: nur Sprache korrigieren, Fachbegriffe unverändert lassen

### Bearbeitungsumfang
- Bearbeite nur den bereitgestellten Text.
- Keine vollständige Dokumentüberarbeitung außerhalb des bereitgestellten Textes ohne expliziten Auftrag.
- Bei Aufforderungen wie "verbessern", "überprüfen" oder "anpassen" wird der bereitgestellte Text vollständig anhand der Checkliste geprüft und überarbeitet.
- Bei langen Texten erfolgt die Bearbeitung abschnittsweise, der gesamte bereitgestellte Text bleibt dennoch vollständig im Prüfbereich.

### Überschriften
Eine Überschrift soll dem Leser direkt vermitteln, was er im Kapitel findet. Zu allgemeine Titel wie "Vorbereitung" oder "Grundlagen" sind zu vermeiden, wenn der konkrete Inhalt nicht erkennbar wird. Schlage bei unspezifischen Überschriften präzisere Alternativen vor, zum Beispiel:
- "Vorbereitung" → "Anforderungsanalyse und Ist-Prozess"
- "Grundlagen" → "Controlling und technische Grundlagen"

### Übergänge zwischen Abschnitten
Ein Abschnitt soll am Ende einen klaren Übergang zum nächsten schaffen. Der Leser muss verstehen, warum der folgende Abschnitt kommt, ohne ihn erst lesen zu müssen. Vermeide abrupte Enden, die den Zusammenhang offen lassen. Stattdessen:
- Die Konsequenz oder den Handlungsbedarf formulieren
- Den logischen Anschluss zum Folgeabschnitt herstellen
- Bei Bedarf einen Brückensatz ergänzen, der das Gesagte mit dem Kommenden verbindet

**Beispiel (Ausgangssituation und Problemstellung):**
- Vorher: "Zur Verbesserung der Datenqualität sowie zur Effizienzsteigerung wurde bereits die Entwicklung einer softwaregestützten Lösung initiiert."
- Nachher: "Zur Effizienzsteigerung wurde bereits eine Lösung mit Microsoft Power Apps und Power Automate begonnen."
- Grund: Redundanz entfernt ("Datenqualität" nicht Kernziel), konkrete Technologien genannt statt "softwaregestützte Lösung"


## Vier Qualitätsdimensionen

### 1. Sachlichkeit
Nüchterner, emotionsfreier Ton. Entferne umgangssprachliche Verstärker:
- "total", "irgendwie", "ziemlich", "eigentlich"
- Wertende Ausdrücke ohne Beleg

### 2. Präzision
Konkrete statt vage Formulierungen:
- Exakte Begriffe statt Näherungen
- Spezifische Angaben statt Verallgemeinerungen

**Beispiel (Technologiebeschreibung):**
- Vorher: "Es dient dazu, häufige Prozesse, die zeitintensiv und fehleranfällig sind, zu automatisieren."
- Nachher: "Die Technologie dient dazu, wiederkehrende Prozesse, die manuell zeitintensiv und fehleranfällig sind, zu automatisieren."
- Grund: "Es" durch konkreten Bezug ersetzt, "häufig" durch "wiederkehrend" präzisiert, "manuell" ergänzt die Begründung für Zeitaufwand


### 3. Nachvollziehbarkeit
Aussagen an Belege oder Argumentation binden:
- Keine unbelegten Absolutheiten wie "beweist zweifelsfrei" oder "jeder weiß"
- Keine Behauptungen ohne Grundlage im Text

### 4. Objektivität
Ausgewogene Darstellung:
- Keine persönliche Meinung
- Keine wertenden Adjektive über Personen oder Positionen

## Zeitformen

Die korrekte Zeitform hängt vom Kapitel und der Art der Aussage ab. Grundregel: Abgeschlossene Untersuchungen und durchgeführte Arbeitsschritte stehen in der Vergangenheit (Präteritum/Perfekt). Präsens nur für allgemeingültige Feststellungen, Funktionsbeschreibungen und Interpretationen.

### Abstract/Zusammenfassung
- **Präsens**: Allgemeine Fakten, Thema der Arbeit umreißen
  - "In der vorliegenden Arbeit wird der Prozess untersucht."
- **Perfekt**: Vergangene Ereignisse
  - "Die Entwicklung hat vor zwei Jahren begonnen."

### Einleitung
- **Präsens**: Ausgangspunkt, Forschungsstand, Ziel der Arbeit
  - "Ziel der Arbeit ist eine Analyse der..."
- **Perfekt**: Historischer Hintergrund
  - "Es wurde bereits eine Lösung entwickelt."

### Theoretischer Teil / Grundlagen
- **Präsens**: Publiziertes Wissen, Definitionen, Funktionsweise (anhand von Abbildungen)
  - "Die Herzfrequenz ist die Anzahl der Herzschläge pro Minute."
- **Präteritum/Perfekt**: Explizite Verweise auf Erfindungen/Schöpfungen anderer
  - "..., was als erstes von Mayer (1980) herausgestellt wurde."

### Methodenteil
- **Präsens**: Beschreibung des Untersuchungsgebiets (besteht noch), bekannte Methoden
  - "Das Versorgungsgebiet erstreckt sich über ca. 20 km²."
- **Präteritum/Perfekt**: Tatsächlich durchgeführte Arbeitsschritte
  - "An der Untersuchung nahmen insgesamt 50 Personen teil."
  - "Die Daten wurden in einer SharePoint-Liste gespeichert."

### Ergebnisteil
- **Präteritum/Perfekt**: Darlegung der Forschungsergebnisse
  - "Die Hypothesen konnten nicht bestätigt werden."
  - "Die Befragung hat ergeben, dass..."

### Fazit / Diskussion
- **Präsens**: Interpretation der gewonnenen Erkenntnisse
  - "Die Untersuchung zeigt, dass..."
- **Präteritum/Perfekt**: Bezug auf konkrete Ergebnisse
  - "Die Experteninterviews haben gezeigt, dass..."

### Nicht empfohlen: Historisches Präsens
Das historische Präsens (vergangene Ereignisse im erzählerischen Ton in Gegenwartsform) ist für wissenschaftliche Arbeiten nicht geeignet.
- Falsch: "Napoleon stirbt am 5. Mai 1821."
- Richtig: "Napoleon starb am 5. Mai 1821."

## Rechtschreibung und Zeichensetzung

Prüfe besonders:
- Deutsche Kommaregeln (Nebensätze, Relativsätze, Infinitivgruppen mit "zu")
- Anführungszeichen als LaTeX-Befehl `\enquote{}`
- Interpunktion bei Aufzählungen, Zitaten und Einschüben

### Hervorhebungen
- Verwende `\textbf{}` nur bei vorhandener Hervorhebung im Original
- Keine neuen Hervorhebungen ohne Anlass

## Ausgabeformat

Gib die Antwort in dieser Reihenfolge aus:

### 1. Überarbeiteter Text
LaTeX-fähig formatiert mit aktiven Befehlen (`\textbf{}`, `\enquote{}`), direkt einfügbar ohne Präambel.

### 2. Sprachliche Korrekturen
Liste der Korrekturen zu Rechtschreibung, Grammatik und Zeichensetzung. Jeder Punkt nennt kurz, was geändert wurde.

Falls keine Korrekturen nötig: "Keine Korrekturen erforderlich."

### 3. Stilistische/inhaltliche Anpassungen
Liste der Änderungen zu den vier Qualitätsdimensionen. Jeder Punkt nennt, was geändert wurde und warum.

Falls keine Anpassungen nötig: "Keine Anpassungen erforderlich."

### Formatregeln für die Ausgabe
- Keine Semikolons.
- Keine eigenständigen Wörter "Ich", "wir" oder "man".
- Klare, kurze Hauptsätze mit eindeutigen Bezügen.

## Schreibstil für Ausgaben

- Ergebnis früh nennen, ohne einleitende Floskeln
- Klare, konkrete Verben
- Kurze Absätze
- Keine Füllwörter, Floskeln, Emojis, Ausrufezeichen
- Keine Konstruktion "Es ist nicht nur X, sondern auch Y"
- Fachbegriffe, Eigennamen, Zitate unverändert lassen

## Ablauf

1. Prüfe, ob Text eingefügt wurde. Falls nicht: gezielt nachfragen
2. Prüfe den gesamten bereitgestellten Text systematisch anhand der vollständigen Checkliste.
3. Überarbeite den Text nach den vier Qualitätsdimensionen.
4. Korrigiere Rechtschreibung, Grammatik und Zeichensetzung.
5. Formatiere LaTeX-kompatibel
6. Erstelle beide Korrekturlisten
7. Führe eine Abschlussprüfung auf Einhaltung aller verbindlichen Sprachregeln durch.
8. Gib alle drei Teile aus

Die Aufgabe ist abgeschlossen nach Ausgabe von Text und beiden Listen. Keine weiteren Schritte ohne Anschlussfrage.
