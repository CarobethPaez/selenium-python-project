# utils/test_data.py

# Usuarios válidos
VALID_USERS = [
    ('standard_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
]

# Usuarios inválidos con mensaje de error esperado
INVALID_USERS = [
    ('invalid_user', 'secret_sauce', 'Username and password do not match'),
    ('locked_out_user', 'secret_sauce', 'Sorry, this user has been locked out'),
    ('', '', 'Username is required'),
    ('standard_user', '', 'Password is required'),
]

# Datos de checkout válidos
VALID_CHECKOUT_DATA = {
    'first_name': 'Carobeth',
    'last_name': 'Paez',
    'postal_code': '12345'
}

# Productos disponibles
PRODUCTS = [
    'sauce-labs-backpack',
    'sauce-labs-bike-light',
    'sauce-labs-bolt-t-shirt',
    'sauce-labs-fleece-jacket',
    'sauce-labs-onesie',
    'test.allthethings()-t-shirt-(red)',
]