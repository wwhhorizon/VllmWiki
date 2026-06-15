# vllm-project/vllm#23415: [Bug]: Florence2-large [rank0]: ValueError: Following weights were not initialized from checkpoint: {'language_model.lm_head.weight'}

| 字段 | 值 |
| --- | --- |
| Issue | [#23415](https://github.com/vllm-project/vllm/issues/23415) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Florence2-large [rank0]: ValueError: Following weights were not initialized from checkpoint: {'language_model.lm_head.weight'}

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python # import os # # NEW: Set the target GPU and limit visibility. # # This line MUST be at the top, before torch or vllm is imported. # # It makes your script see ONLY GPU 3, which it will treat as 'cuda:0'. # os.environ['CUDA_VISIBLE_DEVICES'] = '3' # # TODO(Isotr0py): # # Move to offline_inference_vision_language.py after porting vision backbone # from vllm import LLM, SamplingParams # dtype = "float" # # Create a Florence-2 encoder/decoder model instance # llm = LLM( # model="microsoft/Florence-2-large", # tokenizer="/mnt/driver_g/gsq/hf_cache/Isotr0py/Florence-2-tokenizer", # dtype=dtype, # trust_remote_code=True, # # MODIFIED: Add parameters for GPU and memory control # tensor_parallel_size=1, # Since only one GPU is visible, this must be 1. # gpu_memory_utilization=0.3, # Limit VRAM usage to 30% of the GPU's total memory. # download_dir="/mnt/driver_g/gsq/hf_cache" # ) # prompts = [ # " ", " ", " ", # " ", " ", " ", # " ", " ", " " # ] # # Create a sampling params object. # sampling_params = SamplingParams( # temperature=0, # top_p=1.0, # min_tokens=0, # max_tokens=1024, # ) # # Generate output tokens from the prompts...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: rror: Following weights were not initialized from checkpoint: {'language_model.lm_head.weight'} bug ### Your current environment ### 🐛 Describe the bug ```python # import os # # NEW: Set the target GPU and limit visibil...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: bug ### Your current environment ### 🐛 Describe the bug ```python # import os # # NEW: Set the target GPU and limit visibility. # # This line MUST be at the top, before torch or vllm is imported. # # It makes your scrip...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LLM, SamplingParams # dtype = "float" # # Create a Florence-2 encoder/decoder model instance # llm = LLM( # model="microsoft/Florence-2-large", # tokenizer="/mnt/driver_g/gsq/hf_cache/Isotr0py/Florence-2-tokenizer", # d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: after porting vision backbone # from vllm import LLM, SamplingParams # dtype = "float" # # Create a Florence-2 encoder/decoder model instance # llm = LLM( # model="microsoft/Florence-2-large", # tokenizer="/mnt/driver_g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
