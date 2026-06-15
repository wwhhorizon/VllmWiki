# vllm-project/vllm#12661: [Bug]: Dump when using VLLM_USE_V1 in version 7.0.1 with RTX 4090 or GPU L4 x 4

| 字段 | 值 |
| --- | --- |
| Issue | [#12661](https://github.com/vllm-project/vllm/issues/12661) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash;import_error;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dump when using VLLM_USE_V1 in version 7.0.1 with RTX 4090 or GPU L4 x 4

### Issue 正文摘录

### Your current environment ### Model Input Dumps -------------------------------------------------------------------------- TypeError Traceback (most recent call last) in () 160 return sorted(outputs, key=lambda x: int(x.request_id)) 161 --> 162 llm = LimitLLM( 163 llm_model_pth, 164 #dtype="half", # The data type for the model weights and activations /usr/local/lib/python3.10/dist-packages/vllm/utils.py in inner(*args, **kwargs) 1037 ) 1038 -> 1039 return fn(*args, **kwargs) 1040 1041 return inner # type: ignore /usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py in __init__(self, model, tokenizer, tokenizer_mode, skip_tokenizer_init, trust_remote_code, allowed_local_media_path, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture, disable_custom_all_reduce, disable_async_output_proc, hf_overrides, mm_processor_kwargs, task, override_pooler_config, compilation_config, **kwargs) 238 # to avoid import order issues 239 self.engine_class = self.get_engine_class() --> 240 self.llm_engine = self.engine_class.from_engine_args( 241 engine_args, usage_context=U...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Dump when using VLLM_USE_V1 in version 7.0.1 with RTX 4090 or GPU L4 x 4 bug ### Your current environment ### Model Input Dumps -------------------------------------------------------------------------- TypeError...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Dump when using VLLM_USE_V1 in version 7.0.1 with RTX 4090 or GPU L4 x 4 bug ### Your current environment ### Model Input Dumps -------------------------------------------------------------------------- TypeError...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 0.1 with RTX 4090 or GPU L4 x 4 bug ### Your current environment ### Model Input Dumps -------------------------------------------------------------------------- TypeError Traceback (most recent call last) in () 160 ret...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 161 --> 162 llm = LimitLLM( 163 llm_model_pth, 164 #dtype="half", # The data type for the model weights and activations /usr/local/lib/python3.10/dist-packages/vllm/utils.py in inner(*args, **kwargs) 1037 ) 1038 -> 1039
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ing cuda;fp8;operator;quantization;triton build_error;crash;import_error;nondeterministic dtype;env_dependency;race_condition Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
