from typing import List

from .models import Company, ObchodniJmeno, DalsiUdaje,  Sidlo, AdresaDorucovaci, SeznamRegistraci


def parse_company_data(data:dict) -> Company:
    """
    Parses the JSON response into a Company object.

    Args:
    data: The JSON response from the API. Expected to be a dictionary.

    Returns:
    Company: An instance of the Company class populated with data from the JSON response.

    Raises:
    ValueError: If the input data is not a dictionary.
    """

    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary")

    return Company(
        ico=data.get('ico'),
        obchodniJmeno=data.get('obchodniJmeno'),
        sidlo=parse_sidlo(data),
        pravniForma=data.get('pravniForma'),
        financniUrad=data.get('financniUrad'),
        datumVzniku=data.get('datumVzniku'),
        datumZaniku=data.get('datumZaniku'),
        datumAktualizace=data.get('datumAktualizace'),
        dic=data.get('dic'),
        icoId=data.get('icoId'),
        adresaDorucovaci=parse_adresa_dorucovaci(data),
        seznamRegistraci=parse_seznam_registraci(data),
        primarniZdroj=data.get('primarniZdroj'),
        dalsiUdaje=parse_dalsi_udaje(data),
        czNace=data.get('czNace', []),
        subRegistrSzr=data.get('subRegistrSzr'),
        dicSkDph=data.get('dicSkDph')
    )


def parse_sidlo(data: dict) -> Sidlo:
    sidlo_data = data.get('sidlo', {})
    return Sidlo(
        kodStatu=sidlo_data.get('kodStatu'),
        nazevStatu=sidlo_data.get('nazevStatu'),
        kodKraje=sidlo_data.get('kodKraje'),
        nazevKraje=sidlo_data.get('nazevKraje'),
        kodOkresu=sidlo_data.get('kodOkresu'),
        nazevOkresu=sidlo_data.get('nazevOkresu'),
        kodObce=sidlo_data.get('kodObce'),
        nazevObce=sidlo_data.get('nazevObce'),
        kodSpravnihoObvodu=sidlo_data.get('kodSpravnihoObvodu'),
        nazevSpravnihoObvodu=sidlo_data.get('nazevSpravnihoObvodu'),
        kodMestskehoObvodu=sidlo_data.get('kodMestskehoObvodu'),
        nazevMestskehoObvodu=sidlo_data.get('nazevMestskehoObvodu'),
        kodMestskeCastiObvodu=sidlo_data.get('kodMestskeCastiObvodu'),
        kodUlice=sidlo_data.get('kodUlice'),
        nazevMestskeCastiObvodu=sidlo_data.get('nazevMestskeCastiObvodu'),
        nazevUlice=sidlo_data.get('nazevUlice'),
        cisloDomovni=sidlo_data.get('cisloDomovni'),
        doplnekAdresy=sidlo_data.get('doplnekAdresy'),
        kodCastiObce=sidlo_data.get('kodCastiObce'),
        cisloOrientacni=sidlo_data.get('cisloOrientacni'),
        cisloOrientacniPismeno=sidlo_data.get('cisloOrientacniPismeno'),
        nazevCastiObce=sidlo_data.get('nazevCastiObce'),
        kodAdresnihoMista=sidlo_data.get('kodAdresnihoMista'),
        psc=sidlo_data.get('psc'),
        textovaAdresa=sidlo_data.get('textovaAdresa'),
        cisloDoAdresy=sidlo_data.get('cisloDoAdresy'),
        typCisloDomovni=sidlo_data.get('typCisloDomovni'),
        standardizaceAdresy=sidlo_data.get('standardizaceAdresy'),
        pscTxt=sidlo_data.get('pscTxt')
    )


def parse_adresa_dorucovaci(data: dict) -> AdresaDorucovaci:
    adresa_data = data.get('adresaDorucovaci', {})
    return AdresaDorucovaci(
        radekAdresy1=adresa_data.get('radekAdresy1'),
        radekAdresy2=adresa_data.get('radekAdresy2'),
        radekAdresy3=adresa_data.get('radekAdresy3')
    )


def parse_seznam_registraci(data: dict) -> SeznamRegistraci:
    seznam_registraci_data = data.get('seznamRegistraci', {})
    return SeznamRegistraci(
        stavZdrojeVr=seznam_registraci_data.get('stavZdrojeVr'),
        stavZdrojeRes=seznam_registraci_data.get('stavZdrojeRes'),
        stavZdrojeRzp=seznam_registraci_data.get('stavZdrojeRzp'),
        stavZdrojeNrpzs=seznam_registraci_data.get('stavZdrojeNrpzs'),
        stavZdrojeRpsh=seznam_registraci_data.get('stavZdrojeRpsh'),
        stavZdrojeRcns=seznam_registraci_data.get('stavZdrojeRcns'),
        stavZdrojeSzr=seznam_registraci_data.get('stavZdrojeSzr'),
        stavZdrojeDph=seznam_registraci_data.get('stavZdrojeDph'),
        stavZdrojeSd=seznam_registraci_data.get('stavZdrojeSd'),
        stavZdrojeIr=seznam_registraci_data.get('stavZdrojeIr'),
        stavZdrojeCeu=seznam_registraci_data.get('stavZdrojeCeu'),
        stavZdrojeRs=seznam_registraci_data.get('stavZdrojeRs'),
        stavZdrojeRed=seznam_registraci_data.get('stavZdrojeRed')
    )



def parse_obchodni_jmeno(data: dict) -> List[ObchodniJmeno]:
    obchodni_jmena_data = data.get('obchodniJmeno', [])
    obchodni_jmena = []
    for obchodni_jmeno_data in obchodni_jmena_data:
        obchodni_jmeno = ObchodniJmeno(
            platnostOd=obchodni_jmeno_data.get('platnostOd'),
            platnostDo=obchodni_jmeno_data.get('platnostDo'),
            obchodniJmeno=obchodni_jmeno_data.get('obchodniJmeno'),
            primarniZaznam=obchodni_jmeno_data.get('primarniZaznam')
        )
        obchodni_jmena.append(obchodni_jmeno)
    return obchodni_jmena


def parse_dalsi_udaje(data: dict) -> DalsiUdaje:
    dalsi_udaje_data = data.get('dalsiUdaje', [])
    dalsi_udaje = []
    for du_data in dalsi_udaje_data:
        obchodni_jmena = parse_obchodni_jmeno(du_data.get('obchodniJmeno', []))
        sidla = [Sidlo(**s) for s in du_data.get('sidlo', [])]
        dalsi_udaj = DalsiUdaje(
            obchodniJmeno=obchodni_jmena,
            sidlo=sidla,
            pravniForma=du_data.get('pravniForma'),
            spisovaZnacka=du_data.get('spisovaZnacka'),
            datovyZdroj=du_data.get('datovyZdroj')
        )
        dalsi_udaje.append(dalsi_udaj)
    return dalsi_udaje