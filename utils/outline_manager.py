from connection.outline.outline_vpn.outline_vpn import OutlineVPN

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_url = config["Outline"]["url"]
cert = config["Outline"]["cert"]

client = OutlineVPN(api_url=api_url, cert_sha256=cert)