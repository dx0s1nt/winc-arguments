# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template='Hello, <name>!'):
    if '<name>' in greeting_template:
        greeting=f"{greeting_template[0:greeting_template.find('<')]}{name}{greeting_template[greeting_template.find('>')+1:]}"
        return greeting
    return

def force(mass,body='earth'):
    gravity_planets={
        'sun':274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }
    if body in gravity_planets:
        force_planet=gravity_planets[body] * mass
        return force_planet
    return

def pull(m1, m2, d):
    g=6.674 * 10 ** -11
    pull_force=g*((m1 * m2) / d ** 2)
    return pull_force
    

earth_weight=5.972 * 10 ** 24
print(greet('bob', greeting_template='Hey, how are you <name>?'))
print(force(100.0))
print(pull(0.1, earth_weight, 6371000))