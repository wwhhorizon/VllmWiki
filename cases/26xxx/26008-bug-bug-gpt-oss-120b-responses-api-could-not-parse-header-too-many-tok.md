# vllm-project/vllm#26008: [Bug]: [Bug] [gpt-oss-120b] [Responses API]: Could not parse header: too many tokens remaining after extracting content-type and recipient

| 字段 | 值 |
| --- | --- |
| Issue | [#26008](https://github.com/vllm-project/vllm/issues/26008) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Bug] [gpt-oss-120b] [Responses API]: Could not parse header: too many tokens remaining after extracting content-type and recipient

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug openai.APIError: Could not parse header: too many tokens remaining after extracting content-type and recipient My code: reasoning_model = ChatOpenAI( model=openai_model_name, temperature=0, max_tokens=None, timeout=None, max_retries=2, api_key="local", base_url=openai_model_url, http_async_client=httpx.AsyncClient(verify=False), http_client=httpx.Client(verify=False), reasoning_effort="medium", ) chain = querycheck_prompt | model ai_msg = chain.invoke({"messages": lc_messages, "task": task}) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [Bug] [gpt-oss-120b] [Responses API]: Could not parse header: too many tokens remaining after extracting content-type and recipient bug;stale ### Your current environment ### 🐛 Describe the bug openai.APIError: C...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: se header: too many tokens remaining after extracting content-type and recipient bug;stale ### Your current environment ### 🐛 Describe the bug openai.APIError: Could not parse header: too many tokens remaining after ext...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: k}) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e_url=openai_model_url, http_async_client=httpx.AsyncClient(verify=False), http_client=httpx.Client(verify=False), reasoning_effort="medium", ) chain = querycheck_prompt | model ai_msg = chain.invoke({"messages": lc_mes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oo many tokens remaining after extracting content-type and recipient bug;stale ### Your current environment ### 🐛 Describe the bug openai.APIError: Could not parse header: too many tokens remaining after extracting cont...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
