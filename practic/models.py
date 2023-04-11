from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Users(Page):
    FIO = models.TextField()
    Job_title = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('FIO'),
        FieldPanel('Job_title')
    ]

class Blog(Page):
    Name_blog = models.TextField()
    Date = models.DateTimeField()
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('Name_blog'),
        FieldPanel('Date'),
        FieldPanel('description')
    ]

class Services(Page):
    Name_Services = models.TextField()
    Price = models.IntegerField()

    content_panels = Page.content_panels + [
        FieldPanel('Name_Services'),
        FieldPanel('Price')
    ]

class Partners(Page):
    Name_Partners = models.TextField()
    Partners_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('Name_Partners'),
        FieldPanel('Partners_image')
    ]

class Enterprise_Solutions(Page):
    Name_Enterprise = models.TextField()
    Text = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('Name_Enterprise'),
        FieldPanel('Text')
    ]