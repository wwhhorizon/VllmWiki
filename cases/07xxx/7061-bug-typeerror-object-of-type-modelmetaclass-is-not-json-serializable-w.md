# vllm-project/vllm#7061: [Bug]: TypeError: Object of type ModelMetaclass is not JSON serializable when using guided decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#7061](https://github.com/vllm-project/vllm/issues/7061) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: Object of type ModelMetaclass is not JSON serializable when using guided decoding

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug class AnswerFormat(BaseModel): query: str emotion: str def qwen2(coontent): from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) model = 'Qwen2-72B-Instruct-awq' prompt = """ Classify emotion among positive, negative, neutral. query:打造装备神火被吞。 emotion:neutral ------------------- query:好的，明白了。 emotion:positive ------------------- query:你这不是坑人嘛。 emotion:negative query:{query} emotion: """ prompt = prompt.replace("{query}",coontent) chat_completion = client.chat.completions.create( messages=[{ "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": prompt }], model=model, extra_body={ "guided_json": [AnswerFormat], "guided_decoding_backend": "lm-format-enforcer" } ) print("Chat completion results:") print(chat_completion.choices[0].message.content) return chat_completion.choices[0].message.content qwen2('游戏维护期间能玩吗？')

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TypeError: Object of type ModelMetaclass is not JSON serializable when using guided decoding bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug class A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: "guided_json": [AnswerFormat], "guided_decoding_backend": "lm-format-enforcer" } ) print("Chat completion results:") print(chat_completion.choices[0].message.content) return chat_completion.choices[0].message.content qw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ): query: str emotion: str def qwen2(coontent): from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) model = 'Qwen2-72B-Instruct-aw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e ModelMetaclass is not JSON serializable when using guided decoding bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug class AnswerFormat(BaseModel): query:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
