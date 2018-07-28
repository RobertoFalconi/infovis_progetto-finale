/* Filtri iniziali */
var Filtro1 = "all";
var Filtro2 = "all";
var Filtro3 = "all";

function incidentiPatentatiFiltro(filtro_tipologia, filtro_strada, filtro_gravita, i) {
    var patentati = PatentiPopolazione[i].patenti;
    var incidenti;
    var regioni = getRegioniByYear(annoSelezionato);
    if (filtro_tipologia === "all") {
        if (filtro_strada === "all") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].vu1t + regioni[i].ve1t + regioni[i].vu2t +
                    regioni[i].ve2t + regioni[i].vu3t + regioni[i].ve3t + regioni[i].vu4t +
                    regioni[i].ve4t + regioni[i].put + regioni[i].pet;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].vu1f + regioni[i].ve1f + regioni[i].vu2f +
                    regioni[i].ve2f + regioni[i].vu3f + regioni[i].ve3f + regioni[i].vu4f +
                    regioni[i].ve4f + regioni[i].puf + regioni[i].pef;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].vu1m + regioni[i].ve1m + regioni[i].vu2m +
                    regioni[i].ve2m + regioni[i].vu3m + regioni[i].ve3m + regioni[i].vu4m +
                    regioni[i].ve4m + regioni[i].pum + regioni[i].pem;
            }
        }
        else if (filtro_strada === "urban") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].vu1t + regioni[i].vu2t + regioni[i].vu3t
                    + regioni[i].vu4t + regioni[i].put;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].vu1f + regioni[i].vu2f + regioni[i].vu3f
                    + regioni[i].vu4f + regioni[i].puf;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].vu1m + regioni[i].vu2m + regioni[i].vu3m
                    + regioni[i].vu4m + regioni[i].pum;
            }
        }
        else if (filtro_strada === "interurban") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].ve1t + regioni[i].ve2t + regioni[i].ve3t
                    + regioni[i].ve4t + regioni[i].pet;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].ve1f + regioni[i].ve2f + regioni[i].ve3f
                    + regioni[i].ve4f + regioni[i].pef;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].ve1m + regioni[i].ve2m + regioni[i].ve3m
                    + regioni[i].ve4m + regioni[i].pem;
            }
        }
    }
    else if (filtro_tipologia === "cars") {
        if (filtro_strada === "all") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].vu1t + regioni[i].ve1t + regioni[i].vu2t +
                    regioni[i].ve2t + regioni[i].vu3t + regioni[i].ve3t + regioni[i].vu4t +
                    regioni[i].ve4t;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].vu1f + regioni[i].ve1f + regioni[i].vu2f +
                    regioni[i].ve2f + regioni[i].vu3f + regioni[i].ve3f + regioni[i].vu4f +
                    regioni[i].ve4f;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].vu1m + regioni[i].ve1m + regioni[i].vu2m +
                    regioni[i].ve2m + regioni[i].vu3m + regioni[i].ve3m + regioni[i].vu4m +
                    regioni[i].ve4m;
            }
        }
        else if (filtro_strada === "urban") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].vu1t + regioni[i].vu2t + regioni[i].vu3t
                    + regioni[i].vu4t;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].vu1f + regioni[i].vu2f + regioni[i].vu3f
                    + regioni[i].vu4f;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].vu1m + regioni[i].vu2m + regioni[i].vu3m
                    + regioni[i].vu4m;
            }
        }
        else if (filtro_strada === "interurban") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].ve1t + regioni[i].ve2t + regioni[i].ve3t
                    + regioni[i].ve4t;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].ve1f + regioni[i].ve2f + regioni[i].ve3f
                    + regioni[i].ve4f;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].ve1m + regioni[i].ve2m + regioni[i].ve3m
                    + regioni[i].ve4m;
            }
        }
    }
    else if (filtro_tipologia === "pedestrians") {
        if (filtro_strada === "all") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].put + regioni[i].pet;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].puf + regioni[i].pef;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].pum + regioni[i].pem;
            }
        }
        else if (filtro_strada === "urban") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].put;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].puf;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].pum;
            }
        }
        else if (filtro_strada === "interurban") {
            if (filtro_gravita === "all") {
                incidenti = regioni[i].pet;
            }
            else if (filtro_gravita === "injured") {
                incidenti = regioni[i].pef;
            }
            else if (filtro_gravita === "dead") {
                incidenti = regioni[i].pem;
            }
        }
    }
    return {patentati: patentati, incidenti: incidenti};
}

/* Restituisce tutti i rapporti incidenti/patentati di tutte le regioni a seconda dei filtri utilizzato */
function rapportiRegioni(regioni, filtro_tipologia, filtro_strada, filtro_gravita){
    var i;
    var rapporti = [];
    if (filtro_tipologia === "all") {
        if (filtro_strada === "all") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1t + regioni[i].ve1t + regioni[i].vu2t +
                        regioni[i].ve2t + regioni[i].vu3t + regioni[i].ve3t + regioni[i].vu4t +
                        regioni[i].ve4t + regioni[i].put + regioni[i].pet;
                    rapporti.push((incidenti/PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1f + regioni[i].ve1f + regioni[i].vu2f +
                        regioni[i].ve2f + regioni[i].vu3f + regioni[i].ve3f + regioni[i].vu4f +
                        regioni[i].ve4f + regioni[i].puf + regioni[i].pef;
                    rapporti.push((incidenti/PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1m + regioni[i].ve1m + regioni[i].vu2m +
                        regioni[i].ve2m + regioni[i].vu3m + regioni[i].ve3m + regioni[i].vu4m +
                        regioni[i].ve4m + regioni[i].pum + regioni[i].pem;
                    rapporti.push((incidenti/PatentiPopolazione[i].patenti));
                }
            }
        }
        else if (filtro_strada === "urban") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1t + regioni[i].vu2t + regioni[i].vu3t
                        + regioni[i].vu4t + regioni[i].put;
                    rapporti.push((incidenti/PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1f + regioni[i].vu2f + regioni[i].vu3f
                        + regioni[i].vu4f + regioni[i].puf;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1m + regioni[i].vu2m + regioni[i].vu3m
                        + regioni[i].vu4m + regioni[i].pum;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
        else if (filtro_strada === "interurban") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].ve1t + regioni[i].ve2t + regioni[i].ve3t
                        + regioni[i].ve4t + regioni[i].pet;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].ve1f + regioni[i].ve2f + regioni[i].ve3f
                        + regioni[i].ve4f + regioni[i].pef;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].ve1m + regioni[i].ve2m + regioni[i].ve3m
                        + regioni[i].ve4m + regioni[i].pem;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
    }
    else if (filtro_tipologia === "cars") {
        if (filtro_strada === "all") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1t + regioni[i].ve1t + regioni[i].vu2t +
                        regioni[i].ve2t + regioni[i].vu3t + regioni[i].ve3t + regioni[i].vu4t +
                        regioni[i].ve4t;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1f + regioni[i].ve1f + regioni[i].vu2f +
                        regioni[i].ve2f + regioni[i].vu3f + regioni[i].ve3f + regioni[i].vu4f +
                        regioni[i].ve4f;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1m + regioni[i].ve1m + regioni[i].vu2m +
                        regioni[i].ve2m + regioni[i].vu3m + regioni[i].ve3m + regioni[i].vu4m +
                        regioni[i].ve4m;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
        else if (filtro_strada === "urban") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1t + regioni[i].vu2t + regioni[i].vu3t
                        + regioni[i].vu4t;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1f + regioni[i].vu2f + regioni[i].vu3f
                        + regioni[i].vu4f;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].vu1m + regioni[i].vu2m + regioni[i].vu3m
                        + regioni[i].vu4m;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
        else if (filtro_strada === "interurban") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].ve1t + regioni[i].ve2t + regioni[i].ve3t
                        + regioni[i].ve4t;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].ve1f + regioni[i].ve2f + regioni[i].ve3f
                        + regioni[i].ve4f;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].ve1m + regioni[i].ve2m + regioni[i].ve3m
                        + regioni[i].ve4m;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
    }
    else if (filtro_tipologia === "pedestrians") {
        if (filtro_strada === "all") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].put + regioni[i].pet;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].puf + regioni[i].pef;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].pum + regioni[i].pem;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
        else if (filtro_strada === "urban") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].put;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].puf;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].pum;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
        else if (filtro_strada === "interurban") {
            if (filtro_gravita === "all") {
                for (i in distretti) {
                    incidenti = regioni[i].pet;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "injured") {
                for (i in distretti) {
                    incidenti = regioni[i].pef;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
            else if (filtro_gravita === "dead") {
                for (i in distretti) {
                    incidenti = regioni[i].pem;
                    rapporti.push((incidenti / PatentiPopolazione[i].patenti));
                }
            }
        }
    }
    return rapporti;
}
