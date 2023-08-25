from _typeshed import Incomplete
from docassemble.base.config import daconfig as daconfig
from docassemble.base.functions import debug_status as debug_status, get_default_timezone as get_default_timezone, server as server, word as word
from docassemble.base.generate_key import random_alphanumeric as random_alphanumeric
from docassemble.base.logger import logmessage as logmessage
from docassemble.webapp.app_object import app as app
from docassemble.webapp.backend import delete_user_data as delete_user_data
from docassemble.webapp.db_object import db as db
from docassemble.webapp.translations import setup_translation as setup_translation
from docassemble.webapp.users.forms import EditUserProfileForm as EditUserProfileForm, MyInviteForm as MyInviteForm, NewPrivilegeForm as NewPrivilegeForm, PhoneUserProfileForm as PhoneUserProfileForm, UserAddForm as UserAddForm, UserProfileForm as UserProfileForm
from docassemble.webapp.users.models import MyUserInvitation as MyUserInvitation, Role as Role, UserAuthModel as UserAuthModel, UserModel as UserModel

HTTP_TO_HTTPS: Incomplete
PAGINATION_LIMIT: Incomplete
PAGINATION_LIMIT_PLUS_ONE: Incomplete

def privilege_list(): ...
def user_list(): ...
def delete_privilege(privilege_id): ...
def edit_user_profile_page(user_id): ...
def add_privilege(): ...
def user_profile_page(): ...
def _endpoint_url(endpoint): ...
def invite(): ...
def user_add(): ...
