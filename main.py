from Teste import *
from Repository import *
from Validator import *
from Service import *
from UI import *


repo = FileRepositoryExamen("database.txt")
valid = ValidatorExamen()
service = ServiceExamen(repo, valid)
ui = UIConsole(service)


unittest.main(exit=False)

ui.run()
