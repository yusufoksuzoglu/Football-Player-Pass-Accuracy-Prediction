"""
footballers_train = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Neymar Jr",
    "Kevin De Bruyne",
    "Virgil van Dijk",
    "Manuel Neuer",
    "Mohamed Salah",
    "Luka Modrić",
    "Sergio Ramos",
    "Kylian Mbappé",
    "Robert Lewandowski",
    "N'Golo Kanté",
    "Jan Oblak",
    "Sadio Mané",
    "Joshua Kimmich",
    "Trent Alexander-Arnold",
    "Harry Kane",
    "Paul Pogba",
    "Raheem Sterling",
    "Ederson"
]

identity_of_footballers_train = {
    "positions": [
        "Forvet", "Forvet", "Forvet", "Orta Saha", "Defans", "Kaleci", "Forvet", "Orta Saha",
        "Defans", "Forvet", "Forvet", "Orta Saha", "Kaleci", "Forvet", "Orta Saha", "Defans",
        "Forvet", "Orta Saha", "Forvet", "Kaleci"
    ],
    "youth_academy": [
        "Newell's Old Boys", "Sporting CP", "Santos", "Genk", "Willem II", "Schalke 04",
        "El Mokawloon", "Dinamo Zagreb", "Sevilla", "AS Bondy", "Varsovia Warsaw",
        "JS Suresnes", "Olimpija Ljubljana", "Génération Foot", "VfB Stuttgart", "Liverpool",
        "Tottenham Hotspur", "Le Havre", "Queens Park Rangers", "São Paulo"
    ],
    "coaches": [
        "Pep Guardiola", "Sir Alex Ferguson", "Tite", "Roberto Martínez", "Jürgen Klopp",
        "Joachim Löw", "Jürgen Klopp", "Zlatko Dalić", "José Mourinho", "Didier Deschamps",
        "Hans-Dieter Flick", "Didier Deschamps", "Diego Simeone", "Jürgen Klopp",
        "Julian Nagelsmann", "Jürgen Klopp", "Gareth Southgate", "Didier Deschamps",
        "Gareth Southgate", "Pep Guardiola"
    ],
    "team_strengths": [
        95, 94, 90, 90, 89, 90, 89, 94, 94, 90,
        90, 85, 86, 89, 90, 89, 83, 82, 90, 90
    ]
}
footballers_train = [
    "Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kevin De Bruyne",
    "Virgil van Dijk", "Manuel Neuer", "Mohamed Salah", "Luka Modrić",
    "Sergio Ramos", "Kylian Mbappé", "Robert Lewandowski", "N'Golo Kanté",
    "Jan Oblak", "Sadio Mané", "Joshua Kimmich", "Trent Alexander-Arnold",
    "Harry Kane", "Paul Pogba", "Raheem Sterling", "Ederson"
] 
"""
identity_of_footballers_train = {
    "positions_numeric" : [
        70, 70, 70, 80, 75, 70, 70, 80,
        75, 70, 70, 80, 70, 70, 80, 75,
        70, 80, 70, 70
    ],
    "youth_academy_numeric" : [
        50, 70 ,70, 70, 55, 75, 55,
        55, 75, 50, 55, 55, 60, 55,
        75, 80, 80, 50, 60, 65
    ],
    "coaches_numeric" : [
        85, 80 ,70, 75, 80, 80, 80,
        70, 75, 80, 80, 80, 80, 80,
        75, 80, 75, 80, 75, 85
    ],
    "team_strengths": [
        95, 94, 90, 90, 89, 90, 89, 94, 94, 90,
        90, 85, 86, 89, 90, 89, 83, 82, 90, 90
    ],
    "national_teams_numeric" : [
        75, 80 ,75, 80, 75, 85, 70,
        80, 90, 80, 70, 80, 65, 65,
        85, 80, 80, 80, 80, 75
    ],
    "play_styles_numeric" : [
        90, 70, 70, 90, 80, 80, 70,
        80, 80, 75, 70, 80, 80, 70,
        80, 75, 75, 80, 70, 80
    ]
}

footballers_numeric = [
    83, 81, 80, 84, 88, 80, 76, 82,
    85, 79, 78, 84, 81, 73, 89, 83,
    80, 81, 77, 85
]
