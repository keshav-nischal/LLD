import copy

class GoogleDocTemplate:
    def __init__(self, title, content):
        self.title = title
        self.content = content


    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\n{'-'*20}"


resume_template = GoogleDocTemplate("Resume", "Content of the resume")
article_template = GoogleDocTemplate("Article", "Content of the article")

resume_template_instance = resume_template.clone()

# make changes 
print(resume_template_instance)