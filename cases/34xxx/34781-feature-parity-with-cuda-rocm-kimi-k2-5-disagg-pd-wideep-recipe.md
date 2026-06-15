# vllm-project/vllm#34781: [Feature]: parity with cuda - ROCm Kimi K2.5 disagg PD +wideEP recipe

| 字段 | 值 |
| --- | --- |
| Issue | [#34781](https://github.com/vllm-project/vllm/issues/34781) |
| 状态 | open |
| 标签 | feature request;rocm;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: parity with cuda - ROCm Kimi K2.5 disagg PD +wideEP recipe

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 on CUDA, vLLM disagg PD + wideEP, there is already vLLM recipes for disagg PD+wideEP but unfortunately there is no similar recipes for MoE models on ROCm - https://github.com/minosfuture/vllm/tree/pd_gb200_0114/runs/DS-R1/fp4 - https://github.com/vllm-project/vllm/issues/33583 - https://blog.vllm.ai/2025/12/17/large-scale-serving.html I see that it is on the Q1 2026 roadmap for ROCm but there is only a couple more weeks of Q1 2026 and yet we don't see any recipes. Any help in pritotizing this would be appreicpated! - https://github.com/vllm-project/vllm/issues/32455 ### Alternatives use single node which is not good for large MoE models ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: parity with cuda - ROCm Kimi K2.5 disagg PD +wideEP recipe feature request;rocm;unstale ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 on CUDA, vLLM disagg PD + wideEP, there is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ROCm - https://github.com/minosfuture/vllm/tree/pd_gb200_0114/runs/DS-R1/fp4 - https://github.com/vllm-project/vllm/issues/33583 - https://blog.vllm.ai/2025/12/17/large-scale-serving.html I see that it is on the Q1 2026...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: parity with cuda - ROCm Kimi K2.5 disagg PD +wideEP recipe feature request;rocm;unstale ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 on CUDA, vLLM disagg PD + wideEP, there is alrea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: parity with cuda - ROCm Kimi K2.5 disagg PD +wideEP recipe feature request;rocm;unstale ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 on CUDA, vLLM disagg PD + wideEP, there is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r disagg PD+wideEP but unfortunately there is no similar recipes for MoE models on ROCm - https://github.com/minosfuture/vllm/tree/pd_gb200_0114/runs/DS-R1/fp4 - https://github.com/vllm-project/vllm/issues/33583 - https...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
