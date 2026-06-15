# vllm-project/vllm#39839: [Bug]:  MTP DeepSeek and Eagle Flash Attention Failures in Spec Decode Unit Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#39839](https://github.com/vllm-project/vllm/issues/39839) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;sampling;triton |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  MTP DeepSeek and Eagle Flash Attention Failures in Spec Decode Unit Tests

### Issue 正文摘录

### Your current environment ``` Failure 1: test_eagle_correctness_light[FLASH_ATTN-deepseek_eagle] Model: eagle618/deepseek-v3-random with FLASH_ATTN backend Root cause: Flash Attention 4 (FA4) on SM100/SM110 (Blackwell) does not support head_dim=192 with equal Q and V head dimensions. The validation at vllm/vllm_flash_attn/cute/interface.py:114 enforces: - Standard range: head_dim between 8-128, divisible by 8 - Special DeepSeek shape: (192, 128) only (asymmetric Q/V) The eagle618/deepseek-v3-random model has (head_dim, head_dim_v) = (192, 192) which doesn't match either pattern. The actual DeepSeek-V3 production model uses (192, 128) and would work fine — this is specific to the random test model's symmetric head dims. Error: AssertionError: (head_dim, head_dim_v)=(192, 192) is not supported on SM100/SM110. head_dim and head_dim_v must be between 8 and 128 and divisible by 8, or (192, 128) for DeepSeek. Call chain: _run_eagle_correctness → LLM() → EngineCore init → CUDA graph capture → flash_attn_varlen_func → _validate_head_dims --- Failure 2: test_mtp_correctness[deepseek] Model: ZixiQi/DeepSeek-V3-4layers-MTP-FP8 with auto attention backend Root cause: FlashInfer's TRTLLM fu...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Root cause: Flash Attention 4 (FA4) on SM100/SM110 (Blackwell) does not support head_dim=192 with equal Q and V head dimensions. The validation at vllm/vllm_flash_attn/cute/interface.py:114 enforces: - Standard range: h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: MTP DeepSeek and Eagle Flash Attention Failures in Spec Decode Unit Tests bug ### Your current environment ``` Failure 1: test_eagle_correctness_light[FLASH_ATTN-deepseek_eagle] Model: eagle618/deepseek-v3-ra
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Model: ZixiQi/DeepSeek-V3-4layers-MTP-FP8 with auto attention backend
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Root cause: FlashInfer's TRTLLM fused MoE kernel on SM100 has a strict inequality check: top_k top_k topk_group * args->num_experts / args->n_group) (4 vs. 4) :
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: MTP DeepSeek and Eagle Flash Attention Failures in Spec Decode Unit Tests bug ### Your current environment ``` Failure 1: test_eagle_correctness_light[FLASH_ATTN-deepseek_eagle] Model: eagle618/deepseek-v3-random...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
