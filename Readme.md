## **Analisi del prezzo del carburante in Italia**

_Breve commento data visualization_ 

L'analisi si sviluppa su tre step principali: 
1)Ottenimento dei dataset
2)Pulizia dei dati
3)Data visualization

Per lo step di data visualization sono state tenute soltanto le colonne maggiormente significative
ai fini dell'analisi:
 
prezzo: prezzo del carburante;

bandiera: la bandiera (marchio) del distributore;

provincia: la provincia del distributore;

macroregione: la macroregione del distributore. Puo' essere nord,centro,sud ed e' stata ottenuta categorizzando la Latitudine

isSelf: indica se si tratta di un self-service o di un servito

La prima serie di grafici a barre riguarda il prezzo medio del carburante nelle 3 macroaree italiane: nord, centro, sud.
Sono state prese in considerazione le 2 tipologie principali di carburante: benzina e gasolio.
Sia per la benzina che per il gasolio il prezzo medio maggiore è al sud, seguito da nord e centro.

La seconda serie di grafici a barre riguarda il prezzo del carburante nelle province italiane.
In ciascun grafico della serie sono rappresentate le 5 province con la media più alta e le 5 province con la media più bassa.
Il primo grafico, più 'sporco', prende in considerazione tutte le tipologie di carburante: è poossibile
notare come tra le province più economiche tre siano del centro Italia (Viterbo, Fermo, Rieti), rispecchiando i grafici sulle macroaree;
tra le province più costose è invece interessante constatare che 3 su 5 sono province molto vicine ai confini nazionali (Verbania, Imperia, Bolzano).
Il secondo e il terzo grafico sono invece più puliti, prendendo in considerazione rispettivamente soltanto la benzina e soltanto il diesel.
Nel grafico relativo alla benzina, tra le province più economiche ancora una volta 3 su 5 sono del centro italia, mentre per quanto riguarda
le province più care, spariscono dalla top 5 le zone di confine. Proprio queste ultime riappaiono nel grafico relativo al diesel, dove anche in questo caso
tra le province più economiche 'comandano' quelle del centro Italia.

La terza serie di grafici a barre riguarda il prezzo medio del carburante per bandiera.
Anche in questo caso si è suddiviso l'analisi distinguendo tra benzina e diesel, rappresentando i quattro rifornitori
più costosi ed i quattro rifornitori più economici. Interessante è notare come i cinque più costosi siano i medesimi
sia per la benzina che per il diesel.

La quarta seria di grafici riguarda l'evoluzione nel tempo del prezzo medio del carburante: anche in questo caso si è distinto
tra benzina e diesel.

Gli ultimi due grafici sono infine dei grafici a barre multiple con l'obiettivo di rappresentare, come in precedenza, il prezzo medio di benzina e diesel per provincia,
ma distinguendo in questo caso tra 'servito' e 'self service'.





