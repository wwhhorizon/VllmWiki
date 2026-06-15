# vllm-project/vllm#42489: [Bug]: Same-request resumable streaming_update can overflow prompt width in gpu_input_batch.add_request

| 字段 | 值 |
| --- | --- |
| Issue | [#42489](https://github.com/vllm-project/vllm/issues/42489) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Same-request resumable streaming_update can overflow prompt width in gpu_input_batch.add_request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary A frontend-legal same-request streaming continuation can make vLLM rebuild a renewed prompt whose final token length exceeds the worker input-batch width. The initial request is within bounds. The overflow appears only after vLLM folds already-generated output back into the resumable request and then accepts the next streaming update. On the verified Qwen3 GPTQ run, this ends at `gpu_input_batch.add_request()` with a stable host-side broadcast failure. ## Impact - A legal resumable request sequence can kill a request path without requiring malformed token ids or direct internal-state access - The failure happens after the request has already been accepted, so it is not just an admission-time prompt-length rejection - In practice this is a reliable request-triggered engine failure surface for the affected workload shape ## Affected version - Confirmed on vLLM `0.17.1` - Earlier and later versions have not been checked yet in this report ## Repro model - Official Hugging Face repo: - [`Qwen/Qwen3-0.6B-GPTQ-Int8`](https://huggingface.co/Qwen/Qwen3-0.6B-GPTQ-Int8) - Please download `Qwen3-0.6B-GPTQ-Int8` and run my reprodu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ry A frontend-legal same-request streaming continuation can make vLLM rebuild a renewed prompt whose final token length exceeds the worker input-batch width. The initial request is within bounds. The overflow appears on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e renewed prompt into the existing row and raises a host-side shape mismatch. ## Details ### Trigger path in code 1. The request is marked resumable, so vLLM keeps enough state to accept later streaming updates on the s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: able request and then accepts the next streaming update. On the verified Qwen3 GPTQ run, this ends at `gpu_input_batch.add_request()` with a stable host-side broadcast failure. ## Impact - A legal resumable request sequ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: wen3-0.6B-GPTQ-Int8) - Please download `Qwen3-0.6B-GPTQ-Int8` and run my reproduce script [repro_g6_prompt_overflow_local.py](https://github.com/user-attachments/files/27694025/repro_g6_prompt_overflow_local.py) ## Repr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;mismatch;nan_inf dtype;env_depende...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
