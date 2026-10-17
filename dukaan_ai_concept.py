import random

class DukaanAI:
    def __init__(self, business_name):
        self.business_name = business_name
        self.marketing_tips = [
            f"Promote {self.business_name} on local social media groups.",
            f"Offer a special discount for first-time customers at {self.business_name}.",
            f"Encourage customer reviews on Google Maps for {self.business_name}.",
            f"Partner with other local businesses for cross-promotion.",
            f"Highlight unique products or services of {self.business_name} in your posts.",
            f"Run a small, targeted ad campaign on Facebook for {self.business_name}.",
            f"Create a simple loyalty program for repeat customers of {self.business_name}.",
            f"Share behind-the-scenes content of {self.business_name} to build connection.",
            f"Respond actively to customer inquiries and comments online.",
            f"Consider a small local event or workshop hosted by {self.business_name}."
        ]

    def generate_marketing_idea(self):
        """Generates a random, context-aware marketing idea for the local business."""
        return random.choice(self.marketing_tips)

    def get_business_info(self):
        """Simulates retrieving basic business information."""
        return {
            "name": self.business_name,
            "type": "Local Retail", # Placeholder for more complex AI inference
            "location": "Ankara, Turkey" # Placeholder
        }

# --- Example Usage ---
if __name__ == "__main__":
    # Simulate a local business owner interacting with DukaanAI
    my_shop_name = "Ayşe'nin Manavı"
    ai_assistant = DukaanAI(my_shop_name)

    print(f"Welcome to DukaanAI, your marketing assistant for {my_shop_name}!")
    print("Here's a marketing idea for you:")

    # Generate and display a marketing idea
    marketing_suggestion = ai_assistant.generate_marketing_idea()
    print(f"- {marketing_suggestion}")

    # Simulate getting business info (conceptually, AI would use this)
    business_details = ai_assistant.get_business_info()
    print(f"\n(AI would use details like: {business_details})")
