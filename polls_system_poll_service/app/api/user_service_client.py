import httpx

class UserServiceClient:
    USER_SERVICE_URL = "http://localhost:8000"

    @staticmethod
    async def is_user_registered(user_id: int) -> bool:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{UserServiceClient.USER_SERVICE_URL}/users/{user_id}/is_registered")
                if response.status_code == 200:
                    return response.json().get("is_registered", False)
        except Exception as e:
            raise RuntimeError(f"Error communicating with User Service: {str(e)}")
        return False
