def testing_dataset():
    """
    Zdzieszowice, Mickiewicza 12
    Zdzieszowice Mickiewicza 12
    Aleje Trzech Wieszczów
    Kino pod Baranami
    Grota Łokietka
    Wrocławska 3, Kraków
    Worcławska 3, Kraków
    Wroclawska 3, Kraków
    Worclawska 3, Kraków
    Adaś, Kraków
    Nowotworek, Kraków
    Wawel
    Wawel, Kraków
    Rynek, Kraków
    highest mountain
    highest mountain in Poland
    Rysy, Poland

    Warszawska 12 w Krakowie
    50,0694950, 19,9434211

    Osiedle Dywizjonu 303 66
    Dywizjonu 303 66
    Kraków Osiedle Dywizjonu 303 66
    50.08336/20.00638
    50m

    Szkoła w Ochotnicy Górnej
    Szkoła, Ochotnica Górna
    School, Ochotnica Górna
    Jana Kantego w Krakowie
    Kaplica, Jamne

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
