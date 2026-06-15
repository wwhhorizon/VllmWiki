# vllm-project/vllm#10626: [Bug]: about NCCL error：unhandled system error

| 字段 | 值 |
| --- | --- |
| Issue | [#10626](https://github.com/vllm-project/vllm/issues/10626) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: about NCCL error：unhandled system error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug tensor_parallel_size = 1 no nccl error tensor_parallel_size > 1 will get nccl error ``` self.llm = LLM( model=model_name, tensor_parallel_size=tensor_parallel_size, limit_mm_per_prompt={"image": 25, "video": 1}, max_model_len=32700 ) ``` ``` use_vllm: True tensor_parallel_size: 2 use_vllm2 True vllm INFO 11-25 08:17:27 config.py:350] This model supports multiple tasks: {'generate', 'embedding'}. Defaulting to 'generate'. INFO 11-25 08:17:27 config.py:1020] Defaulting to use mp for distributed inference INFO 11-25 08:17:27 llm_engine.py:249] Initializing an LLM engine (v0.6.4.post1) with config: model='../models/Qwen2-VL-7B-Instruct', speculative_config=None, tokenizer='../models/Qwen2-VL-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32700, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=N...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er_config=None) WARNING 11-25 08:17:28 multiproc_gpu_executor.py:56] Reducing Torch parallelism from 43 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32700, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CL error：unhandled system error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug tensor_parallel_size = 1 no nccl error tensor_parallel_size > 1 will get nccl error ``` self.ll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: gine (v0.6.4.post1) with config: model='../models/Qwen2-VL-7B-Instruct', speculative_config=None, tokenizer='../models/Qwen2-VL-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
