class hash_elm:
    def __init__(self):
        self.id = ""
        self.value = 0
        self.hash_code = 0
        self.collision = False
        self.unaval = False
        self.terminal = False
        self.delining = False
        self.next = None
        self.data = ""



def alpha_mapping(symb):
    mapping = {
        'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10,
        'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20,
        'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ь': 28, 'ъ': 29, 'ы': 30,
        'э': 31, 'ю': 32, 'я': 33,
    }
    symb = symb.lower()
    return mapping.get(symb, -9999999999)
    
def get_value(string):
    value = 0
    if len(string) >= 3:
        range_value = 3
    else:
        range_value = len(string)
    for i in range(range_value):
        value += 33 * alpha_mapping(string[i])
    return value

def get_hash(V, B):
    val = V % 10 + B
    return val

def add_elm(ref, id, data):
    val = get_value(id)
    hsh = get_hash(val, len(id))
    boof = hash_elm()
    is_exists = False

    for i in range(len(ref)):
        if hsh == ref[i].hash_code:
            ref[i].collision = True
            ptr = ref[i]
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = hash_elm()
            ptr = ptr.next
            ptr.data = data
            ptr.next = None
            ptr.id = id
            ptr.value = val
            ptr.hash_code = hsh
            ptr.collision = True
            ptr.unaval = True
            ptr.terminal = False
            ptr.delining = False
            is_exists = True
            break

    if not is_exists:
        boof.data = data
        boof.next = None
        boof.id = id
        boof.value = val
        boof.hash_code = hsh
        boof.collision = False
        boof.unaval = True
        boof.terminal = False
        boof.delining = False
        ref.append(boof)

def rm_elm(ref, id):
    i = 0
    while i < len(ref):
        if ref[i].collision:
            ptr = ref[i]
            while ptr.next != None:
                if ptr.next.id == id and ptr.next.next == None:
                    ptr.next = None
                    break
                elif ptr.next.id == id and ptr.next.next != None:
                    ptr.next = ptr.next.next
                    break
                else:
                    ptr = ptr.next
        elif ref[i].id == id:
            ref.pop(i)
            continue
        i += 1

def print_search_el(ref, id):
    for i in range(len(ref)):
        if ref[i].collision:
            ptr = ref[i]
            while ptr.next != None and id != ptr.id:
                ptr = ptr.next
            if id == ptr.id:
                print("\tИскомое слово принадлежит разделу - ", ptr.data, "\n\n")
        elif ref[i].id == id:
            print("\tИскомое слово принадлежит разделу - ", ref[i].data, "\n\n")

def print_table(ref):
    print("%-10s %-20s %-10s %-10s %-10s %-10s %-10s %-10s %-20s" % ("id", "value", "hash_code", "collision", "unaval", "terminal", "delining", "next", "data"))
    for i in range(len(ref)):
        print("%-10s %-20s %-10s %-10s %-10s %-10s %-10s %-10s %-20s" % (
            ref[i].id, ref[i].value, ref[i].hash_code, int(ref[i].collision),
            int(ref[i].unaval), int(ref[i].terminal), int(ref[i].delining),
            ref[i].next, ref[i].data
        ))
        if ref[i].next is not None:
            print("\n" + "=" * 55  + "  Коллизия  " + "=" * 55)
            print("\n%-10s %-20s %-10s %-10s %-10s %-10s %-10s %-10s %-20s" % (
                "id", "value", "hash_code", "collision", "unaval", "terminal",
                "delining", "next", "data"
            ))
            ptr = ref[i].next
            while ptr is not None:
                print("%-10s %-20s %-10s %-10s %-10s %-10s %-10s %-10s %-20s" % (
                    ptr.id, ptr.value, ptr.hash_code, int(ptr.collision),
                    int(ptr.unaval), int(ptr.terminal), int(ptr.delining),
                    ptr.next, ptr.data
                ))
                ptr = ptr.next
            print("=" * 122 + "\n")

def print_utility():
    print("\t\t\t\t\tВариант 4")
    print("\t\t\t\t\tБиология\n")
    print("\t\t\t\tИспользованные переменные\n")
    table = []
    add_elm(table, "Бактерия", "Микробиология")
    add_elm(table, "Вирус", "Микробиология")
    add_elm(table, "Грибы", "Микология")
    add_elm(table, "Мох", "Ботаника")
    add_elm(table, "Лист", "Ботаника")
    add_elm(table, "Корень", "Ботаника")
    add_elm(table, "Клетка", "Цитология")
    add_elm(table, "Ткань", "Гистология")
    add_elm(table, "Орган", "Органология")
    add_elm(table, "Система органов", "Органология")
    add_elm(table, "Экосистема", "Экология")
    add_elm(table, "Биом", "Экология")
    add_elm(table, "Биомасса", "Экология")
    add_elm(table, "Биосфера", "Экология")
    add_elm(table, "Генетика", "Генетика")
    add_elm(table, "Геном", "Генетика")
    add_elm(table, "Клонирование", "Генетика")
    add_elm(table, "Мутация", "Генетика")
    add_elm(table, "Эволюция", "Эволюционная биология")
    add_elm(table, "Популяция", "Эволюционная биология")
    add_elm(table, "Отбор", "Эволюционная биология")
    add_elm(table, "Адаптация", "Эволюционная биология")
    add_elm(table, "Классификация", "Таксономия")
    add_elm(table, "Филогения", "Филогения")
    print_table(table)
    rm_elm(table,"Отбор")
    print("\n\n\n")
    print_table(table)
    print("\n\n\n")
    print_search_el(table, "Адаптация")
    input("Press Enter to continue...")

if __name__ == "__main__":
    print_utility()