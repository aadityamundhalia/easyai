# import autogen

# config_list = [
#     {
#         'model': 'gpt-3.5-turbo-16k',
#         # 'model': 'gpt-4',
#         'api_key': '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'
#     }
# ]

# llm_config = {
#     "request_timeout": 600,
#     "seed": 42,
#     "config_list": config_list,
#     "temperature": 0
# }

# assistant = autogen.AssistantAgent(
#     name="assistant",
#     llm_config=llm_config,
#     # system_message=""
# )

# user_proxy = autogen.UserProxyAgent(
#     name="user_proxy",
#     human_input_mode="TERMINATE",
#     max_consecutive_auto_reply=10,
#     is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
#     code_execution_config={"work_dir": "web"},
#     llm_config=llm_config,
#     system_message="""Reply TERMINATE if the task has been solved at full
#      satisfaction. Otherwise, reply CONTINUE, or the reason why the task is
#      not solved yet."""
# )

# task = """
# write python code to output numbers 1 to 100, and store it in a file
# """

# user_proxy.initiate_chat(
#     assistant,
#     message=task
# )