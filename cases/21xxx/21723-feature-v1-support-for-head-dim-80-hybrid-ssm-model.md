# vllm-project/vllm#21723: [Feature]: V1 support for head_dim 80 hybrid ssm model

| 字段 | 值 |
| --- | --- |
| Issue | [#21723](https://github.com/vllm-project/vllm/issues/21723) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: V1 support for head_dim 80 hybrid ssm model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now USE_VLLM_V1 only support flashinfer backend, but flashinfer backend cann't support head_dim 80 dims! We have a hybrid ssm model which head_dim 80 ### Alternatives Support other attention backend with Hybird model in V1 ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: le ### 🚀 The feature, motivation and pitch Now USE_VLLM_V1 only support flashinfer backend, but flashinfer backend cann't support head_dim 80 dims! We have a hybrid ssm model which head_dim 80 ### Alternatives Support o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: V1 support for head_dim 80 hybrid ssm model feature request;stale ### 🚀 The feature, motivation and pitch Now USE_VLLM_V1 only support flashinfer backend, but flashinfer backend cann't support head_dim 80 dim...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: V1 support for head_dim 80 hybrid ssm model feature request;stale ### 🚀 The feature, motivation and pitch Now USE_VLLM_V1 only support flashinfer backend, but flashinfer backend cann't support head_dim 80 dim...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: V1 support for head_dim 80 hybrid ssm model feature request;stale ### 🚀 The feature, motivation and pitch Now USE_VLLM_V1 only support flashinfer backend, but flashinfer backend cann't support head_dim 80 dim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
