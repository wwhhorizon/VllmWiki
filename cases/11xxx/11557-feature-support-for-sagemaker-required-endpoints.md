# vllm-project/vllm#11557: [Feature]: Support for SageMaker-required endpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#11557](https://github.com/vllm-project/vllm/issues/11557) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for SageMaker-required endpoints

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This was [discussed before](https://github.com/vllm-project/vllm/issues/2592) and was not supported due to AWS needing to manage the images. I'm wondering if there is interest in at least including routing sourcecode for the required SageMaker endpoints (`/invocations` and `/ping`) to the vLLM source. The main benefit would be the standard openai vLLM image should be automatically compatible with SageMaker endpoints. Currently, interested users have to do so through LMI, or fork vLLM and add these. If there is interest and support from vLLM maintainers, I'm happy to contribute this to the [openai entrypoints](vllm/entrypoints/openai/api_server.py): * a `ping` endpoint rerouting to `/health` * an `invocations` endpoint that routes to the expected existing endpoint (or with an additional parameter so the user dictates the target) My understanding is that these are the only two requirements for SageMaker support. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ge the images. I'm wondering if there is interest in at least including routing sourcecode for the required SageMaker endpoints (`/invocations` and `/ping`) to the vLLM source. The main benefit would be the standard ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ge the images. I'm wondering if there is interest in at least including routing sourcecode for the required SageMaker endpoints (`/invocations` and `/ping`) to the vLLM source. The main benefit would be the standard ope...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for SageMaker-required endpoints feature request ### 🚀 The feature, motivation and pitch This was [discussed before](https://github.com/vllm-project/vllm/issues/2592) and was not supported due to AWS...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
