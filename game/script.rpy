# Vous pouvez placer le script de votre jeu dans ce fichier.

# Définir la police de tout le jeu
define gui.text_font = "fonts/Lora-Italic-VariableFont_wght.ttf"  
define gui.text_size = 28
$ old_font_size = gui.text_size
define gui.text_color = "#FFFFFF"  

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image coworking = Transform("coworking.png", fit="cover")
image parc = Transform("parc.png", fit="cover")
image parc_bad_ending = Transform("parc_bad_ending.jpeg", fit="cover")
image chambre = Transform("chambre.png", fit="cover")
image ecole = Transform("école.png", fit="cover")
image bg = Transform("bg.png", fit="cover")
image birthday = Transform("birthday.jpeg", fit="cover")
image city = Transform("city.png", fit="cover")
image city_bad_ending= Transform("city_bad_ending.jpeg", fit="cover")

# fin de jeu
image fin1 = Transform("fin1.png", fit="cover")
image fin2 = Transform("fin2.png", fit="cover")
image fin3 = Transform("fin3.png", fit="cover")
image fin4 = Transform("fin4.png", fit="cover")
image fin5 = Transform("fin5.png", fit="cover")

# starter kit
image kit_starter = "kit_starter.png"
image assistant_personnel = "assistant_personnel.png"
image ia = "ia.png"
image casque = "casque.png"
image phone = "phone.png"
image drone = "drone.png"
image google_home= "google_home.png"
image medical_app = "medicale_app.png"
image tiktok = "tiktok.png"
image selfie = "selfie.png"
image coaching_de_vie = "coaching_de_vie.png"

image logo = "logo.png"
image woman = "woman.png"
image ai4good = "AI4GOOD_festival.png"

# Personnages 
# Léa
image lea_bad_ending = "lea_bad_ending.png"
image lea_good_ending = "lea_good_ending.png"
image lea_danse = "lea_danse.png"
image lea_interesse = "lea_interesse.png"
image lea_trouble = "lea_trouble.png"
image lea_normal = "lea_normal.png"

# Yanis
image yanis_fier = "yanis_fier.png"
image yanis_idee = "yanis_idee.png"
image yanis_normal = "yanis_normal.png"
image yanis_photo = "yanis_photo.png"
image yanis_vocal = "yanis_vocal.png"
image yanis_bad_ending = "yanis_bad_ending.png"

transform resize_centered:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.1

transform resize_centered_zoom:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 0.9

transform top_right:
    xpos 0.95
    ypos 0.2
    xanchor 1.0
    yanchor 0.0

transform vibration:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    pause 2
    repeat

# Variable pour les points du jeu 
default points = 0
default lea_points = 0
default yanis_points = 0

# Déclarez les personnages utilisés dans le jeu.
define Lea = Character('Léa', font="fonts/Lora-Regular.ttf")
define Yanis = Character('Yanis', font="fonts/Lora-Regular.ttf")

label start:

#--------------------------------------------------------------------- INTRODUCTION ---------------------------------------------------------------------------------
    scene black
    with fade

    show text "{size=40}Et si la technologie connaissait mieux tes besoins que toi-même ?{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Et si tes choix numériques façonnaient ton futur, sans que tu t’en rendes compte ?{/size}" at truecenter with dissolve
    pause 3
    hide text

    scene bg with fade
    show logo at resize_centered with fade
    pause 3
    hide logo

    show text "{size=40}Bienvenue dans MindWare.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Un jeu narratif où chaque interaction compte.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Ici, tu ne joues pas un héros fantastique.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Tu es toi. Dans un monde réaliste, mais subtilement amplifié.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Chaque décision digitale aura des répercussions.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Parfois évidentes. Parfois invisibles.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Tes amis, ton quotidien, ton avenir… Tout peut basculer.{/size}" at truecenter with dissolve
    pause 3
    hide text

    scene birthday with fade
    
    
    "Tu viens tout juste de fêter tes 17 ans."
    
    "En cadeau ? Un objet rare. Trop beau pour être vrai."

    show kit_starter at resize_centered
    "Le Kit Tech Total, signé NeuroLink Systems, une entreprise tech aussi brillante que mystérieuse."
    hide kit_starter

    "À l’intérieur :"

    show assistant_personnel at resize_centered
    "Un assistant personnel ultra-connecté."
    hide assistant_personnel

    show ia at resize_centered
    "Une IA générative polyvalente."
    hide ia

    show casque at resize_centered
    "Un casque de réalité mixte immersif."
    hide casque

    show drone at resize_centered
    "Un drone équipé d'une caméra 4k"
    hide drone

    show phone at resize_centered
    "Et un accès illimité à toutes les applications expérimentales du moment."
    hide phone

    "On te promet que ce kit va améliorer ta vie."
    "Mais personne ne t’a dit à quel prix."
    "Ni comment l’utiliser… ni jusqu’où tu peux lui faire confiance."

    "À tes côtés, deux amis fidèles :"
    show yanis_normal at resize_centered_zoom
    "Yanis, un passionné de création de contenu.\nToujours à la recherche de nouvelles idées pour ses vidéos, il utilise les dernières technologies pour filmer, monter et partager ses créations."
    hide yanis_normal

    show lea_normal at resize_centered_zoom
    "Et Léa, une fille qui adore explorer les dernières tendances et partager ses découvertes.\n Curieuse, enthousiaste et en quête de repères, elle cherche souvent à mieux se comprendre"
    hide lea_normal

    scene black
    with fade
    pause 1

    show text "{size=40}Maintenant, c’est à toi de jouer.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Fais les bons choix. Et surtout, reste maître de toi-même.{/size}" at truecenter with dissolve
    pause 3
    hide text

    show text "{size=40}Clique pour commencer ton histoire.{/size}" at truecenter with dissolve
    pause 3
    hide text

    jump situation_1
    return

#--------------------------------------------------------------------------- Début du jeu ----------------------------------------------------------------------

label situation_1:
    play music "audio/ambiance.mp3" loop volume 0.4

    scene chambre
    with fade

    show yanis_vocal at resize_centered_zoom 
    "En rentrant d’une séance de test VR, ton assistant t’indique un message vocal reçu de Yanis." with dissolve
    show yanis_vocal at vibration
    play music "audio/audio_yanis_vocal.mp3" volume 0.5
    "Il te demande de venir l’aider d’urgence." with dissolve
    stop music fadeout 1.0
    "Mais quelque chose ne colle pas : la voix semble saccadée, avec des pauses bizarres, et une façon de parler qui ne lui ressemble pas." with dissolve
    "Yanis, d’habitude calme et direct, semble là… presque confus. Peut-être qu’il est vraiment en détresse ?"with dissolve
    "Ou alors… est-ce qu’on t’aurait piégé avec un message trafiqué par IA ?" with dissolve
    "Tu ne sais pas quoi penser, mais tu sens qu’agir trop vite pourrait être risqué. Ou trop tard, dangereux." with dissolve
    

    play music "audio/ambiance.mp3" loop volume 0.4
    "Que fais-tu ?"
    stop music fadeout 1.0

    scene black
    with fade

menu:

    "A. Tu appelles immédiatement un proche de Yanis pour confirmer.":
        $ points += 7
        "🟡 Son frère décroche : Yanis va bien, il n’a envoyé aucun message. Tu te rends compte que tu as bien fait de vérifier."
        jump situation_2

    "B. Tu analyses la voix avec ton assistant IA.":
        $ points += 10
        "🟢 Ton assistant détecte plusieurs anomalies dans l’audio. C’était bien un deepfake. Tu viens peut-être d’éviter un piège."
        jump situation_2

    "C. Tu décides d’y aller tout de suite, mieux vaut prévenir que guérir.":
        $ points += 0
        "🔴 Tu fonces… mais personne. Tu réalises trop tard que tu es tombé dans un piège, heureusement sans conséquences graves."
        jump situation_2

    "D. Tu le rappelles sans réfléchir, on ne sait jamais.":
        $ points += 3
        "🟠 Tu tombes sur une messagerie étrange. Aucun doute, ce n’était pas lui. Tu raccroches, inquiet."
        jump situation_2

    


label situation_2:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene parc
    with fade

    show lea_trouble at top_right 
    "Après l’incident, Tu en parles à Léa..."
    "Elle te montre une vidéo étrange qui circule sur elle-même."
    "Elle affirme ne jamais l’avoir postée. La vidéo semble générée par IA, mais elle est en tendance."
    "Léa paraît troublée, mais commence à gagner des abonnés."

    "Que fais-tu ?"
    stop music fadeout 1.0
    
    scene black
    with fade

menu:

    "A. Tu lui proposes ton aide pour la signaler et prouver qu'elle est truquée, mais tu vas freiner sa montée en notoriété.":
        $ points += 10
        $ lea_points += 10
        "🟢 Tu décides de l’aider à signaler la vidéo. C’est l’intégrité qui compte."
        jump situation_3

    "B. Tu la partages avec une touche d’humour, pensant que ça ne peut pas vraiment lui nuire.":
        $ points += 0
        $ lea_points += 0
        "🔴 Tu fais tourner la vidéo avec une blague, sans trop réfléchir aux conséquences."
        jump situation_3
    
    "C. Tu choisis de ne pas intervenir, respectant son choix même si la situation te semble bancale.":
        $ points += 3
        $ lea_points += 3
        "🟠 Tu respectes son choix, même si ça te met un peu mal à l’aise."
        jump situation_3

    "D. Tu lui conseilles de profiter de la tendance, mais en restant prudente.":
        $ points += 7
        $ lea_pointspoints += 7
        "🟡 Tu lui dis de rester vigilante, tout en surfant sur la vague. Après tout, c’est viral."
        jump situation_3




label situation_3:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene city
    with fade

    show yanis_idee at top_right 
    show drone at resize_centered
    "Après une journée intense sur tes projets, tu retrouves Yanis pour une sortie détente."
    "Il te propose une idée originale : utiliser ton drone pour survoler la ville et capturer des vues impressionnantes de lieux peu accessibles."
    "Le but ? Créer un montage stylé pour ses réseaux."
    "Quelle approche choisis-tu pour filmer ?"
    stop music fadeout 1.0

    scene black
    with fade

    menu:

        "A. Vous capturez des images plus proches des fenêtres et des espaces de travail, en vous disant que ce n’est pas vraiment une violation puisque les gens sont en public.":
            $ points += 7
            $ yanis_points += 7
            "🟡 Les images sont percutantes, mais tu sens une gêne. Était-ce vraiment respectueux ?"
            jump situation_4

        "B. Tu suis le plan de Yanis et capturez des images proches de la zone privée de personnes, juste pour améliorer le profil de son réseau social.":
            $ points += 3
            $ yanis_points += 3
            "🟠 Les vues font sensation en ligne, mais un commentaire te fait réfléchir : 'Et la vie privée dans tout ça ?'"
            jump situation_4

        "C. Tu choisis de filmer uniquement des lieux publics connus et accessibles à tous, même si cela limite la créativité du contenu.":
            $ points += 10
            $ yanis_points += 10
            "🟢 Tu privilégies l’éthique à la créativité. Les images sont belles, et tu gardes l’esprit tranquille."
            jump situation_4

        "D. Vous décidez de filmer en vous concentrant uniquement sur l’esthétique.":
            $ points += 0
            $ yanis_points += 0
            "🔴 Le résultat est beau, certes… mais certaines prises risquent de poser problème si elles sont diffusées."
            jump situation_4

label situation_4:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene ecole
    with fade

    show ia at resize_centered

    "De retour à l’école, tu fais face à un devoir important à rendre pour le lendemain."
    "Heureusement, ton assistant IA te génère un texte complet, très bien structuré, en quelques secondes."
    "Que fais-tu avec ce texte généré ?"
    stop music fadeout 1.0

    scene black
    with fade

    menu:

            "A. Tu mets le texte dans une IA humanisante pour le rendre plus humain et éviter qu’il soit détecté comme généré par IA.":
                $ points += 0
                "🔴 Le devoir passe, mais tu as franchi une ligne sans vraiment t’en rendre compte."
                jump situation_5

            "B. Tu modifies légèrement le texte pour y ajouter ta touche personnelle.":
                $ points += 7
                "🟡 Le résultat est bon, mais tu sais que ce n’est pas entièrement ton travail."
                jump situation_5

            "C. Tu transmets le texte intégralement, puisque l’IA est censée nous aider à être plus productifs après tout.":
                $ points += 3
                "🟠 C’est rapide et efficace… mais tu risques de passer à côté de l’apprentissage."
                jump situation_5

            "D. Tu t’inspires du texte généré mais tu réécris tout avec tes mots, en citant l’IA.":
                $ points += 10
                "🟢 Tu montres ton sens de l’éthique et ta capacité à utiliser l’IA comme un outil, pas comme une béquille."
                jump situation_5


label situation_5:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene parc
    with fade

    show lea_interesse at top_right
    show coaching_de_vie at resize_centered
    show coaching_de_vie at vibration

    "Léa teste une nouvelle application de coaching de vie pilotée par une IA."
    "Peu à peu, elle commence à suivre aveuglément ses conseils. Ses choix deviennent presque mécaniques, prévisibles."
    "Que fais-tu face à cette situation ?"
    stop music fadeout 1.0

    scene black
    with fade

    menu:
            "A. Tu la laisses faire, pensant qu’elle trouvera un équilibre seule.":
                $ points += 0
                $ lea_points += 0
                "🔴 Tu choisis de ne pas intervenir. Peut-être trouvera-t-elle seule ses limites, ou peut-être pas…"
                jump situation_6

            "B. Tu lui suggères d’en parler à un adulte ou à un professionnel de santé.":
                $ points += 7
                $ lea_points += 7
                "🟡 Tu restes prudent et responsable. Léa se sent soutenue et réfléchit à cette possibilité."
                jump situation_6
            
            "C. Tu lui parles franchement de ton inquiétude et lui proposes de vérifier ensemble les sources.":
                $ points += 10
                $ lea_points += 10
                "🟢 Tu fais preuve d'écoute et d'esprit critique. Léa commence à prendre du recul sur l'application."
                jump situation_6

            "D. Tu essaies de lui faire voir qu’elle doit être plus authentique, mais sans être sûr de l’approche.":
                $ points += 3
                $ lea_points += 3
                "🟠 Ton message est flou, mais Léa sent ton intention. Peut-être que ça plantera une graine."
                jump situation_6


label situation_6:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene chambre
    with fade

    show google_home at resize_centered
    "Depuis que tu utilises Google Home, il gère ta musique, tes rappels, la météo, et même l'éclairage de ta maison."
    "Au début, c'était pratique, mais maintenant tu te rends compte que tu t'appuies de plus en plus sur lui pour des tâches simples."
    "Google Home est utile, mais il y a des limites. Tu te demandes si tu en fais trop."
    "Quelle est ta réaction ?"
    stop music fadeout 1.0

    scene black
    with fade

    menu:

            "A. Tu laisses Google Home gérer la maison, mais tu t'efforces de garder quelques tâches manuelles pour ne pas devenir trop dépendant.":
                $ points += 7
                "🟡 Tu trouves un équilibre entre confort technologique et autonomie personnelle."
                jump situation_7

            "B. Tu continues à utiliser Google Home, mais tu vérifies si chaque tâche est bien exécutée.":
                $ points += 3
                "🟠 Tu conserves un certain contrôle, mais ta dépendance reste élevée."
                jump situation_7

            "C. Tu laisses tout à Google Home, ne remettant jamais en question son efficacité puisqu’il ne t’a jamais déçu.":
                $ points += 0
                "🔴 Tu fais confiance à la technologie les yeux fermés, sans te poser de questions."
                jump situation_7
            
            "D. Tu désactives certaines fonctions et réapprends à faire des choses par toi-même, même si cela te prend un peu plus de temps.":
                $ points += 10
                "🟢 Tu retrouves une certaine autonomie et redécouvres le plaisir de faire les choses toi-même."
                jump situation_7


label situation_7:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene city
    with fade

    show medical_app at resize_centered
    show medical_app at vibration

    "Une nouvelle application médicale gratuite promet un bilan de santé complet via quelques questions."
    "Mais pour des raisons de sécurité et de suivi, elle demande l’accès à tes données biométriques et à ta carte d’identité."
    "Que choisis-tu de faire ?"
    stop music fadeout 1.0
    scene black
    with fade

    menu:

            "A. Tu lis les conditions, acceptes partiellement et ajustes les autorisations après.":
                $ points += 7
                "🟡 Tu restes prudent tout en profitant des services proposés."
                jump situation_8
            
            "B. Tu ne lis pas tout, mais tu acceptes car l’app a de bons avis.":
                $ points += 3
                "🟠 Tu te fies à la popularité, en espérant que cela suffise."
                jump situation_8
            
            "C. Tu lis les conditions d’utilisation, refuses les accès et cherches une autre solution.":
                $ points += 10
                "🟢 Tu prends le temps d’évaluer les risques et fais un choix éclairé."
                jump situation_8

            "D. Tu valides tout sans lire, c’est gratuit et rapide.":
                $ points += 0
                "🔴 Tu privilégies la facilité sans vraiment savoir ce que tu autorises."
                jump situation_8




label situation_8:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene parc
    with fade

    show woman at resize_centered
    show lea_trouble at top_right

    "Léa commence à poster des photos d’elle sur les réseaux."
    "Elle a un corps tout à fait normal, mais après avoir vu défiler de nombreuses influenceuses et mannequins aux silhouettes très fines, elle commence à complexer."
    "Elle décide de se mettre au sport, ce qui pourrait être positif, mais tu remarques qu’elle devient obsédée par son apparence."
    "Elle compare son corps à chaque nouveau post qu’elle voit, et semble de moins en moins présente au quotidien."
    "Que fais-tu ?"
    stop music fadeout 1.0
    scene black
    with fade

    menu:

            "A. Tu lui proposes de faire du sport ensemble, mais en incluant aussi des moments déconnectés et bienveillants pour le plaisir.":
                $ points += 7
                $ lea_points += 7
                "🟡 Tu lui montres qu’il est possible d’être actif sans pression ni comparaison."
                jump situation_9
            
            "B. Tu likes ses posts et partages des comptes de mannequins pour « l’inspirer » davantage.":
                $ points += 0
                $ lea_points += 0
                "🔴 Ton attitude semble valider son obsession, ce qui pourrait accentuer son mal-être."
                jump situation_9

            "C. Tu engages une vraie discussion avec elle sur la pression sociale et l’obsession de l’image, en l’aidant à se reconnecter à ce qui la rend unique.":
                $ points += 10
                $ lea_points += 10
                "🟢 Tu lui montres que son bien-être compte plus que l’apparence, et elle semble touchée par ton soutien."
                jump situation_9

            "D. Tu l’encourages dans ses efforts sans relever son obsession, pensant que ça passera.":
                $ points += 3
                $ lea_points += 3
                "🟠 Tu préfères ne pas intervenir, même si tu remarques qu’elle s’épuise mentalement."
                jump situation_9

label situation_9:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene parc
    with fade

    show tiktok at resize_centered_zoom
    "Tu passes beaucoup de temps chaque jour sur TikTok, entre vidéos éducatives et trends populaires."
    show lea_interesse at top_right
    "Un soir, Léa te propose de faire ensemble un challenge viral qui cartonne en ce moment."
    hide lea_interesse

    show lea_danse at top_right
    "Tu hésites : c’est fun… mais tu sens aussi que tu commences à perdre le contrôle."
    hide lea_danse
    "Que fais-tu ?"
    stop music fadeout 1.0

    scene black
    with fade

    menu:
            "A. Tu acceptes mais après tu te fixes une limite de temps sur TikTok et tu t’y tiens, pour garder le contrôle.":
                $ points += 7
                $ lea_points += 7
                "🟡 Tu sens que tu reprends le dessus, et ton temps est mieux réparti dans ta journée."
                jump situation_10
            
            "B. Tu passes des heures à scroller TikTok après le défi, t’en a besoin pour décompresser du quotidien.":
                $ points += 0
                $ lea_points += 0
                "🔴 Tu te couches tard, fatigué, et tu regrettes un peu de ne pas avoir mieux géré ton temps."
                jump situation_10

            "C. Tu proposes à Léa un autre défi, plus créatif et plus utile, qui reste fun.":
                $ points += 10
                $ lea_points += 10
                "🟢 Léa accepte avec plaisir, et vous passez un bon moment tout en apprenant quelque chose."
                jump situation_10

            "D. Tu acceptes le challenge de Léa pour passer un bon moment, tout en sachant que c’est pas hyper utile.":
                $ points += 3
                $ lea_points += 3
                "🟠 Vous rigolez bien, mais tu sens que tu t’éloignes un peu de tes priorités."
                jump situation_10



label situation_10:
    play music "audio/ambiance.mp3" loop volume 0.4
    scene coworking
    with fade

    show yanis_fier at top_right
    show selfie at resize_centered_zoom
    "Yanis veut te parler. Il a créé un montage photo où il combine le visage de plusieurs camarades dans des scènes artistiques ou humoristiques grâce à une IA."
    "Un des montages, pourtant bienveillant à ses yeux, choque une personne représentée."
    "Yanis te demande s'il peut le publier malgré tout car 'c’est de l’art'."
    "Que fais-tu ?"
    stop music fadeout 1.0
    scene black
    with fade

    menu:
            "A. Tu l’encourages à publier, la liberté artistique passe avant tout.":
                $ points += 0
                $ yanis_points += 0
                "🔴 Tu réalises que tu n’as pas pris en compte l'impact sur la personne concernée."
                jump fin

            "B. Tu lui proposes de modifier le montage avec le consentement des personnes concernées.":
                $ points += 7
                $ yanis_points += 7
                "🟡 Yanis accepte d’en discuter avec les personnes concernées et de modifier l’image en conséquence."
                jump fin

            "C. Tu lui conseilles de ne rien publier sans l’accord explicite de chacun.":
                $ points += 10
                $ yanis_points += 10
                "🟢 Yanis comprend l'importance du consentement et décide de demander à tout le monde avant de publier."
                jump fin

            "D. Tu partages toi-même l’image sur un groupe privé pour 'tester les réactions'.":
                $ points += 3
                $ yanis_points += 3
                "🟠 Les réactions sont partagées, mais tu t'inquiètes des conséquences si la personne concernée l'apprend."
                jump fin
#----------------------------------------------------------------------- Fin du jeu ---------------------------------------------------------------------
label fin:

    show text "{size=40}Tu arrives au bout de ton parcours numérique...{/size}"
    pause 3
    hide text

    show text "{size=40}Chaque décision a forgé ton profil et influencé ton entourage.{/size}"
    pause 3
    hide text

    show text "{size=40}Découvrons maintenant ton niveau de conscience numérique et l'impact sur Léa et Yanis.{/size}"
    pause 3
    hide text

    #calcul des points de fins de personnages
    if lea_points > 20 :
        scene parc
        with fade

        show lea_good_ending at top_right
        "Grâce à ta présence et à des choix réfléchis, Léa prend conscience de son besoin constant d’approbation en ligne."
        "Elle apprend à décrocher des likes et des trends, se recentre sur ce qui compte vraiment, et retrouve peu à peu une identité moins façonnée par les réseaux."
        "Elle utilise encore les applis, mais avec du recul et une vraie liberté."
    
    else :
        scene parc_bad_ending
        with fade

        show lea_bad_ending at top_right
        "Mal orientée ou peu soutenue, Léa devient obsédée par la visibilité.\nChaque décision, chaque post, chaque action est dictée par ce qui “marche” en ligne."
        "Elle vit au rythme des likes, des stories et des coachs numériques.\nPetit à petit, elle s’éloigne d’elle-même et des autres, enfermée dans un personnage qu’elle entretient pour rester visible."
    


    if yanis_points > 10 : 
        scene city
        with fade

        show yanis_photo at top_right
        "Avec ton aide, Yanis a appris à utiliser la tech avec sens.\nSes projets deviennent plus responsables, il comprend l'importance du respect de la vie privée et adopte des pratiques plus éthiques."
    
    else :
        scene city_bad_ending
        with fade
        show yanis_bad_ending at top_right
        "Yanis s’est enfoncé dans la quête de visibilité.\nIl filme sans limites, bricole la vérité pour des vues, et ne distingue plus l’image de la réalité. Il préfère ses likes à ses liens."




    # Calcul des points totaux de conscience
    if points >= 100:
        scene fin1
        with fade
        "Citoyen numérique éclairé :\nTu utilises la technologie de manière éthique et réfléchie. Tu inspires ton entourage à être critique et équilibré, sans devenir dépendant du digital."

    elif points >= 84:
        scene fin2
        with fade
        "Utilisateur équilibré :\nTu es attentif·ve à l'impact de tes choix, mais tu fais parfois des erreurs. Tu restes modéré·e et évites de te laisser submerger par les tendances."

    elif points >= 60:
        scene fin3
        with fade
        "Dépendant discret :\nTu penses avoir le contrôle, mais la technologie influence de plus en plus tes décisions. Tu es déjà bien immergé·e sans t’en rendre compte."

    elif points >= 36:
        scene fin4
        with fade
        "Identité perdue : \n Tu es fortement influencé·e par les tendances numériques, et ta pensée se laisse guider par les algorithmes. Tu as perdu le contact avec tes valeurs."

    else:
        scene fin5
        with fade
        "Agent du chaos numérique : \nTu participes activement à un système toxique, influencé·e par la désinformation et la manipulation. Tes choix numériques nuisent à ton bien-être."

    scene black
    with fade

    show text "{size=40}Au final, il n'y a pas de bonne ou de mauvaise technologie...{/size}"
    pause 4
    hide text

    show text "{size=40}Elle n'est qu'un outil. C’est la main qui la manipule, l’esprit qui la guide, et le cœur qui choisit son impact.{/size}"
    pause 4
    hide text

    show text "{size=40}Tes choix, même imparfaits, dessinent déjà le monde numérique de demain.{/size}"
    pause 4
    hide text

    show text "{size=40}Merci d’avoir joué. Le futur reste entre tes mains.{/size}"
    pause 4
    hide text

    show ai4good at resize_centered
    pause 4
    hide ai4good

    return


