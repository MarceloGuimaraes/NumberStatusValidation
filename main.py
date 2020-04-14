import sys,os, argparse,time
from datetime import timedelta
import csv
import logging
from classes.GetStatus import GetStatus
from classes.Read_csv_file import ReadFile
from classes.WriteFile import WriteFile
import pandas as pd
from pathlib import Path


COLUMN_STATUS = 'status_validation'
OUTPUT_FILENAME_CSV_STATUS_OK = 'output_status_ok.csv'
OUTPUT_FILENAME_CSV_STATUS_NOK = 'output_status_nok.csv'

#logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

def argsParser():
    parser = argparse.ArgumentParser(description='Python 3 program for validating status on terminals.')
    parser.add_argument('--file_reader', '-f', required = True, help = "CSV file input path.")
    parser.add_argument('--file_writer', '-w', required = True, help = "CSV file output path.")
    parser.add_argument('--block_size', '-b', required = True,type=int, help = "Block size number to terminals validation.")
    #parser.add_argument('--column', '-c', required = True, type=int, help = "Column terminal order in CSV file (initial=0)")
    #parser.add_argument('--proxy', '-c', required = True, choices=["y,n"],default="y", help = "Bloco de telefones enviados")
    return parser.parse_args()

def main():
    start_time = time.time()
    logging.debug('Starting')
    args = argsParser()
    print("CSV file input path = {}".format(args.file_reader))
    print("CSV file output path = {}".format(args.file_writer))
    print("Block size number to terminals validation = {}".format(args.block_size))
    #print("Column terminal order in CSV file (initial=0) = {}".format(args.column))
    read_csv_file(args.file_reader,args.file_writer,args.block_size)
    
    unified_result(args.file_reader,args.file_writer)
    logging.debug('Exiting')
    elapsed_time_secs = time.time() - start_time
    msg = "Program Executed in : %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
    print(msg)    
    return 0
 
def read_csv_file(file_reader,file_writer,block_size):

    try:
        get_status_api = GetStatus()
        outPutFile = WriteFile(file_writer)

        with open(file_reader) as csvfile:
            reader  = csv.reader(csvfile, delimiter=';')
            row_count = 0
            line_numbers = []
            next(reader, None) 
            for row in reader:
                line_numbers.append(row[1])
                #print(row[2])
                #line_numbers.append(row[column])
                if row_count == int(block_size):
                    request_writer_response(get_status_api, line_numbers, outPutFile)
                    row_count = 0
                row_count +=1  
            #print('total linhas =' + str(row_count))
            if line_numbers is not None:
                if len(line_numbers) > 0:
                    request_writer_response(get_status_api, line_numbers, outPutFile)
        csvfile.close()
        outPutFile.close()
        print('Script executado com Sucesso!')
    except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(file_reader, reader.line_num, e))
                print('fechar o arquivo')
                csvfile.close()
                outPutFile.close()

def unified_result(file_reader,file_writer):
    #print(file_reader)
    #print(file_writer)
    data1 = pd.read_csv(file_reader,sep = ';', dtype=str)
    data2 = pd.read_csv(file_writer,sep = ';', dtype=str)
    output=data1
    output[COLUMN_STATUS]=data2.iloc[:,-1]
    output.to_csv(file_writer, sep=';', encoding='utf-8',index=False) 
    rootPath = Path(file_writer)
    push_result(output,rootPath)
    remove_file_writer(file_writer)

def push_result(output_file_writer_responses,output_path):
    #print(output_file_writer_responses.head)
    output_status_nok = output_file_writer_responses[COLUMN_STATUS]=='invalid'
    df_status_nok = output_file_writer_responses[output_status_nok]
    df_status_nok[COLUMN_STATUS].replace({'invalid':'Não'},inplace=True)

    output_status_ok = output_file_writer_responses[COLUMN_STATUS]=='valid'
    df_status_ok = output_file_writer_responses[output_status_ok]
    df_status_ok[COLUMN_STATUS].replace({'valid':'Sim'},inplace=True)
    
    file_writer_ok = os.path.join(os.path.dirname(output_path), OUTPUT_FILENAME_CSV_STATUS_OK)
    file_writer_nok = os.path.join(os.path.dirname(output_path), OUTPUT_FILENAME_CSV_STATUS_NOK)
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

def remove_file_writer(file):
    if os.path.exists(file):
        # removing the file using the os.remove() method
        os.remove(file)
    else:
        # file not found message
        print("File not found in the directory")

if __name__ == '__main__':
    sys.exit(main())
    
#py main.py -f /c/DADOS/fileinput.csv -w /c/DADOS/fileoutput.csv -b 100