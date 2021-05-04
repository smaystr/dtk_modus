from settings import PLOADS, URL
from pipelines import EpbetsPipeline
from spiders.requests_api import RequestsApi

if __name__ == "__main__":
    ploads = PLOADS
    url = URL
    response = RequestsApi(url)
    rows = response.get(params=ploads).json()["rows"]
    epbets_pipeline = EpbetsPipeline()
    for row in rows:
        _ = epbets_pipeline.process_item_test({k.lower(): v for k, v in row.items()})
