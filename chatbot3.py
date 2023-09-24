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
    "Two neighbors dispute the boundary line between their properties.": "Hiring a surveyor to determine the accurate boundary and negotiating an agreement or, if necessary, pursuing a legal re  in court. Relevant Laws- Indian Registration Act, 1908; Transfer of Property Act, 1882; Specific Relief Act, 1963; and local state laws and regulations regarding land and property.",
    "A tenant claims that the landlord has not made necessary repairs in the rental property.": "Document the issues, communicate with the landlord, and if the issues persist, file a complaint with the relevant Rent Control Authority or Tenancy Tribunal. Relevant Laws: Rent Control Laws (varies by state), Transfer of Property Act, 1882, and the Indian Contract Act, 1872.",
    "A couple decides to get divorced and needs to address child custody and property division. ": "Engaging in mediation or collaborative divorce if possible. If not, seeking legal representation to navigate the divorce process and protect their rights. Relevant Laws: The Hindu Marriage Act, 1955; The Special Marriage Act, 1954; The Indian Divorce Act, 1869; and related state-specific family laws.",
    "An individual is charged with theft.": "Hiring a criminal defense attorney to build a defense strategy, gather evidence, and represent the accused in court. Relevant Laws: Indian Penal Code, 1860; Criminal Procedure Code, 1973; and various specialized laws for specific offenses.",
    "Two businesses have a contract dispute over non-payment for services rendered.": "Review the contract terms, attempt negotiation or mediation, and if necessary, file a lawsuit for breach of contract. Relevant Laws: The Indian Contract Act, 1872; Specific Relief Act, 1963; and various industry-specific regulations.",
    "A consumer buys a faulty product and wants a refund.": "Contacting the seller or manufacturer for a refund or replacement, and if unsuccessful, pursuing a consumer complaint with the appropriate consumer protection agency. Relevant Laws: Consumer Protection Act, 2019 (formerly Consumer Protection Act, 1986); Sale of Goods Act, 1930; and various state consumer protection laws.",
    "Issues like wrongful termination, discrimination, or wage disputes. ": "Seeking legal advice, collecting evidence of wrongful termination, and potentially filing a labor complaint or lawsuit for reinstatement or compensation. Relevant Laws: Industrial Disputes Act, 1947; Payment of Wages Act, 1936; Minimum Wages Act, 1948; and various state-specific labor laws.",
    "Legal action by creditors to recover outstanding debts. ":"Understanding one's rights under debt collection laws, negotiating with the creditor, and potentially considering debt settlement or bankruptcy if appropriate. Relevant Laws: The Recovery of Debts Due to Banks and Financial Institutions Act, 1993; and various state-specific money lending laws.",
    "Tickets and legal matters related to traffic offenses.":" Paying the fine or contesting the ticket in court if there are grounds to dispute it. Relevant Laws: Motor Vehicles Act, 1988; and relevant state-specific traffic regulations.",
    "Accidents leading to injuries and compensation claims.":"Engaging in negotiations with the insurance company or, if necessary, filing a personal injury lawsuit. Relevant Laws: Motor Vehicles Act, 1988 (for road accidents); and principles of tort law for other personal injury cases.",
    " A company discovers that another business is using their trademark without permission.":" Sending a cease-and-desist letter, negotiating a licensing agreement, or filing a trademark infringement lawsuit. Relevant Laws: The Trademarks Act, 1999; The Copyright Act, 1957; The Patents Act, 1970; and The Designs Act, 2000.",
    "A person becomes a victim of online identity theft and financial fraud.":" Reporting the crime to the police and relevant cybercrime authorities, and cooperating in the investigation. Relevant Laws: Information Technology Act, 2000; and various sections of the Indian Penal Code related to cybercrimes.",
    "A couple wishes to adopt a child but faces legal hurdles.": "Consulting with an adoption agency or lawyer specializing in adoption, following the legal adoption process, and ensuring compliance with adoption laws. Relevant Laws: The Juvenile Justice (Care and Protection of Children) Act, 2015; and the Guidelines Governing Adoption of Children, 2015.",
    "A person wants to create a will to distribute their assets upon their death.": "Consulting with an estate planning attorney to draft a legally valid will and establish trusts, if necessary. Relevant Laws: The Indian Succession Act, 1925; and The Hindu Succession Act, 1956 (for Hindus).",
    "An individual's visa is about to expire, and they want to extend their stay in India.": "Consulting with an immigration attorney to explore visa extension options, gathering required documents, and submitting an application to the appropriate authority. Relevant Laws: The Foreigners Act, 1946; The Passport Act, 1967; and The Citizenship Act, 1955.",
    "An employee experiences workplace harassment based on their gender.": "Reporting the harassment to HR or management, and if the issue is not resolved, filing a complaint with the relevant labor authority or seeking legal action. Relevant Laws: The Sexual Harassment of Women at Workplace (Prevention, Prohibition, and Redressal) Act, 2013; and various anti-discrimination laws.",
    "A community is concerned about pollution from a nearby factory.": "Engaging in public advocacy, reporting violations to environmental authorities, or pursuing a lawsuit for environmental damage if necessary. Relevant Laws: The Environment (Protection) Act, 1986; and various state-specific environmental regulations.",
    "A taxpayer disagrees with the income tax assessment made by the tax department.": "Filing an appeal with the tax department, presenting evidence, and seeking re  through the tax appeals process. Relevant Laws: The Income Tax Act, 1961; and the Goods and Services Tax (GST) Act, 2017.",
    " An individual believes their freedom of speech is being curtailed unjustly.": "Seeking legal counsel, potentially filing a writ petition in a high court to protect civil liberties, and engaging in advocacy for rights. Relevant Laws: The Constitution of India, particularly Articles 19 and 21, which protect freedom of speech and personal liberty.",
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
