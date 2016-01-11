# Codi font, codi objecte i codi executable; màquines virtuals

*Per crear un programa consta d'arxius que contenen un seguit d'instruccions, escrites en format de text, amb la finalitat del programa.*

Aquestes instruccions hauran de seguir unes pautes determinades en funció del llenguatge de programació que s'utilitzi. Finalment, aquestes instruccions en format text és el que anomenem **codi font**.

> *El codi font pot ser des d’un nivell molt alt, molt a prop del llenguatge humà, fi ns a un de nivell més baix, més proper al codi de les màquines, com ara el codi assemblador.*

Un cop tenim el codi font, per poder executar-lo, aquest ha de passar per el procés de **compilació**. Aquest procés és la traducció del codi font del programa en fitxers amb format binari que contenen les instruccions en un format que el processador pot entendre. El contingut d'aquets fitxers s'anomena **codi objecte** i, com podem intuir, l'encarregat de fer el procés de compilació s'anomena **compilador**.

Finalment, s'insereixen les funcions de les llibreries que són necessàries per al programa i es munta un arxiu executable amb el contingut del programa. L'encarregat de fer aquesta tasca és l'**enllaçador**.

## Màquines virtuals   

> *L'objectiu de les màquines virtuals és facilitar el desenvolupament de compiladors que generen codi per a diferents processadors.*

* La primera parteix del codi font a un llenguatge intermedi obtenint un programa equivalent amb un menor nivell d’abstracció que l’original i que no pot ser directament executat.
* La segona fase tradueix el llenguatge intermedi a un llenguatge comprensible per la màquina
