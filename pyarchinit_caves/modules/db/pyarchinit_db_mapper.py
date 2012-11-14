#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
        pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
        					 stored in Postgres
                             -------------------
    begin                : 2007-12-01
    copyright            : (C) 2008 by Luca Mandolesi
    email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import mapper
from pyarchinit_db_structure import US_table, UT_table, US_table_toimp, Site_table, Periodizzazione_table, Inventario_materiali_table, Struttura_table, Media_table, Media_thumb_table,Media_to_US_table, Tafonomia_table, Inventario_materiali_table_toimp, Pyarchinit_thesaurus_sigle, SCHEDAIND_table, DETSESSO_table, DETETA_table, Archeozoology_table, Ipogeo_table


class US(object):
	#def __init__"
	def __init__(self,
	id_us,
	sito,
	area,
	us,
	d_stratigrafica,
	d_interpretativa,
	descrizione,
	interpretazione,
	periodo_iniziale,
	fase_iniziale,
	periodo_finale,
	fase_finale,
	scavato,
	attivita,
	anno_scavo,
	metodo_di_scavo,
	inclusi,
	campioni,
	rapporti,
	data_schedatura,
	schedatore,
	formazione,
	stato_di_conservazione,
	colore,
	consistenza,
	struttura,
	cont_per,
	order_layer,
	documentazione
	):
		self.id_us = id_us #0
		self.sito = sito #1
		self.area = area #2
		self.us = us #3
		self.d_stratigrafica = d_stratigrafica #4
		self.d_interpretativa = d_interpretativa #5
		self.descrizione = descrizione #6
		self.interpretazione = interpretazione #7
		self.periodo_iniziale = periodo_iniziale #8
		self.fase_iniziale = fase_iniziale #9
		self.periodo_finale = periodo_finale #10
		self.fase_finale = fase_finale #11
		self.scavato = scavato #12
		self.attivita = attivita #13
		self.anno_scavo = anno_scavo #14
		self.metodo_di_scavo = metodo_di_scavo #15
		self.inclusi = inclusi  #16
		self.campioni = campioni #17
		self.rapporti = rapporti #18
		self.data_schedatura = data_schedatura #19
		self.schedatore = schedatore #20
		self.formazione = formazione #21
		self.stato_di_conservazione = stato_di_conservazione #22
		self.colore = colore #23
		self.consistenza = consistenza #24
		self.struttura = struttura #25
		self.cont_per = cont_per #26
		self.order_layer = order_layer #27
		self.documentazione = documentazione #28

	#def __repr__"
	def __repr__(self):
		return "<US(%d, '%s', '%s', %d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s')>" % (
		self.id_us,
		self.sito,
		self.area,
		self.us,
		self.d_stratigrafica,
		self.d_interpretativa,
		self.descrizione,
		self.interpretazione,
		self.periodo_iniziale,
		self.fase_iniziale,
		self.periodo_finale,
		self.fase_finale,
		self.scavato,
		self.attivita,
		self.anno_scavo,
		self.metodo_di_scavo,
		self.inclusi,
		self.campioni,
		self.rapporti,
		self.data_schedatura,
		self.schedatore,
		self.formazione,
		self.stato_di_conservazione,
		self.colore,
		self.consistenza,
		self.struttura,
		self.cont_per,
		self.order_layer,
		self.documentazione
		)
#mapper
mapper(US, US_table.us_table)


class UT(object):
	#def __init__"
	def __init__(self,
	id_ut,
	progetto,
	nr_ut,
	ut_letterale,
	def_ut,
	descrizione_ut,
	interpretazione_ut,
	nazione,
	regione,
	provincia,
	comune,
	frazione,
	localita,
	indirizzo,
	nr_civico,
	carta_topo_igm,
	carta_ctr,
	coord_geografiche,
	coord_piane,
	quota,
	andamento_terreno_pendenza,
	utilizzo_suolo_vegetazione,
	descrizione_empirica_suolo,
	descrizione_luogo,
	metodo_rilievo_e_ricognizione,
	geometria,
	bibliografia,
	data,
	ora_meteo,
	responsabile,
	dimensioni_ut,
	rep_per_mq,
	rep_datanti,
	periodo_I,
	datazione_I,
	interpretazione_I,
	periodo_II,
	datazione_II,
	interpretazione_II,
	documentazione,
	enti_tutela_vincoli,
	indagini_preliminari
	):
		self.id_ut = id_ut #0
		self.progetto = progetto #1
		self.nr_ut = nr_ut #2
		self.ut_letterale = ut_letterale #3
		self.def_ut = def_ut #4
		self.descrizione_ut = descrizione_ut #5
		self.interpretazione_ut = interpretazione_ut #6
		self.nazione = nazione #7
		self.regione = regione #8
		self.provincia = provincia #9
		self.comune = comune #10
		self.frazione = frazione #11
		self.localita = localita #12
		self.indirizzo = indirizzo #13
		self.nr_civico = nr_civico #14
		self.carta_topo_igm = carta_topo_igm #15
		self.carta_ctr = carta_ctr #16
		self.coord_geografiche = coord_geografiche #17
		self.coord_piane = coord_piane #18
		self.quota = quota #19
		self.andamento_terreno_pendenza = andamento_terreno_pendenza #20
		self.utilizzo_suolo_vegetazione = utilizzo_suolo_vegetazione #21
		self.descrizione_empirica_suolo = descrizione_empirica_suolo #22
		self.descrizione_luogo = descrizione_luogo #23
		self.metodo_rilievo_e_ricognizione = metodo_rilievo_e_ricognizione #24
		self.geometria = geometria #25
		self.bibliografia = bibliografia #26
		self.data = data #27
		self.ora_meteo = ora_meteo #28
		self.responsabile = responsabile #29
		self.dimensioni_ut = dimensioni_ut #30
		self.rep_per_mq = rep_per_mq #31
		self.rep_datanti = rep_datanti #32
		self.periodo_I = periodo_I #33
		self.datazione_I = datazione_I #34
		self.interpretazione_I = interpretazione_I #35
		self.periodo_II = periodo_II #36
		self.datazione_II = datazione_II #37
		self.interpretazione_II = interpretazione_II #38
		self.documentazione = documentazione #39
		self.enti_tutela_vincoli = enti_tutela_vincoli #40
		self.indagini_preliminari = indagini_preliminari #41
	#def __repr__"
	def __repr__(self):
		return "<UT(%d, '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%f', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
		
		self.id_ut,
		self.progetto,
		self.nr_ut,
		self.ut_letterale,
		self.def_ut,
		self.descrizione_ut,
		self.interpretazione_ut,
		self.nazione,
		self.regione,
		self.provincia,
		self.comune,
		self.frazione,
		self.localita,
		self.indirizzo,
		self.nr_civico,
		self.carta_topo_igm,
		self.carta_ctr,
		self.coord_geografiche,
		self.coord_piane,
		self.quota,
		self.andamento_terreno_pendenza,
		self.utilizzo_suolo_vegetazione,
		self.descrizione_empirica_suolo,
		self.descrizione_luogo,
		self.metodo_rilievo_e_ricognizione,
		self.geometria,
		self.bibliografia,
		self.data,
		self.ora_meteo,
		self.responsabile,
		self.dimensioni_ut,
		self.rep_per_mq,
		self.rep_datanti,
		self.periodo_I,
		self.datazione_I,
		self.interpretazione_I,
		self.periodo_II,
		self.datazione_II,
		self.interpretazione_II,
		self.documentazione,
		self.enti_tutela_vincoli,
		self.indagini_preliminari
		)

#mapper
mapper(UT, UT_table.ut_table)

class US_TOIMP(object):
	#def __init__"
	def __init__(self,
	id_us,
	sito,
	area,
	us,
	d_stratigrafica,
	d_interpretativa,
	descrizione,
	interpretazione,
	periodo_iniziale,
	fase_iniziale,
	periodo_finale,
	fase_finale,
	scavato,
	attivita,
	anno_scavo,
	metodo_di_scavo,
	inclusi,
	campioni,
	rapporti,
	data_schedatura,
	schedatore,
	formazione,
	stato_di_conservazione,
	colore,
	consistenza,
	struttura
	):
		self.id_us = id_us #0
		self.sito = sito #1
		self.area = area #2
		self.us = us #3
		self.d_stratigrafica = d_stratigrafica #4
		self.d_interpretativa = d_interpretativa #5
		self.descrizione = descrizione #6
		self.interpretazione = interpretazione #7
		self.periodo_iniziale = periodo_iniziale #8
		self.fase_iniziale = fase_iniziale #9
		self.periodo_finale = periodo_finale #10
		self.fase_finale = fase_finale #11
		self.scavato = scavato #12
		self.attivita = attivita #13
		self.anno_scavo = anno_scavo #14
		self.metodo_di_scavo = metodo_di_scavo #15
		self.inclusi = inclusi  #16
		self.campioni = campioni #17
		self.rapporti = rapporti #18
		self.data_schedatura = data_schedatura #19
		self.schedatore = schedatore #20
		self.formazione = formazione #21
		self.stato_di_conservazione = stato_di_conservazione #22
		self.colore = colore #23
		self.consistenza = consistenza #24
		self.struttura = struttura #25


	#def __repr__"
	def __repr__(self):
		return "<US_TOIMP('%d', '%s', '%s', %d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_us,
		self.sito,
		self.area,
		self.us,
		self.d_stratigrafica,
		self.d_interpretativa,
		self.descrizione,
		self.interpretazione,
		self.periodo_iniziale,
		self.fase_iniziale,
		self.periodo_finale,
		self.fase_finale,
		self.scavato,
		self.attivita,
		self.anno_scavo,
		self.metodo_di_scavo,
		self.inclusi,
		self.campioni,
		self.rapporti,
		self.data_schedatura,
		self.schedatore,
		self.formazione,
		self.stato_di_conservazione,
		self.colore,
		self.consistenza,
		self.struttura
		)
#mapper
mapper(US_TOIMP, US_table_toimp.us_table_toimp)

class SITE(object):
	#def __init__"
	def __init__(self,
	id_sito,
	sito,
	nazione,
	regione,
	comune,
	descrizione,
	provincia
	):
		self.id_sito = id_sito #0
		self.sito = sito #1
		self.nazione = nazione #2
		self.regione = regione #3
		self.comune = comune #4
		self.descrizione = descrizione #5
		self.provincia = provincia #5

	#def __repr__"
	def __repr__(self):
		return "<SITE('%d','%s', '%s',%s,'%s','%s')>" % (
		self.id_sito,
		self.sito,
		self.nazione,
		self.regione,
		self.comune,
		self.descrizione,
		self.provincia
		)
#mapper
mapper(SITE, Site_table.site_table)


class PERIODIZZAZIONE(object):
	#def __init__"
	def __init__(self,
	id_perfas,
	sito,
	periodo,
	fase,
	cron_iniziale,
	cron_finale,
	descrizione,
	datazione_estesa,
	cont_per
	):
		self.id_perfas = id_perfas #0
		self.sito = sito #1
		self.periodo = periodo #2
		self.fase = fase #3
		self.cron_iniziale = cron_iniziale #4
		self.cron_finale = cron_finale #5
		self.descrizione = descrizione #6
		self.datazione_estesa = datazione_estesa #7
		self.cont_per = cont_per #8

	#def __repr__"
	def __repr__(self):
		return "<PERIODIZZAZIONE('%d', '%s', '%d', '%d', '%d', '%d', '%s', '%s', '%d')>" % (
		self.id_perfas,
		self.sito,
		self.periodo,
		self.fase,
		self.cron_iniziale,
		self.cron_finale,
		self.descrizione,
		self.datazione_estesa,
		self.cont_per
		)
#mapper

mapper(PERIODIZZAZIONE, Periodizzazione_table.periodizzazione_table)

class INVENTARIO_MATERIALI(object):
	#def __init__"
	def __init__(self,
	id_invmat,
	sito,
	numero_inventario,
	tipo_reperto,
	criterio_schedatura,
	definizione,
	descrizione,
	area,
	us,
	lavato,
	nr_cassa,
	luogo_conservazione,
	stato_conservazione,
	datazione_reperto,
	elementi_reperto,
	misurazioni,
	rif_biblio,
	tecnologie
	):
		self.id_invmat = id_invmat #0
		self.sito = sito #1
		self.numero_inventario = numero_inventario #2
		self.tipo_reperto = tipo_reperto #3
		self.criterio_schedatura = criterio_schedatura #4
		self.definizione = definizione #5
		self.descrizione = descrizione #6
		self.area = area #7
		self.us = us #8
		self.lavato = lavato #9
		self.nr_cassa = nr_cassa #10
		self.luogo_conservazione = luogo_conservazione #11
		self.stato_conservazione = stato_conservazione #12
		self.datazione_reperto = datazione_reperto #13
		self.elementi_reperto = elementi_reperto #14
		self.misurazioni = misurazioni #15
		self.rif_biblio = rif_biblio #16
		self.tecnologie = tecnologie #17

	#def __repr__"
	def __repr__(self):
		return "<INVENTARIO_MATERIALI(%d, '%s', '%d', '%s', '%s', '%s', '%s', %d, %d, '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_invmat,
		self.sito,
		self.numero_inventario,
		self.tipo_reperto,
		self.criterio_schedatura,
		self.definizione,
		self.descrizione,
		self.area,
		self.us,
		self.lavato,
		self.nr_cassa,
		self.luogo_conservazione,
		self.stato_conservazione,
		self.datazione_reperto,
		self.elementi_reperto,
		self.misurazioni,
		self.rif_biblio,
		self.tecnologie
		)
#mapper

mapper(INVENTARIO_MATERIALI, Inventario_materiali_table.inventario_materiali_table)

class INVENTARIO_MATERIALI_TOIMP(object):
	#def __init__"
	def __init__(self,
	id_invmat,
	sito,
	numero_inventario,
	tipo_reperto,
	criterio_schedatura,
	definizione,
	descrizione,
	area,
	us,
	lavato,
	nr_cassa,
	luogo_conservazione,
	stato_conservazione,
	datazione_reperto,
	elementi_reperto,
	misurazioni,
	rif_biblio,
	tecnologie
	):
		self.id_invmat = id_invmat #0
		self.sito = sito #1
		self.numero_inventario = numero_inventario #2
		self.tipo_reperto = tipo_reperto #3
		self.criterio_schedatura = criterio_schedatura #4
		self.definizione = definizione #5
		self.descrizione = descrizione #6
		self.area = area #7
		self.us = us #8
		self.lavato = lavato #9
		self.nr_cassa = nr_cassa #10
		self.luogo_conservazione = luogo_conservazione #11
		self.stato_conservazione = stato_conservazione #12
		self.datazione_reperto = datazione_reperto #13
		self.elementi_reperto = elementi_reperto #14
		self.misurazioni = misurazioni #15
		self.rif_biblio = rif_biblio #16
		self.tecnologie = tecnologie #17

	#def __repr__"
	def __repr__(self):
		return "<INVENTARIO_MATERIALI_TOIMP(%d, '%s', '%d', '%s', '%s', '%s', '%s', %d, %d, '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_invmat,
		self.sito,
		self.numero_inventario,
		self.tipo_reperto,
		self.criterio_schedatura,
		self.definizione,
		self.descrizione,
		self.area,
		self.us,
		self.lavato,
		self.nr_cassa,
		self.luogo_conservazione,
		self.stato_conservazione,
		self.datazione_reperto,
		self.elementi_reperto,
		self.misurazioni,
		self.rif_biblio,
		self.tecnologie
		)
#mapper

mapper(INVENTARIO_MATERIALI_TOIMP, Inventario_materiali_table_toimp.inventario_materiali_table_toimp)

class STRUTTURA(object):
	def __init__(self,
	id_struttura,
	sito,
	sigla_struttura,
	numero_struttura,
	categoria_struttura,
	tipologia_struttura,
	definizione_struttura,
	descrizione,
	interpretazione,
	periodo_iniziale,
	fase_iniziale,
	periodo_finale,
	fase_finale,
	datazione_estesa,
	materiali_impiegati,
	elementi_strutturali,
	rapporti_struttura,
	misure_struttura
	):
		self.id_struttura = id_struttura #0
		self.sito = sito #1
		self.sigla_struttura = sigla_struttura #2
		self.numero_struttura = numero_struttura #3
		self.categoria_struttura = categoria_struttura #4
		self.tipologia_struttura = tipologia_struttura #5
		self.definizione_struttura = definizione_struttura #6
		self.descrizione = descrizione #7
		self.interpretazione = interpretazione #8
		self.periodo_iniziale = periodo_iniziale #9
		self.fase_iniziale = fase_iniziale #10
		self.periodo_finale = periodo_finale #11
		self.fase_finale = fase_finale #12
		self.datazione_estesa = datazione_estesa #13
		self.materiali_impiegati = materiali_impiegati #14
		self.elementi_strutturali = elementi_strutturali #15
		self.rapporti_struttura = rapporti_struttura #16
		self.misure_struttura = misure_struttura #17

	#def __repr__"
	def __repr__(self):
		return "<STRUTTURA('%d', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_struttura,
		self.sito,
		self.sigla_struttura,
		self.numero_struttura,
		self.tipologia_struttura,
		self.categoria_struttura.
		self.definizione_struttura,
		self.descrizione,
		self.interpretazione,
		self.periodo_iniziale,
		self.fase_iniziale,
		self.periodo_finale,
		self.fase_finale,
		self.datazione_estesa,
		self.materiali_impiegati,
		self.elementi_strutturali,
		self.rapporti_struttura,
		self.misure_struttura
		)
#mapper

mapper(STRUTTURA, Struttura_table.struttura_table)

class MEDIA(object):
	#def __init__"
	def __init__(self,
	id_media,
	mediatype,
	filename,
	filetype,
	filepath,
	descrizione,
	tags
	):
		self.id_media = id_media #0
		self.mediatype = mediatype #1
		self.filename = filename #2
		self.filetype = filetype #3
		self.filepath = filepath #4
		self.descrizione = descrizione #5
		self.tags = tags #5

	#def __repr__"
	def __repr__(self):
		return "<MEDIA('%d', '%s', '%s', %s, '%s','%s')>" % (
		self.id_media,
		self.mediatype,
		self.filename,
		self.filetype,
		self.filepath,
		self.descrizione,
		self.tags
		)
#mapper
mapper(MEDIA, Media_table.media_table)


class MEDIA_THUMB(object):
	#def __init__"
	def __init__(self,
	id_media_thumb,
	id_media,
	mediatype,
	media_filename,
	media_thumb_filename,
	filetype,
	filepath
	):
		self.id_media_thumb = id_media_thumb #0
		self.id_media = id_media #1
		self.mediatype = mediatype #2
		self.media_filename = media_filename #3
		self.media_thumb_filename = media_thumb_filename #4
		self.filetype = filetype #5
		self.filepath = filepath #6

	#def __repr__"
	def __repr__(self):
		return "<MEDIA('%d', '%d', '%s', '%s', %s, '%s', '%s')>" % (
		sekf.id_media_thumb,
		self.id_media,
		self.mediatype,
		self.media_filename,
		self.media_thumb_filename,
		self.filetype,
		self.filepath
		)
#mapper
mapper(MEDIA_THUMB, Media_thumb_table.media_thumb_table)


class MEDIATOUS(object):
	#def __init__"
	def __init__(self,
	id_mediaToUs,
	id_us,
	sito,
	area,
	us,
	id_media,
	filepath
	):
		self.id_mediaToUs = id_mediaToUs #0
		self.id_us = id_us
		self.sito = sito
		self.area = area
		self.us = us
		self.id_media = id_media
		self.filepath = filepath

	#def __repr__"
	def __repr__(self):
		return "<MEDIATOUS('%d', '%d', '%s', '%s', '%d', '%d', '%s')>" % (
		self.id_mediaToUs,
		self.id_us,
		self.sito,
		self.area,
		self.us,
		self.id_media,
		self.filepath
		)
#mapper
mapper(MEDIATOUS, Media_to_US_table.media_to_us_table)


class TAFONOMIA(object):
	def __init__(self,
	id_tafonomia,
	sito,
	nr_scheda_taf,
	sigla_struttura,
	nr_struttura,
	nr_individuo,
	rito,
	descrizione_taf,
	interpretazione_taf,
	segnacoli,
	canale_libatorio_si_no,
	oggetti_rinvenuti_esterno,
	stato_di_conservazione,
	copertura_tipo,
	tipo_contenitore_resti,
	orientamento_asse,
	orientamento_azimut,
	corredo_presenza,
	corredo_tipo,
	corredo_descrizione,
	lunghezza_scheletro,
	posizione_scheletro,
	posizione_cranio,
	posizione_arti_superiori,
	posizione_arti_inferiori,
	completo_si_no,
	disturbato_si_no,
	in_connessione_si_no,
	caratteristiche
	):
		self.id_tafonomia = id_tafonomia
		self.sito = sito
		self.nr_scheda_taf = nr_scheda_taf
		self.sigla_struttura = sigla_struttura
		self.nr_struttura = nr_struttura
		self.nr_individuo = nr_individuo
		self.rito = rito
		self.descrizione_taf = descrizione_taf
		self.interpretazione_taf = interpretazione_taf
		self.segnacoli = segnacoli 
		self.canale_libatorio_si_no = canale_libatorio_si_no 
		self.oggetti_rinvenuti_esterno = oggetti_rinvenuti_esterno 
		self.stato_di_conservazione = stato_di_conservazione 
		self.copertura_tipo = copertura_tipo 
		self.tipo_contenitore_resti = tipo_contenitore_resti 
		self.orientamento_asse = orientamento_asse 
		self.orientamento_azimut = orientamento_azimut 
		self.corredo_presenza = corredo_presenza 
		self.corredo_tipo = corredo_tipo
		self.corredo_descrizione = corredo_descrizione
		self.lunghezza_scheletro = lunghezza_scheletro 
		self.posizione_scheletro = posizione_scheletro 
		self.posizione_cranio = posizione_cranio 
		self.posizione_arti_superiori = posizione_arti_superiori
		self.posizione_arti_inferiori = posizione_arti_inferiori
		self.completo_si_no = completo_si_no
		self.disturbato_si_no = disturbato_si_no
		self.in_connessione_si_no = in_connessione_si_no
		self.caratteristiche = caratteristiche

		#def __repr__"
	def __repr__(self):
		return "<TAFONOMIA('%d', '%s', '%d', '%s', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%f', '%s', '%s', '%s', '%r', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_tafonomia,
		self.sito,
		self.nr_scheda_taf,
		self.sigla_struttura,
		self.nr_struttura,
		self.nr_individuo,
		self.rito,
		self.descrizione_taf,
		self.interpretazione_taf,
		self.segnacoli,
		self.canale_libatorio_si_no,
		self.oggetti_rinvenuti_esterno,
		self.stato_di_conservazione,
		self.copertura_tipo,
		self.tipo_contenitore_resti,
		self.orientamento_asse,
		self.orientamento_azimut,
		self.corredo_presenza,
		self.corredo_tipo,
		self.corredo_descrizione,
		self.lunghezza_scheletro,
		self.posizione_scheletro,
		self.posizione_cranio,
		self.posizione_arti_superiori,
		self.posizione_arti_inferiori,
		self.completo_si_no,
		self.disturbato_si_no,
		self.in_connessione_si_no,
		self.caratteristiche,
		self.nr_individuo
		)

#mapper
mapper(TAFONOMIA, Tafonomia_table.tafonomia_table)


class PYARCHINIT_THESAURUS_SIGLE(object):
	#def __init__"
	def __init__(self,
	id_thesaurus_sigle,
	nome_tabella,
	sigla,
	sigla_estesa,
	descrizione,
	tipologia_sigla
	):
		self.id_thesaurus_sigle = id_thesaurus_sigle #0
		self.nome_tabella = nome_tabella #1
		self.sigla = sigla #2
		self.sigla_estesa = sigla_estesa #3
		self.descrizione = descrizione #4
		self.tipologia_sigla = tipologia_sigla #5
		

	#def __repr__"
	def __repr__(self):
		return "<PYARCHINIT_THESAURUS_SIGLE('%d', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_thesaurus_sigle,
		self.nome_tabella,
		self.sigla,
		self.sigla_estesa,
		self.descrizione,
		self.tipologia_sigla
		)
#mapper

mapper(PYARCHINIT_THESAURUS_SIGLE, Pyarchinit_thesaurus_sigle.pyarchinit_thesaurus_sigle)

class SCHEDAIND(object):
	#def __init__"
	def __init__(self,
	id_scheda_ind,
	sito,
	area,
	us,
	nr_individuo,
	data_schedatura,
	schedatore,
	sesso,
	eta_min,
	eta_max,
	classi_eta,
	osservazioni):
		self.id_scheda_ind = id_scheda_ind #1
		self.sito = sito #2
		self.area = area
		self.us = us #3
		self.nr_individuo = nr_individuo #6
		self.data_schedatura = data_schedatura #4
		self.schedatore = schedatore #5
		self.sesso = sesso #7
		self.eta_min = eta_min #8
		self.eta_max = eta_max #9
		self.classi_eta = eta_max #10
		self.osservazioni = osservazioni #11

	#def __repr__"
	def __repr__(self):
		return "<SCHEDAIND('%d','%s', '%d','%s','%d','%s','%s','%s','%d','%d','%s','%s')>" % (
		self.id_scheda_ind,
		self.sito,
		self.area,
		self.us,
		self.nr_individuo,
		self.data_schedatura,
		self.schedatore,
		self.sesso,
		self.eta_min,
		self.eta_max,
		self.classi_eta,
		self.osservazioni
		)
#mapper

mapper(SCHEDAIND, SCHEDAIND_table.individui_table)

class DETSESSO(object):
	#def __init__"
	def __init__(self,
	id_det_sesso,
	sito,
	num_individuo,
	glab_grado_imp,
	pmast_grado_imp,
	pnuc_grado_imp,
	pzig_grado_imp,
	arcsop_grado_imp,
	tub_grado_imp,
	pocc_grado_imp,
	inclfr_grado_imp,
	zig_grado_imp,
	msorb_grado_imp,
	glab_valori,
	pmast_valori,
	pnuc_valori,
	pzig_valori,
	arcsop_valori,
	tub_valori,
	pocc_valori,
	inclfr_valori,
	zig_valori,
	msorb_valori,
	palato_grado_imp,
	mfmand_grado_imp,
	mento_grado_imp,
	anmand_grado_imp,
	minf_grado_imp,
	brmont_grado_imp,
	condm_grado_imp,
	palato_valori,
	mfmand_valori,
	mento_valori,
	anmand_valori,
	minf_valori,
	brmont_valori,
	condm_valori,
	sex_cr_tot,
	ind_cr_sex,
	sup_p_I,
	sup_p_II,
	sup_p_III,
	sup_p_sex,
	in_isch_I,
	in_isch_II,
	in_isch_III,
	in_isch_sex,
	arco_c_sex,
	ramo_ip_I,
	ramo_ip_II,
	ramo_ip_III,
	ramo_ip_sex,
	prop_ip_sex,
	ind_bac_sex):
		self.id_det_sesso = id_det_sesso #1
		self.sito = sito #2
		self.num_individuo = num_individuo #3
		self.glab_grado_imp = glab_grado_imp #4
		self.pmast_grado_imp = pmast_grado_imp #5
		self.pnuc_grado_imp = pnuc_grado_imp #6
		self.pzig_grado_imp = pzig_grado_imp #7
		self.arcsop_grado_imp = arcsop_grado_imp #8
		self.tub_grado_imp = tub_grado_imp #9
		self.pocc_grado_imp = pocc_grado_imp #10
		self.inclfr_grado_imp = inclfr_grado_imp #11
		self.zig_grado_imp = zig_grado_imp #12
		self.msorb_grado_imp = msorb_grado_imp #13
		self.glab_valori = glab_valori #14
		self.pmast_valori = pmast_valori #15
		self.pnuc_valori = pnuc_valori #16
		self.pzig_valori = pzig_valori #17
		self.arcsop_valori = arcsop_valori #18
		self.tub_valori = tub_valori#19
		self.pocc_valori = pocc_valori# 20
		self.inclfr_valori = inclfr_valori# 21
		self.zig_valori = zig_valori #22
		self.msorb_valori = msorb_valori #23
		self.palato_grado_imp = palato_grado_imp #24
		self.mfmand_grado_imp = mfmand_grado_imp #25
		self.mento_grado_imp = mento_grado_imp #26
		self.anmand_grado_imp = anmand_grado_imp #27
		self.minf_grado_imp = minf_grado_imp #28
		self.brmont_grado_imp = brmont_grado_imp #29
		self.condm_grado_imp = condm_grado_imp #30
		self.palato_valori = palato_valori #31
		self.mfmand_valori = mfmand_valori #32
		self.mento_valori = mento_valori #33
		self.anmand_valori = anmand_valori# 34
		self.minf_valori = minf_valori #35
		self.brmont_valori = brmont_valori #36
		self.condm_valori = condm_valori #37
		self.sex_cr_tot = sex_cr_tot #38
		self.ind_cr_sex = ind_cr_sex #39
		self.sup_p_I = sup_p_I #40
		self.sup_p_II = sup_p_II #41
		self.sup_p_III = sup_p_III #42
		self.sup_p_sex = sup_p_sex #43
		self.in_isch_I = in_isch_I #44
		self.in_isch_II = in_isch_II #45
		self.in_isch_III = in_isch_III #46
		self.in_isch_sex = in_isch_sex #47
		self.arco_c_sex = arco_c_sex #48
		self.ramo_ip_I = ramo_ip_I #49
		self.ramo_ip_II = ramo_ip_II #50
		self.ramo_ip_III = ramo_ip_III #51
		self.ramo_ip_sex = ramo_ip_sex #52
		self.prop_ip_sex = prop_ip_sex #53
		self.ind_bac_sex = ind_bac_sex #54

	#def __repr__"
	def __repr__(self):
		return "<DETSESSO('%d','%s','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d', '%d', '%d', '%d', '%d', %d,'%d','%d','%d','%d','%r','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
		self.id_det_sesso,
		self.sito,
		self.num_individuo,
		self.glab_grado_imp,
		self.pmast_grado_imp,
		self.pnuc_grado_imp,
		self.pzig_grado_imp,
		self.arcsop_grado_imp,
		self.tub_grado_imp,
		self.pocc_grado_imp,
		self.inclfr_grado_imp,
		self.zig_grado_imp,
		self.msorb_grado_imp,
		self.glab_valori,
		self.pmast_valori,
		self.pnuc_valori,
		self.pzig_valori,
		self.arcsop_valori,
		self.tub_valori,
		self.pocc_valori,
		self.inclfr_valori,
		self.zig_valori,
		self.msorb_valori,
		self.palato_grado_imp,
		self.mfmand_grado_imp,
		self.mento_grado_imp,
		self.anmand_grado_imp,
		self.minf_grado_imp,
		self.brmont_grado_imp,
		self.condm_grado_imp,
		self.palato_valori,
		self.mfmand_valori,
		self.mento_valori,
		self.anmand_valori,
		self.minf_valori,
		self.brmont_valori,
		self.condm_valori,
		self.sex_cr_tot,
		self.ind_cr_sex,
		self.sup_p_I,
		self.sup_p_II,
		self.sup_p_III,
		self.sup_p_sex,
		self.in_isch_I,
		self.in_isch_II,
		self.in_isch_III,
		self.in_isch_sex,
		self.arco_c_sex,
		self.ramo_ip_I,
		self.ramo_ip_II,
		self.ramo_ip_III,
		self.ramo_ip_sex,
		self.prop_ip_sex,
		self.ind_bac_sex
		)
#mapper

mapper(DETSESSO, DETSESSO_table.detsesso_table)

class DETETA(object):
	#def __init__"
	def __init__(self,
	id_det_eta,
	sito,
	nr_individuo,
	sinf_min,
	sinf_max,
	sinf_min_2,
	sinf_max_2,
	SSPIA,
	SSPIB,
	SSPIC,
	SSPID,
	sup_aur_min,
	sup_aur_max,
	sup_aur_min_2,
	sup_aur_max_2,
	ms_sup_min,
	ms_sup_max,
	ms_inf_min,
	ms_inf_max,
	usura_min,
	usura_max,
	Id_endo,
	Is_endo,
	IId_endo,
	IIs_endo,
	IIId_endo,
	IIIs_endo,
	IV_endo,
	V_endo,
	VI_endo,
	VII_endo,
	VIIId_endo,
	VIIIs_endo,
	IXd_endo,
	IXs_endo,
	Xd_endo,
	Xs_endo,
	endo_min,
	endo_max,
	volta_1,
	volta_2,
	volta_3,
	volta_4,
	volta_5,
	volta_6,
	volta_7,
	lat_6,
	lat_7,
	lat_8,
	lat_9,
	lat_10,
	volta_min,
	volta_max,
	ant_lat_min,
	ant_lat_max,
	ecto_min,
	ecto_max):
		self.id_det_eta = id_det_eta 	#1
		self.sito = sito 				#2
		self.nr_individuo = nr_individuo #3
		self.sinf_min = sinf_min #4
		self.sinf_max = sinf_max #5
		self.sinf_min_2 = sinf_min #4
		self.sinf_max_2= sinf_max #5
		self.SSPIA = SSPIA #6
		self.SSPIB = SSPIB #7
		self.SSPIC = SSPIC #8
		self.SSPID = SSPID #9
		self.sup_aur_min = sup_aur_min #10
		self.sup_aur_max = sup_aur_max #11
		self.sup_aur_min_2 = sup_aur_min #12
		self.sup_aur_max_2 = sup_aur_max #13
		self.ms_sup_min = ms_sup_min #14
		self.ms_sup_max = ms_sup_max #15
		self.ms_inf_min = ms_inf_min #16
		self.ms_inf_max = ms_inf_max #17
		self.usura_min = usura_min #18
		self.usura_max = usura_max #19
		self.Id_endo = Id_endo #20
		self.Is_endo = Is_endo#21
		self.IId_endo = IId_endo#22
		self.IIs_endo = IIs_endo#23
		self.IIId_endo = IIId_endo #24
		self.IIIs_endo = IIIs_endo #25
		self.IV_endo = IV_endo #26
		self.V_endo = V_endo #27
		self.VI_endo = VI_endo #28
		self.VII_endo = VII_endo #29
		self.VIIId_endo = VIIId_endo #30
		self.VIIIs_endo = VIIIs_endo #31
		self.IXd_endo = IXd_endo #32
		self.IXs_endo = IXs_endo #33
		self.Xd_endo = Xd_endo #34
		self.Xs_endo = Xs_endo #35
		self.endo_min = endo_min#36
		self.endo_max = endo_max#37
		self.volta_1 = volta_1 #38
		self.volta_2 = volta_2 #39
		self.volta_3 = volta_3 #40
		self.volta_4 = volta_4 #41
		self.volta_5 = volta_5 #42
		self.volta_6 = volta_6 #43
		self.volta_7 = volta_7 #44
		self.lat_6 = lat_6 #45
		self.lat_7 = lat_7 #46
		self.lat_8 = lat_8 #47
		self.lat_9 = lat_9 #48
		self.lat_10 = lat_10 #49
		self.volta_min = volta_min #50
		self.volta_max = volta_max #51
		self.ant_lat_min = ant_lat_min #52
		self.ant_lat_max = ant_lat_max #53
		self.ecto_min = ecto_min #54
		self.ecto_max = ecto_max #55

	#def __repr__"
	def __repr__(self):
		return "<DETETA('%d','%s','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')>" % (
		self.id_det_eta,
		self.sito,
		self.nr_individuo,
		self.sinf_min,
		self.sinf_max,
		self.sinf_min_2,
		self.sinf_max_2,
		self.SSPIA,
		self.SSPIB,
		self.SSPIC,
		self.SSPID,
		self.sup_aur_min,
		self.sup_aur_max,
		self.sup_aur_min_2,
		self.sup_aur_max_2,
		self.ms_sup_min,
		self.ms_sup_max,
		self.ms_inf_min,
		self.ms_inf_max,
		self.usura_min,
		self.usura_max,
		self.Id_endo,
		self.Is_endo,
		self.IId_endo,
		self.IIs_endo,
		self.IIId_endo,
		self.IIIs_endo,
		self.IV_endo,
		self.V_endo,
		self.VI_endo,
		self.VII_endo,
		self.VIIId_endo,
		self.VIIIs_endo,
		self.IXd_endo,
		self.IXs_endo,
		self.Xd_endo,
		self.Xs_endo,
		self.endo_min,
		self.endo_max,
		self.volta_1,
		self.volta_2,
		self.volta_3,
		self.volta_4,
		self.volta_5,
		self.volta_6,
		self.volta_7,
		self.lat_6,
		self.lat_7,
		self.lat_8,
		self.lat_9,
		self.lat_10,
		self.volta_min,
		self.volta_max,
		self.ant_lat_min,
		self.ant_lat_max,
		self.ecto_min,
		self.ecto_max
		)
#mapper

mapper(DETETA, DETETA_table.deteta_table)


class ARCHEOZOOLOGY(object):
	#def __init__"
	def __init__(self,
	id_archzoo,
	sito,
	area,
	us,
	quadrato,
	coord_x,
	coord_y,
	coord_z,
	bos_bison,
	calcinati,
	camoscio,
	capriolo,
	cervo,
	combusto,
	coni,
	pdi,
	stambecco,
	strie,
	canidi,
	ursidi,
	megacero
	):
		self.id_archzoo = id_archzoo
		self.sito = sito
		self.area = area
		self.us = us
		self.quadrato = quadrato
		self.coord_x = coord_x
		self.coord_y = coord_y
		self.coord_z = coord_z
		self.bos_bison = bos_bison
		self.calcinati = calcinati
		self.camoscio = camoscio
		self.capriolo = capriolo
		self.cervo = cervo
		self.combusto = combusto
		self.coni = coni
		self.pdi = pdi
		self.stambecco = stambecco
		self.strie = strie
		self.canidi = canidi
		self.ursidi = ursidi
		self.megacero = megacero

	#def __repr__"
	def __repr__(self):
		return "<ARCHEOZOOLOGY('%d', '%s', '%d', '%d', '%s', '%r', '%r', '%r', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')>" % (
		self.id_archzoo,
		self.sito,
		self.area,
		self.us,
		self.quadrato,
		self.coord_x,
		self.coord_y,
		self.coord_z,
		self.bos_bison,
		self.calcinati,
		self.camoscio,
		self.capriolo,
		self.cervo,
		self.combusto,
		self.coni,
		self.pdi,
		self.stambecco,
		self.strie,
		self.canidi,
		self.ursidi,
		self.megacero
		)
#mapper
mapper(ARCHEOZOOLOGY, Archeozoology_table.archeozoology_table)

class IPOGEO(object):
	def __init__(self,
	id_ipogeo,
	sito_ipogeo,
	sigla_ipogeo,
	numero_ipogeo,
	categoria_ipogeo,
	tipologia_ipogeo,
	definizione_ipogeo,
	descrizione_ipogeo,
	interpretazione_ipogeo,
	periodo_iniziale_ipogeo,
	fase_iniziale_ipogeo,
	periodo_finale_ipogeo,
	fase_finale_ipogeo,
	datazione_estesa_ipogeo,
	materiali_impiegati_ipogeo,
	elementi_strutturali_ipogeo,
	rapporti_ipogeo,
	misure_ipogeo,
        percentuale_umidita_ipogeo,
        grado_conservazione_ipogeo,
        grado_staticita_ipogeo
	):
		self.id_ipogeo = id_ipogeo #0
		self.sito_ipogeo = sito_ipogeo #1
		self.sigla_ipogeo = sigla_ipogeo #2
		self.numero_ipogeo = numero_ipogeo #3
		self.categoria_ipogeo = categoria_ipogeo #4
		self.tipologia_ipogeo = tipologia_ipogeo #5
		self.definizione_ipogeo = definizione_ipogeo #6
		self.descrizione_ipogeo = descrizione_ipogeo #7
		self.interpretazione_ipogeo = interpretazione_ipogeo #8
		self.periodo_iniziale_ipogeo = periodo_iniziale_ipogeo #9
		self.fase_iniziale_ipogeo = fase_iniziale_ipogeo #10
		self.periodo_finale_ipogeo = periodo_finale_ipogeo #11
		self.fase_finale_ipogeo = fase_finale_ipogeo #12
		self.datazione_estesa_ipogeo = datazione_estesa_ipogeo #13
		self.materiali_impiegati_ipogeo = materiali_impiegati_ipogeo #14
		self.elementi_strutturali_ipogeo = elementi_strutturali_ipogeo #15
		self.rapporti_ipogeo = rapporti_ipogeo #16
		self.misure_ipogeo = misure_ipogeo #17
		self.percentuale_umidita_ipogeo = percentuale_umidita_ipogeo #18
		self.grado_conservazione_ipogeo = grado_conservazione_ipogeo #19
		self.grado_staticita_ipogeo = grado_staticita_ipogeo #20

	#def __repr__"
	def __repr__(self):
		return "<IPOGEO('%d', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%r', '%d', '%d')>" % (
		self.id_ipogeo,
		self.sito_ipogeo,
		self.sigla_ipogeo,
		self.numero_ipogeo,
		self.categoria_ipogeo,
		self.tipologia_ipogeo,
		self.definizione_ipogeo,
		self.descrizione_ipogeo,
		self.interpretazione_ipogeo,
		self.periodo_iniziale_ipogeo,
		self.fase_iniziale_ipogeo,
		self.periodo_finale_ipogeo,
		self.fase_finale_ipogeo,
		self.datazione_estesa_ipogeo,
		self.materiali_impiegati_ipogeo,
		self.elementi_strutturali_ipogeo,
		self.rapporti_ipogeo,
		self.misure_ipogeo,
                self.percentuale_umidita_ipogeo,
                self.grado_conservazione_ipogeo,
                self.grado_staticita_ipogeo,
		)
#mapper

mapper(IPOGEO, Ipogeo_table.ipogeo_table)
