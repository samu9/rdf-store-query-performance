# Query performance for Virtuoso and GraphDB RDF stores
Script utilizzato per misurare e comparare le performance di query in Virtuoso e Graph, dove in SPARQL viene utilizzato lo standard GeoSparql.

Le query sono predefinite e rappresentate come dizionario nel file _queries.py_. Per Virtuoso sono sotto forma di URL, utilizzate per richieste GET, per GraphDB invece sono i payload da mandare nel body di una richiesta POST.

In _app.py_ è presente l'applicazione e la funzione utilizzata per la misurazione dei tempi, che fa uso della libreria __requests__, ed in particolare della proprietà _elapsed_ dell'oggetto ricevuto in risposta.