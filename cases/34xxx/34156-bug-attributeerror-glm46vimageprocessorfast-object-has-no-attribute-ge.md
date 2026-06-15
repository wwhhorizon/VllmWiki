# vllm-project/vllm#34156: [Bug]: AttributeError: 'Glm46VImageProcessorFast' object has no attribute 'get_number_of_image_patches'

| 字段 | 值 |
| --- | --- |
| Issue | [#34156](https://github.com/vllm-project/vllm/issues/34156) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Glm46VImageProcessorFast' object has no attribute 'get_number_of_image_patches'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With transformers==5.1.0 and VLLM latest stable (0.15), I am running following code: ```python import os from vllm import LLM, SamplingParams os.environ["VLLM_USE_V1"] = "1" llm = LLM( model="zai-org/GLM-OCR", trust_remote_code=True, gpu_memory_utilization=0.85, max_model_len=2048, enforce_eager=False, kv_cache_dtype="auto", tensor_parallel_size=1, model_impl="transformers" ) sampling_params = SamplingParams(max_tokens=2048, temperature=0.0) output_text = model.generate({"prompt": inputs}, sampling_params=sampling_params) ``` Which yields (regardless of `model_impl`): ```text INFO 02-09 17:44:34 [scheduler.py:226] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 02-09 17:44:34 [vllm.py:624] Asynchronous scheduling is enabled. INFO 02-09 17:44:34 [utils.py:261] non-default args: {'trust_remote_code': True, 'max_model_len': 2048, 'gpu_memory_utilization': 0.85, 'disable_log_stats': True, 'model_impl': 'transformers', 'model': '/root/.cache/huggingface/glm_ocr'} INFO 02-09 17:44:39 [model.py:541] Resolved architecture: TransformersMultiModalForCausalLM INFO 02-09 17:44:39 [model.py:1561] Using max model len 2048 INF...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: and VLLM latest stable (0.15), I am running following code: ```python import os from vllm import LLM, SamplingParams os.environ["VLLM_USE_V1"] = "1" llm = LLM( model="zai-org/GLM-OCR", trust_remote_code=True, gpu_memory...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: , SamplingParams os.environ["VLLM_USE_V1"] = "1" llm = LLM( model="zai-org/GLM-OCR", trust_remote_code=True, gpu_memory_utilization=0.85, max_model_len=2048, enforce_eager=False, kv_cache_dtype="auto", tensor
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ax_model_len=2048, enforce_eager=False, kv_cache_dtype="auto", tensor_parallel_size=1, model_impl="transformers" ) sampling_params = SamplingParams(max_tokens=2048, temperature=0.0) output_text = model.generate({"prompt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: .cache/huggingface/glm_ocr'} INFO 02-09 17:44:39 [model.py:541] Resolved architecture: TransformersMultiModalForCausalLM INFO 02-09 17:44:39 [model.py:1561] Using max model len 2048 INFO 02-09 17:44:40 [scheduler.py:226...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
