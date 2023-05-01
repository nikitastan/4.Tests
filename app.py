def get_visits():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    geo_logs_filtered = []

    for visit_dict in geo_logs:
        for visit_dict_countries in visit_dict.values():
            if 'Россия' in visit_dict_countries:
                geo_logs_filtered.append(visit_dict)

    return geo_logs_filtered


def get_unique_ids():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    geo_IDs = []
    for geo_ID in ids.values():
        geo_IDs.extend(geo_ID)
    return list(set(geo_IDs))


def max_stats():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    return max(stats, key=stats.get)


if __name__ == "__main__":
    print(get_unique_ids())
