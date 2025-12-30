from week_4.admin import Admin
from week_4.guest import Guest
from week_4.user import User


def main():
    admin = Admin(1, "Alice")
    guest = Guest(2, "Bob")

    print(admin, admin.access_level())
    print(guest, guest.access_level())
    print("Active users:", User.active_users)




if __name__ == "__main__":
    main()
