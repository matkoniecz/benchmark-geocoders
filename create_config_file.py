#!/usr/bin/env python3

# https://docs.python.org/3/library/configparser.html
import configparser

def create_config_file():
    config = configparser.ConfigParser()
    email = input("Please enter your email (will be used in user agent of geolocators to allow their operators to contact you): ")

    config['DEFAULT'] = {
                        'email': email,
                        }
    filename = 'config_file.secret'
    with open(filename, 'w') as configfile:
        config.write(configfile)

    print("data saved as plaintext in", filename, "and will be used by scripts")

def main():
    create_config_file()

if __name__ == "__main__":
    main()