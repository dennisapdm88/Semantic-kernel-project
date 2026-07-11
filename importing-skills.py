import asyncio
from semantic_kernel.planning import SequentialPlanner
from semantic_kernel.core_skills.text_skill import TextSkill
from semantic_kernel.planning.sequential_planner.sequential_planner_config import SequentialPlannerConfig

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, OpenAITextEmbedding
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureTextEmbedding
from IPython.display import display, Markdown

kernel = sk.Kernel()

useAzureOpenAI = False

if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_text_completion_service("azureopenaicompletion", AzureChatCompletion(deployment, endpoint, api_key))
    kernel.add_text_embedding_generation_service("azureopenaiembedding", AzureTextEmbedding("text-embedding-ada-002", api_key, endpoint))
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("openaicompletion", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))
    kernel.add_text_embedding_generation_service("openaiembedding", OpenAITextEmbedding("text-embedding-ada-002", api_key, org_id))
print("I did it boss!")

from semantic_kernel.planning import ActionPlanner
from semantic_kernel.planning import SequentialPlanner

action_planner = ActionPlanner(kernel)

from semantic_kernel.core_skills import FileIOSkill, MathSkill, TextSkill, TimeSkill
kernel.import_skill(MathSkill(), "math")
kernel.import_skill(FileIOSkill(), "fileIO")
kernel.import_skill(TimeSkill(), "time")
kernel.import_skill(TextSkill(), "text")

print("Adding the tools for the kernel to do math, to read/write files, to tell the time, and to play with text.")

# Create SequentialPlanner before main()
seq_planner = SequentialPlanner(kernel, SequentialPlannerConfig(excluded_skills=["this"]))

async def main():
        
    ask = "What is the sum of 110 and 990?"

    print(f"🧲 Finding the most similar function available to get that done...")
    plan = await action_planner.create_plan_async(goal=ask)
    print(f"🧲 The best single function to use is `{plan._skill_name}.{plan._function.name}`")

    ask = "What is today?"
    print(f"🧲 Finding the most similar function available to get that done...")
    plan = await action_planner.create_plan_async(goal=ask)
    print(f"🧲 The best single function to use is `{plan._skill_name}.{plan._function.name}`")

    ask = "How do I write the word 'text' to a file?"
    print(f"🧲 Finding the most similar function available to get that done...")
    plan = await action_planner.create_plan_async(goal=ask)
    print(f"🧲 The best single function to use is `{plan._skill_name}.{plan._function.name}`")


    plugins_directory = "./plugins-sk"
    # writer_plugin = kernel.import_semantic_skill_from_directory(plugins_directory, "LiterateFriend")

    ask = """
    Tomorrow is Valentine's day. I need to come up with a poem. Translate the poem to French.
    """

    # plan = await seq_planner.create_plan_async(goal=ask)

    # result = await plan.invoke_async()

    # for index, step in enumerate(plan._steps):
    #     print(f"✅ Step {index+1} used function `{step._function.name}`")

    # trace_resultp = True

    # display(Markdown(f"## ✨ Generated result from the ask: {ask}\n\n---\n" + str(result)))

asyncio.run(main())