import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)

for item in data.get('imdata', []):
    phys = item.get('l1PhysIf', {})
    attr = phys.get('attributes', {})
    
    dn = attr.get('dn', '')
    desc = attr.get('descr', '')
    speed = attr.get('speed', '')
    mtu = attr.get('mtu', '')
    
    print(f"{dn:<50} {desc:<20} {speed:<6} {mtu:<6}")