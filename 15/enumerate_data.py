from typing import List

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for index, (first_name, last_name) in enumerate(zip(names, countries), start=1):
        print(f"{index}. {first_name:<10} {last_name}")


if __name__ == '__main__':
    enumerate_names_countries()
