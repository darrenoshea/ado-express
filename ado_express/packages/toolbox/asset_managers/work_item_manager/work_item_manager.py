import concurrent.futures

from ado_express.packages.authentication.ms_authentication.ms_authentication import \
    MSAuthentication
from ado_express.packages.shared.enums import RelationTypes


class WorkItemManager:

    def __init__(self, ms_authentication: MSAuthentication):
        self.release_client = ms_authentication.client
        self.work_item_tracking_client = ms_authentication.work_item_tracking_client

    def get_release_urls_from_work_item(self, query_work_item):
        release_urls = []
        work_item = self.get_work_item(query_work_item.id)
        relations = self.get_work_item_relations(work_item)

        for relation in relations:
            release_urls.append(relation.url)
                    
        return release_urls

    def get_query_release_urls(self, query_id):
        release_urls = []
        query_work_items = self.get_query_work_items(query_id)
        # Get workitem release urls
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_release_url_lists = executor.map(self.get_release_urls_from_work_item, query_work_items)
            
            [release_urls.extend(release_url_list) for release_url_list in result_release_url_lists] # Merge lists
        
        return release_urls

    def get_query_work_items(self, query_id):
        query_results = self.work_item_tracking_client.query_by_id(id=query_id)

        return query_results.work_items

    def get_work_item(self, work_item_id, project=None):
        work_item = self.work_item_tracking_client.get_work_item(id=work_item_id, project=project, expand='all')

        return work_item
    
    def get_work_item_relations(self, work_item, relation_names=['integrated in release environment']):
        relations = []

        if work_item.relations:
            
            for relation in work_item.relations:
                attributes_name = relation.attributes['name'] or None

                if attributes_name is not None and str(attributes_name).lower() in relation_names: relations.append(relation)
        
        return relations