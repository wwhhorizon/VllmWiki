# vllm-project/vllm#32732: [Bug]: Regression in v0.14.0: "No valid attention backend found" for nvidia/DeepSeek-R1-0528-NVFP4 on RTX Pro 6000 (Blackwell)

| 字段 | 值 |
| --- | --- |
| Issue | [#32732](https://github.com/vllm-project/vllm/issues/32732) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression in v0.14.0: "No valid attention backend found" for nvidia/DeepSeek-R1-0528-NVFP4 on RTX Pro 6000 (Blackwell)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Summary `nvidia/DeepSeek-R1-0528-NVFP4` works with vLLM v0.13.0 on 8 x RTX Pro 6000 (Blackwell), but fails with vLLM v0.14.0 with the following error: > [v1/executor/multiproc_executor.py:749] ValueError: No valid attention backend found for cuda with AttentionSelectorConfig(head_size=576, dtype=torch.bfloat16, kv_cache_dtype=fp8_e4m3, block_size=None, use_mla=True, has_sink=False, use_sparse=False, use_mm_prefix=False, attn_type=AttentionType.DECODER). Reasons: {FLASH_ATTN_MLA: [kv_cache_dtype not supported, compute capability not supported, FlashAttention MLA not supported on this device], FLASHMLA: [compute capability not supported, FlashMLA Dense is only supported on Hopper devices.], FLASHINFER_MLA: [compute capability not supported], TRITON_MLA: [kv_cache_dtype not supported], FLASHMLA_SPARSE: [kv_cache_dtype not supported, non-sparse not supported, compute capability not supported]}. # Details ``` #!/bin/sh MODEL="nvidia/DeepSeek-R1-0528-NVFP4" docker run -it --rm -v /path/to/cache/huggingface:/root/.cache/huggingface \ -e VLLM_LOGGING_LEVEL=DEBUG \ --gpus 'all' \ vllm/vllm-openai:v0.13.0 \ --model=$MODEL \ --served-mode...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: v0.14.0: "No valid attention backend found" for nvidia/DeepSeek-R1-0528-NVFP4 on RTX Pro 6000 (Blackwell) bug;unstale ### Your current environment ### 🐛 Describe the bug # Summary `nvidia/DeepSeek-R1-0528-NVFP4` works w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: "No valid attention backend found" for nvidia/DeepSeek-R1-0528-NVFP4 on RTX Pro 6000 (Blackwell) bug;unstale ### Your current environment ### 🐛 Describe the bug # Summary `nvidia/DeepSeek-R1-0528-NVFP4` works with vLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Regression in v0.14.0: "No valid attention backend found" for nvidia/DeepSeek-R1-0528-NVFP4 on RTX Pro 6000 (Blackwell) bug;unstale ### Your current environment ### 🐛 Describe the bug # Summary `nvidia/DeepSeek-R...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: orted]}. # Details ``` #!/bin/sh MODEL="nvidia/DeepSeek-R1-0528-NVFP4" docker run -it --rm -v /path/to/cache/huggingface:/root/.cache/huggingface \ -e VLLM_LOGGING_LEVEL=DEBUG \ --gpus 'all' \ vllm/vllm-openai:v0.13.0 \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ueError: No valid attention backend found for cuda with AttentionSelectorConfig(head_size=576, dtype=torch.bfloat16, kv_cache_dtype=fp8_e4m3, block_size=None, use_mla=True, has_sink=False, use_sparse=False, use_mm_prefi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
