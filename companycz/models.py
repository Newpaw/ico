from dataclasses import dataclass
from typing import Optional, List



@dataclass
class Sidlo:
    kodStatu: Optional[str]  
    nazevStatu: Optional[str]  
    kodKraje: Optional[int]  
    nazevKraje: Optional[str]  
    kodOkresu: Optional[int]  
    nazevOkresu: Optional[str]  
    kodObce: Optional[int]  
    nazevObce: Optional[str]  
    kodSpravnihoObvodu: Optional[int]  
    nazevSpravnihoObvodu: Optional[str]  
    kodMestskehoObvodu: Optional[int]  
    nazevMestskehoObvodu: Optional[str]  
    kodMestskeCastiObvodu: Optional[int]  
    kodUlice: Optional[int]  
    nazevMestskeCastiObvodu: Optional[str]  
    nazevUlice: Optional[str]  
    cisloDomovni: Optional[int]  
    doplnekAdresy: Optional[str]  
    kodCastiObce: Optional[int]  
    cisloOrientacni: Optional[int]  
    cisloOrientacniPismeno: Optional[str]  
    nazevCastiObce: Optional[str]  
    kodAdresnihoMista: Optional[int]  
    psc: Optional[int]  
    textovaAdresa: Optional[str]  
    cisloDoAdresy: Optional[str]  
    typCisloDomovni: Optional[str]  
    standardizaceAdresy: Optional[bool]  
    pscTxt: Optional[str]  

@dataclass
class AdresaDorucovaci:
    radekAdresy1: Optional[str]  
    radekAdresy2: Optional[str]  
    radekAdresy3: Optional[str]  

@dataclass
class SeznamRegistraci:
    stavZdrojeVr: Optional[str]  
    stavZdrojeRes: Optional[str]  
    stavZdrojeRzp: Optional[str]  
    stavZdrojeNrpzs: Optional[str]  
    stavZdrojeRpsh: Optional[str]  
    stavZdrojeRcns: Optional[str]  
    stavZdrojeSzr: Optional[str]  
    stavZdrojeDph: Optional[str]  
    stavZdrojeSd: Optional[str]  
    stavZdrojeIr: Optional[str]  
    stavZdrojeCeu: Optional[str]  
    stavZdrojeRs: Optional[str]  
    stavZdrojeRed: Optional[str]  

@dataclass
class ObchodniJmeno:
    platnostOd: Optional[str]  
    platnostDo: Optional[str]  
    obchodniJmeno: Optional[str]  
    primarniZaznam: Optional[bool]  

@dataclass
class DalsiUdaje:
    obchodniJmeno: List[ObchodniJmeno]
    sidlo: List[Sidlo]
    pravniForma: Optional[str]  
    spisovaZnacka: Optional[str]  
    datovyZdroj: Optional[str]  


@dataclass
class Company:
    ico: Optional[str]  
    obchodniJmeno: Optional[str]  
    sidlo: Optional[Sidlo]  
    pravniForma: Optional[str]  
    financniUrad : Optional[str]  
    datumVzniku : Optional[str]  
    datumZaniku : Optional[str]  
    datumAktualizace : Optional[str]  
    dic : Optional[str]  
    icoId : Optional[str]  
    adresaDorucovaci: Optional[AdresaDorucovaci]
    seznamRegistraci: Optional[SeznamRegistraci]
    primarniZdroj : Optional[str]  
    dalsiUdaje: Optional[List[DalsiUdaje]]  
    czNace: Optional[List[str]]  
    subRegistrSzr: Optional[str]  
    dicSkDph: Optional[str]  