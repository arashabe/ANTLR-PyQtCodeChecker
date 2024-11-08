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

- **antlr4-python3-runtime**: per usare il lexer e parser generati da ANTLR in Python.
- **Python 3.x**: Per eseguire l'applicazione e gestire la logica del programma.
- **PyQt5**: Per la realizzazione dell'interfaccia grafica (GUI).
- **Git**: Per il controllo di versione e la gestione del repository.


## Passaggi di Installazione

1. **Installare Python 3**:
   Scaricare e installare Python 3 dal sito ufficiale: [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Installare PyQt5**:
   ```bash
   pip install PyQt5
   ```

3. **Installare ANTLR Runtime per Python**:
   Questo pacchetto permette di usare il lexer e parser generati da ANTLR in Python.
   ```bash
   pip install antlr4-python3-runtime==4.9.2
   ```

4. **Scaricare ANTLR JAR**:
   Scaricare `antlr-4.9.2-complete.jar` da [https://www.antlr.org/download.html](https://www.antlr.org/download.html) e salvare in una directory accessibile, ad esempio `C:\Program Files\antlr`.

5. **Generare il Lexer e Parser**:
   - Creare il file della grammatica `Language.g4` nella cartella principale del progetto e aggiungere le regole del linguaggio.
   - Dal terminale, esegui il seguente comando per generare i file Python per il lexer, parser e visitor:
     ```bash
     java -jar "C:\Program Files\antlr\antlr-4.9.2-complete.jar" -Dlanguage=Python3 -visitor Language.g4 -o generated
     ```

6. **Verifica la Struttura dei File Generati**:
   Si deve avere una cartella `generated` con i file:
   - `LanguageLexer.py`: il lexer generato per riconoscere i token.
   - `LanguageParser.py`: il parser generato per analizzare la struttura sintattica.
   - `LanguageVisitor.py`: il visitor generato per eseguire l’analisi semantica.

## Componenti del Progetto

### 1. `Language.g4`
   - Definisce la grammatica del linguaggio che stai analizzando.
   - Include regole per riconoscere i token (`int`, `float`, `=`) e per dichiarazioni, espressioni, ecc.
   - La regola `COMMENT` è usata per ignorare i commenti in stile `//`.

### 2. `main.py`
   - È il file principale che avvia l'interfaccia grafica.
   - Contiene la classe `CodeAnalyzerGUI` che costruisce l'interfaccia con PyQt5 e include un’area per l'inserimento del codice, una console per l’output e un pulsante “Run” per eseguire l'analisi.
   - La funzione `run_analysis` raccoglie il codice inserito dall’utente, lo passa al lexer, parser e al visitor per eseguire tutte le verifiche.

### 3. `Driver.py`
   - È un file di test per il lexer e il parser generati da ANTLR.
   - Serve per verificare che il lexer e parser funzionino correttamente anche senza l’interfaccia grafica.
   - Puoi utilizzarlo eseguendo il comando `python Driver.py input.txt`, dove `input.txt` è un file di esempio.

### 4. `semantic_analyzer.py`
   - Contiene la classe `SemanticAnalyzer`, che estende il visitor generato da ANTLR (`LanguageVisitor`).
   - Implementa i metodi `visitDeclaration` e `visitExpression` per rilevare errori semantici:
     - **visitDeclaration**: verifica che ogni variabile sia dichiarata una sola volta.
     - **visitExpression**: verifica che ogni variabile sia stata dichiarata prima di essere utilizzata.
   - I risultati dell’analisi vengono riportati alla GUI attraverso `semantic_analyzer.errors`.

## Come Funziona il Progetto

1. **Tokenizzazione**: 
   - Il lexer generato (`LanguageLexer.py`) converte il codice in una serie di token, come `int`, `float`, `=`, `;`, ecc.
   - Ignora i commenti e gli spazi bianchi.

2. **Parsing**:
   - Il parser (`LanguageParser.py`) organizza i token in una struttura gerarchica (un albero di parsing) in base alle regole grammaticali.
   - Verifica se il codice rispetta le regole sintattiche definite nella grammatica, come la presenza di `;` alla fine delle dichiarazioni.

3. **Analisi Semantica**:
   - Il visitor (`LanguageVisitor.py`) attraversa l’albero sintattico prodotto dal parser.
   - La classe `SemanticAnalyzer` controlla la validità semantica del codice, come l'uso di variabili non dichiarate e la dichiarazione duplicata di variabili.

4. **Interfaccia Grafica**:
   - In `main.py`, l'interfaccia grafica permette all’utente di inserire il codice e di eseguirne l'analisi cliccando su "Run".
   - Eventuali errori (lessicali, sintattici o semantici) vengono visualizzati nella console di output.
     
## Esecuzione del Progetto

1. Avviare il progetto eseguendo `main.py`:
   ```bash
   python main.py
   ```

2. Inserire del codice nell'area di testo, ad esempio:
   ```plaintext
   int x = 10;
   x = x + 5;
   y = 7;  // variabile non dichiarata
   ```

3. Cliccare su “Run” per eseguire l’analisi:
   - Gli errori verranno mostrati nella console di output.
   - Se non ci sono errori, apparirà il messaggio “Nessun errore trovato!”

   
