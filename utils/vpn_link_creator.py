from urllib import parse
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

IP = '193.188.23.227:5000'


def create_vpn_link(vpn_key: str) -> str:
    parsed_key = parse.quote_plus(vpn_key)
    return f'http://{IP}/connect?key={parsed_key}'


