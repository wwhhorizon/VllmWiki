# vllm-project/vllm#8508: [Misc]: Speed of serving Starcoder models

| 字段 | 值 |
| --- | --- |
| Issue | [#8508](https://github.com/vllm-project/vllm/issues/8508) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Speed of serving Starcoder models

### Issue 正文摘录

### Anything you want to discuss about vllm. I used vLLM for serving different models and to my surprise, Starcoder seems to have a very low sequence/token: StarCoder2 15b --> input: 16.36 toks/s, output: 94.40 toks/s Llama-2-13b-chat-hf -> input: 227.97 toks/s, output: 116.06 toks/s Is there any reason why theres is thus huge gap? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Misc]: Speed of serving Starcoder models stale ### Anything you want to discuss about vllm. I used vLLM for serving different models and to my surprise, Starcoder seems to have a very low sequence/token: StarCoder2 15b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ap? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Speed of serving Starcoder models stale ### Anything you want to discuss about vllm. I used vLLM for serving different models and to my surprise, Starcoder seems to have a very low sequence/token: StarCoder2 15b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
