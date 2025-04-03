from openautopay.sdk import OpenAutoPaySDK

# Mock keys and URLs
WALLET_KEY = "mock_lightning_wallet_key"
NOSTR_KEY = "your_nostr_private_key_hex"  # 64-char hex string
SERVICE_URL = "http://marketplace.example.com/api/data"
MCP_SERVER = "http://mcp.example.com"

# Initialize SDK
sdk = OpenAutoPaySDK(WALLET_KEY, NOSTR_KEY, MCP_SERVER)

# Process a transaction
result = sdk.process_transaction(SERVICE_URL, "Get marketplace pricing")
print(f"Transaction completed: {result}")