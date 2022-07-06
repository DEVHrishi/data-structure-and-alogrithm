'''Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".'''

# TC = O(n*n)

def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

# TC = O(n)

def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))