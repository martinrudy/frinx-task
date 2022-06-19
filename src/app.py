from database import db_session, init_db
from models import (
    Interface
)
import json

def add_interface():
    with open('configClear_v2.json', 'r') as f:
        data = json.load(f)
    
    interfaces = data['frinx-uniconfig-topology:configuration']['Cisco-IOS-XE-native:native']['interface']

    if 'Port-channel' in interfaces:
        for interface in interfaces['Port-channel']:
            interface_store = Interface(interface['name'], None, None, interface)
            if 'description' in interface:
                interface_store.description = interface['description']
            if 'mtu' in interface:
                interface_store.max_frame_size = interface['mtu']

            db_session.add(interface_store)
            db_session.commit()
    if 'GigabitEthernet' in interfaces:
        for interface in interfaces['GigabitEthernet']:
            interface_store = Interface(interface['name'], None, None, interface)
            if 'description' in interface:
                interface_store.description = interface['description']
            if 'mtu' in interface:
                interface_store.max_frame_size = interface['mtu']
            if 'Cisco-IOS-XE-ethernet:channel-group' in interface:
                interface_store.port_channel_id = interface['Cisco-IOS-XE-ethernet:channel-group']['number']
            db_session.add(interface_store)
            db_session.commit()

    if 'TenGigabitEthernet' in interfaces:
        for interface in interfaces['TenGigabitEthernet']:
            interface_store = Interface(interface['name'], None, None, interface)
            if 'description' in interface:
                interface_store.description = interface['description']
            if 'mtu' in interface:
                interface_store.max_frame_size = interface['mtu']
            if 'Cisco-IOS-XE-ethernet:channel-group' in interface:
                interface_store.port_channel_id = interface['Cisco-IOS-XE-ethernet:channel-group']['number']
            db_session.add(interface_store)
            db_session.commit()



if __name__ == "__main__":
    init_db()
    add_interface()
