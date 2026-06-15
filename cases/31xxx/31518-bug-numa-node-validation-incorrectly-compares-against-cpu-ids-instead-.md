# vllm-project/vllm#31518: [Bug]: NUMA node validation incorrectly compares against CPU IDs instead of NUMA node IDs

| 字段 | 值 |
| --- | --- |
| Issue | [#31518](https://github.com/vllm-project/vllm/issues/31518) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NUMA node validation incorrectly compares against CPU IDs instead of NUMA node IDs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `` vLLM version: 0.14.0rc1.dev97+g3ce791ac7.d20251228 Platform: CPU (Linux) Python version: 3.10 ``` ## How would you like to use vLLM Offline batched inference on CPU with NUMA architecture ## Description When using the `CPU_VISIBLE_MEMORY_NODES` environment variable to control which NUMA nodes are visible to vLLM on CPU, the validation logic incorrectly compares NUMA node IDs against CPU ID s, causing invalid NUMA nodes to pass validation. This leads to CPU thread binding failures with errors like: ``` libnuma: Warning: cpu argument 30 out of range ``` ## Reproduction Steps 1. On a system with multiple NUMA nodes (e.g., 1 NUMA node with CPUs 0-19) 2. Set `CPU_VISIBLE_MEMORY_NODES=0` (or any valid NUMA node ID that happens to be within the range of CPU IDs) 3. If you set a NUMA node ID that is larger than the maximum CPU ID, the bug becomes apparent 4. Run vLLM on CPU - thread binding will fail ## Root Cause In `vllm/platforms/cpu.py` at line 391 (introduced in PR #23903), the code validates NUMA node IDs by checking if they exist in `allowed_cpu_id_list` instead of `allowed_numa_nodes`: ```python # Current (buggy) code: allowed...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: IDs bug ### Your current environment ### 🐛 Describe the bug `` vLLM version: 0.14.0rc1.dev97+g3ce791ac7.d20251228 Platform: CPU (Linux) Python version: 3.10 ``` ## How would you like to use vLLM Offline batched inferenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: w would you like to use vLLM Offline batched inference on CPU with NUMA architecture ## Description When using the `CPU_VISIBLE_MEMORY_NODES` environment variable to control which NUMA nodes are visible to vLLM on CPU,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
