# vllm-project/vllm#36251: [Bug]: Qwen3.5-397B-A17B-FP8 crashes with TP=4 + Expert Parallelism - dimension mismatch in fused linear sharding

| 字段 | 值 |
| --- | --- |
| Issue | [#36251](https://github.com/vllm-project/vllm/issues/36251) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-397B-A17B-FP8 crashes with TP=4 + Expert Parallelism - dimension mismatch in fused linear sharding

### Issue 正文摘录

### Your current environment - vLLM version: `0.16.0rc2.dev207+g79c7e0923` - Docker image: `artifactory.turkcell.com.tr/.../nightly/2026-02-20/vllm/vllm-openai:main-1` - GPU: 4x NVIDIA H200 141GB - Platform: OpenShift/Kubernetes - CUDA version: 12.9 (from image) ### How would you like to use vLLM? I want to serve **Qwen3.5-397B-A17B-FP8** with both **Tensor Parallelism (TP=4)** and **Expert Parallelism** enabled to optimize memory usage across 4x H200 GPUs. ### 🐛 Describe the bug Related to #34893, but this is a **different bug** when combining `--tensor-parallel-size=4` with `--enable-expert-parallel`. **Issue #34893** fixed TP=4 without expert parallelism. However, when **both TP=4 AND expert parallelism** are enabled, the model crashes during weight loading with a dimension mismatch error. #### Reproduction Steps ```bash vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --max-model-len 76000 \ --gpu-memory-utilization 0.9 ``` #### Error ```python (Worker_TP1_EP1 pid=452) ERROR RuntimeError: start (0) + length (2048) exceeds dimension size (96). File "vllm/model_executor/layers/linear.py", line 858, in _load_fused_module_from_checkpoin...

## 现有链接修复摘要

#36460 [Bugfix] Fix FP8 block-scale dimension mismatch in fused linear weight loading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: n mismatch in fused linear sharding ### Your current environment - vLLM version: `0.16.0rc2.dev207+g79c7e0923` - Docker image: `artifactory.turkcell.com.tr/.../nightly/2026-02-20/vllm/vllm-openai:main-1` - GPU: 4x NVIDI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3.5-397B-A17B-FP8 crashes with TP=4 + Expert Parallelism - dimension mismatch in fused linear sharding ### Your current environment - vLLM version: `0.16.0rc2.dev207+g79c7e0923` - Docker image: `artifactory.t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Qwen3.5-397B-A17B-FP8 crashes with TP=4 + Expert Parallelism - dimension mismatch in fused linear sharding ### Your current environment - vLLM version: `0.16.0rc2.dev207+g79c7e0923` - Docker image: `artifactory.t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Qwen3.5-397B-A17B-FP8 crashes with TP=4 + Expert Parallelism - dimension mismatch in fused linear sharding ### Your current environment - vLLM version: `0.16.0rc2.dev207+g79c7e0923` - Docker image: `artifactory.t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-397B-A17B-FP8 crashes with TP=4 + Expert Parallelism - dimension mismatch in fused linear sharding ### Your current environment - vLLM version: `0.16.0rc2.dev207+g79c7e0923` - Docker image: `artifactory.t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36460](https://github.com/vllm-project/vllm/pull/36460) | closes_keyword | 0.95 | [Bugfix] Fix FP8 block-scale dimension mismatch in fused linear weight loading | Closes #36251 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
