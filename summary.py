import tkinter as tk
from tkinter import ttk

# Define a dictionary with articles and summaries
articles_and_summaries = {
   	"Article 1: Name and territory of the Union": "This article establishes India as a Union of States, with the name 'India' and describes its territories, which include the States and Union Territories.",
"Article 2: Admission or establishment of new States":  "Article 2 empowers the President to admit new States into the Union or establish new States within the territory of India. It requires the Parliament's approval through legislation.",

"Article 3: Formation of new States and alteration of areas, boundaries, or names of existing States" : "Article 3 gives the Parliament the authority to form new States, alter the boundaries or areas of existing States, or change their names. This process requires a separate law passed by the Parliament.",

"Article 4: Laws made under Articles 2 and 3 to provide for the amendment of the First and the Fourth Schedules" : "Article 4 clarifies that laws made under Articles 2 and 3 (related to admission of new States and alteration of State boundaries) can also amend the First and Fourth Schedules of the Constitution.",

"Article 5: Citizenship at the commencement of the Constitution" : "Article 5 defines who is considered a citizen of India at the commencement of the Constitution. It outlines the criteria for citizenship based on birthplace, domicile, and residence.",

"Article 6: Rights of citizenship of certain persons who have migrated to India from Pakistan" : "Article 6 addresses the citizenship of persons who migrated to India from Pakistan after the partition in 1947. It establishes their right to citizenship under certain conditions.",

"Article 7: Rights of citizenship of certain migrants to Pakistan" : "Article 7 deals with the rights of certain persons who migrated to Pakistan from India but later returned. It specifies that they shall not be considered Indian citizens unless certain conditions are met.",

"Article 8: Rights of citizenship of certain persons of Indian origin residing outside India" : "Article 8 defines the rights of persons of Indian origin who are residing outside India but want to acquire Indian citizenship. It outlines the conditions and procedures for acquiring citizenship.",

"Article 9: Persons voluntarily acquiring citizenship of a foreign State not to be citizens" : "Article 9 stipulates that if an Indian citizen voluntarily acquires citizenship of a foreign country, they may lose their Indian citizenship.",

"Article 10: Continuance of the rights of citizenship" : "Article 10 ensures that any person who is a citizen at the commencement of the Constitution continues to be a citizen unless they voluntarily acquire the citizenship of another country or are disqualified as per the law.",

"Article 11: Parliament to regulate the right of citizenship by law" : "Article 11 grants the Parliament the authority to make laws regarding the acquisition and termination of Indian citizenship. It allows Parliament to regulate citizenship-related matters through legislation.",

"Article 12: Definition of the State" : "Article 12 defines what constitutes the 'State' for the purposes of fundamental rights. It includes the government, Parliament, state legislatures, and other authorities under the control of the government.",

"Article 13: Laws inconsistent with or in derogation of the fundamental rights" : "Article 13 establishes that any law, whether pre- or post-constitution, that is inconsistent with or violates fundamental rights is void to the extent of such inconsistency. It empowers the judiciary to strike down such laws.",

"Article 14: Equality before the law" : "Article 14 guarantees the right to equality before the law and equal protection of the law to all citizens. It prohibits discrimination on grounds of religion, race, caste, sex, or place of birth.",

"Article 15: Prohibition of discrimination on grounds of religion, race, caste, sex, or place of birth" : "Article 15 elaborates on the prohibition of discrimination and extends it to access to public places, educational institutions, and public employment. It allows the government to make special provisions for socially and educationally backward classes.",

"Article 16: Equality of opportunity in matters of public employment" : "Article 16 ensures equality of opportunity in public employment and prohibits discrimination based on religion, race, caste, sex, descent, place of birth, or residence. It allows for reservations in public employment for certain groups.",

"Article 17: Abolition of 'Untouchability'" : "Article 17 abolishes the practice of 'Untouchability' and forbids its practice in any form. It treats such practices as a punishable offense.",

"Article 18: Abolition of titles" : "Article 18 prohibits the granting of titles and recognizes that no citizen of India can accept titles from any foreign state.",

"Article 19: Protection of certain rights regarding freedom of speech, etc." : "Article 19 guarantees several fundamental freedoms, including freedom of speech and expression, assembly, association, movement, residence, and the right to practice any profession, occupation, trade, or business.",

"Article 20: Protection in respect of conviction for offenses" : "Article 20 provides safeguards for persons accused of crimes, including the right to be protected against double jeopardy, self-incrimination, and retrospective criminal laws.",

"Article 21: Protection of life and personal liberty" : "Article 21 protects the right to life and personal liberty and states that no person shall be deprived of these rights except in accordance with the procedure established by law.",

"Article 22: Protection against arrest and detention in certain cases" : "Article 22 outlines safeguards regarding arrest and detention. It includes the right to be informed of the grounds of arrest, consult a legal practitioner, and be produced before a magistrate within 24 hours.",

"Article 23: Prohibition of traffic in human beings and forced labor" : "Article 23 prohibits human trafficking and forced labor, making them punishable offenses.",

"Article 24: Prohibition of employment of children in factories, etc." : "Article 24 prohibits the employment of children below the age of 14 years in factories, mines, or other hazardous employment.",

"Article 25: Freedom of conscience and free profession, practice, and propagation of religion" : "Article 25 guarantees freedom of religion, including the right to practice, profess, and propagate any religion subject to public order, morality, and health.",

"Article 26: Freedom to manage religious affairs" : "Article 26 grants religious denominations and institutions the freedom to manage their own religious affairs.",

"Article 27: Freedom as to payment of taxes for promotion of any particular religion" : "Article 27 prohibits the use of public funds for promoting any particular religion.",

"Article 28: Freedom from attending religious instruction or religious worship in certain educational institutions" : "Article 28 ensures that no one is compelled to attend religious instruction or worship in educational institutions wholly maintained by the state.",

"Article 29: Protection of interests of minorities" : "Article 29 protects the educational and cultural rights of minorities, including the right to establish and administer educational institutions.",

"Article 30: Right of minorities to establish and administer educational institutions" : "Article 30 further elaborates on the rights of religious and linguistic minorities to establish and administer educational institutions of their choice.",

"Article 31: Right to Property Abolished" : "Article 31, which originally dealt with the right to property as a fundamental right, has been repealed and omitted from the Constitution by the 44th Amendment Act, 1978",

"Article 32: Right to Constitutional Remedies" : "Article 32 provides the right to constitutional remedies, allowing citizens to approach the Supreme Court directly to enforce their fundamental rights, with the court having the power to issue various writs for protection",

"Article 33: Power of Parliament to Modify Rights" : "Article 33 empowers Parliament to modify or restrict the application of fundamental rights to armed forces, police forces, intelligence agencies, and other law enforcement authorities for their proper functioning",

"Article 34: Restriction on Rights of Persons Arrested or Detained" : "Article 34 allows Parliament to enact laws for preventive detention for reasons connected with defense, foreign affairs, or the security of India",

"Article 35: Legislation to Give Effect to Directive Principles" : "Article 35 deals with the power of the Parliament and state legislatures to make laws for the effective implementation of fundamental rights, including laws related to the restriction of certain rights for the sovereignty and integrity of India",

"Article 36: Definition of 'State'" : "Article 36 defines the term 'State' for the purposes of Part IV of the Constitution, which deals with Directive Principles of State Policy",

"Article 37: Application of Directive Principles" : "Article 37 declares that the Directive Principles of State Policy are not enforceable by any court but are fundamental in the governance of the country",

"Article 38: State to Secure a Social Order for the Promotion of Welfare" : "Article 38 discusses the Directive Principle of State Policy related to the duty of the State to secure a social order that promotes the welfare of the people, emphasizing reducing inequality and striving for the common good",

"Article 39: Certain Principles of Policy to be Followed by the State" : "Article 39 outlines various Directive Principles, including securing social and economic justice, ensuring equal pay for equal work, preventing the concentration of wealth and resources, and protecting children and workers from exploitation",

"Article 40: Organization of Village Panchayats" : "Article 40 emphasizes the importance of organizing village panchayats and endorses the idea of local self:government in rural areas",

"Article 41: Right to Work, to Education and to Public Assistance in Certain Cases" : "Article 41 directs the State to provide public assistance to those who are unable to maintain themselves, especially in cases of old age, sickness, or disability",

"Article 42: Provision for Just and Humane Conditions of Work and Maternity Relief" : "Article 42 focuses on the improvement of working conditions and the provision of maternity relief",

"Article 43: Living Wage, etc., for Workers" : "Article 43 promotes a living wage and fair conditions of work for all workers, particularly in industries where labor is unorganized",

"Article 44: Uniform Civil Code for the Citizens" : "Article 44 advocates a uniform civil code for all citizens, irrespective of their religion, as a Directive Principle of State Policy",

"Article 45: Provision for Early Childhood Care and Education to Children below the Age of Six Years" : "Article 45 directs the State to provide free and compulsory education for children up to the age of fourteen years",

"Article 46: Promotion of Educational and Economic Interests of Scheduled Castes, Scheduled Tribes, and Other Weaker Sections" : "Article 46 aims at promoting the educational and economic interests of Scheduled Castes, Scheduled Tribes, and other weaker sections",

"Article 47: Duty of the State to Raise the Level of Nutrition and the Standard of Living and to Improve Public Health" : "Article 47 directs the State to raise the level of nutrition and the standard of living and to improve public health",

"Article 48: Organization of Agriculture and Animal Husbandry" : "Article 48 discusses the protection and improvement of the environment, safeguarding forests and wildlife, and prohibiting the slaughter of cows, calves, and other milch and draught cattle",

"Article 49: Protection of Monuments and Places and Objects of National Importance" : "Article 49 emphasizes the protection of monuments and places of national importance",

"Article 50: Separation of Judiciary from Executive" : "Article 50 calls for the separation of the judiciary from the executive to ensure the independence of the judiciary",

"Article 51: Promotion of International Peace and Security" : "Article 51 outlines India's foreign policy goals, including the promotion of international peace and security and adherence to principles of international law",

"Article 51A: Fundamental Duties" : "Article 51A lists the fundamental duties of citizens, including respect for the Constitution, promotion of harmony and the spirit of inquiry, safeguarding public property, and protecting the environment",

"Article 52: Definition of the President of India" : "Article 52 defines the office of the President of India and states that there shall be a President of India",

"Article 53: Executive Power of the Union" : "Article 53 vests the executive power of the Union in the President, to be exercised in accordance with the Constitution",

"Article 54: Election of President" : "Article 54 describes the method of election of the President of India by an electoral college consisting of the elected members of both Houses of Parliament",

"Article 55: Manner of Election of President" : "Article 55 further details the manner of the election of the President, including the allocation of votes among states and union territories",

"Article 56: Term of Office of President" : "Article 56 specifies the term of office of the President and the eligibility for re:election",

"Article 57: Eligibility for Re:election" : "Article 57 allows for the re:election of the President for a second term",

"Article 58: Qualifications for Election as President" : "Article 58 sets forth the qualifications required for a candidate to be elected as President",

"Article 59: Conditions of President's Office" : "Article 59 outlines the conditions of the President's office, including the oath or affirmation of office",

"Article 60: Oath or Affirmation by the President" : "Article 60 prescribes the oath or affirmation to be taken by the President before entering upon office",

"Article 61: Procedure for Impeachment of the President" : "Article 61 provides for the procedure of impeachment of the President on the grounds of violation of the Constitution",

"Article 62: Time of Holding Presidential Election" : "Article 62 specifies the time for holding a presidential election",

"Article 63: Number of Votes Required for Election" : "Article 63 establishes the number of votes required for a candidate to be declared elected as President",

"Article 64: Conditions of Vice President's Office" : "Article 64 outlines the conditions of the Vice President's office, including the oath or affirmation of office",

"Article 65: Election of Vice President" : "Article 65 describes the method of election of the Vice President of India by an electoral college consisting of members of both Houses of Parliament",

"Article 66: Election of the Vice President": "This article deals with the election of the Vice President of India, including the manner of election and the qualifications for the office.",

"Article 67: Term of office of the Vice President": "Article 67 specifies the term of office of the Vice President and the conditions under which the Vice President may be removed from office.",

"Article 68: Time of holding election to fill vacancy in the office of Vice President and the term of office of a person elected to fill casual vacancy": "This article outlines the procedure for holding elections to fill a vacancy in the office of the Vice President and the term of the person elected to fill such a vacancy.",

"Article 69: Oath or affirmation by the Vice President": "It mandates that the Vice President must take an oath or affirmation before entering upon their office.",

"Article 70: Discharge of President's functions in other contingencies": "Article 70 addresses situations where the Vice President may discharge the functions of the President in case of the President's inability to perform their duties.",

"Article 71: Matters relating to or connected with the election of a President or Vice President": "Article 71 establishes the authority of the Supreme Court in matters related to the election of the President or Vice President.",

"Article 72: Power of President to grant pardons, etc., and to suspend, remit or commute sentences in certain cases": "This article grants the President the power to grant pardons, reprieves, respites, or remissions of punishment and to suspend, remit, or commute sentences in certain cases.",

"Article 73: Extent of executive power of the Union": "Article 73 defines the extent of the executive power of the Union and clarifies that it extends to matters on which Parliament has the power to legislate.",

"Article 74: Council of Ministers to aid and advise President": "It establishes the Council of Ministers headed by the Prime Minister and specifies their duty to aid and advise the President in the exercise of his functions.",

"Article 75: Other provisions as to Ministers": "Article 75 outlines various provisions regarding the appointment, tenure, and responsibilities of Ministers in the Union government.",

"Article 76: Attorney General for India": "This article defines the role and duties of the Attorney General for India, who is the chief legal advisor to the government.",

"Article 77: Conduct of business of the Government of India": "Article 77 deals with the conduct of government business and the allocation of responsibilities among various authorities.",

"Article 78: Duties of Prime Minister as respects the furnishing of information to the President, etc.": "Article 78 describes the Prime Minister's duties in furnishing information to the President regarding the administration of affairs of the Union.",

"Article 79: Constitution of Parliament": "It lays down the structure of the Indian Parliament, which consists of the President and two Houses, the Council of States (Rajya Sabha) and the House of the People (Lok Sabha).",

"Article 80: Composition of the Council of States": "Article 80 specifies the composition of the Rajya Sabha, including the allocation of seats to states and union territories.",

"Article 81: Composition of the House of the People": "Article 81 outlines the composition of the Lok Sabha, including the allocation of seats to states and union territories based on population.",

"Article 82: Readjustment after each census": "It deals with the periodic readjustment of the number of seats in the Lok Sabha and the allocation of seats to states following each census.",

"Article 83: Duration of Houses of Parliament": "Article 83 sets the duration of the Lok Sabha and the Rajya Sabha, with a maximum term of five years.",

"Article 84: Qualifications for membership of Parliament": "It specifies the qualifications required for a person to become a member of either House of Parliament.",

"Article 85: Sessions of Parliament, prorogation and dissolution": "Article 85 addresses the convening, prorogation, and dissolution of sessions of Parliament.",

"Article 86: Right of President to address and send messages to Houses": "It grants the President the right to address and send messages to either House of Parliament.",

"Article 87: Special address by the President": "Article 87 allows the President to address both Houses of Parliament together or separately.",

"Article 88: Rights of Ministers and Attorney General as respects the Houses": "It outlines the rights of Ministers and the Attorney General to speak in and otherwise participate in the proceedings of Parliament.",

"Article 89: Vacation of seats": "Article 89 deals with the vacation of seats by members of Parliament.",

"Article 90: Vacation of seats of members elected on more than one seat": "It specifies that members elected to more than one seat in either House of Parliament must vacate the extra seat.",

"Article 91: Powers, privileges, etc., of the Houses of Parliament and of the members and committees thereof": "Article 91 grants powers and privileges to the Houses of Parliament, members, and their committees.",

"Article 92: Committees of Parliament": "It authorizes each House of Parliament to form its own committees for various purposes.",

"Article 93: Speaker and Deputy Speaker of the House of the People": "Article 93 deals with the election and duties of the Speaker and Deputy Speaker of the Lok Sabha.",

"Article 94: The Chairman and Deputy Chairman of the Council of States": "Article 94 addresses the election and responsibilities of the Chairman and Deputy Chairman of the Rajya Sabha.",

"Article 95: Vacation of the offices of Chairman and Deputy Chairman": "It specifies the circumstances under which the offices of Chairman and Deputy Chairman of the Rajya Sabha may become vacant.",

"Article 96: The Deputy Speaker of the House of the People": "Article 96 outlines the election and duties of the Deputy Speaker of the Lok Sabha.",

"Article 97: Salaries and allowances of the Speaker and Deputy Speaker and the Chairman and Deputy Chairman": "Article 97 determines the salaries and allowances of the Speaker, Deputy Speaker, Chairman, and Deputy Chairman of Parliament.",

"Article 98: Secretariat of Parliament": "It deals with the establishment of a separate Secretariat for Parliament to assist in its functioning.",

"Article 99: Oath or affirmation by members": "Article 99 mandates that members of Parliament must take an oath or affirmation before assuming their office.",

"Article 100: Voting in Houses, power of Houses to act notwithstanding vacancies and quorum": "Article 100 sets rules for voting in Parliament, its ability to function despite vacancies, and the quorum required for its proceedings.",

"Article 101: Vacation of seats": "It specifies the conditions under which members of Parliament shall vacate their seats.",

"Article 102: Disqualifications for membership": "Article 102 outlines disqualifications for membership in Parliament.",

"Article 103: Decision on questions as to disqualifications of members": "It empowers the President, the Speaker, or the Chairman, as the case may be, to decide questions related to the disqualification of members.",

"Article 104: Penalty for sitting and voting before making oath or affirmation under article 99 or when not qualified or when disqualified": "Article 104 imposes penalties for members who sit and vote in Parliament without taking the required oath or affirmation, when they are not qualified, or when they are disqualified.",

"Article 105: Powers, privileges, etc., of the Houses of Parliament and of the members and committees thereof": "Article 105 grants powers and privileges to the Houses of Parliament, members, and their committees, similar to Article 91.",

"Article 106: Salaries and allowances of members": "It determines the salaries and allowances of members of Parliament.",

"Article 107: Provisions as to introduction and passing of Bills": "Article 107 outlines the procedure for the introduction and passing of bills in Parliament.",

"Article 108: Joint sitting of both Houses in certain cases": "Article 108 allows for a joint sitting of both Houses of Parliament in certain situations to resolve disagreements on bills.",

"Article 109: Special procedure in respect of Money Bills": "It specifies the special procedure for the consideration and passage of Money Bills in Parliament.",

"Article 110: Definition of 'Money Bills'": "Article 110 defines what constitutes a 'Money Bill' and lists the characteristics of such bills.",

"Article 111: Assent to Bills": "It outlines the President's role in giving assent to bills passed by Parliament and the consequences of withholding assent.",

"Article 112: Annual financial statement": "Article 112 requires the presentation of an annual financial statement, known as the Budget, to Parliament.",

"Article 113: Procedure in Parliament with respect to estimates": "It details the procedure in Parliament for the discussion and voting on estimates of expenditure.",

"Article 114: Appropriation Bills": "Article 114 pertains to the procedure for the introduction and passing of Appropriation Bills in Parliament.",

"Article 115: Supplementary, additional or excess grants": "It covers the procedure for supplementary, additional, or excess grants in Parliament.",

"Article 116: Votes on account, votes of credit and exceptional grants": "Article 116 outlines the procedure for votes on account, votes of credit, and exceptional grants in Parliament.",

"Article 117: Special provisions as to financial Bills": "It specifies the procedure for the introduction and consideration of financial Bills in Parliament.",

"Article 118: Rules of procedure": "Article 118 allows each House of Parliament to make its own rules of procedure.",

"Article 119: Regulation by law of procedure in Parliament in relation to financial business": "It enables Parliament to regulate its own procedure in relation to financial business through legislation.",

"Article 120: Language to be used in Parliament": "Article 120 mandates the use of either Hindi or English for official purposes in Parliament.",

"Article 121: Restriction on discussion in Parliament": "It restricts discussions in Parliament on certain matters related to the conduct of judges of the Supreme Court and high courts.",

"Article 122: Courts not to inquire into proceedings of Parliament": "Article 122 prohibits the courts from inquiring into the proceedings of Parliament.",

"Article 123: Power of President to promulgate Ordinances during recess of Parliament": "This article grants the President the power to promulgate ordinances when Parliament is not in session.",

"Article 124: Establishment and constitution of Supreme Court": "Article 124 establishes the Supreme Court of India and outlines its composition and jurisdiction.",

"Article 125: Salaries, etc., of Judges": "Article 125 determines the salaries and allowances of judges of the Supreme Court.",

"Article 126: Appointment of acting Chief Justice": "It addresses the appointment of an acting Chief Justice of India in certain situations.",

"Article 127: Appointment of ad hoc Judges": "Article 127 allows for the appointment of ad hoc judges in the Supreme Court.",

"Article 128: Attendance of retired Judges at sittings of the Supreme Court": "It permits retired judges to attend sittings of the Supreme Court.",

"Article 129: Supreme Court to be a court of record": "Article 129 designates the Supreme Court as a court of record with all the powers of such a court.",

"Article 130: Seat of the Supreme Court": "It specifies the seat of the Supreme Court.",

"Article 131: Original jurisdiction of the Supreme Court": "Article 131 grants the Supreme Court original jurisdiction in certain disputes between the Union and States or between States.",

"Article 132: Appellate jurisdiction of the Supreme Court in appeals from High Courts in certain cases": "It outlines the appellate jurisdiction of the Supreme Court in certain cases.",

"Article 133: Appellate jurisdiction of the Supreme Court in appeals from High Courts in regard to civil matters": "Article 133 deals with the appellate jurisdiction of the Supreme Court in civil matters.",

"Article 134: Appellate jurisdiction of the Supreme Court in regard to criminal matters": "It pertains to the appellate jurisdiction of the Supreme Court in criminal matters.",

"Article 135: Jurisdiction and powers of the Federal Court under existing law to be exercisable by the Supreme Court": "Article 135 transfers the jurisdiction and powers of the Federal Court under existing law to the Supreme Court.",

"Article 136: Special leave to appeal by the Supreme Court": "Article 136 grants the Supreme Court the discretionary power to grant special leave to appeal in any case.",

"Article 137: Review of judgments or orders by the Supreme Court": "It allows the Supreme Court to review its judgments or orders.",

"Article 138: Enlargement of the jurisdiction of the Supreme Court": "Article 138 empowers the Parliament to expand the jurisdiction of the Supreme Court.",

"Article 139: Conferment on the Supreme Court of powers to issue certain writs": "It authorizes the Supreme Court to issue writs for the enforcement of fundamental rights.",

"Article 140: Ancillary powers of Supreme Court": "Article 140 grants ancillary powers to the Supreme Court to ensure the enforcement of its orders.",

"Article 141: Law declared by Supreme Court to be binding on all courts": "It establishes that the law declared by the Supreme Court is binding on all courts in India.",

"Article 142: Enforcement of decrees and orders of Supreme Court and orders as to discovery, etc.": "Article 142 enables the Supreme Court to enforce its decrees and orders and issue orders for discovery, production of documents, etc.",

"Article 143: Power of President to consult Supreme Court": "It allows the President to seek the Supreme Court's opinion on certain questions of law or fact.",

"Article 144: Civil and judicial authorities to act in aid of the Supreme Court": "Article 144 mandates that all civil and judicial authorities in India must act in aid of the Supreme Court.",

"Article 145: Rules of procedure": "Article 145 allows the Supreme Court to make its own rules of procedure.",

"Article 146: Officers and servants and the expenses of the Supreme Court": "It deals with the appointment of officers and servants and the allocation of expenses for the Supreme Court.",

"Article 147: Interpretation": "Article 147 empowers the President to appoint a person to interpret the Constitution when a question arises in the discharge of his functions.",

"Article 148: Comptroller and Auditor-General of India": "This article deals with the appointment, duties, and powers of the Comptroller and Auditor-General of India.",

"Article 149: Duties and powers of the Comptroller and Auditor-General": "Article 149 specifies the duties and powers of the Comptroller and Auditor-General in auditing government accounts.",

"Article 150: Form of accounts of the Union and of the States": "It outlines the form in which the accounts of the Union and States shall be kept.",

"Article 151: Audit reports": "Article 151 deals with the submission of audit reports to the President and Governors.",

"Article 152: Definitions": "This article provides definitions for certain terms related to the States.",

"Article 153: Governors of States": "Article 153 establishes the office of the Governor in each State and outlines their appointment, powers, and duties.",

"Article 154: Executive power of State": "It specifies that the executive power of the State shall be vested in the Governor and shall be exercised by him either directly or through officers.",

"Article 155: Appointment of Governor": "Article 155 deals with the appointment and term of the Governor.",

"Article 156: Term of office of Governor": "This article specifies the term of office of the Governor and the conditions under which a Governor may be removed from office.",

"Article 157: Qualifications for appointment as Governor": "It outlines the qualifications required for a person to be appointed as a Governor.",

"Article 158: Conditions of Governor's office": "Article 158 discusses the conditions of the Governor's office, including the oath or affirmation required.",

"Article 159: Oath or affirmation by the Governor": "This article mandates that the Governor must take an oath or affirmation before entering upon their office.",

"Article 160: Discharge of the functions of the Governor in certain contingencies": "Article 160 addresses situations where the functions of the Governor may be discharged by the President or another person.",

"Article 161: Power of Governor to grant pardons, etc., and to suspend, remit or commute sentences in certain cases": "This article grants the Governor the power to grant pardons, reprieves, respites, or remissions of punishment and to suspend, remit, or commute sentences in certain cases.",

"Article 162: Extent of executive power of State": "Article 162 defines the extent of the executive power of a State and clarifies that it extends to matters on which the State Legislature has the power to make laws.",

"Article 163: Council of Ministers to aid and advise Governor": "It establishes the Council of Ministers in the State government and specifies their duty to aid and advise the Governor in the exercise of his functions.",

"Article 164: Other provisions as to Ministers": "Article 164 outlines various provisions regarding the appointment, tenure, and responsibilities of Ministers in a State government.",

"Article 165: Advocate General for the State": "This article defines the role and duties of the Advocate General for the State, who is the chief legal advisor to the State government.",

"Article 166: Conduct of business of the Government of a State": "Article 166 deals with the conduct of government business in a State and the allocation of responsibilities among various authorities.",

"Article 167: Duties of Chief Minister as respects the furnishing of information to Governor, etc.": "Article 167 describes the Chief Minister's duties in furnishing information to the Governor regarding the administration of affairs of the State.",

"Article 168: Constitution of Legislatures in States": "It lays down the structure of the State Legislatures, which consist of the Governor and two Houses, the Legislative Council and the Legislative Assembly.",

"Article 169: Abolition or creation of Legislative Councils in States": "Article 169 empowers the Parliament to abolish or create Legislative Councils in States.",

"Article 170: Composition of the Legislative Assemblies": "Article 170 specifies the composition of the Legislative Assembly of States, including the allocation of seats to various categories.",

"Article 171: Composition of the Legislative Councils": "It outlines the composition of the Legislative Councils of States, including the allocation of seats to various categories.",

"Article 172: Duration of State Legislatures": "Article 172 sets the duration of the Legislative Assembly and Legislative Council of States, with a maximum term of five years.",

"Article 173: Qualifications for membership of the State Legislature": "It specifies the qualifications required for a person to become a member of the Legislative Assembly or Legislative Council of a State.",

"Article 174: Sessions of the State Legislature, prorogation and dissolution": "Article 174 addresses the convening, prorogation, and dissolution of sessions of the State Legislature.",

"Article 175: Right of Governor to address and send messages to the Houses": "It grants the Governor the right to address and send messages to the Legislative Assembly and Legislative Council of a State.",

"Article 176: Special address by the Governor": "Article 176 allows the Governor to address both Houses of the State Legislature together or separately.",

"Article 177: Rights of Ministers and Advocate General as respects the Houses": "It outlines the rights of Ministers and the Advocate General to speak in and otherwise participate in the proceedings of the State Legislature.",

"Article 178: Vacation of seats": "Article 178 deals with the vacation of seats by members of the State Legislature.",

"Article 179: Vacation of seats of members elected on more than one seat": "It specifies that members elected to more than one seat in the State Legislature must vacate the extra seat.",

"Article 180: Powers, privileges, etc., of the Houses of the State Legislature and of the members and committees thereof": "Article 180 grants powers and privileges to the Houses of the State Legislature, members, and their committees.",

"Article 181: Oath or affirmation by members": "Article 181 mandates that members of the State Legislature must take an oath or affirmation before assuming their office.",

"Article 182: Voting in Houses, power of Houses to act notwithstanding vacancies and quorum": "Article 182 sets rules for voting in the State Legislature, its ability to function despite vacancies, and the quorum required for its proceedings.",

"Article 183: Vacation of seats": "It specifies the conditions under which members of the State Legislature shall vacate their seats.",

"Article 184: Disqualifications for membership": "Article 184 outlines disqualifications for membership in the State Legislature."

}


def get_article_summary(article_prefix):
    for key in articles_and_summaries:
        if key.startswith(article_prefix):
            return [key,articles_and_summaries[key]]
    return "Article not found."

