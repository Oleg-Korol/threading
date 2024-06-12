from concurrent.futures import ThreadPoolExecutor

devices = [
    {"name": "Server1", "ip": "192.168.1.1", 'status': True},
    {"name": "Router1", "ip": "192.168.1.2", 'status': True},
    {"name": "Switch1", "ip": "192.168.1.3", 'status': False},
    {"name": "Server10", "ip": "192.168.1.28", 'status': True},
    {"name": "Router10", "ip": "192.168.1.29", 'status': False},
    {"name": "Switch10", "ip": "192.168.1.30", 'status': True}
]

def monitor_device(device):
    print(f"Мониторинг устройства: {device['name']}, с IP {device['ip']} статус: {device['status']}")
    return device

def handle_device_status(future):
    device=future.result()
    if device.get('status'):
        print(f"Устройство {device['name']} активно и работает нормально.")
    else:
        print(f"Внимание: Устройство {device['name']} неактивно! Включаем устройство.")
        for dev in devices:
            if dev.get('name') == device.get('name'):
                ind = devices.index(dev)
                devices[ind]['status'] = True
        print(f"Устройство {device['name']} успешно включено!")


with ThreadPoolExecutor(max_workers=len(devices)) as executor:
    futures = [executor.submit(monitor_device, device) for device in devices]
    for future in futures:
        future.add_done_callback(handle_device_status)
