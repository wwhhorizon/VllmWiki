# vllm-project/vllm#24637: [Bug]: GPT-OSS Responses API: Incomplete Output When Using Function-Call

| 字段 | 值 |
| --- | --- |
| Issue | [#24637](https://github.com/vllm-project/vllm/issues/24637) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS Responses API: Incomplete Output When Using Function-Call

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug --- ``` { "arguments": "{\"numbers\":[{\"number\":\"1\"},{\"number\":\"2\"},{\"number\":\"3\"},{\"number\":\"4\"}]}", "call_id": "call_c2fa810793ba4b79abd260a109f99413", "name": "calculator", "type": "function_call", "id": "fc_c2fa810793ba4b79abd260a109f99413", "status": null } ``` I notice that vLLM only outputs one function call `calculator`, while the OpenAI online service consistently outputs two function calls. Openai online: ``` { "arguments": "{\"numbers\":[{\"number\":\"1\"},{\"number\":\"2\"},{\"number\":\"3\"},{\"number\":\"4\"}]}", "call_id": "call_uoNPQZhpWh9UGfDsPeNBPFve", "name": "calculator", "type": "function_call", "id": "fc_68c24c05ed908194a601a73509c9682d0c397773300e01d1", "status": "completed" }, { "arguments": "{\"city\":\"San Francisco\",\"country\":\"United States\",\"unit\":\"fahrenheit\"}", "call_id": "call_MA6p89zmObpC9oxIWECfLaJu", "name": "get_current_weather", "type": "function_call", "id": "fc_68c24c06272081948ba948d816af9b890c397773300e01d1", "status": "completed" } ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0e01d1", "status": "completed" }, { "arguments": "{\"city\":\"San Francisco\",\"country\":\"United States\",\"unit\":\"fahrenheit\"}", "call_id": "call_MA6p89zmObpC9oxIWECfLaJu", "name": "get_current_weather", "type": "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: GPT-OSS Responses API: Incomplete Output When Using Function-Call bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug --- ``` { "arguments": "{\"numbers\":[{\"number\":\"1\"},{\"num
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: GPT-OSS Responses API: Incomplete Output When Using Function-Call bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug --- ``` { "arguments": "{\"numbers\":[{\"number\":\"1\"},{\"number\":\"2\"},{\"n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
