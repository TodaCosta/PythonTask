#https://www.djangosnippets.org/snippets/322/
#https://www.djangosnippets.org/tags/calendar/

from datetime import datetime, tzinfo

from django.db.models import signals
from django.dispatch import dispatcher
from django.utils.tzinfo import FixedOffset, LocalTimezone

from gdata.calendar import CalendarEventEntry
from gdata.calendar.service import CalendarService


class CalendarModelFacade(object):
    """
    A proxy between an instance of a model and Google Calendar.
    """

    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.000Z'

    def __init__(self, instance):
        """ Creates a new instance of CalendarModelFacade. """
        self.instance = instance

    def get_edit_href(self):
        """
        Should return the address used to edit a CalendarEventEntry.
        """
        raise NotImplementedError

    def set_edit_href(self, href):
        """
        Should store the address used to edit a CalendarEventEntry.
        """
        raise NotImplementedError

    def get_when(self):
        """
        Should return a list of gdata.calendar.When objects, which
        define when the event starts/finishes.
        """
        raise NotImplementedError

    def get_title(self):
        """
        May return an atom.Title object, which will be the title of the
        CalendarEventEntry.
        """
        return None

    def get_content(self):
        """
        May return an atom.Content object, which will be the content of the
        CalendarEventEntry.
        """
        return None

    def get_where(self):
        """
        Should return a list of gdata.calendar.Where objects, which
        define where the CalendarEventEntry takes place.
        """
        return []

    def get_categories(self):
        """
        Should return a list of atom.Category objects, which define
        what categories the CalendarEventEntry will fall under.
        """
        return []

    def format_datetime(self, date):
        """
        A utility method that converts the datetime to UTC serialized
        for Google Calendar.
        """
        local = date.replace(tzinfo=LocalTimezone(date))
        return local.astimezone(FixedOffset(0)).strftime(self.DATE_FORMAT)

    def populate_event(self, event):
        """
        A utility method to populate an instance of CalendarEventEntry
        with values obtained from the model instance this is a proxy
        for.
        """
        event.when = self.get_when()
        event.title = self.get_title()
        event.content = self.get_content()
        event.where = self.get_where()
        event.categories = self.get_categories()


class CalendarObserver(object):
    """
    An observer which monitors the lifecycle of a model instance, and
    automatically updates Google Calendar.

    Requires the type of the model to observe and the type of a facade
    object for that model.  Also required are the login details for
    Google Calendar.  Unless specified, the account's default feed will
    be used.
    """

    def __init__(self, model, facade, email, password,
                 feed='/calendar/feeds/default/private/full'):
        """ Creates a new instance of CalendarObserver. """
        self.facade = facade
        self.email = email
        self.password = password
        self.feed = feed
        dispatcher.connect(self.update,
                           signal=signals.pre_save,
                           sender=model)
        dispatcher.connect(self.delete,
                           signal=signals.post_delete,
                           sender=model)

    def update(self, signal, sender, instance):
        """
        Called when an instance of the observed model is saved.  If
        no entry exists (ie. has not yet been created, or has been
        manually deleted), a new CalendarEventEntry will be created.
        Otherwise, the existing CalendarEventEntry will be updated.
        """
        service = self.get_service()
        proxy = self.facade(instance)
        event = self.get_event(service, proxy) or CalendarEventEntry()
        proxy.populate_event(event)
        if event.GetEditLink():
            service.UpdateEvent(event.GetEditLink().href, event)
        else:
            new_event = service.InsertEvent(event, self.feed)
            proxy.set_edit_href(new_event.GetEditLink().href)

    def delete(self, signal, sender, instance):
        """
        Called when an instance of the observed model is deleted.
        """
        service = self.get_service()
        proxy = self.facade(instance)
        event = self.get_event(service, proxy)
        if event:
            service.DeleteEvent(event.GetEditLink().href)

    def get_service(self):
        """
        Returns a logged in instance of CalendarService.
        """
        service = CalendarService(email=self.email, password=self.password)
        service.ProgrammaticLogin()
        return service

    def get_event(self, service, proxy):
        """
        Loads a CalendarEventEntry from Google Calendar.  If that fails,
        returns None.
        """
        try:
            return service.GetCalendarEventEntry(proxy.get_edit_href())
        except:
            return None