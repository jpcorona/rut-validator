# rut_validator/valrut.py

from itertools import cycle

def clean_rut(rut):
    """Remove any non-numeric characters except 'K' and format the RUT."""
    rut = rut.upper().replace(".", "").replace("-", "")
    return rut

def calculate_verifier(rut):
    """Calculate the verifier digit for the given RUT."""
    reversed_digits = map(int, reversed(rut))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    mod = (-s) % 11
    return "K" if mod == 10 else str(mod)

def validate_rut(rut):
    """Validate the given RUT."""
    rut = clean_rut(rut)
    if not rut[:-1].isdigit() or (rut[-1] not in "0123456789K"):
        return False
    return calculate_verifier(rut[:-1]) == rut[-1]

# Alias for convenience
valrut = validate_rut
