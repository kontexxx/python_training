kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober",
        "november", "detsember"]
sood = ["mees", "naine", "mees", "naine", "mees", "naine", "mees", "naine"]
jarjekord = ["teadmata järjekorranumbriga", "esimesena", "teisena", "kolmandana", "neljandana", "viiendana",
             "kuuendana", "seitsmendana", "kaheksandana", "üheksandana", "kümnendana", "üheteistkümnendana",
             "kaheteistkümnendana", "kolmeteistkümnendana", "neljateistkümnendana", "viieteistkümnendana",
             "kuueteistkümnendana", "seitsmeteistkümnendana", "kaheksateistkümnendana", "üheksateistkümnendana",
             "kahekümnendana", "kahekümne esimesena", "kahekümne teisena", "kahekümne kolmandana",
             "kahekümne neljandana", "kahekümne viiendana", "kahekümne kuuendana", "kahekümne seitsmendana",
             "kahekümne kaheksandana", "kahekümne üheksandana", "kolmekümnendana"]

kuressaare = 0
tartu = 10
idaTallinn = 20
idaViru = 220
maarjaMoisa = 270
narva = 370
parnu = 420
haapsalu = 470
jarvamaa = 490
rakvere = 520
valga = 570
viljandi = 600
lounaEesti = 650

isikukood = input("Sisestage oma isikukood: ")

# pikkuse kontroll..
# noinspection PyInterpreter
if len(isikukood) == 11:
    # Eeldatav kontrollkood:
    # esimene järk..
    first_check = ((int(isikukood[0]) * 1) + (int(isikukood[1]) * 2) + (int(isikukood[2]) * 3) +
                   (int(isikukood[3]) * 4) + (int(isikukood[4]) * 5) + (int(isikukood[5]) * 6) +
                   (int(isikukood[6]) * 7) + (int(isikukood[7]) * 8) + (int(isikukood[8]) * 9) + (
                               int(isikukood[9]) * 1)) % 11
    # teine järk, kui jääk = 10..
    if first_check == 10:
        first_check = ((int(isikukood[0]) * 3) + (int(isikukood[1]) * 4) + (int(isikukood[2]) * 5) + (
                    int(isikukood[3]) * 6) +
                       (int(isikukood[4]) * 7) + (int(isikukood[5]) * 8) + (int(isikukood[6]) * 9) + (
                                   int(isikukood[7]) * 1) +
                       (int(isikukood[8]) * 2) + (int(isikukood[9]) * 3)) % 11
    # kas sisestatud == arvutatud..
    if first_check == int(isikukood[10]):
        # soo määramine
        for sugu in sood:
            sugu = int(isikukood[0])
            sooNimi = sood[sugu - 1]
        # kas soo väärtus on õige..
        if int(isikukood[0]) <= 8 and int(isikukood[0]) >= 1:
            # paneme aasta paika..
            if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
                aasta = "18" + str(isikukood[1] + isikukood[2])
            if int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
                aasta = "19" + str(isikukood[1] + isikukood[2])
            if int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
                aasta = "20" + str(isikukood[1] + isikukood[2])
            if int(isikukood[0]) == 7 or int(isikukood[0]) == 8:
                aasta = "21" + str(isikukood[1] + isikukood[2])
            # leian kuu väärtuse ja määran kuu nime
            for kuuNimi in kuud:
                kuu = int(isikukood[3] + isikukood[4])
                kuuNimi = kuud[kuu - 1]
            # kas kuu on korrektne..
            if kuu >= 1 and kuu <= 12:
                # leian päeva väärtuse
                paev = int(isikukood[5] + isikukood[6])
                # kontrollin päeva korrektsust..
                if paev >= 1 and paev <= 31:
                    # määran haigla koodi
                    haigla = int(isikukood[7] + isikukood[8] + isikukood[9])
                    # Määran haigla nime koodi järgi
                    if haigla in range(1, 11):
                        haiglaNimi = "Kuressaare Haiglas"
                        # järjekorranumbri määramine
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - kuressaare)
                    elif haigla in range(11, 20):
                        haiglaNimi = "Tartu Ülikooli Naistekliinikus"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - tartu)
                    elif haigla in range(21, 221):
                        haiglaNimi = "kas Ida-Tallinna Keskhaiglas, Pelgulinna sünnitusmajas, Hiiumaa haiglas, Keila haiglas, Rapla haiglas või Loksa haiglas."
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - idaTallinn)
                    elif haigla in range(221, 271):
                        haiglaNimi = "Ida-Viru Keskhaiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - idaViru)
                    elif haigla in range(271, 371):
                        haiglaNimi = "Maarjamõisa Kliinikumis või Jõgeva Haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - maarjamoisa)
                    elif haigla in range(371, 421):
                        haiglaNimi = "Narva Haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - narva)
                    elif haigla in range(421, 471):
                        haiglaNimi = "Pärnu Haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - parnu)
                    elif haigla in range(471, 491):
                        haiglaNimi = "Pelgulinna sünnitusmajas või Haapsalu haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - haapsalu)
                    elif haigla in range(491, 521):
                        haiglaNimi = "Järvamaa Haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - jarvamaa)
                    elif haigla in range(521, 571):
                        haiglaNimi = "Rakvere või Tapa haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - rakvere)
                    elif haigla in range(571, 601):
                        haiglaNimi = "Valga Haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - valga)
                    elif haigla in range(601, 651):
                        haiglaNimi = "Viljandi Haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - viljandi)
                    elif haigla in range(651, 701):
                        haiglaNimi = "Lõuna-Eesti Haiglas või Põlva haiglas"
                        jarjekorraNr = (int(isikukood[7] + isikukood[8] + isikukood[9]) - lounaEesti)
                    else:
                        haiglaNimi = "teadmata haiglas"
                        jarjekorraNr = 0
                    # järjekorra määramine, et saaks tekstina väljastada..
                    for jarjekorraNumber in jarjekord:
                        jarjekorraNumber = jarjekorraNr
                        jarjekorraNumbriNimi = jarjekord[jarjekorraNumber]
                        # Tekst
                    print("Tervist, oled " + sooNimi + ". Sündisid aastal " + aasta + ", sinu sünnipäev on " + str(
                        paev) + ". " + kuuNimi + ". Sündisid " + haiglaNimi + " antud päeval " + jarjekorraNumbriNimi + ".")
                else:  # kui päeva väärtuse kontroll nurjub..
                    print("Ebakorrektne päeva väärtus. Proovi uuesti!")
            else:  # kui kuu väärtuse kontroll nurjub..
                print("Ebakorrektne kuu väärtus. Proovi uuesti!")
        else:  # kui soo tunnuse kontroll nurjub..
            print("Ebakorrektne soo tunnus. Proovi uuesti!")
    else:  # kui kontrollkoodi väärtuse kontroll nurjub..
        print("Ebakorrektne kontrollkoodi väärtus. Proovi uuesti!")
else:  # Kui pikkuse kontroll nurjub - veateade..
    print("Ebakorrektne sisend. Proovi uuesti!")

