from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import schedule
import time
import json
import gc

class ETL:

    def query(self, collection_source):
        
        client = MongoClient("mongodb://ivan:ivan@10.88.26.183:27017")
        db = client["AT"]
        collection = db[collection_source]

        df = pd.DataFrame.from_records(collection.find({}))
            
        return df
            
    def get_view(self, df, collection_src):

        if collection_src == "L4A_defectinfo":

            df = df[['lm_time','eqp_id','op_id','recipe_id','chip_id','ins_cnt','BIN']]
            df.loc[:, 'lm_time'] = pd.to_datetime(df['lm_time'])
            df.loc[:, 'lm_time'] = df['lm_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)

        elif collection_src == "L6B_FS_defectinfo":

            df = df[['sheet_start_time','eqp_id','op_seq','lot_id','recipe_id','sheet_id','ins_cnt','BIN']]
            df.loc[:, 'sheet_start_time'] = pd.to_datetime(df['sheet_start_time'])
            df.loc[:, 'sheet_start_time'] = df['sheet_start_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)

        elif collection_src == "L6B_SW_AT2_defectinfo":

            df = df[['sheet_start_time','eqp_id','recipe_id','sheet_id','ins_cnt','BIN']]
            df.loc[:, 'sheet_start_time'] = pd.to_datetime(df['sheet_start_time'])
            df.loc[:, 'sheet_start_time'] = df['sheet_start_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)

        elif collection_src == "L6B_SW_TC01_defectinfo":

            df = df[['sheet_start_time','eqp_id','op_id','lot_id','recipe_id','sheet_id','ins_cnt','BIN']]
            df.loc[:, 'sheet_start_time'] = pd.to_datetime(df['sheet_start_time'])
            df.loc[:, 'sheet_start_time'] = df['sheet_start_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)   

        elif collection_src == "L6B_SW_TC02_defectinfo":

            df = df[['sheet_start_time','eqp_id','op_id','lot_id','recipe_id','sheet_id','ins_cnt','BIN']]
            df.loc[:, 'sheet_start_time'] = pd.to_datetime(df['sheet_start_time'])
            df.loc[:, 'sheet_start_time'] = df['sheet_start_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)   

        elif collection_src == "L6K_defectinfo":

            df = df[['sheet_start_time','eqp_id','op_id','lot_id','recipe_id','sheet_id','BIN']]
            df.loc[:, 'sheet_start_time'] = pd.to_datetime(df['sheet_start_time'])
            df.loc[:, 'sheet_start_time'] = df['sheet_start_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)                           

        elif collection_src == "L4A_charge2d":
            
            df = df[['lm_time','eqp_id','op_id','recipe_id','chip_id','ins_cnt','step','charge_type']]
            df.loc[:, 'lm_time'] = pd.to_datetime(df['lm_time'])
            df.loc[:, 'lm_time'] = df['lm_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)   

        elif collection_src == "L6B_FS_charge2d":
            
            df = df[['lm_time','eqp_id','op_seq','lot_id','recipe_id','sheet_id','ins_cnt','step','charge_type']]
            df.loc[:, 'lm_time'] = pd.to_datetime(df['lm_time'])
            df.loc[:, 'lm_time'] = df['lm_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)

        elif collection_src == "L6B_SW_AT2_charge2d":

            df = df[['lm_time','eqp_id','recipe_id','sheet_id','ins_cnt','step','charge_type']]
            df.loc[:, 'lm_time'] = pd.to_datetime(df['lm_time'])
            df.loc[:, 'lm_time'] = df['lm_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)  
                    
        elif collection_src == "L6B_SW_TC01_charge2d":

            df = df[['lm_time','eqp_id','op_id','lot_id','recipe_id','sheet_id','ins_cnt','step','charge_type']]
            df.loc[:, 'lm_time'] = pd.to_datetime(df['lm_time'])
            df.loc[:, 'lm_time'] = df['lm_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)  

        elif collection_src == "L6B_SW_TC02_charge2d":
            
            df = df[['lm_time','eqp_id','op_id','lot_id','recipe_id','sheet_id','ins_cnt','step','charge_type']]
            df.loc[:, 'lm_time'] = pd.to_datetime(df['lm_time'])
            df.loc[:, 'lm_time'] = df['lm_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)
        
        elif collection_src == "L6K_charge2d":

            df = df[['sheet_start_time','eqp_id','op_id','lot_id','recipe_id','sheet_id','step','charge_type']]
            df.loc[:, 'sheet_start_time'] = pd.to_datetime(df['sheet_start_time'])
            df.loc[:, 'sheet_start_time'] = df['sheet_start_time'].apply(lambda x: x.strftime("%Y/%m/%d"))
            df = df.drop_duplicates()
            df = df.reset_index(drop=True)                                                    
            
        return df

def job():

    print("The current date and time is", datetime.now().strftime("%Y/%m/%d, %H:%M:%S"))
    
    collections_src = ['L4A_defectinfo',
                        'L6B_FS_defectinfo',
                        'L6B_SW_AT2_defectinfo',
                        'L6B_SW_TC01_defectinfo',
                        'L6B_SW_TC02_defectinfo',
                        'L6K_defectinfo',
                        
                        'L4A_charge2d',
                        'L6B_FS_charge2d',
                        'L6B_SW_AT2_charge2d',
                        'L6B_SW_TC01_charge2d',
                        'L6B_SW_TC02_charge2d',
                        'L6K_charge2d'
                        ]  
    
    collections_tgt = [c+"_view" for c in collections_src]    
    
    print("instantiate object")
    etl_obj = ETL()  
    
    client = MongoClient('mongodb://ivan:ivan@10.88.26.183:27017')
    db = client["AT_view"]   

    for collection_src, collection_tgt in zip(collections_src, collections_tgt):
    
        print("[Before ETL: " + collection_tgt + "]")  
        df = etl_obj.query(collection_src)
        print(df)
        
        print("[After ETL: " + collection_tgt + "]")  
        df = etl_obj.get_view(df, collection_src)
        print(df)

        print("delete database")
        db.drop_collection(collection_tgt)
        
        print("upload database")
        db[collection_tgt].insert_many(json.loads(df.to_json(orient="records")))
        gc.collect()         

    print("==========Done==========")

if __name__ == '__main__':

    # 啟動 Job
    job()
    schedule.every(30).minutes.do(job)

    while True:  
        schedule.run_pending()    
        time.sleep(1)
