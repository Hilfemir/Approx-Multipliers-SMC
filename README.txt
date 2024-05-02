Bakalarska prace

Nazev: Statisticke overovani modelu pribliznych vypocetnich systemu
Autor: Michal Blazek
Skola: FIT VUT Brno
Rok: 2024

Struktura repozitare:
/density - vse co se tyka pravdepodobnostnich rozdeleni
         -> zdrojove kody jednotlivych zkoumanych algoritmu
         -> skript pro sbirani dvojic nasobenych cisel z algoritmu
         -> skripty pro vizualizaci ziskanych rozdeleni (heatmapy, PDF, ...)
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

/scalability - zkoumani skalovatelnosti
             -> csv soubory s namerenymi daty
	     -> skripty pro vizualizaci
	     -> grafy

/thesis - soubory textu technicke zpravy
