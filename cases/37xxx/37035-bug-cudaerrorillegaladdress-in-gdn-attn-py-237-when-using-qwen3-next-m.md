# vllm-project/vllm#37035: [Bug]: cudaErrorIllegalAddress in gdn_attn.py:237 when using qwen3_next_mtp with num_speculative_tokens=5 under load

| 字段 | 值 |
| --- | --- |
| Issue | [#37035](https://github.com/vllm-project/vllm/issues/37035) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cudaErrorIllegalAddress in gdn_attn.py:237 when using qwen3_next_mtp with num_speculative_tokens=5 under load

### Issue 正文摘录

### Your current environment - **vLLM version**: `v0.17.1rc1.dev126+gbc2c0c86e` (nightly, `vllm/vllm-openai:nightly`) - **Model**: `cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4` - **Quantization**: `compressed-tensors` (AWQ BF16 INT4) - **Hardware**: 2× NVIDIA GPU (tensor-parallel-size=2), WSL2 (Linux 6.6.87.2-microsoft-standard-WSL2) - **Attention backend**: FlashInfer (`--attention-backend FLASHINFER`) - **Python**: 3.12 - **PyTorch**: inferred from nightly image ### 🐛 Describe the bug ## Summary vLLM crashes with `CUDA error: an illegal memory access was encountered` in `gdn_attn.py:237` (`spec_state_indices_tensor = block_table_tensor[...]`) when running `qwen3_next_mtp` speculative decoding with `num_speculative_tokens=5` and FlashInfer attention backend under concurrent load. Both TP workers (TP0 and TP1) crash with the same error. The crash occurs consistently once the request queue fills (~500 waiting requests) and KV cache usage exceeds ~63%. The crash reproduces reliably across multiple runs (observed twice within a single session, ~7 minutes apart). ## Suspected Root Cause FlashInfer PR [#2679](https://github.com/flashinfer-ai/flashinfer/pull/2679) ("feat(gdn): add BF16 state ker...

## 现有链接修复摘要

#37052 fix(gdn_attn): prevent CUDA illegal memory access with >4 speculative tokens

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lative_tokens=5 under load bug ### Your current environment - **vLLM version**: `v0.17.1rc1.dev126+gbc2c0c86e` (nightly, `vllm/vllm-openai:nightly`) - **Model**: `cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4` - **Quantization**:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: rrorIllegalAddress in gdn_attn.py:237 when using qwen3_next_mtp with num_speculative_tokens=5 under load bug ### Your current environment - **vLLM version**: `v0.17.1rc1.dev126+gbc2c0c86e` (nightly, `vllm/vllm-openai:ni...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: htly, `vllm/vllm-openai:nightly`) - **Model**: `cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4` - **Quantization**: `compressed-tensors` (AWQ BF16 INT4) - **Hardware**: 2× NVIDIA GPU (tensor-parallel-size=2), WSL2 (Linux 6.6.87.2-m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: cudaErrorIllegalAddress in gdn_attn.py:237 when using qwen3_next_mtp with num_speculative_tokens=5 under load bug ### Your current environment - **vLLM version**: `v0.17.1rc1.dev126+gbc2c0c86e` (nightly, `vllm/vl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: lel-size=2), WSL2 (Linux 6.6.87.2-microsoft-standard-WSL2) - **Attention backend**: FlashInfer (`--attention-backend FLASHINFER`) - **Python**: 3.12 - **PyTorch**: inferred from nightly image ### 🐛 Describe the bug ## S...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37052](https://github.com/vllm-project/vllm/pull/37052) | closes_keyword | 0.95 | fix(gdn_attn): prevent CUDA illegal memory access with >4 speculative tokens | Fixes #37035 This PR addresses a critical CUDA illegal memory access error that occurs in the GDN attention backend when using qwen3_next_mtp speculative decoding with >4 speculat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
