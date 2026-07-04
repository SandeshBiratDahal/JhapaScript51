class Variable:
    def __init__(self, name: str, size: int = 1, type: str = "int") -> None:
        self.name = name
        self.size = size
        self.type = type

    def __repr__(self) -> str:
        return f"Variable < {self.name} >"

RAMtracker = [False for _ in range(128)]

portsTracker = {float(f"{i}.{j}"): 1 for i in range(4) for j in range(8)}

variableTracker: dict[Variable, int] = {}

def getUnallocatedAddr(size: int = 1):
    start = None
    count = 0

    for addr in range(len(RAMtracker)):
        if not RAMtracker[addr]:
            if start is None: start = addr
            count += 1
            if count == size: return start
        else:
            start = None
            count = 0
    return -1

def allocateAddr(addr: int, size: int = 1):
    last = size + addr
    while addr < last: RAMtracker[addr] = True; addr += 1

def freeAddr(addr: int, size: int = 1):
    last = size + addr
    while addr < last: RAMtracker[addr] = False; addr += 1