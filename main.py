import sys,os, argparse,time,math
from datetime import timedelta
import csv
import logging
from classes.GetStatus import GetStatus
from classes.Read_csv_file import ReadFile
from classes.WriteFile import WriteFile
from classes.Util import Util
import pandas as pd
from pathlib import Path


COLUMN_STATUS = 'status_validation'
SUFFIX_RESPONSE = '_RESPONSE.csv'
CONS_CSV = '.csv'
STATUS_OK = 'STATUS_OK.csv'
STATUS_NOK = 'STATUS_NOK.csv'
NEGATIVE_STATUS = 'Não'
POSITIVE_STATUS = 'Sim'

#logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

def argsParser():
    parser = argparse.ArgumentParser(description='Python 3 program for validating status numbers.')
    parser.add_argument('--csv_input', '-i', required = True, help = "CSV file input path.")
    parser.add_argument('--numbers_per_request', '-b', required = True,type=int, help = "Total numbers per request validation.")
    parser.add_argument('--unified_result', '-u', required = False ,type=bool, help = "Usage ONLY for unified result (skeep status validation)")  
    return parser.parse_args()

def main():
    start_time = time.time()
    logging.debug('Starting')

    args = argsParser()
    run(args)

    logging.debug('Exiting')
    elapsed_time_secs = time.time() - start_time
    print("Program Executed in : {} secs (Wall clock time)".format(timedelta(seconds=round(elapsed_time_secs))))
    return 0

def run(arguments):

    csv_rows=Util.get_row_count(arguments.csv_input)
    print("CSV file input: \n- Path: {} \n- Count of lines: {}".format(arguments.csv_input,csv_rows))
    swap_file = arguments.csv_input.replace(CONS_CSV,SUFFIX_RESPONSE)

    print("Count of requests: ~{}".format(Util.round_up(csv_rows/arguments.numbers_per_request)))

    if arguments.unified_result != True:
        read_csv_file(arguments.csv_input,swap_file,arguments.numbers_per_request)

    result_file_unified = unified_result(arguments.csv_input,swap_file)
    push_result(result_file_unified,arguments.csv_input)
    Util.delete_swap_file(swap_file)


def read_csv_file(csv_input_file,swap_file,numbers_per_request):
    try:
        get_status_api = GetStatus()
        outPutFile = WriteFile(swap_file)

        with open(csv_input_file) as csvfile:
            reader  = csv.reader(csvfile, delimiter=';')
            row_count = 0
            request_count = 1
            line_numbers = []
            next(reader, None) 
            for row in reader:
                line_numbers.append(row[1])
                #print(row[2])
                #line_numbers.append(row[column])
                if row_count == int(numbers_per_request):
                    request_writer_response(get_status_api, line_numbers, outPutFile)
                    logging.debug("Request count: {} ".format(request_count))
                    request_count +=1
                    row_count = 0
                row_count +=1  
            
            if line_numbers is not None:
                if len(line_numbers) > 0:
                    request_writer_response(get_status_api, line_numbers, outPutFile)
                    print("Request count: {} ".format(request_count))
                    request_count +=1
        csvfile.close()
        outPutFile.close()
        print('Script successfully executed!')
    except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(csv_input_file, reader.line_num, e))
                print('File Closed')
                csvfile.close()
                outPutFile.close()

def unified_result(csv_input_file,file_writer):
    #print(csv_input_file)
    #print(file_writer)
    data1 = pd.read_csv(csv_input_file,sep = ';', dtype=str)
    data2 = pd.read_csv(file_writer,sep = ';', dtype=str)
    output=data1
    output[COLUMN_STATUS]=data2.iloc[:,-1]
    output.to_csv(file_writer, sep=';', encoding='utf-8',index=False)
    return output 
    #rootPath = Path(file_writer)

def push_result(output_file_writer_responses,csv_input_file):
    #print(output_file_writer_responses.head)
    output_status_nok = output_file_writer_responses[COLUMN_STATUS]=='invalid'
    df_status_nok = output_file_writer_responses[output_status_nok]
    df_status_nok[COLUMN_STATUS].replace({'invalid':NEGATIVE_STATUS},inplace=True)

    output_status_ok = output_file_writer_responses[COLUMN_STATUS]=='valid'
    df_status_ok = output_file_writer_responses[output_status_ok]
    df_status_ok[COLUMN_STATUS].replace({'valid':POSITIVE_STATUS},inplace=True)

    base_name = Util.get_base_name(csv_input_file)
    
    file_writer_ok = os.path.join(os.path.dirname(csv_input_file), "{}_{}".format(base_name, STATUS_OK))
    file_writer_nok = os.path.join(os.path.dirname(csv_input_file), "{}_{}".format(base_name, STATUS_NOK))
    df_status_ok.to_csv(file_writer_ok, sep=';', encoding='utf-8',index=False) 
    df_status_nok.to_csv(file_writer_nok, sep=';', encoding='utf-8',index=False)  

    print("Total {count} numbers with STATUS OK: {file}".format(count=len(df_status_ok.index), file=file_writer_ok))
    print("Total {count} numbers with STATUS NOK: {file}".format(count=len(df_status_nok.index), file=file_writer_nok))


def request_writer_response(get_status_api, line_numbers, outPutFile):
    get_status_api.request(line_numbers)
    line_numbers.clear()
    json_data = get_status_api.getResponse()
    if json_data is not None:
        for line in json_data:
            strLine = str(line)
            #print(strLine)
            outPutFile.writer(strLine)

if __name__ == '__main__':
    sys.exit(main())
    
#py main.py -f /c/DADOS/fileinput.csv -w /c/DADOS/fileoutput.csv -b 100
