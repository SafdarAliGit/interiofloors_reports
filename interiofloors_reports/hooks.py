from . import __version__ as app_version

app_name = "interiofloors_reports"
app_title = "Interiofloors Reports"
app_publisher = "portal"
app_description = "this is reports app"
app_email = "safdar211@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/interiofloors_reports/css/interiofloors_reports.css"
# app_include_js = "/assets/interiofloors_reports/js/interiofloors_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/interiofloors_reports/css/interiofloors_reports.css"
# web_include_js = "/assets/interiofloors_reports/js/interiofloors_reports.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "interiofloors_reports/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "interiofloors_reports.utils.jinja_methods",
#	"filters": "interiofloors_reports.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "interiofloors_reports.install.before_install"
# after_install = "interiofloors_reports.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "interiofloors_reports.uninstall.before_uninstall"
# after_uninstall = "interiofloors_reports.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "interiofloors_reports.utils.before_app_install"
# after_app_install = "interiofloors_reports.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "interiofloors_reports.utils.before_app_uninstall"
# after_app_uninstall = "interiofloors_reports.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "interiofloors_reports.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"interiofloors_reports.tasks.all"
#	],
#	"daily": [
#		"interiofloors_reports.tasks.daily"
#	],
#	"hourly": [
#		"interiofloors_reports.tasks.hourly"
#	],
#	"weekly": [
#		"interiofloors_reports.tasks.weekly"
#	],
#	"monthly": [
#		"interiofloors_reports.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "interiofloors_reports.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "interiofloors_reports.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "interiofloors_reports.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["interiofloors_reports.utils.before_request"]
# after_request = ["interiofloors_reports.utils.after_request"]

# Job Events
# ----------
# before_job = ["interiofloors_reports.utils.before_job"]
# after_job = ["interiofloors_reports.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"interiofloors_reports.auth.validate"
# ]
