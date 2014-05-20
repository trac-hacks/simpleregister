from trac.core import *
from trac.web.chrome import INavigationContributor, ITemplateProvider
from trac.web.main import IRequestHandler

from genshi.builder import tag

from pkg_resources import resource_filename


class SimpleRegisterPlugin(Component):
	implements(INavigationContributor, IRequestHandler, ITemplateProvider)

	
	def __init__(self):
		self.email = self.config.get('simpleregister', 'email', 
				'admin@yourdomain')

	
	# INavigationContributor methods

	def get_active_navigation_item(self, req):
		return 'register'

	def get_navigation_items(self, req):
		if req.authname == 'anonymous':
			yield 'metanav', 'register', tag.a("Register", 
					href=req.href.register())

    
	# IRequestHandler methods

	def match_request(self, req):
		return req.path_info == '/register'

	def process_request(self, req):
		if req.authname != 'anonymous':
			req.redirect(req.href())
		return 'simpleregister.html', {'email': self.email}, None

    
	# ITemplateProvider methods
	
	def get_templates_dirs(self):
		return [resource_filename(__name__, 'templates')]

	def get_htdocs_dirs(self):
		return []
