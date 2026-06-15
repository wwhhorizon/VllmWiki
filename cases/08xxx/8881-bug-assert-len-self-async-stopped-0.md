# vllm-project/vllm#8881: [Bug]: assert len(self._async_stopped) == 0

| 字段 | 值 |
| --- | --- |
| Issue | [#8881](https://github.com/vllm-project/vllm/issues/8881) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert len(self._async_stopped) == 0

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are wrapping around vllm's `AsyncLLMEngine`, code can be simplified as below. ``` engine = AsyncLLMEngine.from_engine_args(self.engine_args) ``` and then use `engine` to handle request ``` def request_handler(): engine.generate( inputs=prompt, sampling_params=sampling_params, request_id=request_id, lora_request=lora_request, priority=priority, ) ``` The error is ``` INFO 09-27 03:03:51 llm_engine.py:223] Initializing an LLM engine (v0.6.1.post2) with config: model='/models/mistral-large2', speculative_config=None, tokenizer='/models/mistral-large2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=Obs...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: assert len(self._async_stopped) == 0 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are wrapping around vllm's `AsyncLLMEngine`, code can be simplified as bel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disabl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tput_proc=True) WARNING 09-27 03:03:51 multiproc_gpu_executor.py:56] Reducing Torch parallelism from 96 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: self._async_stopped) == 0 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are wrapping around vllm's `AsyncLLMEngine`, code can be simplified as below. ``` engine = A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
