def testing_dataset():
    """
    Zdzieszowice, Mickiewicza 12
    Zdzieszowice Mickiewicza 12
    Aleje Trzech Wieszczów
    Kino pod Baranami
    Grota Łokietka

    import from PKW tests
    """
    return [
        {'query': 'Długa 12, Kraków',
         'lat': 50.06715,
         'lon': 19.93860,
         'allowed_mismatch_in_meters': 8,
         'comment': 'potential failure is to prefer Długa 12, Skała, Kraków County',
         'info_about_known_failures': {
             'nominatim': 'https://github.com/osm-search/Nominatim/issues/1916',
            },
        },
        {'query': 'rotmistrza Witolda Pileckiego, Bydgoszcz',
         'lat': 53.13900,
         'lon': 17.98695,
         'allowed_mismatch_in_meters': 1100,
         'comment': 'road without addresses',
        },
        {'query': 'rotm. Witolda Pileckiego, Bydgoszcz',
         'lat': 53.13900,
         'lon': 17.98695,
         'comment': 'expanding (or dropping) shortened part - shortening of quite unusual Polish word',
         'info_about_known_failures': {
             'nominatim': 'https://github.com/osm-search/Nominatim/issues/1208 (more specific report in https://github.com/osm-search/Nominatim/issues/1896',
             },
         'allowed_mismatch_in_meters': 1100,
        }
        ]
