from utils.input_parser_reader import JSONInputParserReader
from models.input_file_formats import InputFileFormat

def getInputFileParser(file_type :str):
    input_type=InputFileFormat(file_type)
    if(input_type==InputFileFormat.JSON):
        print('get JSON input parser') 
        return JSONInputParserReader
    elif(input_type==InputFileFormat.EXCEL):
        print('get Excel pandas input parser') 
        return JSONInputParserReader
    