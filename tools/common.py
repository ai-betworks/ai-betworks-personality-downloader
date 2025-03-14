from langchain_anthropic import ChatAnthropic

def default_llm():
    return ChatAnthropic(
        model="claude-3-5-haiku-20241022",
        # model="claude-3-5-sonnet-20241022",
        temperature=0,
    )

def reduce_dict_merge(left: dict | None, right: dict | None) -> dict:
    """merge two dicts, handling cases where either or both inputs might be None"""
    if not left:
        left = {}
    if not right:
        right = {}
    return {**left, **right}

