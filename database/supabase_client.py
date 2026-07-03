from supabase import create_client
from config.settings import *

class SupabaseClient:

    _client = None

    @classmethod
    def get_client(cls):

        if cls._client is None:
            cls._client = create_client(
                SUPABASE_URL,
                SUPABASE_KEY
            )

        return cls._client