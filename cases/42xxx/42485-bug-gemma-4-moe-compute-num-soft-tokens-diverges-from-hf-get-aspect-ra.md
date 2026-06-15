# vllm-project/vllm#42485: [Bug]: (Gemma 4 MoE) _compute_num_soft_tokens diverges from HF get_aspect_ratio_preserving_size

| 字段 | 值 |
| --- | --- |
| Issue | [#42485](https://github.com/vllm-project/vllm/issues/42485) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (Gemma 4 MoE) _compute_num_soft_tokens diverges from HF get_aspect_ratio_preserving_size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi Team, Thank you for your hard work. Device: DGX Spark (GB10, single-node, 128GB RAM, running `Gemma-4-26B-A4B-it-NVFP4A16`) vLLM: `0.19.1rc1.dev36+g9a528260e`, running via `eugr/spark-vllm-docker` `Gemma4ProcessingInfo._compute_num_soft_tokens()` in `vllm/model_executor/models/gemma4_mm.py` is a re-implementation of HF's `get_aspect_ratio_preserving_size()` that omits HF's `max_side_length` clamp, so on extreme-aspect-ratio images (≥ ~30:1 — full-page receipt scans, stitched chat screenshots, leaderboards, vertical banners) vLLM emits more placeholders in the prompt than the encoder produces embeddings. `_merge_multimodal_embeddings` then asserts inside EngineCore, killing the engine and aborting every in-flight request: ``` ValueError: Attempted to assign 529 + 280 multimodal tokens to 809 placeholders ``` I believe @skyloevil semi-fixed the issue with PR #42217: the `pixel_values contains inconsistent shapes` TensorSchema/batching error is fixed and is working, but the verification script in that PR only uses images up to ~4.7:1 aspect ratio (`1024×1024`, `256×128`, `1400×300`, `300×1400`), so the per-image count divergence...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: P4A16`) vLLM: `0.19.1rc1.dev36+g9a528260e`, running via `eugr/spark-vllm-docker` `Gemma4ProcessingInfo._compute_num_soft_tokens()` in `vllm/model_executor/models/gemma4_mm.py` is a re-implementation of HF's `get_aspect_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: (Gemma 4 MoE) _compute_num_soft_tokens diverges from HF get_aspect_ratio_preserving_size bug ### Your current environment ### 🐛 Describe the bug Hi Team, Thank you for your hard work. Device: DGX Spark (GB10, sin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ce: DGX Spark (GB10, single-node, 128GB RAM, running `Gemma-4-26B-A4B-it-NVFP4A16`) vLLM: `0.19.1rc1.dev36+g9a528260e`, running via `eugr/spark-vllm-docker` `Gemma4ProcessingInfo._compute_num_soft_tokens()` in `vllm/mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: (Gemma 4 MoE) _compute_num_soft_tokens diverges from HF get_aspect_ratio_preserving_size bug ### Your current environment ### 🐛 Describe the bug Hi Team, Thank you for your hard work. Device: DGX Spark (GB10, sin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
