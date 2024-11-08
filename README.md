![Logo Università](https://www.unibg.it/themes/custom/unibg/logo.svg) 
# **ANTLR-PyQtCodeChecker**

Questo progetto è stato sviluppato per il corso di **Linguaggi Formali e Compilatori (LFC)**, con l'obiettivo di creare un **analizzatore di codice** in grado di rilevare errori lessicali, sintattici e semantici in un linguaggio di programmazione semplice definito da una grammatica personalizzata. L'analizzatore utilizza **ANTLR** per generare il lexer e il parser, mentre l'interfaccia utente (GUI) è realizzata utilizzando **PyQt5**.

L'applicazione permette di:
- Effettuare una tokenizzazione del codice sorgente attraverso un lexer generato da ANTLR.
- Analizzare la struttura sintattica del codice con un parser e creare un albero sintattico.
- Eseguire verifiche semantiche sul codice usando un visitor pattern per controllare la validità di dichiarazioni e operazioni.
- Offrire un'interfaccia grafica interattiva per caricare il codice, visualizzare errori e correggerli facilmente.

Questo strumento fornisce un ambiente di sviluppo utile per chi desidera analizzare e correggere il codice in modo automatico durante la fase di scrittura, favorendo un miglior flusso di lavoro e una maggiore qualità del codice.

---

## **Toolchain e Dipendenze**

Il progetto utilizza una serie di strumenti per implementare e far funzionare correttamente l'analizzatore di codice:

- **ANTLR 4.9.2**: Utilizzato per generare il lexer e il parser dal file di grammatica. È necessario il file `antlr4-4.9.2-complete.jar`.
- **Python 3.x**: Per eseguire l'applicazione e gestire la logica del programma.
- **PyQt5**: Per la realizzazione dell'interfaccia grafica (GUI).
- **Git**: Per il controllo di versione e la gestione del repository.

