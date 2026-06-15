# vllm-project/vllm#8326: [Bug]: TimeoutError During Benchmark Profiling with Torch Profiler on vLLM v0.6.0

| 字段 | 值 |
| --- | --- |
| Issue | [#8326](https://github.com/vllm-project/vllm/issues/8326) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TimeoutError During Benchmark Profiling with Torch Profiler on vLLM v0.6.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am attempting to profile the performance of vLLM v0.6.0 by following the [vLLM profiling documentation](https://docs.vllm.ai/en/latest/dev/profiling/profiling_index.html). Here’s the process I followed: 1. Set up the profiler environment: ```bash export VLLM_TORCH_PROFILER_DIR=/app/vllm_profile ``` 2. Launched the OpenAI server: ```bash python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 1 \ --model /mnt/llm_dataset/willhe/ckpt/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 \ --trust-remote-code --max-model-len 8192 ``` 3. Launched the benchmark process: ```bash python benchmark_serving.py --backend vllm --model /mnt/llm_dataset/willhe/ckpt/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 \ --dataset-name sharegpt --dataset-path sharegpt.json --num-prompts 2 --profile ``` 4. Error Encountered: While running the benchmark, I encountered a TimeoutError: Server didn't reply within 5000 ms in the vLLM OpenAI server log. The relevant section of the log is as follows: ```text WARNING 09-10 16:07:55 api_server.py:327] Torch Profiler is enabled in the API server. This should ONLY be used for local development! INFO 09-10 16:07:55 a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: om_all_reduce=False, disable_frontend_multiprocessing=False, disable_log_requests=False, disable_log_stats=False, disable_logprobs_during_spec_decoding=None, disable_sliding_window=False, distributed_executor_backend=No...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ocal development! INFO 09-10 16:07:55 api_server.py:459] vLLM API server version 0.6.0 INFO 09-10 16:07:55 api_server.py:460] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: TimeoutError During Benchmark Profiling with Torch Profiler on vLLM v0.6.0 bug ### Your current environment ### 🐛 Describe the bug I am attempting to profile the performance of vLLM v0.6.0 by following the [vLLM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: size 1 \ --model /mnt/llm_dataset/willhe/ckpt/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 \ --trust-remote-code --max-model-len 8192 ``` 3. Launched the benchmark process: ```bash python benchmark_serving.py --backend vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ython -m vllm.entrypoints.openai.api_server --tensor-parallel-size 1 \ --model /mnt/llm_dataset/willhe/ckpt/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 \ --trust-remote-code --max-model-len 8192 ``` 3. Launched the benchm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
