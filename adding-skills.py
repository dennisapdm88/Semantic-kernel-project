import asyncio
import semantic_kernel as sk

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion

kernel = sk.Kernel()

useAzureOpenAI = False

if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_text_completion_service("azureopenai", AzureChatCompletion(deployment, endpoint, api_key))
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("openai", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

print("A kernel is now ready.")   

from semantic_kernel.planning import ActionPlanner

planner = ActionPlanner(kernel)

from semantic_kernel.core_skills import FileIOSkill, MathSkill, TextSkill, TimeSkill
kernel.import_skill(MathSkill(), "math")
kernel.import_skill(FileIOSkill(), "fileIO")
kernel.import_skill(TimeSkill(), "time")
kernel.import_skill(TextSkill(), "text")

print("Adding the tools for the kernel to do math, to read/write files, to tell the time, and to play with text.")

async def main():
    ask = "What is the sum of 110 and 990?"

    print(f"🧲 Finding the most similar function available to get that done...")
    plan = await planner.create_plan_async(goal=ask)
    print(f"🧲 The best single function to use is `{plan._skill_name}.{plan._function.name}`")

    ask = "What is today?"
    print(f"🧲 Finding the most similar function available to get that done...")
    plan = await planner.create_plan_async(goal=ask)
    print(f"🧲 The best single function to use is `{plan._skill_name}.{plan._function.name}`")

    ask = "How do I write the word 'text' to a file?"
    print(f"🧲 Finding the most similar function available to get that done...")
    plan = await planner.create_plan_async(goal=ask)
    print(f"🧲 The best single function to use is `{plan._skill_name}.{plan._function.name}`")




asyncio.run(main())