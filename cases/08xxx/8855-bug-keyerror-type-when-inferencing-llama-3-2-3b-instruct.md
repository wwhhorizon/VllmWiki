# vllm-project/vllm#8855: [Bug]: KeyError: 'type'. when inferencing Llama 3.2 3B Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#8855](https://github.com/vllm-project/vllm/issues/8855) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'type'. when inferencing Llama 3.2 3B Instruct

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Error: ``` KeyError Traceback (most recent call last) [ ](https://localhost:8080/#) in () 14 15 # Create an LLM. ---> 16 llm = LLM( 17 model="meta-llama/Llama-3.2-3B-Instruct", 18 tokenizer="meta-llama/Llama-3.2-3B-Instruct", 4 frames [/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py](https://localhost:8080/#) in __init__(self, model, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, **kwargs) 91 use `float16` instead. 92 quantization: The method used to quantize the model weights. Currently, ---> 93 we support "awq", "gptq", and "fp8" (experimental). 94 If None, we first check the `quantization_config` attribute in the 95 model config file. If that is None, we assume the model weights are [/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py](https://localhost:8080/#) in from_engine_args(cls, engine_args) 238 "decoding_config=%r, observability_config=%r, " 239 "seed=%d, served_model_name=%s, use_v2_block_manager=%s, " --> 240 "num_scheduler_steps=%d, multi_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: KeyError: 'type'. when inferencing Llama 3.2 3B Instruct bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Error: ``` KeyError Traceback (most recent call last) [ ](https...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: KeyError: 'type'. when inferencing Llama 3.2 3B Instruct bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Error: ``` KeyError Traceback (most recent call last) [ ](htt
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: del, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, **kwargs) 91 use `float16` instead. 92 quantization:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ors into the model when KV cache ---> 93 type is FP8_E4M3 on ROCm (AMD GPU). In the future these will also 94 be used to load activation and weight scaling factors when the 95 model dtype is FP8_E4M3 on ROCm. [/usr/loca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: erved_model_name=%s, use_v2_block_manager=%s, " --> 240 "num_scheduler_steps=%d, multi_step_stream_outputs=%s, " 241 "enable_prefix_caching=%s, use_async_output_proc=%s, " 242 "use_cached_outputs=%s, mm_processor_kwargs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
