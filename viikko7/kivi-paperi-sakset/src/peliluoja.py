from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli(vastaus):
    peli = None
    if vastaus.endswith("a"):
        peli = KPSPelaajaVsPelaaja()
    elif vastaus.endswith("b"):
        peli = KPSTekoaly()
    elif vastaus.endswith("c"):
        peli = KPSParempiTekoaly()

    return peli
