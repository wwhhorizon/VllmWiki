# vllm-project/vllm#20869: [Feature]: TPU Embedding models support?

| 字段 | 值 |
| --- | --- |
| Issue | [#20869](https://github.com/vllm-project/vllm/issues/20869) |
| 状态 | closed |
| 标签 | feature request;tpu;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: TPU Embedding models support?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi I want to run latest Embedding models, eg `Qwen/Qwen3-Embedding-0.6B`, on TPU nodes. I found that although vLLM has support on TPU it does not really support embedding models since the only available attention implementation on TPU is `PALLAS` which is DECODER only. https://github.com/vllm-project/vllm/blob/99b4f080d83ae284941b01922d7fe3b9a39034fd/vllm/v1/attention/backends/pallas.py#L164-L168 Meanwhile, Qwen3 Embedding is ENCODER-only so it can't run on TPU. https://github.com/vllm-project/vllm/blob/99b4f080d83ae284941b01922d7fe3b9a39034fd/vllm/model_executor/models/qwen3.py#L166-L173 It will be nice if we can support Qwen3 Embedding on TPU, ### Alternatives I am trying to use Qwen3 Embedding via `transformers` but it's not as performant as vLLM. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: TPU Embedding models support? feature request;tpu;stale ### 🚀 The feature, motivation and pitch Hi I want to run latest Embedding models, eg `Qwen/Qwen3-Embedding-0.6B`, on TPU nodes. I found that although vL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: TPU Embedding models support? feature request;tpu;stale ### 🚀 The feature, motivation and pitch Hi I want to run latest Embedding models, eg `Qwen/Qwen3-Embedding-0.6B`, on TPU nodes. I found that although vL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ect/vllm/blob/99b4f080d83ae284941b01922d7fe3b9a39034fd/vllm/v1/attention/backends/pallas.py#L164-L168 Meanwhile, Qwen3 Embedding is ENCODER-only so it can't run on TPU. https://github.com/vllm-project/vllm/blob/99b4f080...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: st;tpu;stale ### 🚀 The feature, motivation and pitch Hi I want to run latest Embedding models, eg `Qwen/Qwen3-Embedding-0.6B`, on TPU nodes. I found that although vLLM has support on TPU it does not really support embed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
