from fastapi import HTTPException, status


class OrganizationService:
    def __init__(self, db):
        self.db = db

    def get_org_by_id(self, model_name, org_id):
        org = self.db.query(model_name).filter(model_name.id == org_id).first()
        if org is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No org found with this id",
            )
        return org

    def create_org(self, model_name, data):
        db_org = model_name(name=data.name, user_id=data.user_id)
        self.db.add(db_org)
        self.db.commit()
        self.db.refresh(db_org)
        return db_org

    def delete_org(self, model_name, org_id):
        org = self.db.query(model_name).filter(model_name.id == org_id).first()
        if org is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No org found with this id",
            )
        self.db.delete(org)
        self.db.commit()
        return org

    def update_org(self, model_name, org_id, org_data):
        org = self.db.query(model_name).filter(model_name.id == org_id).first()
        if org is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No org found with this id",
            )

        # Update fields dynamically
        update_data = org_data.dict(exclude_unset=True)  # Only update fields provided
        for key, value in update_data.items():
            setattr(org, key, value)

        self.db.commit()
        self.db.refresh(org)
        return org
