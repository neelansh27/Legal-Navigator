import random
from fuzzywuzzy import fuzz

# Define a list of user inputs and corresponding chatbot responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "what's your name": "I'm a chatbot, so I don't have a name.",
    "bye": "Goodbye! Have a great day!",
    "What is the Indian Constitution?": "The Indian Constitution is the supreme law of India, which lays down the framework for the country's political system, governance, and fundamental rights of citizens.",
    "When was the Indian Constitution adopted?": "The Indian Constitution was adopted on January 26, 1950.",
    "Who is known as the 'Father of the Indian Constitution'?": "Dr. B.R. Ambedkar is often referred to as the 'Father of the Indian Constitution.",
    "How many articles are there in the Indian Constitution?": "There are 395 articles in the Indian Constitution as of September 2021.",
    "What are the fundamental rights in the Indian Constitution?": "Fundamental rights are a set of basic rights and freedoms guaranteed to all citizens, including the right to equality, right to freedom, right against exploitation, right to freedom of religion, cultural and educational rights, and the right to constitutional remedies.",
    "What is the Preamble of the Indian Constitution?": "The Preamble is the introductory statement of the Constitution that outlines the guiding principles and objectives of the Constitution.",
    "What is the significance of the Preamble?": "The Preamble serves as a guiding light and reflects the ideals and aspirations of the Indian Constitution, emphasizing justice, liberty, equality, and fraternity.",
    "How many schedules are there in the Indian Constitution?": "There are 12 schedules in the Indian Constitution.",
    "What is the significance of the Directive Principles of State Policy (DPSP) in the Constitution?": "DPSPs are guidelines for the government to promote the welfare of the people and establish a just society. They are not legally enforceable but serve as a moral and political obligation.",
    "Who can amend the Indian Constitution, and under what conditions?": "The Indian Constitution can be amended by Parliament, but certain amendments require a special majority and ratification by at least half of the state legislatures.",
    "What is the role of the President in the Indian Constitution?": "The President is the ceremonial head of state, and their role includes granting assent to bills, appointing the Prime Minister, and representing India internationally.",
    "Who is the head of the Indian Parliament?": "The President of India is the nominal head of Parliament, while the Prime Minister is the leader of the majority party in the Lok Sabha (House of the People).",
    "What are the Lok Sabha and Rajya Sabha in the Indian Parliament?": "The Lok Sabha is the lower house, representing the people's voice through direct elections. The Rajya Sabha is the upper house, representing the states.",
    "What is the significance of the 'Emergency provisions' in the Constitution?": "Emergency provisions grant special powers to the President during times of crisis, allowing for temporary suspension of certain fundamental rights and increased central authority.",
    "What is the tenure of a Member of Parliament (MP) in India?": "The tenure of an MP in the Lok Sabha is five years.",
    "What is the Supreme Court of India, and what is its role?": "The Supreme Court is the highest judicial authority in India, responsible for interpreting and upholding the Constitution.",
    "What is the role of the Attorney General of India?": "The Attorney General is the chief legal advisor to the government and represents the government in legal matters.",
    "What is the significance of the 'Right to Education' in the Indian Constitution?": "The Right to Education is a fundamental right that guarantees free and compulsory education to all children between the ages of 6 and 14.",
    "What are the official languages of India according to the Constitution?": "Hindi and English are the official languages of India, with Hindi in the Devanagari script as the official language of the central government.",
    "What is the process for amending the Constitution?": "Amendments can be initiated in either house of Parliament and require a special majority (i.e., a majority of the total membership and at least two-thirds of members present and voting).",
    "What is the significance of the 73rd and 74th Amendments to the Constitution?": "These amendments empowered local self-governance by establishing Panchayats (rural) and Municipalities (urban) to promote decentralization.",
    "What is the 'Right to Information (RTI)' Act, and when was it enacted?": "The RTI Act, 2005 allows citizens to access information from public authorities, promoting transparency and accountability.",
    "What is the role of the Election Commission of India?": "The Election Commission conducts free and fair elections in India for Parliament and state legislatures.",
    "What are the 'Scheduled Tribes' and 'Scheduled Castes' in India, as per the Constitution?": "Scheduled Tribes and Scheduled Castes are historically disadvantaged groups identified in the Constitution for special protections and benefits.",
    "What is the 'Doctrine of Basic Structure' in constitutional law?": "The Doctrine of Basic Structure asserts that certain core provisions and principles of the Constitution cannot be amended, preserving its fundamental character.",
    "What is 'Federalism' in the Indian context?": "India follows a federal system of governance where powers are divided between the central government and state governments.",
    "What is the significance of the 'Right to Equality' in the Constitution?": "The Right to Equality ensures that all citizens are treated equally before the law and prohibits discrimination on various grounds.",
    "What is 'President's Rule' or 'Governor's Rule' in Indian states?": "It is the suspension of the state government and the imposition of direct central rule in a state in cases of breakdown of constitutional machinery.",
    "What is the 'Goods and Services Tax (GST)' and its constitutional significance?": "GST is a unified tax system that replaced various indirect taxes, bringing uniformity in taxation across India.",
    "What is the role of the Chief Justice of India in the Indian judiciary?": "The Chief Justice of India is the head of the Indian judiciary and plays a pivotal role in administering justice and assigning cases to judges.",
}

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined responses
    if user_input in responses:
        return responses[user_input]
    best_match = max(responses.keys(), key=lambda key: fuzz.ratio(user_input, key))
    if fuzz.ratio(user_input, best_match) > 50:  # Adjust the threshold as needed
        return responses[best_match]
    else:
        return "I'm sorry, I don't understand that."

# Main chat loop
