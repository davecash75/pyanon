import pydicom
import xnat
import os
import pprint
from antlr4 import FileStream, CommonTokenStream
from DE6Lexer import DE6Lexer
from DE6Parser import DE6Parser
from DE6ParserVisitor import DE6ParserVisitor
from anoncore import Anonymiser


# Read in the DICOM EDIT script
in_das = "./dicomedit.script.example"
input_stream = FileStream(in_das)

in_dcm_dir = "/Users/davecash/Data/GENFI/01-019-11"
print(f"Reading in DICOM files form {in_dcm_dir}")
dcm_list = []
for root, dirs, files in os.walk(in_dcm_dir):
    for name in files:
        if name.endswith(".dcm"):
            dcm = pydicom.dcmread(os.path.join(root,name))
            if dcm:
                dcm_list.append(dcm)
                break

de_lexer = DE6Lexer(input_stream)
token_stream = CommonTokenStream(de_lexer)
de_parser = DE6Parser(token_stream)
tree = de_parser.script()
my_visitor = DE6ParserVisitor()
result = my_visitor.visit(tree)
pprint.pprint(result)

with xnat.connect('https://xnat.bmia.nl') as connection:
    scan = connection.projects['sandbox'].subjects["ANONYMIZ"].experiments["ANONYMIZ"].scans["T1"]
    dicom_data = scan.read_dicom()

anonymiser = Anonymiser(dicom_data)
for action in result:
    action = action['children']
    print(f'Attempting to perform action: {action}')
    anonymiser.perform_action(action)

print(f"Variable set in Anonymiser: {anonymiser.variables}")