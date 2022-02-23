# –– coding: utf-8 ––
class Informatica(object):
    def __init__(self, language):
        self.language = language
    def languages(self):
        for line in self.language:
            print(line)

language_script = Informatica(["bash", "Perl", "Python"])

other_languages = Informatica(["C", "Java"])

language_script.languages()
other_languages.languages()
