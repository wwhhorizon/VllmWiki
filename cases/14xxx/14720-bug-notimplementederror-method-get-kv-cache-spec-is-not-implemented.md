# vllm-project/vllm#14720: [Bug]: NotImplementedError: Method 'get_kv_cache_spec' is not implemented.

| 字段 | 值 |
| --- | --- |
| Issue | [#14720](https://github.com/vllm-project/vllm/issues/14720) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NotImplementedError: Method 'get_kv_cache_spec' is not implemented.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to deploy a llama-3.2b-instruct with finetuned LoRA adapter on a VM with a GPU Nvidia L4 with VRAM 24Gb (~18Gb available). I would like to be able to use the Quantisation for both the model + adapter and the KV Cache. I'm not sure this is actually a bug, maybe it's the way I'm trying to use VLLM that is wrong, as there are several parameters to be considered. I undestood that bitsandbyte quantisation is still experimental with LoRA, nevertheless, I've been trying to play around with different parameters and found that the behaviour changes when using 4bit or 8bit quantisation, see below. Is there an alternative way / better supported way to quantize a model with the LoRA adapter? The relevant part of the code is as follows (FYI I'm using Flashinfer): ```python from vllm import EngineArgs, SamplingParams from vllm.lora.request import LoRARequest from vllm.v1.engine.llm_engine import LLMEngine quantization_config = { "quantization_config": { "load_in_8bit": True, "bnb_8bit_compute_dtype": "float16", "quant_method": "bitsandbytes" } } engine_args = EngineArgs( model=model_path, enable_lora=True, max_loras=1, max_lora_rank...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 4 with VRAM 24Gb (~18Gb available). I would like to be able to use the Quantisation for both the model + adapter and the KV Cache. I'm not sure this is actually a bug, maybe it's the way I'm trying to use VLLM that is w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r current environment ### 🐛 Describe the bug I'm trying to deploy a llama-3.2b-instruct with finetuned LoRA adapter on a VM with a GPU Nvidia L4 with VRAM 24Gb (~18Gb available). I would like to be able to use the Quant...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he code is as follows (FYI I'm using Flashinfer): ```python from vllm import EngineArgs, SamplingParams from vllm.lora.request import LoRARequest from vllm.v1.engine.llm_engine import LLMEngine quantization_config = { "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: NotImplementedError: Method 'get_kv_cache_spec' is not implemented. bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to deploy a llama-3.2b-instruct with finetuned LoRA adapter on a VM with a GPU...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: oRA adapter? The relevant part of the code is as follows (FYI I'm using Flashinfer): ```python from vllm import EngineArgs, SamplingParams from vllm.lora.request import LoRARequest from vllm.v1.engine.llm_engine import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
