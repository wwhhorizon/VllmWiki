# vllm-project/vllm#35925: [Bug]: Qwen3.5-35B-A3B generates corrupted responses when AITER is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#35925](https://github.com/vllm-project/vllm/issues/35925) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-35B-A3B generates corrupted responses when AITER is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run with Mi300x TP=1. ROCM version 6.4.2 / 7.0 I ran MMMU benchmark with Qwen3.5, and ~70 out of 900 results contain repetitive exclamation marks like !!!!!. The issue can be steadily reproduced when the input requests are multimodal. AITER ATTN (encoder + transformer) + AITER MOE : 70 / 900 bad responses ``` CUDA_VISIBLE_DEVICES=0 VLLM_ROCM_USE_AITER=1 VLLM_ROCM_USE_AITER_MHA=1 VLLM_ROCM_USE_AITER_MOE=1 VLLM_ROCM_USE_AITER_LINEAR=0 VLLM_ROCM_USE_AITER_RMSNORM=0 VLLM_ROCM_USE_AITER_TRITON_ROPE=0 VLLM_GPU_MEMORY_UTILIZATION=0.95 lm_eval --model vllm-vlm --model_args pretrained=$HOME/hf_models/Qwen/Qwen3.5-35B-A3B,max_model_len=65536,trust_remote_code=True --tasks mmmu_val --batch_size auto ``` AITER ATTN (transformer) + AITER MOE : 70 / 900 bad responses ``` CUDA_VISIBLE_DEVICES=0 VLLM_ROCM_USE_AITER=1 VLLM_ROCM_USE_AITER_MHA=1 VLLM_ROCM_USE_AITER_MOE=1 VLLM_ROCM_USE_AITER_LINEAR=0 VLLM_ROCM_USE_AITER_RMSNORM=0 VLLM_ROCM_USE_AITER_TRITON_ROPE=0 VLLM_GPU_MEMORY_UTILIZATION=0.95 lm_eval --model vllm-vlm --model_args pretrained=$HOME/hf_models/Qwen/Qwen3.5-35B-A3B,max_model_len=65536,trust_remote_code=True,mm_encoder_attn_backend=TRI...

## 现有链接修复摘要

#37228 [ROCM][Bugfix] Use correct stride in cp_mha_gather_cache_kernel for hybrid model (#37228)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Qwen3.5-35B-A3B generates corrupted responses when AITER is enabled bug;rocm ### Your current environment ### 🐛 Describe the bug Run with Mi300x TP=1. ROCM version 6.4.2 / 7.0 I ran MMMU benchmark with Qwen3.5, and ~70...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3.5-35B-A3B generates corrupted responses when AITER is enabled bug;rocm ### Your current environment ### 🐛 Describe the bug Run with Mi300x TP=1. ROCM version 6.4.2 / 7.0 I ran MMMU benchmark with Qwen3.5, a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rrent environment ### 🐛 Describe the bug Run with Mi300x TP=1. ROCM version 6.4.2 / 7.0 I ran MMMU benchmark with Qwen3.5, and ~70 out of 900 results contain repetitive exclamation marks like !!!!!. The issue can be ste...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Qwen3.5-35B-A3B generates corrupted responses when AITER is enabled bug;rocm ### Your current environment ### 🐛 Describe the bug Run with Mi300x TP=1. ROCM version 6.4.2 / 7.0 I ran MMMU benchmark with Qwen3.5, a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ribe the bug Run with Mi300x TP=1. ROCM version 6.4.2 / 7.0 I ran MMMU benchmark with Qwen3.5, and ~70 out of 900 results contain repetitive exclamation marks like !!!!!. The issue can be steadily reproduced when the in...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37228](https://github.com/vllm-project/vllm/pull/37228) | closes_keyword | 0.95 | [ROCM][Bugfix] Use correct stride in cp_mha_gather_cache_kernel for hybrid model (#37228) | fix it if it's needed for hybrid model **Test** Ran cmd in #35925, no corrupted responses observed anymore |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
