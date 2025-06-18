from datetime import datetime


def get_days(datas: list) -> list:
    hoje = datetime.now().day
    dias = []
    for dia in datas:
        dias.append(dia.day)
    return dias

if __name__ == "__main__":
    lista_de_datas = [
        datetime(2023, 9, 12),
        datetime(2030, 6, 11)
    ]
    print(get_days(lista_de_datas))
