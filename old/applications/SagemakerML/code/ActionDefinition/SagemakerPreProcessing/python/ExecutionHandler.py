import json

from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, Table, TargetColumn):
        all_columns = Table.columns.tolist()
        print("Columns In Dataframe  : ", all_columns)

        all_columns.remove(target_column)
        print("Columns Without Target: ", all_columns)

        all_columns.sort()
        print("Feature Column Order  : ", all_columns)

        column_order = [TargetColumn] + all_columns
        print("All Column Final Order: ", column_order)

        output_df = Table[column_order]

        return output_df

