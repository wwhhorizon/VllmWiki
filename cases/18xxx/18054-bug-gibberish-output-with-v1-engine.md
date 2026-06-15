# vllm-project/vllm#18054: [Bug]: Gibberish output with v1 engine.

| 字段 | 值 |
| --- | --- |
| Issue | [#18054](https://github.com/vllm-project/vllm/issues/18054) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gibberish output with v1 engine.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried Qwen/Qwen2.5-14B-Instruct-AWQ and Qwen/Qwen2.5-32B-Instruct-AWQ. My prompt contained some json data and a text to summarize. With simple text only it worked, but as soon as introduced the json elements, v1 produced unreliable outputs. It randomly starts using chinese characters or just gibberish. Unfortunately due to privacy/legal reasons I can't share my prompt, but it seems to be a known problem as this huggingface issue states:[ v1 engine implementation doesn't calculate attention accurately, so some quality loss is expected](https://huggingface.co/ISTA-DASLab/gemma-3-27b-it-GPTQ-4b-128g/discussions/2#67df493f29e06976ae9d123b) Do you have it on your radar? The AI on the website returned the following related issues: [#12741](https://github.com/vllm-project/vllm/issues/12741) [#15533](https://github.com/vllm-project/vllm/issues/15533) [#16068](https://github.com/vllm-project/vllm/issues/16068) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g;stale ### Your current environment ### 🐛 Describe the bug I tried Qwen/Qwen2.5-14B-Instruct-AWQ and Qwen/Qwen2.5-32B-Instruct-AWQ. My prompt contained some json data and a text to summarize. With simple text only it w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 68) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ly, so some quality loss is expected](https://huggingface.co/ISTA-DASLab/gemma-3-27b-it-GPTQ-4b-128g/discussions/2#67df493f29e06976ae9d123b) Do you have it on your radar? The AI on the website returned the following rel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Gibberish output with v1 engine. bug;stale ### Your current environment ### 🐛 Describe the bug I tried Qwen/Qwen2.5-14B-Instruct-AWQ and Qwen/Qwen2.5-32B-Instruct-AWQ. My prompt contained some json data and a tex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
