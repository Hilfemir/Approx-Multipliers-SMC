Bakalarska prace

Nazev: Statisticke overovani modelu pribliznych vypocetnich systemu
Autor: Michal Blazek
Skola: FIT VUT Brno
Rok: 2024

------------------------------------------------------------------------------------

Struktura adresare:

/auxiliary - /density - vse co se tyka pravdepodobnostnich rozdeleni
                -> zdrojove kody jednotlivych zkoumanych algoritmu
                -> skript pro sbirani dvojic nasobenych cisel z algoritmu
                -> skripty pro vizualizaci ziskanych rozdeleni (heatmapy, PDF, ...)
                -> grafy
           - /scalability - zkoumani skalovatelnosti
                          -> csv soubory s namerenymi daty
	                  -> skripty pro vizualizaci
	                  -> grafy

/models - preklad modelu z Verilogu do UPPAAL
        -> vstupni soubory ve Verilogu
	-> prekladaci skript parse.py
	-> vygenerovane XML soubory pro UPPAAL

/results - zpracovani vysledku simulaci
         -> vysledky simulaci - csv soubory v ./sim_results
	 -> skript pro zpracovani vysledku z csv do Pandas df
	 -> skripty pro vizualizaci vysledku
	 -> grafy

/thesis - zdrojove soubory textu

------------------------------------------------------------------------------------

Navod na pouziti:

Podrobnejsi navod se nachazi v textu prace v priloze B.

Skript /models/parse.py lze spoustet nasledujicim prikazem:
   $ python3 parse.py input_file [-h] [-d DISTRIBUTION] [--noout]

Vyznam argumentu je nasledujici:
   - input_file - cesta ke vstupnimu souboru s modelem nasobicky ve Verilogu,
   - -h - zobrazi navod na spusteni skriptu (+ moznosti vyberu rozdeleni),
   - -d DISTRIBUTION - vyber pravdepodobnostniho rozdeleni,
   - --noout - zakaz vygenerovani vysledneho souboru. Vhodne k ladeni.

Vysledne soubory se ukladaji do adresare /models/out/<DISTRIBUTION>/...
Tyto soubory lze pote otevrit v nastroji UPPAAL a provadet simulace.