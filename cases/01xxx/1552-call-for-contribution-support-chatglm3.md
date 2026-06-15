# vllm-project/vllm#1552: Call for Contribution: Support ChatGLM3

| 字段 | 值 |
| --- | --- |
| Issue | [#1552](https://github.com/vllm-project/vllm/issues/1552) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Call for Contribution: Support ChatGLM3

### Issue 正文摘录

Hi vLLM community, We are aware of the enthusiasm ([https://github.com/vllm-project/vllm/issues/247](https://github.com/vllm-project/vllm/issues/247) [https://github.com/vllm-project/vllm/issues/231](https://github.com/vllm-project/vllm/issues/231)) to add support for ChatGLM model. However, the team is currently overwhelmed by other higher priorities work like improving latency and enhance quantization. Currently, there are total of five stale PRs, each in different states, none of them are mergable. [https://github.com/vllm-project/vllm/pull/1477](https://github.com/vllm-project/vllm/pull/1477) [https://github.com/vllm-project/vllm/pull/1261](https://github.com/vllm-project/vllm/pull/1261) [https://github.com/vllm-project/vllm/pull/1109](https://github.com/vllm-project/vllm/pull/1109) [https://github.com/vllm-project/vllm/pull/649](https://github.com/vllm-project/vllm/pull/649) [https://github.com/vllm-project/vllm/pull/625](https://github.com/vllm-project/vllm/pull/625) I believe we can directly support [https://github.com/THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3). We are looking for people who can help us take the model to completion. We will do our best in reviewing...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is currently overwhelmed by other higher priorities work like improving latency and enhance quantization. Currently, there are total of five stale PRs, each in different states, none of them are mergable. [https://githu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: elmed by other higher priorities work like improving latency and enhance quantization. Currently, there are total of five stale PRs, each in different states, none of them are mergable. [https://github.com/vllm-project/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: bution: Support ChatGLM3 Hi vLLM community, We are aware of the enthusiasm ([https://github.com/vllm-project/vllm/issues/247](https://github.com/vllm-project/vllm/issues/247) [https://github.com/vllm-project/vllm/issues...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s://github.com/vllm-project/vllm/issues/231)) to add support for ChatGLM model. However, the team is currently overwhelmed by other higher priorities work like improving latency and enhance quantization. Currently, ther...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng latency and enhance quantization. Currently, there are total of five stale PRs, each in different states, none of them are mergable. [https://github.com/vllm-project/vllm/pull/1477](https://github.com/vllm-project/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
