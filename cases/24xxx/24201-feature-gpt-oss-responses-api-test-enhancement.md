# vllm-project/vllm#24201: [Feature][gpt-oss] Responses API test enhancement

| 字段 | 值 |
| --- | --- |
| Issue | [#24201](https://github.com/vllm-project/vllm/issues/24201) |
| 状态 | closed |
| 标签 | feature request;stale;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][gpt-oss] Responses API test enhancement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current gpt-oss test only ensures that the workflow doesn't crash. It doesn't have correctness check. Help wanted on making the test more strict to avoid regression. https://github.com/vllm-project/vllm/blob/main/tests/entrypoints/openai/test_response_api_with_harmony.py When implementing it, please make sure the tests are not flaky. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][gpt-oss] Responses API test enhancement feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Current gpt-oss test only ensures that the workflow doesn't crash. It doesn't have correctness chec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature][gpt-oss] Responses API test enhancement feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Current gpt-oss test only ensures that the workflow doesn't crash. It doesn't have correctness chec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature][gpt-oss] Responses API test enhancement feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Current gpt-oss test only ensures that the workflow doesn't crash. It doesn't have correctness chec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
