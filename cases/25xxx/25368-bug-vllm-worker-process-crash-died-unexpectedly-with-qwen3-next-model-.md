# vllm-project/vllm#25368: [Bug]: vLLM Worker Process Crash (died unexpectedly) with Qwen3-Next Model when Enabling MTP on NVIDIA A800

| 字段 | 值 |
| --- | --- |
| Issue | [#25368](https://github.com/vllm-project/vllm/issues/25368) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Worker Process Crash (died unexpectedly) with Qwen3-Next Model when Enabling MTP on NVIDIA A800

### Issue 正文摘录

### Your current environment **vLLM Version**: 0.10.2 **Model**: Qwen3-Next **Hardware**: NVIDIA A800 GPUs **Startup Command**: The engine was configured with speculative decoding: `speculative_config=SpeculativeConfig(method='qwen3_next_mtp', model='/model', num_spec_tokens=2) # <-- CRASH CONDITION` **Other Relevant Config:** tensor_parallel_size=4 max_seq_len=131072 ### 🐛 Describe the bug I'm experiencing a consistent and fatal crash when running the Qwen3-Next model on NVIDIA A800 GPUs using vLLM. The crash occurs specifically and only when MTP speculative decoding is enabled. The worker process dies unexpectedly, leading to a complete shutdown of the executor. The model operates perfectly normally and is stable under high load when MTP is disabled. When enable MTP, with the configuration of 100 input tokens, 1000 output tokens, and 128 concurrent requests, we can stably reproduce this issue. **Error info：** `Engine 000: Avg prompt throughput: 108.0 tokens/s, Avg generation throughput: 138.7 tokens/s, Running: 128 reqs, Waiting: 0 reqs, GPU KV cache usage: 19.8%, Prefix cache hit rate: 0.0% SpecDecoding metrics: Mean acceptance length: 2.25, Accepted throughput: 76.61 tokens/s,...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: **: NVIDIA A800 GPUs **Startup Command**: The engine was configured with speculative decoding: `speculative_config=SpeculativeConfig(method='qwen3_next_mtp', model='/model', num_spec_tokens=2) # <-- CRASH CONDITION` **O...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_siz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hen Enabling MTP on NVIDIA A800 bug ### Your current environment **vLLM Version**: 0.10.2 **Model**: Qwen3-Next **Hardware**: NVIDIA A800 GPUs **Startup Command**: The engine was configured with speculative decoding: `s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM Worker Process Crash (died unexpectedly) with Qwen3-Next Model when Enabling MTP on NVIDIA A800 bug ### Your current environment **vLLM Version**: 0.10.2 **Model**: Qwen3-Next **Hardware**: NVIDIA A800 GPUs...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ='/model', num_spec_tokens=2), tokenizer='/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
