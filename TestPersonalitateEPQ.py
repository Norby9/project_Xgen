import tkinter as tk

EXTROVERSIA, LIE, NEUROTICISM, PSIHOTICISM = 0.0, 0.0, 0.0, 0.0
rEXTROVERSIA, rLIE, rNEUROTICISM, rPSIHOTICISM = 0.0, 0.0, 0.0, 0.0
i = 1
RASPUNS=""

Intrebari = {
    1: "1. Ai hobiuri (pasiuni) multe și diferite?",
    2: "2. Dispoziția ta se schimbă des din rău în bine și invers?",
    3: "3. Ai fost vreodată lăudat pentru ceva care știai că nu ai realizat tu?",
    4: "4. Ești o persoană vorbăreață?",
    5: "5. Ești neliniștit dacă ai datorii?",
    6: "6. Te simți vreodată nenorocit, supărat fără nici un motiv?",
    7: "7. Ai fost tentat vreodată (te-ai gândit) să-ți însușești ceva mai mult decăt ți se cuvine?",
    8: "8. Te simți vioi destul de des?",
    9: "9. Ești afectat (tulburat) dacă vezi un copil sau un animal suferind?",
    10: "10. Ești necăjit adesea din cauza lucrurilor pe care ar fi trebuit să le faci sau să le spui?",
    11: "11. Dacă promiți ceva, te ții întotdeauna de cuvânt, chiar dacă îți este greu să-ți îndeplinești promisiunea?",
    12: "12. La petreceri te simți în largul tău de obicei?",
    13: "13. Ești o persoană irascibilă (care se enervează ușor)?",
    14: "14. Îți place să întâlnești persoane noi?",
    15: "15. Poți fi jignit ușor?",
    16: "16. Toate obiceiurile tale sunt bune și le accepți?",
    17: "17. Îți place să stai mai retras în societate ( la înturniri, petreceri etc.)?",
    18: "18. Te-ai gândit vreodată să iei medicamente care pot avea efecte neobișnuite sau periculoase?",
    19: "19. Simți adesea că ți s-a făcut lehamite (că nu-ți mai pasă, că nu te interesează)?",
    20: "20. Ți-ai însușit vreodata ceva care aparținea altcuiva?",
    21: "21. Îți place să ieși în societate ?",
    22: "22. Îi jignești deseori pe cei care îi iubești?",
    23: "23. Simți adesea un sentiment de vinovăție?",
    24: "24. Preferi să citești în loc să te întâlnești cu prietenii?",
    25: "25. Crezi că ești o persoană nervoasă?",
    26: "26. Ai mulți prieteni?",
    27: "27. Îți place să faci glume care pot răni (jigni) pe cineva?",
    28: "28. Îți faci griji pentru orice?",
    29: "29. În copilarie făceai imediat ce ți se cerea fără să comentezi?",
    30: "30. Curățenia și bunele maniere contează mult pentru tine?",
    31: "31. Ți-e frică deseori că ți s-ar putea întâmpla lucruri îngrozitoare?",
    32: "32. Ai stricat sau ai pierdut vreodată ceva care aparținea altcuiva?",
    33: "33. De obicei iei singur inițiative de a lega noi prietenii?",
    34: "34. Înțelegi ușor ce simt oamenii când iți povestesc necazurile lor?",
    35: "35. Ești de obicei încordat sau în tensiune?",
    36: "36. Arunci pe jos țigarile, hârtiile sau gunoaiele dacă nu găsești un coș de gunoi?",
    37: "37. Ești de obicei tăcut în prezența altor persoane?",
    38: "38. Căsătoria e un lucru demodat la care trebuie să se renunțe?",
    39: "39. Ți se face din când în când milă de propria persoană?",
    40: "40. Îți place să te lauzi?",
    41: "41. Îți este ușor să-i faci pe alții să se distreze la o petrecere sau atunci când atmosfera este plictisitoare?",
    42: "42. Te enervează șoferii care conduc cu multă grija?",
    43: "43. Te îngrijorează des sănătatea ta?",
    44: "44. Ai spus vreodată ceva urât sau răutăcios despre cineva?",
    45: "45. Îți place să spui glume sau bancuri?",
    46: "46. Mâncărurile au același gust pentru tine?",
    47: "47. Ești deseori morocănos, prost dispus?",
    48: "48. În copilărie ai fost vreodată obraznic cu părinții?",
    49: "49. Îți place să stai printre oameni (să nu fii singur)?",
    50: "50. Ești necăjit atunci când exista greșeli în munca ta?",
    51: "51. Te simți adesea obosit și sleit de puteri fără motiv?",
    52: "52. Ai trișat vreodată la cărți sau la alte jocuri?",
    53: "53. Îți place să faci lucruri pentru care trebuie să acționezi rapid și să nu pierzi timpul?",
    54: "54. Mama ta a fost sau este o femeie bună?",
    55: "55. Simți uneori că viața este foarte plicticoasă?",
    56: "56. Ai profitat vreodată de cineva, cu bani sau alte avantaje?",
    57: "57. Te angajezi adesea la mai multe treburi dacât poți rezolva?",
    58: "58. Te îngrijorează înfățișarea ta?",
    59: "59. Te gândești adesea să mori?",
    60: "60. Dacă ai fi sigur că nu ești prins, ai evita să plătești taxele, impozitele sau alte obligații?",
    61: "61. Ești capabil să înveselești o petrecere?",
    62: "62. Încerci sa nu fii dur cu oamenii?",
    63: "63. Ești prea mult timp necăjit după o întâmplare jenantă, neplăcută?",
    64: "64. Suferi de nervi?",
    65: "65. Jignești, uneori, pe cineva cu intenție?",
    66: "66. Prieteniile tale se destramă (se desfac) ușor fără vina ta?",
    67: "67. Ești adesea însingurat?",
    68: "68. Aplici în practică tot ceea ce spui?",
    69: "69. Îți place uneori să necăjești animalele?",
    70: "70. Te simți jignit când alții găsesc greșeli în comportamentul sau în munca ta?",
    71: "71. Ai întârziat vreodată la întalnire sau la serviciu?",
    72: "72. Îți place ca în jurul tău să fie animație (multă lume)?",
    73: "73. Ți-ar placea ca altora să le fie frică de tine?",
    74: "74. Căteodată ești plin de energie și alteori ești fără vlagă?",
    75: "75. Uneori amâni lucrurile pe care le poți face astăzi?",
    76: "76. Ceilalți te consideră plin de viață?",
    77: "77. Ești foarte sensibil la anumite lucruri?",
    78: "78. Ești întotdeauna dispus să recunoști când greșești?",
    79: "79. Te simți foarte rău, supărat, când vezi un animal rănit sau prins în capcană?"}
Descriere = "Interpretate\n" \
            "Răspunsurile oferite de subiect primește un punctaj care se calculează pentru fiecare scală și se " \
            "compara cu mediile populaționale, obținându-se informații legate " \
            "de extroversia, introversia, nevroticismul și psihoticismul subiecților, dar și legate de tendințele " \
            "de a da răspunsuri favorabile (scala L,""de micniună"" în care " \
            "sunt incluși 9 itemi și care prezintă comportamente sociale negative dar pe care majoritatea populației " \
            "le încalca frecvent, în comportamentul informal).\n\n" \
            "Descrierea factorilor\n" \
            "Extroversia (extraversia) - Introversia (intraversia)\n" \
            "Extravertiul tipic este sociabil, are muți prieteni și îi place să fie înconjurat de oameni. Are " \
            "tendința de a fi agresiv și dominant, își perde ușor " \
            "stăpânirea de sine. Îi place să riște, caută schimbare precum și emoțiile puternice, preferă mișcarea " \
            "și acțiunea. În general este optimist și nepăsător. " \
            "Introvertitul tipic este ponderat și introspectiv. Îi place viața liniștită, ordonată, care se " \
            "desfășoară în cadrul unor coordonate precise. Față de " \
            "majoritatea oamenilor este rezervat și distant, excepție făcând doar prietenii săi intimi. Este mai " \
            "degrabă un pesimist, prevăzător, la care implicarea " \
            " eului în activitate se realizează mai greu. Evită senzațiile tari. Își stapânește impulsurile de moment" \
            " și în general nu are impulsuri agresive. " \
            "De regulă, își controlează sentimentele într-o măsură mai mare decât extravertitul. Acordă o deosebită" \
            " valoare criteriilor etice.\n\n" \
            "Nevrotismul (neuroticismul)\n" \
            "Nevroticii se caracterizează printr-o labilitate emoțională accentuată și realedificultăți în " \
            "restabilirea echilibrului psihic dupa șocuri emoționale. " \
            "Se pâng fecvent de dereglări somatice difuze (ex. dureri de cap) dureri dorsale, tulburări digestive, " \
            "insomnii etc. Pe plan psihic acuză stări de anxietate " \
            "și sunt framântați de numeroase griji. Sub influența stresului, aceste persoane sunt predispuse la " \
            "tulburări nevrotice. Predispozițiile amintite nu se " \
            "confundă cu adevarata depresie nervoasă. Un subiect cu nota N ridicată se poate adapta totuși în mod " \
            "adecvat exigențelor muncii, ale vieții de familie etc. " \
            "Nevroticul este descris de Eysenck în următorii termeni: ""subiect nevrotic, în medie este o persoană " \
            "defectivă mental și corporal, sub medie ca inteligența, " \
            "voință, control emoțional, acuitate senzorială și capacitate de a se afirma. Este sugestibil, lipsit de " \
            "persistență și lent în gândire și acțiune, nesociabil " \
            "și tinde să reprime faptele neplăcute"".\n" \
            "Stabil emoțional (la polul pozotiv), sunt subiecții cu notele scazute la scara N, note specifice " \
            "persoanelor stabile d.p.d.v. emoțional. Caracteristic acestora " \
            "este gradul ridicat de integrare, puterea eului, autocontrolul ridicat.\n\n" \
            "Psihotismul (psihoticismul)\n" \
            "Psihotismul, cea mai complexă dimensiune, este definită de interrelațiile dintre trăsăturile: " \
            "agresivitate, egocentrism, comportament antisocial și lipsa de empatie. " \
            "Se caracterizează prin tendința de a produce tulburări, a fi solidar, a arăta cruzime, a fi ostil " \
            "altora, a prefera lucruri ciudate și neobișnuite. La un pol apar " \
            "persoane care nu au nici o considerație fața de regulile sociale, iar la celălalt cei înalt socializați," \
            " mai ales legați de apărarea drepturilor altor persoane. " \
            "Tipul cu scoruri ridicate la psihotism, în scala E.P.Q., se regăseștefrecvent în cadrul expertizelor" \
            " medico-legale psihiatrice, în cazul criminalilor și în special " \
            "a celor recidiviști.\n"


def onclick(args):
    global i, EXTROVERSIA, LIE, NEUROTICISM, PSIHOTICISM, rEXTROVERSIA, rLIE, rNEUROTICISM, rPSIHOTICISM
    if args == 1:
        EXTROVERSIA = 20.28
        LIE = 24.68
        NEUROTICISM = 30.74
        PSIHOTICISM = 39.68
        rEXTROVERSIA = 2.557
        rLIE = 2.237
        rNEUROTICISM = 2.247
        rPSIHOTICISM = 4.586
        frame1.destroy()
        frame2.pack(fill=tk.BOTH, expand=True)
    elif args == 2:
        EXTROVERSIA = 23.39
        LIE = 19.3
        NEUROTICISM = 25.59
        PSIHOTICISM = 41.49
        rEXTROVERSIA = 2.531
        rLIE = 2.421
        rNEUROTICISM = 1.919
        rPSIHOTICISM = 5.713
        frame1.destroy()
        frame2.pack(fill=tk.BOTH, expand=True)
    elif args == 3:
        if i == 18 or i == 22 or i == 27 or i == 38 or i == 42 or i == 46 or i == 69 or i == 73:
            PSIHOTICISM += rPSIHOTICISM
        elif i == 1 or i == 4 or i == 8 or i == 12 or i == 14 or i == 21 or i == 26 or i == 33 or i == 41 or i == 45 or i == 49 or i == 53 or i == 61 or i == 72 or i == 76:
            EXTROVERSIA += rEXTROVERSIA
        elif i == 2 or i == 6 or i == 10 or i == 13 or i == 15 or i == 19 or i == 23 or i == 25 or i == 28 or i == 31 or i == 35 or i == 39 or i == 43 or i == 51 or i == 55:
            NEUROTICISM += rNEUROTICISM
        elif i == 11 or i == 16 or i == 29 or i == 78:
            LIE += rLIE
        i += 1
        if i == 80:
            frame2.destroy()
            RASPUNS = "Scor obținut:\nLIE: " + str("%.3f" % LIE) + "\nEXTROVERSIA: " + str("%.3f" % EXTROVERSIA) + "\nNEUROTICISM: " + str("%.3f" % NEUROTICISM) + "\nPSIHOTICISM: " + str("%.3f" % PSIHOTICISM) + "\n" + "\nScoruriel T - standardizate\n  <30\trezultate extrem de mici\n30-40\trezultate mici\n40-60\trezultate medii\n60-70\trezultate mari\n  >70\trezultate foarte mari\n\n"
            label_r.config(text=RASPUNS)
            frame3.pack(fill=tk.BOTH, expand=True)
        lable_i.config(text=Intrebari[i])
    elif args == 4:
        if i == 5 or i == 9 or i == 30 or i == 34 or i == 50 or i == 54 or i == 62 or i == 79:
            PSIHOTICISM += rPSIHOTICISM
        elif i == 17 or i == 24 or i == 37:
            EXTROVERSIA += rEXTROVERSIA
        elif i == 58 or i == 59 or i == 63 or i == 64 or i == 66 or i == 67 or i == 70 or i == 74 or i == 77:
            NEUROTICISM += rNEUROTICISM
        elif i == 3 or i == 7 or i == 20 or i == 32 or i == 36 or i == 40 or i == 44 or i == 47 or i == 48 or i == 52 or i == 56 or i == 57 or i == 60 or i == 65 or i == 68 or i == 71 or i == 75:
            LIE += rLIE
        i += 1
        if i == 80:
            frame2.destroy()
            RASPUNS = "Scor obținut:\nLIE: " + str("%.3f" % LIE) + "\nEXTROVERSIA: " + str("%.3f" % EXTROVERSIA) + "\nNEUROTICISM: " + str("%.3f" % NEUROTICISM) + "\nPSIHOTICISM: " + str("%.3f" % PSIHOTICISM) + "\n" + "\nScoruriel T - standardizate\n  <30\trezultate extrem de mici\n30-40\trezultate mici\n40-60\trezultate medii\n60-70\trezultate mari\n  >70\trezultate foarte mari\n\n"
            label_r.config(text=RASPUNS)
            frame3.pack(fill=tk.BOTH, expand=True)
        lable_i.config(text=Intrebari[i])


window = tk.Tk()
window.title("Test de personalitate EPQ")

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

lable_s = tk.Label(frame1, text="Apăsați butonul corespunzător sexului dumneavoastră", font=("Courier", 10), wraplength=1000, justify=tk.LEFT, fg="white", bg="black")
lable_i = tk.Label(frame2, text=Intrebari[1], font=("Courier", 10), wraplength=1000, justify=tk.LEFT, fg="white", bg="black")
lable_d = tk.Label(frame3, text=Descriere, font=("Courier", 10), wraplength=1000, justify=tk.LEFT, fg="white", bg="black")
label_r = tk.Label(frame3, text="", font=("Courier", 10), justify=tk.LEFT, fg="white", bg="black")
button_b = tk.Button(frame1, text="Bărbat", width=25, height=5, bg="blue", fg="white", command=lambda: onclick(1))
button_f = tk.Button(frame1, text="Femeie", width=25, height=5, bg="pink", fg="black", command=lambda: onclick(2))
button_da = tk.Button(frame2, text="DA", width=25, height=5, bg="green", fg="white", command=lambda: onclick(3))
button_nu = tk.Button(frame2, text="NU", width=25, height=5, bg="red", fg="white", command=lambda: onclick(4))

frame1.pack(fill=tk.BOTH, expand=True)
lable_s.pack(fill=tk.BOTH, expand=True)
button_b.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
button_f.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


lable_i.pack(fill=tk.BOTH, expand=True)
button_da.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
button_nu.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label_r.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lable_d.pack(fill=tk.BOTH, expand=True)

window.mainloop()
