#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openai==0.28


# In[2]:


get_ipython().run_line_magic('env', 'OPENAI_API_KEY=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')


# In[3]:


import os
import openai
import wandb


openai.api_key = os.getenv("OPENAI_API_KEY")


# In[6]:


gpt_prompt = """
Imagine that you are an MBA student at Stanford University. Your task is to evaluate how urgent someone should respond to a message.

Instructions for evaluating urgency from most important to least important:
1. Find how frequently words like ASAP, urgent, soon, immediately, promptly, and similar appear in the message. If they appear, the message should be responded to urgently.
2. If there are any deadlines, mark the message as urgent.
3. If there are any words like assignment, meeting, schedule, etc. the message should be marked urgent.
4. If any times are mentioned, mark the message as urgent.

Output: urgency (one hour, couple hours, one day, a couple days, one week, a couple weeks, one month, never) as well as the reasoning as to how you determined this.

Message: I am creating as final a version of the program plan as I can now. James, maybe you and I can touch base later in today about all the other docs and make a final todo for Tony
Reasoning: This message has a sence of urgency as it mentions that the sender wants to talk to the recipient today. The content is also interesting as it is related to tech. This makes it sound like there is a sence of urgency.
Expected output: one hour
####################
Message: The 'advisory timeline' figure is also a potential space-suck.
Reasoning: This message mentions no time or immediate request for RSVP. Additionally, there is no sense of urgency as there are no words like “now” in the message. 
Expected output: one week
###################
Message: Our podcast, <http:\/\/neuronspodcast.com|From Our Neurons to Yours>, is back this week with a fantastic conversation with Jaimie Henderson about the state of the art in brain-computer interfaces for patients with neurological injury and reflections Krishna Shenoy's outsize impact on the field. Season 3 drops Thursday morning \u2013 don't miss it
Output: 
"""

response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=300,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)


print(response['choices'][0]['text'])


# In[7]:


gpt_prompt = """
Imagine that you are an MBA student at Stanford University. Your task is to evaluate how urgent someone should respond to a message.

Instructions for evaluating urgency from most important to least important.:
1. Find how frequently words like ASAP, urgent, soon, immediately, promptly, and similar appear in the message. If they appear, the message should be responded to urgently.
2. If there are any deadlines, mark the message as urgent.
3. If there are any words like assignment, meeting, schedule, etc. the message should be marked urgent.
4. If any times are mentioned, mark the message as urgent.

Output: urgency (one hour, couple hours, one day, a couple days, one week, a couple weeks, one month, never) as well as the reasoning as to how you determined this.

Message: the line spacing on faculty profiles seems awfully wide. Also the pipes \"|\" on working papers don't look quite right
Reasoning: This message is not urgent as there are no direct action items and no timelines. Thus, there is no sense of urgency.
Expected output: couple days
####################
Message: Hey All!\ For session 2 on Demystifying AI, we will cover Generative AI and LLMs.\nPlease indicate your comfort level with these topics\nand expectations from the session, on the google form. Session 2 Details: RSVP : <https:\/\/forms.gle\/psMzLLbbHosmuXwFA|Fill the form to get a google invite.
Reasoning: This message is urgent because it is suggesting that one should register for an event. It mentions a deadline for the registeration.
Expected output: couple hours
###################
Message: Is anyone interested in doing electrophysiology on pig tissue on 2\/8? If so, we will work with VSC staffs to fasten the enuc process as soon as possible after postmortem.
Output: 
"""


response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=300,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response['choices'][0]['text'])


# In[11]:


gpt_prompt = """
Imagine that you are an MBA student at Stanford University. Your task is to evaluate how urgent someone should respond to a message.

Instructions for evaluating urgency from most important to least important.:
1. Find how frequently words like ASAP, urgent, soon, immediately, promptly, and similar appear in the message. If they appear, the message should be responded to urgently.
2. If there are any deadlines, mark the message as urgent.
3. If there are any words like assignment, meeting, schedule, etc. the message should be marked urgent.
4. If any times are mentioned, mark the message as urgent.

Output: urgency (one hour, couple hours, one day, a couple days, one week, a couple weeks, one month, never) as well as the reasoning as to how you determined this.

Message: Thursday we will be hearing from *Ian Huang* at 12:15 pm in *Packard 202.* As usual, food will be out a little earlier. Please find the abstract below.\n\n*Abstract:* Recent advancements in Large Language Models (LLMs) have demonstrated their capability to function as common-sense reasoning modules.
Reasoning: This message is fairly urgent as it is notifying the user about an event that is happening soon, specifically today. It also has a sense of urgency surround it.
Expected output: one hour
####################
Message: Stanford Administrative Champions Introductory Meeting_\n\nJoin SAC's intro meeting <https:\/\/medwiki.stanford.edu\/x\/_4WgCQ|scheduled for Feb 1> and learn about the team.\n\u2022 What we're working on\n\u2022 SAC Structure: Committees and Core Team\n\u2022 SAC Successes\n\u2022 Resources\nAnd learn how _*you*_ can get involved! :teamwork_:
Reasoning:This message is not urgent as there are no words indicating an upcoming deadline. There is no sense of urgency as no words like "asap" and "today" are present. Thus, it is not urgent. There are no months mentioned as well.
Expected output: one day
###################
Message: Hi Frans! Girl Scout Cookie season is upon us! Boxes are $6 a box and delivery starts early February ASAP. You can place your orders online and those of us participating can deliver to the building. (Scout parents, feel free to post your girl's cookie link below in the thread!)  :cookie: :cookie_blob:
Output:
"""

response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=300,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response['choices'][0]['text'])


# In[ ]:




