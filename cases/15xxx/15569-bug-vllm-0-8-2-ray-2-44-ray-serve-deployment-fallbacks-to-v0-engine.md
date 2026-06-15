# vllm-project/vllm#15569: [Bug]: Vllm 0.8.2 + Ray 2.44 (Ray serve deployment) fallbacks to V0 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#15569](https://github.com/vllm-project/vllm/issues/15569) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm 0.8.2 + Ray 2.44 (Ray serve deployment) fallbacks to V0 Engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying vllm 0.8.2 with ray 2.44.0 , vllm falls back to V0. Logs from ray serve deployment: ![Image](https://github.com/user-attachments/assets/1663f5d7-c53d-448e-b778-334a68ad857b) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Vllm 0.8.2 + Ray 2.44 (Ray serve deployment) fallbacks to V0 Engine bug;ray;stale ### Your current environment ### 🐛 Describe the bug When deploying vllm 0.8.2 with ray 2.44.0 , vllm falls back to V0. Logs from r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 7b) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m 0.8.2 + Ray 2.44 (Ray serve deployment) fallbacks to V0 Engine bug;ray;stale ### Your current environment ### 🐛 Describe the bug When deploying vllm 0.8.2 with ray 2.44.0 , vllm falls back to V0. Logs from ray serve d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
