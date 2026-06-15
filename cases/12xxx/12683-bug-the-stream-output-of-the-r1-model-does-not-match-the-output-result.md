# vllm-project/vllm#12683: [Bug]: The stream output of the R1 model does not match the output results of the official DeepSeek API.

| 字段 | 值 |
| --- | --- |
| Issue | [#12683](https://github.com/vllm-project/vllm/issues/12683) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The stream output of the R1 model does not match the output results of the official DeepSeek API.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM: ``` data: {"id":"chatcmpl-62486dd022194f4480a1036d7651eb56","object":"chat.completion.chunk","created":1738568539,"model":"deepseek-r1-70b","choices":[{"index":0,"delta":{"reasoning_content":"users"},"logprobs":null,"finish_reason":null}]} ``` Actually, the output example of DeepSeek API: ``` data: {"id":"4860a1de-8c50-47ff-9b8c-7c4f37f1002b","object":"chat.completion.chunk","created":1738568506,"model":"deepseek-reasoner","system_fingerprint":"fp_7e73fd9a08","choices":[{"index":0,"delta":{"content":null,"reasoning_content":"think"},"logprobs":null,"finish_reason":null}],"usage":null} ``` In fact, when the reasoning_content field exists, the content field at the same level should be null instead of directly deleting this field. This will help the upstream application layer do compatible processing more simply. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ream output of the R1 model does not match the output results of the official DeepSeek API. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM: ``` data: {"id":"chatcm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: The stream output of the R1 model does not match the output results of the official DeepSeek API. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM: ``` data:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: odel does not match the output results of the official DeepSeek API. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM: ``` data: {"id":"chatcmpl-62486dd022194f4480a1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
