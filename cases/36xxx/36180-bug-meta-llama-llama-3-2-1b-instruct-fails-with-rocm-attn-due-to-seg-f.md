# vllm-project/vllm#36180: [Bug]: meta-llama/Llama-3.2-1B-Instruct Fails With ROCM_ATTN Due To Seg Fault

| 字段 | 值 |
| --- | --- |
| Issue | [#36180](https://github.com/vllm-project/vllm/issues/36180) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-3.2-1B-Instruct Fails With ROCM_ATTN Due To Seg Fault

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve meta-llama/Llama-3.2-1B-Instruct --attention-backend ROCM_ATTN` fails with the following error: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 51/51 [00:00 (q= , k_cache=0x7c027ca00000, v_cache=0x7c0438a8c000, num_kv_heads= , scale= , block_tables= , seq_lens= , query_start_loc_ptr= , max_num_blocks_per_seq= , alibi_slopes= , q_stride= , kv_block_stride= , kv_head_stride= , exp_sums=0x7c3af2098e00, max_logits=0x7c3af20a8e00, out=0x7c39a0e00000, final_out= , max_ctx_blocks= , k_scale= , v_scale= ) at /projects/vllm/build/temp.linux-x86_64-cpython-312/csrc/rocm/attention.hip:1086 1086 Klocal[d] = k_ptrh8[d * BLOCK_SIZE + physical_block_offset]; ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39849 [ROCm] route known-bad gfx9 ROCM_ATTN mfma4 shapes to Triton | #42421 [ROCm] Fix #36180: OOB Q-load in `paged_attention_ll4mi_QKV_mfma4_kernel`

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: meta-llama/Llama-3.2-1B-Instruct Fails With ROCM_ATTN Due To Seg Fault bug;rocm ### Your current environment ### 🐛 Describe the bug `vllm serve meta-llama/Llama-3.2-1B-Instruct --attention-backend ROCM_ATTN` fail...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: al_out= , max_ctx_blocks= , k_scale= , v_scale= ) at /projects/vllm/build/temp.linux-x86_64-cpython-312/csrc/rocm/attention.hip:1086 1086 Klocal[d] = k_ptrh8[d * BLOCK_SIZE + physical_block_offset]; ``` ### Before submi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: _ATTN` fails with the following error: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: scribe the bug `vllm serve meta-llama/Llama-3.2-1B-Instruct --attention-backend ROCM_ATTN` fails with the following error: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: k_cache=0x7c027ca00000, v_cache=0x7c0438a8c000, num_kv_heads= , scale= , block_tables= , seq_lens= , query_start_loc_ptr= , max_num_blocks_per_seq= , alibi_slopes= , q_stride= , kv_block_stride= , kv_head_stride= , exp_...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39849](https://github.com/vllm-project/vllm/pull/39849) | mentioned | 0.6 | [ROCm] route known-bad gfx9 ROCM_ATTN mfma4 shapes to Triton | VL reranker score drift on gfx950 (`head_size=128`, `gqa_ratio=2`) - `#36180`: `meta-llama/Llama-3.2-1B-Instruct` illegal memory access during graph capture on gfx942 (`head_size=… |
| [#42421](https://github.com/vllm-project/vllm/pull/42421) | closes_keyword | 0.95 | [ROCm] Fix #36180:  OOB Q-load in `paged_attention_ll4mi_QKV_mfma4_kernel` | Fixes #36180. The gfx9 mfma4 variant of `paged_attention_ll4mi_QKV_mfma4_kernel` reads past the per-head Q allocation under specific shape conditions. The crash surfaces as `hip |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
