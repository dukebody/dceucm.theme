from plone.app.layout.viewlets.common import SiteActionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
class dceucm_site_actions(SiteActionsViewlet):
    render = ViewPageTemplateFile("site_actions.pt")
