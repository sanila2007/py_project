def child(Subject, Marks):
    print("Subject = ", Subject)
    print("Marks", Marks)


child("Sinhala", 95)

print("--------------------------------")


def languages(Favourite, *Most_skilled):
    print("My favourite programming language is = ", Favourite)
    print("Languages that I perform well = ", Most_skilled)


languages("Python", "Python", "HTML", "Pyrogram")

print("---------------------------------")


def default(OS="Windows 11", IDLE="pycharm", version=3.10):
    print("My OS = ", OS)
    print("My IDLE = ", IDLE)
    print("My python version = ", version)


default()

print("---------------------------------")


def friend_marks(subject, **friend):
    print("Subject = ", subject)
    for key, value in friend.items():
        print(key, " = ", value)


friend_marks("Sinhala", Nimal=90, Amal=88)

print("-----------------------------------")


def bot(**Languages):
    for key, value in Languages.items():
        print(key, " = ", value)


bot(Torrent_Downloader="python",Song_downloader="python")
