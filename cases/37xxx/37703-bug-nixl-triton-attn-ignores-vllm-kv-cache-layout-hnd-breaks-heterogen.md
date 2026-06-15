# vllm-project/vllm#37703: [Bug][NIXL]: TRITON_ATTN ignores `VLLM_KV_CACHE_LAYOUT=HND`, breaks heterogeneous TP with NIXL

| 字段 | 值 |
| --- | --- |
| Issue | [#37703](https://github.com/vllm-project/vllm/issues/37703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][NIXL]: TRITON_ATTN ignores `VLLM_KV_CACHE_LAYOUT=HND`, breaks heterogeneous TP with NIXL

### Issue 正文摘录

Fixes https://github.com/vllm-project/vllm/issues/37333. ### Your current environment ### 🐛 Describe the bug ## Description TRITON_ATTN's `get_kv_cache_stride_order` always returns NHD (identity) stride order, ignoring `VLLM_KV_CACHE_LAYOUT=HND`. This breaks heterogeneous TP disaggregated serving (P_TP != D_TP) via the NIXL connector. The NIXL connector sets `VLLM_KV_CACHE_LAYOUT=HND` and computes a byte `rank_offset` to split KV heads across D-side TP ranks. This offset assumes heads are physically contiguous (HND layout: `[num_heads, block_size, head_dim]`). Because TRITON_ATTN keeps the NHD layout (`[block_size, num_heads, head_dim]`), the offset splits along the **token** dimension instead of the **head** dimension, causing each D-rank to read corrupted KV data. FLASH_ATTN and FlashInfer both respect `VLLM_KV_CACHE_LAYOUT` and are unaffected. ## Affected Models Any model using TRITON_ATTN with heterogeneous TP + NIXL. ## Reproduction ```bash # Qwen3-0.6B with forced TRITON_ATTN, PTP=1 DTP=2 vllm serve Qwen/Qwen3-0.6B \ --attention-backend TRITON_ATTN \ --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' \ --tensor-parallel-size 2 # decoder side # With a...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: [Bug][NIXL]: TRITON_ATTN ignores `VLLM_KV_CACHE_LAYOUT=HND`, breaks heterogeneous TP with NIXL bug Fixes https://github.com/vllm-project/vllm/issues/37333. ### Your current environment ### 🐛 Describe the bug ## Descript...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug][NIXL]: TRITON_ATTN ignores `VLLM_KV_CACHE_LAYOUT=HND`, breaks heterogeneous TP with NIXL bug Fixes https://github.com/vllm-project/vllm/issues/37333. ### Your current environment ### 🐛 Describe the bug ## Descript...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _ATTN's implementation: ```python from vllm.v1.attention.backends.utils import get_kv_cache_layout @staticmethod def get_kv_cache_stride_order( include_num_layers_dimension: bool = False, ) -> tuple[int, ...]: cache_lay...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: er Fix **Qwen3-0.6B**, `--attention-backend TRITON_ATTN`, PTP=1 DTP=2, gsm8k 5-shot: | Check | Value | Status | |-------|-------|--------| | Quick sanity | `"Paris. The capital of France is also the capital of the Repub...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: fer both respect `VLLM_KV_CACHE_LAYOUT` and are unaffected. ## Affected Models Any model using TRITON_ATTN with heterogeneous TP + NIXL. ## Reproduction ```bash # Qwen3-0.6B with forced TRITON_ATTN, PTP=1 DTP=2 vllm ser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
