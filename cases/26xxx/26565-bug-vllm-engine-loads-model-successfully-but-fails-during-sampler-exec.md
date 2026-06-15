# vllm-project/vllm#26565: [Bug]: vLLM engine loads model successfully but fails during sampler execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#26565](https://github.com/vllm-project/vllm/issues/26565) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM engine loads model successfully but fails during sampler execution.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # summary The vLLM engine first loads the model and then invokes the TopKTopPSampler to generate outputs. The sampler utilizes flashinfer.sampling as its backend implementation if the flashinfer import succeeds. However, successful import does not guarantee flashinfer's operational readiness, as it may fail during execution due to incompatible CUDA architectures. Flashinfer employs check_cuda_arch to verify that the architecture meets the minimum requirement of sm75. When running on older architectures like V100 (sm70), this results in a runtime exception. The significant time investment in model loading—7.56 seconds in our case—is consequently wasted. We should implement more granular pre-validation checks to confirm flashinfer's operational readiness before proceeding with model loading. In flashinfer, the check_cuda_arch() function fails with a runtime error on incompatible CUDA architectures. code snippet: https://github.com/flashinfer-ai/flashinfer/blob/c3ff7e76e67d7ca6875ed6137322eedf5c356f32/flashinfer/jit/core.py#L283-L292 # mini repro The bug can be reproduced by running any model on CUDA architectures below sm75 like v1...

## 现有链接修复摘要

#26566 [Bugfix] Check flashinfer availability using flashinfer.sampling.get_sampling_module

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: izes flashinfer.sampling as its backend implementation if the flashinfer import succeeds. However, successful import does not guarantee flashinfer's operational readiness, as it may fail during execution due to incompat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: en invokes the TopKTopPSampler to generate outputs. The sampler utilizes flashinfer.sampling as its backend implementation if the flashinfer import succeeds. However, successful import does not guarantee flashinfer's op...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: erational readiness, as it may fail during execution due to incompatible CUDA architectures. Flashinfer employs check_cuda_arch to verify that the architecture meets the minimum requirement of sm75. When running on olde...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine loads model successfully but fails during sampler execution. bug;stale ### Your current environment ### 🐛 Describe the bug # summary The vLLM engine first loads the model and then invokes the TopKTopPSampler to g...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: df5c356f32/flashinfer/jit/core.py#L283-L292 # mini repro The bug can be reproduced by running any model on CUDA architectures below sm75 like v100. Command used: ```bash python -m vllm.entrypoints.openai.api_server \ --...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26566](https://github.com/vllm-project/vllm/pull/26566) | mentioned | 0.6 | [Bugfix] Check flashinfer availability using flashinfer.sampling.get_sampling_module | nfer requires GPUs with sm75 or higher") ``` ## Test Plan I used the #26565 mini repro command on v100. ```bash python -m vllm.entrypoints.openai.api_server \ --model ../merged-mo… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
