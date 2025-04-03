from .payments import L402Payment
from .context import MCPContext
from .comms import NostrComms

class OpenAutoPaySDK:
    def __init__(self, wallet_key, nostr_key, mcp_server="http://mcp.example.com"):
        self.payment = L402Payment(wallet_key)
        self.context = MCPContext(mcp_server)
        self.comms = NostrComms(nostr_key)

    def process_transaction(self, service_url, query):
        """Execute a full DAMPP transaction."""
        # Step 1: Fetch context
        context_data = self.context.fetch_context(query, self.payment)
        print(f"Context: {context_data}")

        # Step 2: Execute payment
        result = self.payment.request_service(service_url)
        print(f"Service Result: {result}")

        # Step 3: Broadcast payment event
        event_id = self.comms.send_payment_event(f"Payment Intent: {context_data['cost']} sats for {query}")
        print(f"Nostr Event ID: {event_id}")

        return result