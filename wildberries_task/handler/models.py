import logging

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ArticleModel(BaseModel):
    nm_id: int
    brand_name: str = "Not found"
    imt_name: str = "Not found"

    def __init__(self, **kwargs):
        try:
            kwargs["brand_name"] = kwargs["selling"]["brand_name"]
        except KeyError as err:
            logger.error(f"No such key {err}.")

        super().__init__(**kwargs)
