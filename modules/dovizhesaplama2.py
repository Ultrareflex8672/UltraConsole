from application.DovizKurlari import DovizKurlari
from application.ultraconsole import UltraConsole as UC

def dovizhesaplama(**kwargs):
    kurlar = DovizKurlari()
    print(kurlar.DegerSor("EUR",4))
    # UC.create_frame("Döviz", DovizKurlari.DegerSor("EUR",1), "info")
    input()