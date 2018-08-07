from jet.dashboard.modules import DashboardModule
from blog.blog.models import Person


class RecentPersons(DashboardModule):
    title = 'Recent Persons'
    title_url = Person.get_admin_changelist_url()
    #template = 'contact/dashboard_modules/recent_tickets.html'
    limit = 10

    def init_with_context(self, context):
        self.children = Person.objects[:self.limit]