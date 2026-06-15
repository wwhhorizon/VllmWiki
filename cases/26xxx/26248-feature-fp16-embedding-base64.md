# vllm-project/vllm#26248: [Feature]: FP16 Embedding Base64

| 字段 | 值 |
| --- | --- |
| Issue | [#26248](https://github.com/vllm-project/vllm/issues/26248) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FP16 Embedding Base64

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We use embedding models through the OpenAI interface. The models generate FP16 vectors, but the Base64 response is always FP32, which doubles the bandwidth and memory consumption. If vLLM returns the vector in its original form, we can reduce the bandwidth and save the received Base64 bytes into our vector database without converting them. I think this is useful for anyone working with large volumes of vectors in batch mode. Thanks. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eature request ### 🚀 The feature, motivation and pitch We use embedding models through the OpenAI interface. The models generate FP16 vectors, but the Base64 response is always FP32, which doubles the bandwidth and memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: FP16 Embedding Base64 feature request ### 🚀 The feature, motivation and pitch We use embedding models through the OpenAI interface. The models generate FP16 vectors, but the Base64 response is always FP32, wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
