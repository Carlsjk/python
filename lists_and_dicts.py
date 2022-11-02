def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "jhonatan", "lastname": "ramirez"}

    super_list = [
        {"firstname": "jhonatan", "lastname": "ramirez"},
        {"firstname": "jhonatan", "lastname": "ramirez"},
        {"firstname": "jhonatan", "lastname": "ramirez"},
        {"firstname": "jhonatan", "lastname": "ramirez"},
        {"firstname": "jhonatan", "lastname": "ramirez"}
    ]

    super_dict = {
        "numeros enteros": [1, 2 , 3, 4, 5, 6],
        "numeros reales": [1, 2, 3, 4, 5, 6, 7],
        "numeros float": [1.3, 1.4, 1.5,]


    }

    for key, value in super_dict.items():
        print(key, "-", value)





if __name__ == '__main__':
    run()