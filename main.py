import pymysql
from datetime import datetime


def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Mozdabek15",
        database="python"
    )



def schedule_match(team_a, team_b, home_team, match_date):
    con = connect_to_database()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO games (team_a, team_b, home_team, match_date) VALUES (%s, %s, %s, %s)",
        (team_a, team_b, home_team, match_date)
    )
    con.commit()
    con.close()
    print("Utakmica uspešno zakazana!")


def previous_games():
    con = connect_to_database()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM games WHERE match_date < %s", (datetime.now(),))
    games = cursor.fetchall()
    con.close()

    print("Prethodne utakmice:")
    for match in games:
        print(f"{match[1]} vs {match[2]}, domaćin: {match[3]}, datum: {match[4]}")


def upcoming_games():
    con = connect_to_database()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM games WHERE match_date >= %s", (datetime.now(),))
    games = cursor.fetchall()
    con.close()

    print("Nadolazeće utakmice:")
    for match in games:
        print(f"{match[1]} vs {match[2]}, domaćin: {match[3]}, datum: {match[4]}")




while True:
    print("\nOpcije:")
    print("1. Zakazivanje nove utakmice")
    print("2. Prikaz prethodnih utakmica")
    print("3. Prikaz nadolazećih utakmica")
    print("4. Izlaz")

    choice = input("Izaberite opciju: ")

    if choice == "1":
        team_a = input("Unesite naziv Tima A: ")
        team_b = input("Unesite naziv Tima B: ")
        home_team = input("Koji tim je domaćin? (Tim A / Tim B): ")
        match_date = input("Unesite datum i vreme utakmice (YYYY-MM-DD HH:MM:SS): ")

        schedule_match(team_a, team_b, home_team, match_date)

    elif choice == "2":
        previous_games()
    elif choice == "3":
        upcoming_games()
    elif choice == "4":
        print("Izlaz iz programa.")
        break
    else:
        print("Nepoznata opcija. Pokušajte ponovo.")
