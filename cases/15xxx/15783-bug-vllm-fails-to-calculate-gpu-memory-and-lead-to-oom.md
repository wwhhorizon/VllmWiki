# vllm-project/vllm#15783: [Bug]: vllm fails to calculate gpu_memory and lead to OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#15783](https://github.com/vllm-project/vllm/issues/15783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm fails to calculate gpu_memory and lead to OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm fails to calculate gpu_memory and lead to OOM. I'm using vllm==0.7.2 and initalize vllm.LLM as ``` llm = LLM( model='Qwen/Qwen2-VL-7B-Instruct', device='cuda:7', gpu_memory_utilization=0.85, dtype=torch.bfloat16, enable_prefix_caching=True, enforce_eager=True, mm_processor_kwargs=self.mm_processor_kwargs, max_model_len=9216, ) ``` The output logs are: ``` vllm is running on: cuda:7 INFO 03-31 01:47:44 config.py:542] This model supports multiple tasks: {'generate', 'classify', 'embed', 'reward', 'score'}. Defaulting to 'generate'. WARNING 03-31 01:47:44 arg_utils.py:1079] --enable-prefix-caching is currently not supported for multimodal models in v0 and has been disabled. WARNING 03-31 01:47:44 cuda.py:95] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used WARNING 03-31 01:47:44 config.py:678] Async output processing is not supported on the current platform type cuda. INFO 03-31 01:47:44 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.2) with config: model='Qwen/Qwen2-VL-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2-VL-7B-I...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: OOM. I'm using vllm==0.7.2 and initalize vllm.LLM as ``` llm = LLM( model='Qwen/Qwen2-VL-7B-Instruct', device='cuda:7', gpu_memory_utilization=0.85, dtype=torch.bfloat16, enable_prefix_caching=True, enforce_eager=True,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm fails to calculate gpu_memory and lead to OOM bug;stale ### Your current environment ### 🐛 Describe the bug vllm fails to calculate gpu_memory and lead to OOM. I'm using vllm==0.7.2 and initalize vllm.LLM as...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -7B-Instruct', device='cuda:7', gpu_memory_utilization=0.85, dtype=torch.bfloat16, enable_prefix_caching=True, enforce_eager=True, mm_processor_kwargs=self.mm_processor_kwargs, max_model_len=9216, ) ``` The output logs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ': 2007040}, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, INFO 03-31 01:47:45 cuda.py:230] Using Flash Atten...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: when initializing LLM are ``` INFO 03-31 02:25:20 worker.py:267] Memory profiling takes 4.95 seconds INFO 03-31 02:25:20 worker.py:267] the current vLLM instance can use total_gpu_memory (79.32GiB) x gpu_memory_utilizat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
