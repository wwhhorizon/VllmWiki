# vllm-project/vllm#26976: [Bug]: AssertionError in lora_shrink_op during profile_run - visual encoder incorrectly marked as LoRA-enabled even when adapter contains no visual weights

| 字段 | 值 |
| --- | --- |
| Issue | [#26976](https://github.com/vllm-project/vllm/issues/26976) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in lora_shrink_op during profile_run - visual encoder incorrectly marked as LoRA-enabled even when adapter contains no visual weights

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Problem vLLM crashes with `AssertionError` in `lora_shrink_op.py` during `profile_run()` when loading a LoRA adapter for Qwen3-VL-MoE, even though the adapter contains **only language model weights** (0 visual encoder weights). **Root Cause**: Visual encoder layers are incorrectly marked as LoRA-enabled. During encoder cache initialization with dummy video inputs, these layers attempt LoRA operations causing `token_lora_mapping` dimension mismatch (language tokens vs video tokens). **Evidence**: - LoRA adapter verified: 384 weights, **0 visual encoder weights** - Error in `model.visual.*.attn.proj()` - visual encoder layer - Disabling LoRA → model starts successfully - Same vLLM version without LoRA → works perfectly ### Error Traceback ```python # Call path: profile_run → _process_video_input → visual encoder forward File "vllm/v1/worker/gpu_model_runner.py", line 3688, in profile_run dummy_encoder_outputs = self.model.get_multimodal_embeddings(...) ↓ File "vllm/model_executor/models/qwen3_vl.py", line 1445, in _process_video_input video_embeds = self.visual(pixel_values_videos, ...) # Visual encoder ↓ File "vllm/model_execu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l encoder layer - Disabling LoRA → model starts successfully - Same vLLM version without LoRA → works perfectly ### Error Traceback ```python # Call path: profile_run → _process_video_input → visual encoder forward File...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ora_shrink_op.py` during `profile_run()` when loading a LoRA adapter for Qwen3-VL-MoE, even though the adapter contains **only language model weights** (0 visual encoder weights). **Root Cause**: Visual encoder layers a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: layers attempt LoRA operations causing `token_lora_mapping` dimension mismatch (language tokens vs video tokens). **Evidence**: - LoRA adapter verified: 384 weights, **0 visual encoder weights** - Error in `model.visual...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: k_op.py` during `profile_run()` when loading a LoRA adapter for Qwen3-VL-MoE, even though the adapter contains **only language model weights** (0 visual encoder weights). **Root Cause**: Visual encoder layers are incorr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: dy done, still crashes | ### Related Context **Issue #16364**: Feature request for vision layer LoRA (different issue - this is a bug) **Expected behavior from code**: `_filter_unsupported_mm_module()` in `vllm/lora/mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
