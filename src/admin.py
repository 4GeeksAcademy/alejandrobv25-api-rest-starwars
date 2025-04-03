import os
from flask_admin import Admin
from models import db, User, Character, Planet, UserFavorite
from flask_admin.contrib.sqla import ModelView

class UserFavoriteAdmin(ModelView):
    # Columnas a mostrar
    column_list = ('id', 'user', 'character', 'planet')
    # Personalizar los nombres de las columnas
    column_labels = {
        'id': 'ID',
        'user': 'Username',
        'character': 'Character',
        'planet': 'Planet'
    }
    # Formatear las columnas relacionadas
    column_formatters = {
        'user': lambda v, c, m, p: m.user.username if m.user else 'N/A',
        'character': lambda v, c, m, p: m.character.name if m.character else 'N/A',
        'planet': lambda v, c, m, p: m.planet.name if m.planet else 'N/A'
    }

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(UserFavoriteAdmin(UserFavorite, db.session))
    

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))