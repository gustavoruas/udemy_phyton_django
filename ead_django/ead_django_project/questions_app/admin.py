from django.contrib import admin
from. import models as question_models

# Register your models here.

#Customizing the manner some objects are managed in Admin tempaltes
class CustomAnswerAdmin(admin.ModelAdmin):
    #customize columns to display
    list_display = ["answer_id","correct_answer","active","question_answer"]
    


admin.site.register(question_models.Difficulty)
admin.site.register(question_models.Subject)
admin.site.register(question_models.Question)
admin.site.register(question_models.Answer, CustomAnswerAdmin)

