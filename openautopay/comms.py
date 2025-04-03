from pynostr import Event, Relay
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ed25519

class NostrComms:
    def __init__(self, private_key_hex):
        self.private_key = ed25519.Ed25519PrivateKey.from_private_bytes(bytes.fromhex(private_key_hex))
        self.public_key = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        ).hex()
        self.relay = Relay("wss://relay.example.com")  # Replace with real relay

    def send_payment_event(self, content):
        """Broadcast a payment intent or confirmation via Nostr."""
        event = Event(
            kind=7000,  # Custom Payment Event Type
            content=content,
            pubkey=self.public_key
        )
        event.sign(self.private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw
        ).hex())
        self.relay.publish(event)
        return event.id