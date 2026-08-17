# LaTeX-Tipps für die Projektarbeit

## Projekt kompilieren

### Reihenfolge (mit biblatex/biber)
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
Oder mit `latexmk` (empfohlen):
```bash
latexmk -pdf main.tex
```

### Häufige Kompilier-Fehler
| Fehler | Lösung |
|--------|--------|
| "Undefined reference" | Nochmal kompilieren (2x) |
| "Citation undefined" | `biber main` ausführen |
| "Missing \begin{document}" | Encoding-Problem → UTF-8 prüfen |
| "Too many unprocessed floats" | `\clearpage` einfügen |

## Abbildungen

### Grundstruktur
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{images/screenshot_app.png}
    \caption{Hauptansicht der Stundenbuchungs-App}
    \label{fig:hauptansicht}
\end{figure}
```

### Im Text referenzieren
```latex
Abbildung~\ref{fig:hauptansicht} zeigt die Hauptansicht der Applikation.
```
**Wichtig**: Tilde `~` verhindert Zeilenumbruch zwischen "Abbildung" und Nummer!

### Positionierung
- `h` = here (hier versuchen)
- `t` = top (oben auf der Seite)
- `b` = bottom (unten auf der Seite)
- `p` = eigene Seite (bei großen Bildern)
- `H` = GENAU hier (braucht `float`-Paket) → sparsam verwenden!

### Eigene Darstellung kennzeichnen
```latex
\caption{Architektur des Stundenbuchungstools (eigene Darstellung)}
```

### Fremde Abbildung
```latex
\caption{Aufbau der Power Platform \cite[vgl.][S.~23]{microsoft2025}}
```

## Tabellen

### Grundstruktur
```latex
\begin{table}[htbp]
    \centering
    \caption{Funktionale Anforderungen}
    \label{tab:anforderungen}
    \begin{tabular}{lp{8cm}l}
        \toprule
        \textbf{ID} & \textbf{Beschreibung} & \textbf{Priorität} \\
        \midrule
        FA-01 & Erfassung von Stunden pro Projekt & Hoch \\
        FA-02 & Dropdown-Auswahl für Projekte & Hoch \\
        FA-03 & Validierung der Eingaben & Mittel \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Lange Tabellen (über mehrere Seiten)
```latex
\begin{longtable}{lp{8cm}l}
    \caption{Vollständige Anforderungsliste} \label{tab:anforderungen_voll} \\
    \toprule
    \textbf{ID} & \textbf{Beschreibung} & \textbf{Priorität} \\
    \midrule
    \endfirsthead
    \multicolumn{3}{c}{\textit{Fortsetzung von vorheriger Seite}} \\
    \toprule
    \textbf{ID} & \textbf{Beschreibung} & \textbf{Priorität} \\
    \midrule
    \endhead
    \bottomrule
    \endfoot
    % Inhalt hier...
    FA-01 & Erfassung von Stunden & Hoch \\
\end{longtable}
```

## Code-Listings

### Inline-Code
```latex
Die Funktion \lstinline|calculateHours()| berechnet die Gesamtstunden.
```

### Code-Block
```latex
\begin{lstlisting}[
    language=JavaScript,
    caption={Power Fx-Formel zur Stundenberechnung},
    label={lst:berechnung}
]
Set(
    totalHours,
    Sum(
        Filter(TimeEntries, ProjectID = selectedProject),
        Hours
    )
)
\end{lstlisting}
```

### Sprachen konfigurieren
```latex
\lstdefinelanguage{PowerFx}{
    keywords={Set, If, Filter, Sum, Navigate, Patch, Collect},
    sensitive=true,
    comment=[l]{//},
    string=[b]"
}
```

## Querverweise

### Labels setzen
```latex
\chapter{Grundlagen}
\label{chap:grundlagen}

\section{Power Apps}
\label{sec:powerapps}

\begin{figure}...
\label{fig:architektur}

\begin{table}...
\label{tab:testfaelle}

\begin{lstlisting}...
\label{lst:code_beispiel}
```

### Referenzieren
```latex
Wie in Kapitel~\ref{chap:grundlagen} beschrieben...
Abbildung~\ref{fig:architektur} zeigt...
Tabelle~\ref{tab:testfaelle} listet...
Listing~\ref{lst:code_beispiel} demonstriert...
Auf Seite~\pageref{fig:architektur} ist...
```

## Akronyme / Abkürzungen

### Definition (in der Präambel oder eigener Datei)
```latex
\newacronym{api}{API}{Application Programming Interface}
\newacronym{ui}{UI}{User Interface}
\newacronym{crud}{CRUD}{Create, Read, Update, Delete}
\newacronym{sap}{SAP}{Systeme, Anwendungen und Produkte in der Datenverarbeitung}
```

### Verwendung im Text
```latex
Die \gls{api} ermöglicht...        % Erste Verwendung: "Application Programming Interface (API)"
Die \gls{api} wird...               % Danach nur: "API"
Mehrere \glspl{api} werden...       % Plural: "APIs"
```

## Formeln (falls benötigt)

### Inline
```latex
Die Berechnung ergibt sich aus $t_{gesamt} = \sum_{i=1}^{n} t_i$.
```

### Block (nummeriert)
```latex
\begin{equation}
    \text{Stundensatz} = \frac{\text{Gesamtkosten}}{\text{Produktivstunden}}
    \label{eq:stundensatz}
\end{equation}
```

## Nützliche Pakete (bereits im Template)

| Paket | Zweck |
|-------|-------|
| `booktabs` | Schöne Tabellen (`\toprule`, `\midrule`, `\bottomrule`) |
| `graphicx` | Bilder einbinden |
| `hyperref` | Klickbare Links im PDF |
| `listings` | Code-Listings |
| `glossaries` | Abkürzungsverzeichnis |
| `csquotes` | Korrekte deutsche Anführungszeichen mit `\enquote{}` |
| `subcaption` | Mehrere Bilder nebeneinander |
| `pdfpages` | PDF-Seiten einbinden (z.B. Aufgabenstellung) |

## Typografie-Tipps

### Gedankenstrich vs. Bindestrich
```latex
Bindestrich: Power-Apps-Anwendung
Gedankenstrich: Analyse -- Umsetzung -- Test
Bis-Strich: Seiten 15--20, März--Juni 2026
```

### Geschützte Leerzeichen
```latex
Abbildung~\ref{fig:x}     % Kein Umbruch zwischen "Abbildung" und "3.1"
S.~15                       % Kein Umbruch zwischen "S." und "15"
z.\,B.                      % Schmales Leerzeichen in Abkürzungen
d.\,h.
u.\,a.
```

### Deutsche Anführungszeichen
```latex
\enquote{Dies ist ein Zitat}    % Ergibt: „Dies ist ein Zitat"
```

## Ordnerstruktur des Projekts

```
projektarbeit/
├── main.tex                 % Hauptdatei
├── literatur.bib           % Literaturverzeichnis
├── chapters/
│   ├── 00_titelblatt.tex
│   ├── 00_erklaerung.tex
│   ├── 00_zusammenfassung.tex
│   ├── 00_abstract.tex
│   ├── 01_einleitung.tex
│   ├── 02_grundlagen.tex
│   ├── 03_analyse.tex
│   ├── 04_umsetzung.tex
│   ├── 05_test.tex
│   ├── 06_reflexion.tex
│   └── anhang.tex
├── images/
│   ├── dhbw_logo.png
│   ├── architektur.png
│   └── ...
└── .gitignore              % LaTeX-Temp-Dateien ignorieren
```
