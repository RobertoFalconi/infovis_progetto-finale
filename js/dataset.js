		/* Demografica dei distretti (oggetti ottenuti dal file csv tramite script Python) */

		var DIST1 = {id: "DIST1", totale: 691474, bianchi: 292771, neri: 345746, ispanici: 72236, asiatici: 12254, uomini: 322348, donne: 369126, totRace: 723007};
		var DIST2 = {id: "DIST2", totale: 713917, bianchi: 264797, neri: 406653, ispanici: 99610, asiatici: 5436, uomini: 334166, donne: 379751, totRace: 776496};
		var DIST3 = {id: "DIST3", totale: 720930, bianchi: 529893, neri: 38140, ispanici: 238646, asiatici: 30281, uomini: 361574, donne: 359356, totRace: 836960};
		var DIST4 = {id: "DIST4", totale: 695098, bianchi: 385144, neri: 26083, ispanici: 487383, asiatici: 25740, uomini: 352478, donne: 342620, totRace: 924350};
		var DIST5 = {id: "DIST5", totale: 723373, bianchi: 593685, neri: 18194, ispanici: 139326, asiatici: 50171, uomini: 356625, donne: 366748, totRace: 801376};
		var DIST6 = {id: "DIST6", totale: 722323, bianchi: 599312, neri: 19108, ispanici: 67177, asiatici: 65830, uomini: 353209, donne: 369114, totRace: 751427};
		var DIST7 = {id: "DIST7", totale: 723481, bianchi: 256647, neri: 341264, ispanici: 119971, asiatici: 53760, uomini: 343743, donne: 379738, totRace: 771642};
		var DIST8 = {id: "DIST8", totale: 717789, bianchi: 465992, neri: 33339, ispanici: 210817, asiatici: 92202, uomini: 362008, donne: 355781, totRace: 802350};
		var DIST9 = {id: "DIST9", totale: 724071, bianchi: 514493, neri: 72697, ispanici: 78549, asiatici: 93906, uomini: 350566, donne: 373505, totRace: 759645};
		var DIST10 = {id: "DIST10", totale: 710610, bianchi: 505898, neri: 48352, ispanici: 159809, asiatici: 80123, uomini: 351902, donne: 358708, totRace: 794182};
		var DIST11 = {id: "DIST11", totale: 730480, bianchi: 478688, neri: 77608, ispanici: 196939, asiatici: 62504, uomini: 357773, donne: 372707, totRace: 815739};
		var DIST12 = {id: "DIST12", totale: 693736, bianchi: 541201, neri: 117759, ispanici: 23528, asiatici: 10412, uomini: 343254, donne: 350482, totRace: 692900};
		var DIST13 = {id: "DIST13", totale: 704699, bianchi: 573421, neri: 77940, ispanici: 23987, asiatici: 27069, uomini: 348787, donne: 355912, totRace: 702417};
		var DIST14 = {id: "DIST14", totale: 736397, bianchi: 636375, neri: 25846, ispanici: 93109, asiatici: 33119, uomini: 368410, donne: 367987, totRace: 788449};
		var DIST15 = {id: "DIST15", totale: 700549, bianchi: 648770, neri: 31367, ispanici: 18784, asiatici: 4540, uomini: 347422, donne: 353127, totRace: 703461};
		var DIST16 = {id: "DIST16", totale: 687998, bianchi: 623579, neri: 23523, ispanici: 64186, asiatici: 9120, uomini: 343262, donne: 344736, totRace: 720408};
		var DIST17 = {id: "DIST17", totale: 691212, bianchi: 565738, neri: 80747, ispanici: 64640, asiatici: 10007, uomini: 340563, donne: 350649, totRace: 721132};
		var DIST18 = {id: "DIST18", totale: 713402, bianchi: 647359, neri: 29237, ispanici: 20093, asiatici: 18309, uomini: 351634, donne: 361768, totRace: 714998};
		var DIST19 = {id: "DIST19", totale: 713405, bianchi: 447359, neri: 19237, ispanici: 10093, asiatici: 8309, uomini: 251634, donne: 261768, totRace: 614998};
        var DIST20 = {id: "DIST20", totale: 713405, bianchi: 447359, neri: 19237, ispanici: 10093, asiatici: 8309, uomini: 251634, donne: 261768, totRace: 614998};

        /* 'distretti' è un array contenente i singoli distretti come oggetti */
		var distretti = [DIST1, DIST2, DIST3, DIST4, DIST5, DIST6, DIST7, DIST8, DIST9, DIST10, DIST11, DIST12, DIST13, DIST14, DIST15, DIST16, DIST17, DIST18,DIST19,DIST20];
		
		/* Fermi totali per distretto (oggetti ottenuti dal file csv tramite script Python) */

		var DIST1_fermi = {id: "DIST1_fermi", totale: 147521, bianchi: 116922, neri: 18201, ispanici: 9686, asiatici: 2712, uomini: 97604, donne: 50230};
		var DIST2_fermi = {id: "DIST2_fermi", totale: 264959, bianchi: 169797, neri: 39585, ispanici: 50190, asiatici: 1387, uomini: 201906, donne: 63815};
		var DIST3_fermi = {id: "DIST3_fermi", totale: 373639, bianchi: 210546, neri: 71600, ispanici: 74840, asiatici: 16653, uomini: 264496, donne: 110366};
		var DIST4_fermi = {id: "DIST4_fermi", totale: 72500, bianchi: 39900, neri: 15200, ispanici: 12400, asiatici: 5000, uomini: 50300, donne: 22600};
		var DIST5_fermi = {id: "DIST5_fermi", totale: 190868, bianchi: 128496, neri: 35312, ispanici: 22393, asiatici: 4667, uomini: 139566, donne: 51668};
		var DIST6_fermi = {id: "DIST6_fermi", totale: 186445, bianchi: 139081, neri: 30013, ispanici: 11764, asiatici: 5587, uomini: 133619, donne: 53268};
		var DIST7_fermi = {id: "DIST7_fermi", totale: 172221, bianchi: 145611, neri: 14840, ispanici: 9037, asiatici: 2733, uomini: 120321, donne: 52093};
		var DIST8_fermi = {id: "DIST8_fermi", totale: 176887, bianchi: 145808, neri: 23346, ispanici: 4599, asiatici: 3134, uomini: 122553, donne: 54687};
		var DIST9_fermi = {id: "DIST9_fermi", totale: 222377, bianchi: 174787, neri: 34402, ispanici: 8841, asiatici: 4347, uomini: 144790, donne: 78099};
		var DIST10_fermi = {id: "DIST10_fermi", totale: 245675, bianchi: 181506, neri: 46663, ispanici: 11231, asiatici: 6275, uomini: 166741, donne: 79272};
		var DIST11_fermi = {id: "DIST11_fermi", totale: 295616, bianchi: 216970, neri: 67507, ispanici: 7373, asiatici: 3766, uomini: 204131, donne: 91952};
		var DIST12_fermi = {id: "DIST12_fermi", totale: 237257, bianchi: 198287, neri: 27541, ispanici: 8022, asiatici: 3407, uomini: 164708, donne: 72947};
		var DIST13_fermi = {id: "DIST13_fermi", totale: 245741, bianchi: 207372, neri: 29195, ispanici: 6562, asiatici: 2612, uomini: 165508, donne: 80555};
		var DIST14_fermi = {id: "DIST14_fermi", totale: 96920, bianchi: 89400, neri: 4833, ispanici: 2052, asiatici: 635, uomini: 64481, donne: 32528};
		var DIST15_fermi = {id: "DIST15_fermi", totale: 90135, bianchi: 60394, neri: 14682, ispanici: 5412, asiatici: 1643, uomini: 50552, donne: 41190};
		var DIST16_fermi = {id: "DIST16_fermi", totale: 141978, bianchi: 115115, neri: 15262, ispanici: 9007, asiatici: 2594, uomini: 96535, donne: 45746};
		var DIST17_fermi = {id: "DIST17_fermi", totale: 128992, bianchi: 105809, neri: 11890, ispanici: 9013, asiatici: 2280, uomini: 90111, donne: 39059};
		var DIST18_fermi = {id: "DIST18_fermi", totale: 155197, bianchi: 136320, neri: 12746, ispanici: 3823, asiatici: 2308, uomini: 104707, donne: 50760};
        var DIST19_fermi = {id: "DIST19_fermi", totale: 90135, bianchi: 60394, neri: 14682, ispanici: 5412, asiatici: 1643, uomini: 50552, donne: 41190};
        var DIST20_fermi = {id: "DIST20_fermi", totale: 90135, bianchi: 60394, neri: 14682, ispanici: 5412, asiatici: 1643, uomini: 50552, donne: 41190};

        /* 'distretti_fermi' è un array contenente le informazioni sui fermi dei singoli distretti come oggetti */
		var distretti_fermi = [DIST1_fermi, DIST2_fermi, DIST3_fermi, DIST4_fermi, DIST5_fermi, DIST6_fermi, DIST7_fermi, DIST8_fermi, DIST9_fermi,
		DIST10_fermi, DIST11_fermi, DIST12_fermi, DIST13_fermi, DIST14_fermi, DIST15_fermi, DIST16_fermi, DIST17_fermi, DIST18_fermi,DIST19_fermi,DIST20_fermi];
