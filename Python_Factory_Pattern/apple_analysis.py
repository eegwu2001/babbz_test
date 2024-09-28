
class WorkFlow:
    def __init__(self):
        pass

    def runner(self):      
        transactionInputDF = get_data_source(
            data_type = "csv",
            file_path = "dbfs:/FileStore/tables/Transaction_Updated.csv"
        ).get_data_frame()

        transactionInputDF.show()

workflow = WorkFlow().runner()