# vllm-project/vllm#24067: [Bug]: how to get purely deterministic output for gpt-oss-120b?

| 字段 | 值 |
| --- | --- |
| Issue | [#24067](https://github.com/vllm-project/vllm/issues/24067) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: how to get purely deterministic output for gpt-oss-120b?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using vllm v0.10.1 to serve "openai/gpt-oss-120b". I need to get purely deterministic output. (Same input shall get exactly same output). I found following ticket: https://huggingface.co/openai/gpt-oss-20b/discussions/23 But I still can't get deterministic output even with following configuration: ``` "seed": 42, # should be a very large number? "temperature": 0, "n": 1, "top_p": 0.01, # top_p must be in (0, 1] "extra_body": { "top_k": 1, "min_p": 1, "repeat_penalty": 1, }, ``` Could you please help to guide me? Is it possible to get purely deterministic output via vllm v0.10.1 + "openai/gpt-oss-120b"? If Yes, could you please help to provide the parameter for openai client? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: how to get purely deterministic output for gpt-oss-120b? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I'm using vllm v0.10.1 to serve "openai/gpt-oss-120b". I need to get purely determini...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: how to get purely deterministic output for gpt-oss-120b? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I'm using vllm v0.10.1 to serve "openai/gpt-oss-120b". I need to get purely determini...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: how to get purely deterministic output for gpt-oss-120b? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I'm using vllm v0.10.1 to serve "openai/gpt-oss-120b". I need to get purely determini...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: how to get purely deterministic output for gpt-oss-120b? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I'm using vllm v0.10.1 to serve "openai/gpt-oss-120b". I need to get purely determini...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
