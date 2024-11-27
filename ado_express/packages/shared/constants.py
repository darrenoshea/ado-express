import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class Constants:
    DEPLOYMENT_PLAN_FILE_PATH = os.path.join(ROOT_DIR,'../../files/deployment/deployment-plan.md')
    DEPLOYMENT_PLAN_HEADERS = ['Project Name', 'Release Name', 'Release Number', 'Rollback Number', 'Release Url', 'Rollback Url']
    LOG_FILE_PATH = os.path.join(ROOT_DIR,'../../files/logs/deployment.log')
    SEARCH_RESULTS_DEPLOYMENT_PLAN_FILE_PATH = os.path.join(ROOT_DIR,'../../files/search-results/deployment-plan.md')