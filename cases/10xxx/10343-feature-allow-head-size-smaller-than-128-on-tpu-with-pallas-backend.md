# vllm-project/vllm#10343: [Feature]: Allow head_size smaller than 128 on TPU with Pallas backend

| 字段 | 值 |
| --- | --- |
| Issue | [#10343](https://github.com/vllm-project/vllm/issues/10343) |
| 状态 | closed |
| 标签 | feature request;tpu |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow head_size smaller than 128 on TPU with Pallas backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like to serve smaller models (e.g facebook/opt-125m) using VLLM on TPU. I can't do this currently because the Pallas backend has the limitation `NotImplementedError: Head size must be a multiple of 128`. I can't find a reason why this limitation is in place, and it would be great to be able to remove it with a flag or entirely. If my understanding is incorrect and there is a reason to have this limitation in place, please let me know! Thanks for your work on VLLM. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Allow head_size smaller than 128 on TPU with Pallas backend feature request;tpu ### 🚀 The feature, motivation and pitch I would like to serve smaller models (e.g facebook/opt-125m) using VLLM on TPU. I can't...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Allow head_size smaller than 128 on TPU with Pallas backend feature request;tpu ### 🚀 The feature, motivation and pitch I would like to serve smaller models (e.g facebook/opt-125m) using VLLM on TPU. I can't...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: u ### 🚀 The feature, motivation and pitch I would like to serve smaller models (e.g facebook/opt-125m) using VLLM on TPU. I can't do this currently because the Pallas backend has the limitation `NotImplementedError: Hea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re]: Allow head_size smaller than 128 on TPU with Pallas backend feature request;tpu ### 🚀 The feature, motivation and pitch I would like to serve smaller models (e.g facebook/opt-125m) using VLLM on TPU. I can't do thi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
