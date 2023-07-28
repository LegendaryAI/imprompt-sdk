from pydantic import BaseModel


class User(BaseModel):
    id: int

    def get_marketplaces(self):
        pass

    def get_marketplace(self, marketplace_id):
        pass

    def update_marketplace(self, marketplace_id, data):
        pass

    def delete_marketplace(self, marketplace_id):
        pass
