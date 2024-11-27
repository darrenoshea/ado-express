import os
import pandas as pd

from typing import List

from ado_express.packages.shared.models import DeploymentDetails

class MarkdownManager:

    def __init__(self):
        self.pd = pd

    def align_text(self, df: pd.DataFrame, position='center'):
        return df.style.set_properties(**{'text-align': position})
    
    def create_dataframe(self, file_headers: List[str] = None):
        df = self.pd.DataFrame()

        if file_headers:
            for index, name in enumerate(file_headers):
                df.insert(loc=index, column=str(name), value=None)

        return df

    def convert_deployment_detail_to_excel_row(self, file_headers: List[str], deployment_details: DeploymentDetails):
        return self.pd.DataFrame({
                file_headers[0]: deployment_details.release_project_name, 
                file_headers[1]: deployment_details.release_name, 
                file_headers[2]: deployment_details.release_number,
                file_headers[3]: deployment_details.release_rollback,
                file_headers[4]: deployment_details.release_url,
                file_headers[5]: deployment_details.rollback_url
                }, index=[0])

    def insert_row(self, df, new_df: pd.DataFrame):
        return pd.concat([df, new_df], axis=0)
    
    def save_or_concat_file(self, df: pd.DataFrame, file_path, starting_search=False):
        projects = {
            "b69cd1e4-f121-43a2-84e7-f0665b5624a2": "OCAS Portfolio"
        }

        # Create new file if search is just beginning
        if not starting_search and os.path.isfile(file_path):
            with open(file_path, 'a') as f:
                for row in df.itertuples():
                    project = projects[row[1]]
                    release = row[2]
                    release_number = str(row[3])
                    rollback_number = str(row[4])
                    release_url = str(row[5])
                    rollback_url = str(row[6])
                    f.write(f'| {project} | {release} | [{release_number}]({release_url}) | [{rollback_number}]({rollback_url}) |')
                    f.write('\n')
        else:
            with open(file_path, 'w') as f:
                f.write('| Project Name | Release Name | Release Number | Rollback Number |')
                f.write('\n')
                f.write('| ------------ | ------------ | -------------- | --------------- |')
                f.write('\n')
                for row in df.itertuples():
                    project = projects[row[1]]
                    release = row[2]
                    release_number = str(row[3])
                    rollback_number = str(row[4])
                    release_url = str(row[5])
                    rollback_url = str(row[6])
                    f.write(f'| {project} | {release} | [{release_number}]({release_url}) | [{rollback_number}]({rollback_url}) |')
                    f.write('\n')

