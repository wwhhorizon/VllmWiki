# vllm-project/vllm#17357: [Bug]:   The qwen3 235B model is deployed through vllm. When enable_thinking is False, the returned content is empty, but reason_content has a value

| 字段 | 值 |
| --- | --- |
| Issue | [#17357](https://github.com/vllm-project/vllm/issues/17357) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:   The qwen3 235B model is deployed through vllm. When enable_thinking is False, the returned content is empty, but reason_content has a value

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **The qwen3 235B model is deployed through vllm. When enable_thinking is False, the returned content is empty, but reason_content has a value** ```python from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "Bearer skxx" openai_api_base = "http://10.24xx:8009/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) chat_response = client.chat.completions.create( model="qwen3-235b-a22b", messages=[ {"role": "user", "content": "9.9和9.11哪个大？"}, ], temperature=0.7, extra_body={"chat_template_kwargs": {"enable_thinking": False}}, ) print("Chat response:", chat_response) ``` ### **output** `Chat response: ChatCompletion(id='chatcmpl-b5f737ea218d45db9107e5c7c943ac06', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content='我们来一步一步地进行比较：\n\n---\n\n### 第一步：比较整数部分\n\n- **9.9** 的整数部 分是 **9** \n- **9.11** 的整数部分也是 **9**\n\n所以，**整数部分相等**，我们继续比较小数部分。\n\n---\n\n### 第二步：比较小数部分\n\n我们分别来看两位小数：\n\n| 数值 | 小数部分第一位 | 小数部分第...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The qwen3 235B model is deployed through vllm. When enable_thinking is False, the returned content is empty, but reason_content has a value bug;stale ### Your current environment ### 🐛 Describe the bug **The qwen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ntent is empty, but reason_content has a value** ```python from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "Bearer skxx" openai_api_base = "http://10.24xx:8009/v1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ) ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: The qwen3 235B model is deployed through vllm. When enable_thinking is False, the returned content is empty, but reason_content has a value bug;stale ### Your current environment ### 🐛 Describe the bug **The qwen3 235B...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: False, the returned content is empty, but reason_content has a value bug;stale ### Your current environment ### 🐛 Describe the bug **The qwen3 235B model is deployed through vllm. When enable_thinking is False, the retu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
