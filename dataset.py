def testing_dataset():
    """
    Zdzieszowice, Mickiewicza 12
    Zdzieszowice Mickiewicza 12
    Aleje Trzech Wieszczów
    Kino pod Baranami


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
        },
        {'query': 'Grota Łokietka',
         'lat': 50.2016322,
         'lon': 19.8188971,
         'comment': 'in case of OSM based ones - test whatever it includes data from edit made on 2020-09-02',
         'allowed_mismatch_in_meters': 6,
        },
        {'query': 'Jaskinia Łokietka',
         'lat': 50.2016322,
         'lon': 19.8188971,
         'allowed_mismatch_in_meters': 6,
        },
        {'query': 'Wrocławska 50, Kraków',
         'lat': 50.07812,
         'lon': 19.92365,
         'allowed_mismatch_in_meters': 9,
        },
        {'query': 'Worcławska 50, Kraków',
         'lat': 50.07812,
         'lon': 19.92365,
         'comment': 'typo tolerance test (street name is Wrocławska)',
         'allowed_mismatch_in_meters': 9,
        },
        {'query': 'Wroclawska 50, Kraków',
         'lat': 50.07812,
         'lon': 19.92365,
         'comment': 'ł vs l tolerance test (street name is Wrocławska)',
         'allowed_mismatch_in_meters': 9,
        },
        {'query': 'Worclawska 50, Kraków',
         'lat': 50.07812,
         'lon': 19.92365,
         'comment': 'combo: typo test, ł vs l tolerance test (street name is Wrocławska)',
         'allowed_mismatch_in_meters': 9,
        },
        {'query': 'Adaś, Kraków',
         'lat': 50.06147,
         'lon': 19.93799,
         'comment': 'loc_name usage for OSM, local name data for others',
         'allowed_mismatch_in_meters': 4,
        },
        {'query': 'Nowotworek, Kraków',
         'lat': 50.05716,
         'lon': 19.93337,
         'comment': 'loc_name usage for OSM, local name data for others',
         'allowed_mismatch_in_meters': 40,
        },
        {'query': 'Wawel',
         'lat': 50.05408,
         'lon': 19.93529,
         'comment': 'some OSM geocoders fail to select important object',
         'allowed_mismatch_in_meters': 65,
        },
        {'query': 'Wawel, Kraków',
         'lat': 50.05408,
         'lon': 19.93529,
         'comment': 'some OSM geocoders fail to select important object',
         'allowed_mismatch_in_meters': 65,
        },
        {'query': 'Rynek, Kraków',
         'lat': 50.06173,
         'lon': 19.93736,
         'comment': 'some OSM geocoders fail to select important object',
         'allowed_mismatch_in_meters': 40,
         'info_about_known_failures': {
             'photon': 'https://github.com/komoot/photon/issues/487 (wontfixed)',
            },
        },
        {'query': 'Warszawska 12, Kraków',
         'lat': 50.0694950,
         'lon': 19.9434211,
         'allowed_mismatch_in_meters': 8,
        },
        {'query': 'Warszawska 12 w Krakowie',
         'lat': 50.0694950,
         'lon': 19.9434211,
         'allowed_mismatch_in_meters': 8,
        },
        {'query': 'Warszawska 12 in Kraków',
         'lat': 50.0694950,
         'lon': 19.9434211,
         'allowed_mismatch_in_meters': 8,
        },
        {'query': 'Mount Everest',
         'lat': 27.9878675,
         'lon': 86.9248308,
         'allowed_mismatch_in_meters': 3,
        },
        {'query': 'highest mountain',
         'lat': 27.9878675,
         'lon': 86.9248308,
         'comment': 'descriptive query',
         'allowed_mismatch_in_meters': 3,
        },
        {'query': 'Rysy, Poland',
         'lat': 49.1795862,
         'lon': 20.0880476,
         'allowed_mismatch_in_meters': 3,
        },
        {'query': 'highest mountain in Poland',
         'lat': 49.1795862,
         'lon': 20.0880476,
         'comment': 'descriptive query',
         'allowed_mismatch_in_meters': 3,
        },
        {'query': 'Osiedle Dywizjonu 303 66, Kraków',
         'lat': 50.08336,
         'lon': 20.00638,
         'comment': '(1) number in name "Osiedle Dywizjonu 303", (2) it is not a street',
         'allowed_mismatch_in_meters': 50,
        },
        {'query': 'Osiedle Dywizjonu 303, 66, Kraków',
         'lat': 50.08336,
         'lon': 20.00638,
         'comment': '(1) number in name "Osiedle Dywizjonu 303", (2) it is not a street - but with helper comma',
         'allowed_mismatch_in_meters': 50,
        },
        {'query': 'Kraków Osiedle Dywizjonu 303 66, Kraków',
         'lat': 50.08336,
         'lon': 20.00638,
         'comment': '(1) number in name "Osiedle Dywizjonu 303", (2) it is not a street (3) city name at start',
         'allowed_mismatch_in_meters': 50,
        },
        {'query': 'Osiedle Dywizjonu 303 66',
         'lat': 50.08336,
         'lon': 20.00638,
         'comment': '(1) number in name "Osiedle Dywizjonu 303", (2) it is not a street (3) without specifying city location',
         'allowed_mismatch_in_meters': 50,
        },
        {'query': 'Dywizjonu 303 66',
         'lat': 50.08336,
         'lon': 20.00638,
         'comment': '(1) number in name "Osiedle Dywizjonu 303", (2) it is not a street (3) without specifying city location (4) osiedle prefix dropped',
         'allowed_mismatch_in_meters': 50,
        },
        {'query': 'Konopnickiej 5, Przeworsk',
         'lat': 50.06119,
         'lon': 22.49045,
         'allowed_mismatch_in_meters': 60,
        },
        {'query': 'M. Konopnickiej 5, Przeworsk',
         'lat': 50.06119,
         'lon': 22.49045,
         'comment': 'dealing with shortened name in input',
         'allowed_mismatch_in_meters': 60,
        },
        ]
