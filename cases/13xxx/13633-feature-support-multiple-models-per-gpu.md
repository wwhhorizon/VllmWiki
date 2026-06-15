# vllm-project/vllm#13633: [Feature]: Support multiple models per GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#13633](https://github.com/vllm-project/vllm/issues/13633) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multiple models per GPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Sometimes, you have e.g. H100s or ML300xs, but you want to host inference for small language models (SLMs). You might want to host anywhere from 2-5 of these models per GPU. Maybe they are different architectures, but maybe they are merely different full finetunes for the same model, or different lora finetunes for the same model. VLLM does not appear to support any of these modes today: 1. Serving multiple independent LoRA finetunes for one model (one VLLM service) 2. Serving multiple full finetunes for one model (one VLLM service) 3. Serving multiple models on the same GPU (i.e. independent VLLM services) IMO this is somewhat surprising for a user of VLLM. Why is it surprising? VLLM exposes several APIs: the engine arguments, the openai API: A. In the openai API, there is a models endpoint, but this is always a single model. B. In the engine arguments, there is a gpu-memory-utilization parameter, which suggests that the GPU could be divided across VLLM services. A and B aren't some existential tragedy, but they are somewhat counterintuitive. In fact, there have been several conversations where users are surprised about these aspects of VLL...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ;stale ### 🚀 The feature, motivation and pitch Sometimes, you have e.g. H100s or ML300xs, but you want to host inference for small language models (SLMs). You might want to host anywhere from 2-5 of these models per GPU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support multiple models per GPU feature request;stale ### 🚀 The feature, motivation and pitch Sometimes, you have e.g. H100s or ML300xs, but you want to host inference for small language models (SLMs). You mi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: PU, but this is relatively wasteful if the traffic to the service is anticipated to be relatively small compared to the GPU's capacity. One might say "host on smaller GPUs", but in practice you often have the GPUs you'v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support multiple models per GPU feature request;stale ### 🚀 The feature, motivation and pitch Sometimes, you have e.g. H100s or ML300xs, but you want to host inference for small language models (SLMs). You mi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
