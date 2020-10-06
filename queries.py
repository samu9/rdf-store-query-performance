# dizionario con le richieste necessarie per la richiesta al database

QUERIES = {
    "virtuoso": [
        "http://localhost:8890/sparql/?default-graph-uri=&query=PREFIX+uom%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Fuom%2FOGC%2F1.0%2F%3E%0D%0APREFIX+geosparql%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Font%2Fgeosparql%23%3E%0D%0APREFIX+geof%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Ffunction%2Fgeosparql%2F%3E%0D%0APREFIX+ns9%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0D%0A%0D%0ASELECT+%3Fo+%3Fname+%3Fdist%0D%0AWHERE+%7B%0D%0A++++%3Fo+geosparql%3AhasGeometry+%3Fg.%0D%0A++++%3Fo+ns9%3Aname+%3Fname.%0D%0A++++%3Fg+geosparql%3AasWKT+%3FfWKT.+%0D%0A++++BIND%28geof%3Adistance%28%3FfWKT%2C+%22POINT%2810.68511+43.8900944%29%22%5E%5Egeosparql%3AwktLiteral%2C+uom%3Ametre%29+as+%3Fdist%29.%0D%0A%7D+%0D%0AORDER+BY+ASC+%28%3Fdist%29%0D%0ALIMIT+10%0D%0A&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+",
        "http://localhost:8890/sparql/?default-graph-uri=&query=PREFIX+geosparql%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Font%2Fgeosparql%23%3E%0D%0APREFIX+geof%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Ffunction%2Fgeosparql%2F%3E%0D%0APREFIX+ns9%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0D%0ASELECT+%3Fo+%3Fname+%3Fcoords+%3FwktLit%0D%0AWHERE+%7B+%0D%0A++++%3Fo+geosparql%3AhasGeometry+%3Fg.%0D%0A++++%3Fo+ns9%3Aname+%3Fname.%0D%0A++++%3Fo+geo%3Alat+%3Flat.%0D%0A++++%3Fo+geo%3Along+%3Flong.%0D%0A++++bind%28concat%28str%28%3Flat%29%2C%27+%27%2Cstr%28%3Flong%29%29+as+%3Fcoords%29%0D%0A%09%3Fg+geosparql%3AasWKT+%3FwktLit%0D%0A++++FILTER%28geof%3AsfWithin%28%3FwktLit%2C%22POLYGON%28%2811.254528+43.773484%2C11.257732+43.773576%2C11.257837+43.772577%2C11.254422970886221+43.77269737369775%2C11.254528+43.773484%29%29%22%5E%5Egeosparql%3AwktLiteral%29%29%0D%0A%7D%0D%0A&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+",
        "http://localhost:8890/sparql/?default-graph-uri=&query=PREFIX+geosparql%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Font%2Fgeosparql%23%3E%0D%0APREFIX+geof%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Ffunction%2Fgeosparql%2F%3E%0D%0APREFIX+ns9%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0D%0ASELECT+%3Fo+%3Fname+%3FwktLit+where+%7B%0D%0A++++%09%3Fo+geosparql%3AhasGeometry+%3Fg.%0D%0A+++%09%3Fo+ns9%3Aname+%3Fname.%0D%0A%3Fg+geosparql%3AasWKT+%3FwktLit+.%0D%0A++++FILTER%28geof%3AsfIntersects%28%3FwktLit%2C%22LINESTRING%2811.237879347818556+43.81197797309732%2C11.2732415914709+43.77096176563369%29%22%5E%5Egeosparql%3AwktLiteral%29%29%0D%0A%7D%0D%0A&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+"

    ],
    "graphdb": [
        "query=PREFIX+uom%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Fuom%2FOGC%2F1.0%2F%3E%0APREFIX+geosparql%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Font%2Fgeosparql%23%3E%0APREFIX+geof%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Ffunction%2Fgeosparql%2F%3E%0APREFIX+ns9%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0A%0ASELECT+%3Fo+%3Fname+%3Fdist%0AWHERE+%7B%0A++++%3Fo+geosparql%3AhasGeometry+%3Fg.%0A++++%3Fo+ns9%3Aname+%3Fname.%0A++++%3Fg+geosparql%3AasWKT+%3FfWKT.+%0A++++BIND(geof%3Adistance(%3FfWKT%2C+%22POINT(10.68511+43.8900944)%22%5E%5Egeosparql%3AwktLiteral%2C+uom%3Ametre)+as+%3Fdist).%0A%7D+%0AORDER+BY+ASC+(%3Fdist)%0ALIMIT+10%0A&infer=true&sameAs=true&limit=1000&offset=0",
        "query=PREFIX+geosparql%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Font%2Fgeosparql%23%3E%0APREFIX+geof%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Ffunction%2Fgeosparql%2F%3E%0APREFIX+ns9%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+geo%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E%0ASELECT+%3Fo+%3Fname+%3Fcoords+%3FwktLit%0AWHERE+%7B+%0A++++%3Fo+geosparql%3AhasGeometry+%3Fg.%0A++++%3Fo+ns9%3Aname+%3Fname.%0A++++%3Fo+geo%3Alat+%3Flat.%0A++++%3Fo+geo%3Along+%3Flong.%0A++++bind(concat(str(%3Flat)%2C'+'%2Cstr(%3Flong))+as+%3Fcoords)%0A%09%3Fg+geosparql%3AasWKT+%3FwktLit%0A++++FILTER(geof%3AsfWithin(%3FwktLit%2C%22POLYGON((11.254528+43.773484%2C11.257732+43.773576%2C11.257837+43.772577%2C11.254422970886221+43.77269737369775%2C11.254528+43.773484))%22%5E%5Egeosparql%3AwktLiteral))%0A%7D%0A&infer=true&sameAs=true&limit=1000&offset=0",
        "query=PREFIX+geosparql%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Font%2Fgeosparql%23%3E%0APREFIX+geof%3A+%3Chttp%3A%2F%2Fwww.opengis.net%2Fdef%2Ffunction%2Fgeosparql%2F%3E%0APREFIX+ns9%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Fo+%3Fname+%3FwktLit+where+%7B%0A++++%09%3Fo+geosparql%3AhasGeometry+%3Fg.%0A+++%09%3Fo+ns9%3Aname+%3Fname.%0A%3Fg+geosparql%3AasWKT+%3FwktLit+.%0A++++FILTER(geof%3AsfIntersects(%3FwktLit%2C%22LINESTRING(11.237879347818556+43.81197797309732%2C11.2732415914709+43.77096176563369)%22%5E%5Egeosparql%3AwktLiteral))%0A%7D%0A&infer=true&sameAs=true&limit=1000&offset=0",
    ]
}