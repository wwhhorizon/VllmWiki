# vllm-project/vllm#8686: [Bug]: RuntimeError on A800 using vllm0.6.1.post2

| 字段 | 值 |
| --- | --- |
| Issue | [#8686](https://github.com/vllm-project/vllm/issues/8686) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError on A800 using vllm0.6.1.post2

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Example of command: python benchmark_throughput.py --trust-remote-code --enforce-eager --dtype float16 --num-prompts 1 --input-len 2 --output-len 128 --model Llama-2-7b-chat-hf Output: Namespace(backend='vllm', dataset=None, input_len=2, output_len=128, model='Llama-2-7b-chat-hf', tokenizer='Llama-2-7b-chat-hf/', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_iters_warmup=1, num_prompts=1, seed=0, hf_max_batch_size=None, trust_remote_code=True, max_model_len=None, dtype='float16', gpu_memory_utilization=0.9, enforce_eager=True, kv_cache_dtype='auto', quantization_param_path=None, device='auto', num_scheduler_steps=1, use_v2_block_manager=False, enable_prefix_caching=False, enable_chunked_prefill=False, max_num_batched_tokens=None, download_dir=None, output_json=None, distributed_executor_backend=None, load_format='auto', disable_async_output_proc=False, async_engine=False, disable_frontend_multiprocessing=False) Traceback (most recent call last): File "/data/test/benchmark_throughput.py", line 617, in main(args) File "/data/test/benchmark_throughput.py", line 382, in...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 800 using vllm0.6.1.post2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Example of command: python benchmark_throughput.py --trust-remote-code --enforce-eager --dtype...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: RuntimeError on A800 using vllm0.6.1.post2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Example of command: python benchmark_throughput.py --trust-remote-code...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding cuda;operator;quantization;triton buil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d: python benchmark_throughput.py --trust-remote-code --enforce-eager --dtype float16 --num-prompts 1 --input-len 2 --output-len 128 --model Llama-2-7b-chat-hf Output: Namespace(backend='vllm', dataset=None, input_len=2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Dumps _No response_ ### 🐛 Describe the bug Example of command: python benchmark_throughput.py --trust-remote-code --enforce-eager --dtype float16 --num-prompts 1 --input-len 2 --output-len 128 --model Llama-2-7b-chat-hf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
