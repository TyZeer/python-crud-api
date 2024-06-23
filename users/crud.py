from users.schemas import CreateUser


def create_user(created_user: CreateUser):
    user = created_user.model_dump()
    return {"success": {"user": user}}
