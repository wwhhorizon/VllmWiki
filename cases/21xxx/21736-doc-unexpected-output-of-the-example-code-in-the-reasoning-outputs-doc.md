# vllm-project/vllm#21736: [Doc]: Unexpected output of the example code in the Reasoning Outputs document

| 字段 | 值 |
| --- | --- |
| Issue | [#21736](https://github.com/vllm-project/vllm/issues/21736) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Unexpected output of the example code in the Reasoning Outputs document

### Issue 正文摘录

### 📚 The doc issue When running the example code in the [Streaming chat completions section of the Reasoning Outputs document](https://docs.vllm.ai/en/latest/features/reasoning_outputs.html#streaming-chat-completions) using ibm-granite/granite-3.2-8b-instruct (with `thinking=True`). Code: ```Python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}] # For granite, add: `extra_body={"chat_template_kwargs": {"thinking": True}}` # For Qwen3 series, if you want to disable thinking in reasoning mode, add: # extra_body={"chat_template_kwargs": {"enable_thinking": False}} stream = client.chat.completions.create(model=model, messages=messages, stream=True) print("client: Start streaming chat completions...") printed_reasoning_content = False printed_content = False for chunk in stream: reasoning_content = None content = None # Check the content is reasoning_content or content if hasa...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: t things. But given the nature of the question, it appears to be a basic numerical comparison. The numbers 9.11 and 9.8 are both decimal numbers close to each other. To determine which is greater, we just need to compar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: te-3.2-8b-instruct (with `thinking=True`). Code: ```Python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}] # For granite, add: `ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g mode, add: # extra_body={"chat_template_kwargs": {"enable_thinking": False}} stream = client.chat.completions.create(model=model, messages=messages, stream=True) print("client: Start streaming chat completions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
