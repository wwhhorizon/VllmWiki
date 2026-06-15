# vllm-project/vllm#43396: CUDA illegal memory access in FP8 MoE moe_permute with cutlass backend at batch size 8192

| 字段 | 值 |
| --- | --- |
| Issue | [#43396](https://github.com/vllm-project/vllm/issues/43396) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA illegal memory access in FP8 MoE moe_permute with cutlass backend at batch size 8192

### Issue 正文摘录

## Bug Description vLLM crashes with `CUDA error: an illegal memory access was encountered` during FP8 MoE inference when the scheduled batch hits exactly 8192 tokens. The crash occurs in the CUTLASS MoE permutation kernel. ## Environment - vLLM version: 0.17.1 (via `ghcr.io/llm-d/llm-d-cuda:v0.6.0`) - GPU: NVIDIA H200 (140GB) - Model: `RedHatAI/Qwen3-30B-A3B-FP8-dynamic` (128 experts, top-2 routing, compressed-tensors FP8) - TP=1, single GPU - `max_model_len=2100`, `enable_prefix_caching=True` ## Steps to Reproduce 1. Deploy Qwen3-30B-A3B-FP8-dynamic with vLLM v0.17.1 2. Send ~100 concurrent requests with `prompt_tokens=1000, max_tokens=1` 3. vLLM schedules 9 requests in one batch (8×1001 + 1×184 = 8192 total tokens) 4. Engine crashes on the first model execution step ## Stack Trace ``` File "/opt/vllm-source/vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py", line 90, in moe_permute a1q_scale = a1q_scale[permuted_idx.clamp(max=n_token * topk - 1) // topk] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` Full call chain: ``` core.py:1102 → EngineCore fatal error → gpu_worker.py:728 execute_mode...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 7: CUDA illegal memory access in FP8 MoE moe_permute with cutlass backend at batch size 8192 ## Bug Description vLLM crashes with `CUDA error: an illegal memory access was encountered` during FP8 MoE inference when the sch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: sh occurs in the CUTLASS MoE permutation kernel. ## Environment - vLLM version: 0.17.1 (via `ghcr.io/llm-d/llm-d-cuda:v0.6.0`) - GPU: NVIDIA H200 (140GB) - Model: `RedHatAI/Qwen3-30B-A3B-FP8-dynamic` (128 experts, top-2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: CUDA illegal memory access in FP8 MoE moe_permute with cutlass backend at batch size 8192 ## Bug Description vLLM crashes with `CUDA error: an illegal memory access was encountered` during FP8 MoE inference when the sch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: CUDA illegal memory access in FP8 MoE moe_permute with cutlass backend at batch size 8192 ## Bug Description vLLM crashes with `CUDA error: an illegal memory access was encountered` during FP8 MoE inference when the sch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 7.1 (via `ghcr.io/llm-d/llm-d-cuda:v0.6.0`) - GPU: NVIDIA H200 (140GB) - Model: `RedHatAI/Qwen3-30B-A3B-FP8-dynamic` (128 experts, top-2 routing, compressed-tensors FP8) - TP=1, single GPU - `max_model_len=2100`, `enabl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
