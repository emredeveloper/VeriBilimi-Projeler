import json
import random

def get_sample_feedback():
    """Generates a list of simulated customer survey strings."""
    feedback_list = []

    positive_usability = [
        "The interface is so intuitive!",
        "I love how easy it is to use this product.",
        "This is the most user-friendly software I've ever used.",
        "Great design, very easy to navigate.",
        "Kudos to the design team for making it so simple!",
        "I was able to get started right away, no learning curve at all.",
        "The user experience is fantastic.",
        "Everything is exactly where I expect it to be.",
        "Smooth and seamless operation.",
        "Makes my work so much easier, thank you!"
    ]

    support_complaints = [
        "I was on hold for an hour waiting for support.",
        "Customer service needs to be faster.",
        "The wait times for support are unacceptable.",
        "Nobody picked up when I called support.",
        "It took three days to get a response to my email.",
        "Can you please improve your support response time?",
        "Frustratingly long hold times.",
        "Support is very slow to respond.",
        "I gave up waiting for a support agent.",
        "Need more agents in customer support."
    ]

    pricing_questions = [
        "Can you explain the difference between the basic and premium plans?",
        "Is there a discount for yearly subscriptions?",
        "What are the features included in the pro plan?",
        "How much does the enterprise level cost?",
        "Are there any hidden fees I should be aware of?",
        "Is it possible to upgrade my plan later?",
        "Do you offer a non-profit discount?",
        "What payment methods do you accept?",
        "Could you detail the limitations of the free trial?",
        "Is the pricing per user or per team?"
    ]

    feature_suggestions = [
        "It would be great if you could add a dark mode.",
        "I wish there was an option to export data to CSV.",
        "Please add an integration with Salesforce.",
        "A mobile app would be fantastic!",
        "Can you add support for two-factor authentication?",
        "I'd love to see more customization options.",
        "An API for developers would be a great addition.",
        "Could you implement a bulk edit feature?",
        "It would be helpful to have a search function within the settings.",
        "Consider adding a feature to schedule reports."
    ]

    all_feedback_templates = positive_usability + support_complaints + pricing_questions + feature_suggestions
    
    # Ensure between 30 and 50 feedback items
    num_feedback_items = random.randint(30, 50)

    # Make sure we have at least a few of each category if possible, 
    # without being too prescriptive if num_feedback_items is low.
    feedback_list.extend(random.sample(positive_usability, min(len(positive_usability), max(1, num_feedback_items // 4))))
    feedback_list.extend(random.sample(support_complaints, min(len(support_complaints), max(1, num_feedback_items // 4))))
    feedback_list.extend(random.sample(pricing_questions, min(len(pricing_questions), max(1, num_feedback_items // 4))))
    feedback_list.extend(random.sample(feature_suggestions, min(len(feature_suggestions), max(1, num_feedback_items // 4))))

    # Fill the rest with random choices from all templates until we reach num_feedback_items
    while len(feedback_list) < num_feedback_items:
        feedback_list.append(random.choice(all_feedback_templates))
    
    # Shuffle to make the order random
    random.shuffle(feedback_list)
    
    return feedback_list[:num_feedback_items] # Ensure exact number

if __name__ == "__main__":
    feedback_data = get_sample_feedback()
    print(f"Generated {len(feedback_data)} feedback items.")

    with open("sample_feedback.json", "w") as f:
        json.dump(feedback_data, f, indent=2)
    
    print("Sample feedback saved to sample_feedback.json")
