# vllm-project/vllm#19038: [RFC]: Prefill-only optimizations for PD disaggregation in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#19038](https://github.com/vllm-project/vllm/issues/19038) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8 |
| 症状 | build_error;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Prefill-only optimizations for PD disaggregation in vLLM

### Issue 正文摘录

### Motivation. As vLLM is moving towards full PD disaggregation, this allow us to add new optimizations just for prefill workload: - **Much larger context length on prefill nodes**: As there is no decoding steps in prefill nodes, we can directly store the generated KV caches to CPU instead of GPU. This gives us much much longer context length (about 7x longer). - **Better scheduling**: Also, since there is no decoding, the time it takes to run each request (aka job completion time) is completely deterministic. This means that we can do better scheduling for prefill nodes by using the job completion time as the input to the scheduler. Please see more details in https://arxiv.org/abs/2505.07203 ### Proposed Change. ## User-facing API - Add `vllm prefill`, which will only accept prefill requests (`max_tokens=1`) and performs prefill-only optimizations. ## Longer context length The key technique that enables longer context length is to directly store the generated KV cache to CPU, and also control the peak memory usage for long-context inference. Traditionally this is done by chunked prefill, however it requires keeping the previous KV caches (we want to save it in CPU). Instead, we...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ils in https://arxiv.org/abs/2505.07203 ### Proposed Change. ## User-facing API - Add `vllm prefill`, which will only accept prefill requests (`max_tokens=1`) and performs prefill-only optimizations. ## Longer context l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ime it takes to run each request (aka job completion time) is completely deterministic. This means that we can do better scheduling for prefill nodes by using the job completion time as the input to the scheduler. Pleas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: provement: ~7x on A100 40 GB, model RedHatAI/DeepSeek-R1-DistillQwen-32B-FP8-dynamic Proposed changes: - Support a compilation level that only triggers `torch.compile` - Inside the compilation pass of `torch.compile`, i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Prefill-only optimizations for PD disaggregation in vLLM RFC;keep-open ### Motivation. As vLLM is moving towards full PD disaggregation, this allow us to add new optimizations just for prefill workload: - **Much...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fectiveness of hybrid prefilling: Context length improvement: ~7x on A100 40 GB, model RedHatAI/DeepSeek-R1-DistillQwen-32B-FP8-dynamic Proposed changes: - Support a compilation level that only triggers `torch.compile`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
