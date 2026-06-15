# vllm-project/vllm#19923: [Bug]: Unexpected Memory Usage in cutlass_moe_fp8() on Latest main 6bc7b57

| 字段 | 值 |
| --- | --- |
| Issue | [#19923](https://github.com/vllm-project/vllm/issues/19923) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected Memory Usage in cutlass_moe_fp8() on Latest main 6bc7b57

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary We discovered a significant memory issue with the latest `cutlass_moe_fp8()` implementation in the `main` branch of vLLM. The function now allocates **at least 24.5 GB** of GPU memory per rank, which appears **abnormally high** and prevents us from rebasing our [PR #19843](https://github.com/vllm-project/vllm/pull/19843) onto `main`. This issue did **not** exist in `v0.8.5.post1`, where the memory footprint of the same function was much smaller under otherwise identical conditions. ### Error Log --- ### 💡 Context - **Model**: [DeepSeek-R1](https://huggingface.co/deepseek-ai/deepseek-llm-7b-base) - **GPUs**: 8x NVIDIA H20 - **Tensor Parallelism (TP)**: 8 - **Quantization**: `--quantization fp8` - **vLLM Version (working)**: `v0.8.5.post1` - **vLLM Version (issue)**: `main` branch (latest: 6bc7b573153afebe51de036f9b28d37ff6cbb733) - **Backend**: Cutlass MoE FP8 (`cutlass_moe_fp8()`) --- ### 🔁 Reproduction Steps It's a bit hard but 1. Check out the latest `main` branch of vLLM (6bc7b573153afebe51de036f9b28d37ff6cbb733). 2. Apply changes [PR #19843](https://github.com/vllm-project/vllm/pull/19843) 3. Follow the setup proc...

## 现有链接修复摘要

#19843 Add Cutlass integration for MoE FP8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Parallelism (TP)**: 8 - **Quantization**: `--quantization fp8` - **vLLM Version (working)**: `v0.8.5.post1` - **vLLM Version (issue)**: `main` branch (latest: 6bc7b573153afebe51de036f9b28d37ff6cbb733) - **Backend**: Cut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Unexpected Memory Usage in cutlass_moe_fp8() on Latest main 6bc7b57 bug;stale ### Your current environment ### 🐛 Describe the bug ### Summary We discovered a significant memory issue with the latest `cutlass_moe_fp8()`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Unexpected Memory Usage in cutlass_moe_fp8() on Latest main 6bc7b57 bug;stale ### Your current environment ### 🐛 Describe the bug ### Summary We discovered a significant memory issue with the latest `cutlass_moe_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Unexpected Memory Usage in cutlass_moe_fp8() on Latest main 6bc7b57 bug;stale ### Your current environment ### 🐛 Describe the bug ### Summary We discovered a significant memory issue with the latest `cutlass_moe_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: `v0.8.5.post1`, where the memory footprint of the same function was much smaller under otherwise identical conditions. ### Error Log --- ### 💡 Context - **Model**: [DeepSeek-R1](https://huggingface.co/deepseek-ai/deepse...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19843](https://github.com/vllm-project/vllm/pull/19843) | mentioned | 0.6 | Add Cutlass integration for MoE FP8 | nt difference. ## Found Issue ⚠️❗ This PR is currently blocked by [#19923](https://github.com/vllm-project/vllm/issues/19923), which tracks an OOM issue on `main` branch during `c… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
