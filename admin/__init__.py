from django.contrib import admin
from webapps.new_hightech.models.FeedbackModel import FeedBack
from webapps.new_hightech.models.title import *
from webapps.new_hightech.models.baseModel import *
from webapps.new_hightech.models.serviceModel import *
from webapps.new_hightech.models.aboutModel import *
from webapps.new_hightech.models.projectModel import *
from webapps.new_hightech.models.staffModel import *
from webapps.new_hightech.models.blogModel import *
from webapps.new_hightech.models.contactModel import *
from webapps.new_hightech.models.testimonialModel import *
from webapps.new_hightech.models.footerModel import *
from webapps.new_hightech.models.privacyModel import *
from webapps.new_hightech.models.termsModel import *
from webapps.new_hightech.models.faqModel import *
from webapps.new_hightech.models.advertModel import *
from webapps.new_hightech.models.studentModel import *
# Register your models here.


admin.site.register(Fact)
admin.site.register(FAQs)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Staff)
admin.site.register(Point)
admin.site.register(Slider)
admin.site.register(Footer)
admin.site.register(Contact)
admin.site.register(Courses)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Privacy)
admin.site.register(FeedBack)
admin.site.register(Position)
admin.site.register(TitleModel)
admin.site.register(Testimonial)
admin.site.register(Advertisement)
admin.site.register(TermsAndCondition)
admin.site.register(StudentsRegisterModel)
