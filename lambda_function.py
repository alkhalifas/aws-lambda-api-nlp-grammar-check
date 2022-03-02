import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

def lambda_handler(event, context):
    matches = tool.check(event["content"])
    return matches
