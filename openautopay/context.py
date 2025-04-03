import requests
import json

class MCPContext:
    def __init__(self, server_url):
        self.server_url = server_url

    def fetch_context(self, query, l402_payment):
        """Fetch context data using MCP with L402 authentication."""
        crp = {
            "query": query,  # e.g., "Get API pricing"
            "budget": 500,   # Max sats willing to pay
            "purpose": "marketplace_transaction"
        }
        payload = json.dumps(crp)
        
        # Use L402 to authenticate and pay for context
        response = l402_payment.request_service(f"{self.server_url}/context")
        context_data = json.loads(response)
        return context_data