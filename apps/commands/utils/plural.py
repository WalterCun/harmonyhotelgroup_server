from pathlib import Path


def plural(obj: Path):
    # Obtiene la parte del nombre del archivo sin la extensión
    stem = obj.stem  # Nombre del archivo sin extensión
    suffix = obj.suffix  # La extensión del archivo

    # 1. Reglas para plurales irregulares
    irregulars = {
        "foot": "feet",
        "tooth": "teeth",
        "mouse": "mice",
        "person": "people"
    }
    if stem in irregulars:  # Si es una palabra irregular, usar su plural correspondiente
        return obj.with_name(irregulars[stem] + suffix)

    # 2. Terminadas en 'f' o 'fe' -> Cambiar a 'ves'
    if stem.endswith("f"):
        return obj.with_name(stem[:-1] + "ves" + suffix)  # Ej.: wolf -> wolves
    if stem.endswith("fe"):
        return obj.with_name(stem[:-2] + "ves" + suffix)  # Ej.: knife -> knives

    # 3. Palabras terminadas en 'y'
    if stem.endswith("y"):
        if len(stem) > 1 and stem[-2] in "aeiou":  # Vocal antes de 'y', añadir 's'
            return obj.with_name(stem + "s" + suffix)
        return obj.with_name(stem[:-1] + "ies" + suffix)  # Consonante antes de 'y', cambiar a 'ies'

    # 4. Palabras terminadas en 's', 'ss', 'x', 'z', 'ch', 'sh' -> Añadir 'es'
    if stem.endswith(("s", "ss", "x", "z", "ch", "sh")):
        return obj.with_name(stem + "es" + suffix)

    # 5. Palabras terminadas en 't', añadir 's'
    if stem.endswith("t"):
        return obj.with_name(stem + "s" + suffix)

    # 6. Palabras terminadas normalmente (regla general)
    return obj.with_name(stem + "s" + suffix)  # Caso general


if __name__ == '__main__':
    print(plural(Path("test.py")))
    print(plural(Path("animal.py")))
    print(plural(Path("dog.py")))
    print(plural(Path("house.py")))
    print(plural(Path("city.py")))
