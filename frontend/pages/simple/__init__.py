from .dashboard import create_dashboard_page
from .deadlines import create_deadlines_page
from .notes import create_notes_page
from .tracker import create_tracker_page
from .features import create_features_page

__all__ = [
    'create_welcome_page',
    'create_dashboard_page', 
    'create_deadlines_page',
    'create_notes_page',
    'create_tracker_page',
    'create_features_page'
]