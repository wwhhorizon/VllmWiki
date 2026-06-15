# vllm-project/vllm#26243: [Bug]: Perturb and restore the model parameters with Worker Extension

| 字段 | 值 |
| --- | --- |
| Issue | [#26243](https://github.com/vllm-project/vllm/issues/26243) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;nondeterministic;oom |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Perturb and restore the model parameters with Worker Extension

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using a `worker_extension_cls` to implement a weight perturbation method, similar to techniques used in RLHF examples. The goal is to add randomly generated noise to the model's weights, perform an operation (e.g., inference), and then perfectly restore the original weights by subtracting the same noise. However, after setting the generator, seed and the noise's dtype, I always find the result to be mismatching. The mismatching is even greater when the variance of `torch.normal` grows. Is there any way to keep the before and after model weight the same? Many thanks in advance! PS: I also tried to offload the model to cpu and restore it but it turns out to be killed due to OOM. Here is my implementation: ```python import os import ray import random import numpy as np import torch from ray.util.placement_group import placement_group from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy from vllm import LLM, SamplingParams class WorkerExtension: def update_weight_in_place(self, seed): """ Performs a deterministic, in-place update on a model weight. """ # Set all seeds for full reproducibility (good practic...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: turns out to be killed due to OOM. Here is my implementation: ```python import os import ray import random import numpy as np import torch from ray.util.placement_group import placement_group from ray.util.scheduling_st...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: he generator, seed and the noise's dtype, I always find the result to be mismatching. The mismatching is even greater when the variance of `torch.normal` grows. Is there any way to keep the before and after model weight...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: generator, seed and the noise's dtype, I always find the result to be mismatching. The mismatching is even greater when the variance of `torch.normal` grows. Is there any way to keep the before and after model weight th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Perturb and restore the model parameters with Worker Extension bug ### Your current environment ### 🐛 Describe the bug I am using a `worker_extension_cls` to implement a weight perturbation method, similar to tec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Extension", tensor_parallel_size=1, distributed_executor_backend="ray", seed=42, ) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", "In a shock...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
