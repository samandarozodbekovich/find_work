from .register import register_view
from .profile import profile_view
from .edit_profile import edit_profile_view
from .portfolio import add_portfolio_view, edit_portfolio_view, delete_portfolio_view
from .certificate import add_certificate_view, edit_certificate_view, delete_certificate_view
from .skills import add_skill_view, edit_skill_view, delete_skill_view
from .education import add_education_view, edit_education_view, delete_education_view
from .experience import add_experience_view, edit_experience_view, delete_experience_view
from .language import add_language_view, edit_language_view, delete_language_view
from .login import CustomLoginView
from .logout import CustomLogoutView
from .posts import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
)
