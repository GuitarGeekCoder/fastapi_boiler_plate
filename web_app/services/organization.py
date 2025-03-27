from fastapi import FastAPI, HTTPException

class OrganizationService():
    def __init__(self,db):
        self.db = db

    def get_org_by_id(self,model_name,org_id):
        org = self.db.query(model_name).filter(model_name.id == org_id).first()
        if org is None:
            raise HTTPException("No org found with this id")
        return org

    def create_org(self,model_name,data):
        db_org = model_name(name=data.name,user_id = data.user_id)
        self.db.add(db_org)
        self.db.commit()
        self.db.refresh(db_org)
        return db_org