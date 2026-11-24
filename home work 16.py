class People:
    odamlar_soni = 0

    def __init__(self, ism, familiya, password, tyil):
        if People.odamlar_soni >= 20:
            print("odamlar soni maxga toldi")
        else:
            self.ism, self.familiya, self.__password, self.tyil = ism, familiya, password, tyil
            People.odamlar_soni += 1

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.tyil} tugilgan"

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi


class Student(People):
    def __init__(self, ism, familiya, password, tyil):
        super().__init__(ism, familiya, password, tyil)
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        self.fanlar.remove(fan) if fan in self.fanlar else print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        return f"Talaba: {self.ism} {self.familiya}, fanlar: {[f.nomi for f in self.fanlar]}"


class Professor(People):
    def __init__(self, ism, familiya, password, tyil, kafedra):
        super().__init__(ism, familiya, password, tyil)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, kafedra: {self.kafedra}"


class Foydalanuvchi(People):
    def __init__(self, ism, familiya, password, tyil, login):
        super().__init__(ism, familiya, password, tyil)
        self.login = login

    def get_info(self):
        return f"Foydalanuvchi: {self.login} ({self.ism} {self.familiya})"


class Admin(Foydalanuvchi):
    def ban_user(self):
        print("Foydalanuvchi bloklandi")

    def get_info(self):
        return f"Admin: {self.login} ({self.ism} {self.familiya})"


matematika, fizika = Fan("Matematika"), Fan("Fizika")
talaba = Student("Ali", "Valiyev", "1234", 2005)
talaba.fanga_yozil(matematika)
talaba.remove_fan(fizika)
print(talaba.get_info())
Admin("Jasur", "Aliyev", "9999", 2002, "admin1").ban_user()
