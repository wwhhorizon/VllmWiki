# vllm-project/vllm#17386: [Bug]: vLLM serve `google/gemma-3-1b-it` with version `0.8.5` interrupted `SIGTERM`

| 字段 | 值 |
| --- | --- |
| Issue | [#17386](https://github.com/vllm-project/vllm/issues/17386) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM serve `google/gemma-3-1b-it` with version `0.8.5` interrupted `SIGTERM`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, When deploying the `gemma-3-1b-it` the `vLLM` pod always crashes with the same error while waiting for core engine process to start. It never starts successfully. GPU used has 24GB of memory so it should not be an issue to run this model on only one GPU. Above are detailed outputs of the pod and the simple setup for K8s to reproduce it.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: vLLM serve `google/gemma-3-1b-it` with version `0.8.5` interrupted `SIGTERM` bug ### Your current environment ### 🐛 Describe the bug Hi, When deploying the `gemma-3-1b-it` the `vLLM` pod always crashes with the s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: v_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory attention;cuda;operator;quantization;sampling crash;slowdown dtype;env_dependency Your current envir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM serve `google/gemma-3-1b-it` with version `0.8.5` interrupted `SIGTERM` bug ### Your current environment ### 🐛 Describe the bug Hi, When deploying the `gemma-3-1b-it` the `vLLM` pod always crashes with the s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: `gemma-3-1b-it` the `vLLM` pod always crashes with the same error while waiting for core engine process to start. It never starts successfully. GPU used has 24GB of memory so it should not be an issue to run this model...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Above are detailed outputs of the pod and the simple setup for K8s to reproduce it. performance attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
