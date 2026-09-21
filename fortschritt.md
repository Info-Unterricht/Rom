# Projekt: Rom-Schnelldurchlauf (Klasse 6) – Fortschrittsprotokoll

Stand: wird nach jedem Schritt aktualisiert. Quellcode liegt in `src/`, fertige Seite entsteht per `python3 build.py` → `index.html`.

## Plan (6 Stunden)
| Std. | Kapitel |
|---|---|
| 1 | K1 Gründung Roms · K2 Ausbreitung in Italien |
| 2 | K3 Punische Kriege |
| 3 | K4 Verhältnisse in Rom: Adel gegen Bauern |
| 4 | K5 Weitere Kriege & Folgen für die Menschen in Rom |
| 5 | K6 Caesar, Ermordung, Augustus |
| 6 | K7 Teilung in West- & Ostrom · K8 Zerfall Westroms · Abschlussquiz |

## Bausteine
- [x] A. Kartendaten (Küsten, Provinzen mit Jahreszahlen, Städte, Wege) – `src/geo.py` → `geo.json`
- [x] B. Design (CSS) – `src/style.css`
- [x] C. Motor (Zeitstrahl, Karte, Aufgabentypen, Navigation, Speichern) – `src/engine.js`
- [x] D. Startseite mit Zeitmaschine (Karte zum Abspielen)
- [x] K1 Gründung Roms
- [x] K2 Ausbreitung in Italien
- [x] K3 Punische Kriege
- [x] K4 Adel gegen Bauern
- [x] K5 Weitere Kriege & Folgen
- [x] K6 Caesar & Augustus
- [x] K7 Teilung Ost/West
- [x] K8 Zerfall Westroms
- [x] Abschlussquiz Stunde 6
- [x] Zusammenbauen, Testen, Veröffentlichen

## Protokoll

- Kartendaten fertig: 33 Gebiete mit Jahreszahlen (753 v. Chr. bis 106 n. Chr.), Nachfolgereiche 409–476, Städte, Wege (Hannibal, Hunnen …). Vorschau geprüft (Jahr 264 v. Chr. und 117 n. Chr.).

- Design-Entwurf `src/style.css` fertig (Farben, Zeitstrahl, Karte, Aufgaben, Heftkarten, Dunkelmodus).
- Planänderung: Statt die Seite hier fertigzubauen, wurde ein vollständiger Prompt für Claude Code erstellt (`PROMPT_Claude_Code.md`). Bausteine C–K9 sind dort beschrieben und noch offen.

- Etappen C–K9 fertig: Motor (`src/engine.js`), Kapitel `src/kap1.js`–`kap9.js`, Build `build.py` → `index.html` (ca. 170 KB, eine Datei).
- Tests: `node tests/smoke.js` (jsdom: alle Seiten, alle Stationen, alle 68 Aufgaben werden per Klick gelöst, Datenchecks, Speicher) bestanden; Karten mit Playwright/Edge geprüft (`node tests/maps.js`, Screenshots 375/1280 px, hell/dunkel).

## Entscheidungen
- Wort-Erklärungen im Text als `[[Wort|Erklärung]]`, fett als `**…**`.
- Stationen mit ungefähren Jahren tragen `about:true` („um 750 v. Chr.“) oder ein eigenes Label `yl`.
- Zeitrechnung (K1) steht als Einstieg vor der Zeitreise; Kartenmodus Blau/Orange ab 395, Nachfolgereiche ab 409.
- Neu-Hervorhebung automatisch: Gebiete mit Jahr zwischen Vorstation und aktueller Station.
- Route „vandalen_west“ (Rhein→Spanien) zusätzlich zu „vandalen“ ergänzt; einige Orte in `geo.py` neu (Benevent, Philippi, Pontus …).
- Mobil: Karte bleibt beim Scrollen oben kleben, damit der Kartenwechsel sichtbar ist.
- Git: lokales Repo ohne globale Identität angelegt; tests/node_modules ausgeschlossen.
