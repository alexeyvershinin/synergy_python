def get_user_response(structure, lifestyle, tools):
    response = []
    for i in range(len(structure)):
        response.append(
            get_user_input(
                f'Особенности строения: {structure[i]}\n'
                f'Образ жизни: {lifestyle[i]}\n'
                f'Орудия труда: {tools[i]}\n'
                f'Ваш ответ: '
            )
        )
    return response


def get_user_input(prompt):
    return input(prompt)


def main():
    features_of_the_structure = [
        'Рост 120-140 см. Объем черепа – 500-600 куб. см, прямохождение',
        'Объем мозга – 680 куб. см',
        'Рост 170 см. Объем мозга – 900-110 куб. см. Стопа имеет свод, правая рука лучше развита, постоянное прямохождение, изменение челюстного аппарата, появление изгибов позвоночника',
        'Рост 156 см. Объем мозга – 1400 куб. см. Есть зачаток подбородочного выступа, развитая кисть, сводчатая стопа, высокий свод черепа, не столь массивная нижняя челюсть',
        'Рост 180 см, объем мозга – 1600 куб. см. Внешний облик присущ современному человеку'
    ]
    lifestyle = [
        'Не сооружали постоянных жилищ, не пользовались огнем, образ жизни – стадный',
        'Не умели пользоваться огнем',
        'Поддерживали огонь, строили жилища, совместно охотились. Имелись зачатки членораздельной речи',
        'Могли сооружать жилища, добывать и поддерживать огонь. Проживание в группах по 50-100 человек.',
        'Развитая речь, появились зачатки религии и искусства, умение изготавливать одежду. Проживание в поселениях в составе родовой общине. Освоение земледелия и скотоводства'
    ]
    tools_of_labor = [
        'Палки и камни',
        'Орудия труда в виде камней с заостренными краями',
        'Различные орудия из камня, среди которых самое главное – каменное рубило',
        'Орудия труда самые разные: скребла, остроконечники из камня, кости и дерева',
        'Для изготовления орудий труда использовали самый разнообразный материал: дерево, кости, камни, рога. Из них изготавливали копья, дротики, ножи, скребла'
    ]

    try:
        if len(features_of_the_structure) != len(lifestyle) or len(features_of_the_structure) != len(tools_of_labor):
            raise ValueError("Длины входных массивов должны быть одинаковыми.")

        print(
            f'Вы увидите основные отличительные характеристики из таблицы "Этапы эволюции человека". '
            f'Ваша задача - проанализировать эти характеристики и, основываясь на них, определить, к какому этапу развития человека они относятся.'
        )

        user_responses = get_user_response(features_of_the_structure, lifestyle, tools_of_labor)

        print(*user_responses, sep='=>')

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()