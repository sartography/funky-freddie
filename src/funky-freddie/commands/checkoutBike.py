"""AddDynamoItem."""
import json


class CheckoutBike:
    """Checkout a bike."""

    def __init__(self, bike_id: str, user_id: str):
        self.bike_id = bike_id
        self.user_id = user_id

    def execute(self, config, task_data):
        """Execute."""
        print("**** Executing CheckoutBike *****");

        # Typically, this is just a call to your existing application code, or, a call
        # to another API.  For now, we'll just build a response and send it back. But
        # this is your code and it can function in any way you want - it can be django app,
        # or a call to a Java Spring Application or a call to an external API Service.
        # You are in full control at this point.
        response = {
            "status": "OK",
            "bike_id": self.bike_id,
            "user_id": self.user_id,
        }
        return dict(response=json.dumps(response), mimetype="application/json")
