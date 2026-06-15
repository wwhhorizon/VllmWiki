# vllm-project/vllm#12958: [Bug]: VLLM_USE_V1=1 VLLM_CUDA_MEM_ALIGN_KV_CACHE=1 Failed with DeepSeek-R1

| 字段 | 值 |
| --- | --- |
| Issue | [#12958](https://github.com/vllm-project/vllm/issues/12958) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM_USE_V1=1 VLLM_CUDA_MEM_ALIGN_KV_CACHE=1 Failed with DeepSeek-R1

### Issue 正文摘录

### Your current environment VLLM_USE_V1=1 VLLM_CUDA_MEM_ALIGN_KV_CACHE=1 python3 -m vllm.entrypoints.openai.api_server --model DeepSeek-R1 --tokenizer DeepSeek-R1 --tensor-parallel-size 8 --max-num-batched-tokens 4096 --gpu-memory-utilization 0.95 --trust-remote-code ### 🐛 Describe the bug 10|deepseek-r1 | INFO 02-08 11:13:31 config.py:542] This model supports multiple tasks: {'classify', 'reward', 'score', 'generate', 'embed'}. Defaulting to 'generate'. 10|deepseek-r1 | INFO 02-08 11:13:31 config.py:1401] Defaulting to use mp for distributed inference 10|deepseek-r1 | INFO 02-08 11:13:31 config.py:1556] Chunked prefill is enabled with max_num_batched_tokens=4096. 10|deepseek-r1 | WARNING 02-08 11:13:31 fp8.py:52] Detected fp8 checkpoint. Please note that the format is experimental and subject to change. 10|deepseek-r1 | INFO 02-08 11:13:31 core.py:47] Initializing a V1 LLM engine (v0.7.2) with config: model='/fdata_llm/models/DeepSeek-R1/', speculative_config=None, tokenizer='/fdata_llm/models/DeepSeek-R1/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_le...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: th max_num_batched_tokens=4096. 10|deepseek-r1 | WARNING 02-08 11:13:31 fp8.py:52] Detected fp8 checkpoint. Please note that the format is experimental and subject to change. 10|deepseek-r1 | INFO 02-08 11:13:31 core.py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: inference 10|deepseek-r1 | INFO 02-08 11:13:31 config.py:1556] Chunked prefill is enabled with max_num_batched_tokens=4096. 10|deepseek-r1 | WARNING 02-08 11:13:31 fp8.py:52] Detected fp8 checkpoint. Please note that th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: VLLM_USE_V1=1 VLLM_CUDA_MEM_ALIGN_KV_CACHE=1 Failed with DeepSeek-R1 bug ### Your current environment VLLM_USE_V1=1 VLLM_CUDA_MEM_ALIGN_KV_CACHE=1 python3 -m vllm.entrypoints.openai.api_server --model DeepSeek-R1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: UDA_MEM_ALIGN_KV_CACHE=1 python3 -m vllm.entrypoints.openai.api_server --model DeepSeek-R1 --tokenizer DeepSeek-R1 --tensor-parallel-size 8 --max-num-batched-tokens 4096 --gpu-memory-utilization 0.95 --trust-remote-code...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
