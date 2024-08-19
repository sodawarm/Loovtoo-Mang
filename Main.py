from alus import *
otsus_1 = vastus ("foull.jpg","Vastane sooritab vea ja referee annab teile vabalöögi",["Proovid ise värava lüüa", "Lased sõbral võtta löögi"])
if otsus_1 == "Proovid ise värava lüüa":
        
        otsus2 = vastus("valik.jpg", "Kuidas palli lööd?", ["Lööd kaarega ümber müüri", "Lööd täie jõuga palli"])  
        if otsus2 == "Lööd kaarega ümber müüri":
            
            otsus3 = vastus("sisse.jpg", "GOOOOOOAAAL, Lõid palli väravasse, kõik on rõõmsad, aga mida sa karjääriga edasi teed?", ["Proovin leida uut klubi", "Jään Püünsi jalgpalli klubisse"]) 
            if otsus3 == "Proovin leida uut klubi":  plt("lfc.png", "Liverpooli scoutid arvasid, et sa olid hea jalpallis ja signisid sind.")
            elif otsus3 == "Jään Püünsi jalgpalli klubisse":  plt("legend.jpg", "Sa said Püünsi kooli legendiks ja teenisid Eestile palju auhindu")  
        
        elif otsus2 == "Lööd täie jõuga palli": plt("mcmooda.jpg", "Löid palli väravast mööda ja su vanemad pettusid")
elif otsus_1 == "Lased sõbral võtta löögi": plt("soberlook.jpg", "Su sõber lööb täitsa mööda väravast")

pygame.quit()