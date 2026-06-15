# vllm-project/vllm#16681: [Bug]: Mistral Small 3.1 fails to load with mistal tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#16681](https://github.com/vllm-project/vllm/issues/16681) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral Small 3.1 fails to load with mistal tokenizer

### Issue 正文摘录

### Your current environment Trying to load Mistral Small 3.1 in RunPod on vLLM 0.8.4 (latest) with the following arguments: `--host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.1-24B-Instruct-2503 --gpu-memory-utilization 0.75 --tensor-parallel-size 2 --tokenizer-mode mistral` Model loads fine and works if you remove `--tokenizer-mode mistral`. Otherwise throws the following errors: ### 🐛 Describe the bug ```text INFO 04-15 13:23:10 [core.py:61] Initializing a V1 LLM engine (v0.8.4) with config: model='mistralai/Mistral-Small-3.1-24B-Instruct-2503', speculative_config=None, tokenizer='mistralai/Mistral-Small-3.1-24B-Instruct-2503', skip_tokenizer_init=False, tokenizer_mode=mistral, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=F...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Mistral Small 3.1 fails to load with mistal tokenizer bug;stale ### Your current environment Trying to load Mistral Small 3.1 in RunPod on vLLM 0.8.4 (latest) with the following arguments: `--host 0.0.0.0 --port...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disabl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Mistral Small 3.1 fails to load with mistal tokenizer bug;stale ### Your current environment Trying to load Mistral Small 3.1 in RunPod on vLLM 0.8.4 (latest) with the following arguments: `--host 0.0.0.0 --port...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 8.4 (latest) with the following arguments: `--host 0.0.0.0 --port 8000 --model mistralai/Mistral-Small-3.1-24B-Instruct-2503 --gpu-memory-utilization 0.75 --tensor-parallel-size 2 --tokenizer-mode mistral` Model loads f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
