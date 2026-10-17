
import time
from pathlib import Path
import csv
from datetime import datetime
from tkinter import messagebox, ttk
import sys,os
sys.path.append(os.getcwd())
from db import DBHandler

class Exporter:
    def export_button(self, doc_ids):
       '''Makes an export data to csv format'''
       def is_valid_date(date_string, date_format="%Y-%m-%d %H:%M:%S"):
           '''Aux function to test datetime data within TableData'''
           if (type(date_string) is not str):
               return False
           try:
               datetime.strptime(date_string, date_format)
               return True
           except ValueError:
               return False

       headers=[]
       value_rows=[]
       tmp_row=[]
       dbc = DBHandler()
       index_row=0
       for doc_id in doc_ids:
           #prepare data for df
           result_set=dbc.search_record_by_id("_data", doc_id)
           if (result_set == None):
               continue
           for header in result_set.keys():
              if header not in headers:
                 headers.append(header)
              else:
                 continue
           
       #manual allign of df
       for doc_id in doc_ids:
          result_set=dbc.search_record_by_id("_data", doc_id)
          if (result_set == None):
              continue
          for key_inst in headers:
              try:
                  if (type(result_set[key_inst]) is str):
                      tmp_row.append(result_set[key_inst].strip('\n'))
                  else:
                      tmp_row.append(result_set[key_inst])
              except KeyError:
                  #no key -> no value, hence data exists somewhere else.
                  tmp_row.append("")
              except TypeError:
                  print ("Some data mistyped during export")
          value_rows.append(tmp_row.copy())
          tmp_row.clear()
          index_row += 1 
       ts=time.time()   
       export_path = Path("export/"+str(ts)+".csv")
       export_path.parent.mkdir(parents=True, exist_ok=True)
       with open(export_path, mode="w+", newline='',encoding='UTF-8') as csv_file:
           exporter = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
           exporter.writerow(headers)
           for value_row in value_rows:
               exporter.writerow(value_row)
       messagebox.showinfo('Info', "Data is exported at " + str(export_path))
