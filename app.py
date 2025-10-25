from nicegui import ui
import pandas as pd
import plotly.express as px

# Variables globales pour les filtres
filters = {
    'cpty': 'gran1',
    'overall': 'group1',
    'underlying': 'undl1'
}

current_page = 'home'

def create_header():
    with ui.header().classes('bg-blue-100 p-4'):
        ui.label('📊 Mon Application Dashboard').classes('text-2xl font-bold')

def create_sidebar():
    with ui.left_drawer().classes('bg-gray-100 p-4 w-64'):
        ui.label('🏠 Navigation').classes('text-xl font-bold mb-4')
        
        # Navigation
        with ui.column().classes('w-full gap-2'):
            ui.button('Accueil', on_click=lambda: switch_page('home')).classes('w-full')
            ui.button('Process', on_click=lambda: switch_page('process')).classes('w-full')
            ui.button('Reporting', on_click=lambda: switch_page('reporting')).classes('w-full')
            ui.button('Analytics', on_click=lambda: switch_page('analytics')).classes('w-full')
        
        ui.separator()
        ui.label('🎛️ Filtres').classes('text-xl font-bold mb-4')
        
        # Filtres
        with ui.column().classes('w-full gap-4'):
            ui.select(
                ['gran1', 'gran2', 'gran3', 'gran4'],
                value=filters['cpty'],
                on_change=lambda e: update_filter('cpty', e.value)
            ).props('label="Cpty" outlined')
            
            ui.select(
                ['group1', 'group2', 'group3'],
                value=filters['overall'],
                on_Change=lambda e: update_filter('overall', e.value)
            ).props('label="Overall" outlined')
            
            ui.select(
                ['undl1', 'undl2', 'undl3'],
                value=filters['underlying'],
                on_change=lambda e: update_filter('underlying', e.value)
            ).props('label="Underlying" outlined')
        
        ui.separator()
        ui.label('Filtres Actifs:').classes('font-bold')
        ui.label(f"Cpty: {filters['cpty']}")
        ui.label(f"Overall: {filters['overall']}")
        ui.label(f"Underlying: {filters['underlying']}")

def update_filter(filter_name, value):
    filters[filter_name] = value
    refresh_content()

def switch_page(page_name):
    global current_page
    current_page = page_name
    refresh_content()

def create_home_page():
    with ui.column().classes('w-full gap-6'):
        ui.label('📊 Tableau de Bord Principal').classes('text-3xl font-bold')
        
        # Métriques
        with ui.row().classes('w-full gap-4'):
            with ui.card().classes('p-4 text-center'):
                ui.label('87%').classes('text-2xl font-bold')
                ui.label('Performance')
            
            with ui.card().classes('p-4 text-center'):
                ui.label('92%').classes('text-2xl font-bold')
                ui.label('Taux de Réussite')
            
            with ui.card().classes('p-4 text-center'):
                ui.label('1,234').classes('text-2xl font-bold')
                ui.label('Volume')
            
            with ui.card().classes('p-4 text-center'):
                ui.label('78%').classes('text-2xl font-bold')
                ui.label('Efficacité')
        
        # Données
        ui.label('Données selon les filtres:').classes('text-xl font-bold')
        data = pd.DataFrame({
            'Métrique': ['Ventes', 'Profits', 'Clients', 'Conversion'],
            'Valeur': [120, 45, 890, 0.15],
            'Cible': [100, 50, 800, 0.20]
        })
        
        ui.table.from_pandas(data).classes('w-full')

def create_process_page():
    with ui.column().classes('w-full gap-6'):
        ui.label('⚙️ Gestion des Processus').classes('text-3xl font-bold')
        
        with ui.row().classes('w-full gap-6'):
            # État des processus
            with ui.column().classes('gap-4 flex-1'):
                ui.label('État des Processus').classes('text-xl font-bold')
                
                status_data = [
                    ['Validation', '✅ Terminé', '100%'],
                    ['Traitement', '🔄 En cours', '65%'],
                    ['Contrôle', '⏸️ En pause', '0%'],
                    ['Rapport', '✅ Terminé', '100%']
                ]
                
                columns = [
                    {'name': 'processus', 'label': 'Processus', 'field': 'processus'},
                    {'name': 'statut', 'label': 'Statut', 'field': 'statut'},
                    {'name': 'progression', 'label': 'Progression', 'field': 'progression'}
                ]
                rows = [{'processus': row[0], 'statut': row[1], 'progression': row[2]} for row in status_data]
                
                ui.table(columns=columns, rows=rows).classes('w-full')
            
            # Actions
            with ui.column().classes('gap-4 flex-1'):
                ui.label('Actions Rapides').classes('text-xl font-bold')
                
                ui.button('🔄 Lancer le Processus', on_click=lambda: ui.notify('Processus démarré!'))
                ui.button('📊 Générer Rapport', on_click=lambda: ui.notify('Rapport en cours...'))
                ui.button('🧹 Nettoyer Données', on_click=lambda: ui.notify('Nettoyage en cours...'))

def refresh_content():
    # Cette fonction met à jour le contenu principal
    content.clear()
    with content:
        if current_page == 'home':
            create_home_page()
        elif current_page == 'process':
            create_process_page()
        elif current_page == 'reporting':
            create_reporting_page()
        elif current_page == 'analytics':
            create_analytics_page()

def create_reporting_page():
    with ui.column().classes('w-full gap-6'):
        ui.label('📈 Reporting Avancé').classes('text-3xl font-bold')
        ui.label('Page Reporting - En développement...')

def create_analytics_page():
    with ui.column().classes('w-full gap-6'):
        ui.label('🔍 Analytics Avancés').classes('text-3xl font-bold')
        ui.label(f"Filtres actuels: Cpty={filters['cpty']}, Overall={filters['overall']}, Underlying={filters['underlying']}")

# Construction de l'interface
create_header()
create_sidebar()

# Contenu principal
content = ui.column().classes('p-8 w-full')
create_home_page()

# Lancement
ui.run(title="Mon Application", port=8080)