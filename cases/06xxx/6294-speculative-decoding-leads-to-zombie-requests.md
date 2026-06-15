# vllm-project/vllm#6294: Speculative decoding leads to zombie requests

| 字段 | 值 |
| --- | --- |
| Issue | [#6294](https://github.com/vllm-project/vllm/issues/6294) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | crash;slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Speculative decoding leads to zombie requests

### Issue 正文摘录

### Anything you want to discuss about vllm. when turns on speculative decoding, the openai api server failed on concurrent requests, raising error `exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup`. After all requests finish, there are some zombie tasks in the queue (**Running: 54 reqs**): ``` Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 54 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 47.4%, CPU KV cache usage: 0.0% ``` but the gpu utilization always is zero, and new request reports `Internal Server Error`. This does not happen when turns off speculative decoding. To reproduce the problem: - vllm: 0.5.1 - docker image: nvidia/cuda:12.4.1-base-ubuntu22.04 1. Concurrent test: ``` python3 benchmarks/benchmark_serving.py \ --backend openai-chat \ --endpoint "/chat/completions" \ --model qwen-14b-chat \ --base-url http://[ip]:8000/v1 \ --dataset ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 5 \ --save-result \ --tokenizer /mnt/data/Qwen1.5-14B-Chat/ ``` 2. OpenAI API server - without speculative decoding: ``` python3 -m vllm.entrypoints.openai.api_server \ --served-model-name 'qwen-14b-chat' \ --max-mo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Speculative decoding leads to zombie requests stale ### Anything you want to discuss about vllm. when turns on speculative decoding, the openai api server failed on concurrent requests, raising error `exceptiongroup.Exc
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rns off speculative decoding. To reproduce the problem: - vllm: 0.5.1 - docker image: nvidia/cuda:12.4.1-base-ubuntu22.04 1. Concurrent test: ``` python3 benchmarks/benchmark_serving.py \ --backend openai-chat \ --endpo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: re some zombie tasks in the queue (**Running: 54 reqs**): ``` Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 54 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 47.4%,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1. Concurrent test: ``` python3 benchmarks/benchmark_serving.py \ --backend openai-chat \ --endpoint "/chat/completions" \ --model qwen-14b-chat \ --base-url http://[ip]:8000/v1 \ --dataset ShareGPT_V3_unfiltered_cleane...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --model=Qwen1.5-14B-Chat \ --tensor-parallel-size 2 \ --use-v2-block-manager \ --gpu-memory-utilization 0.95 ``` - with speculative decoding: ``` python3 -m vllm.entrypoints.openai.api_server \ --served-model-name 'qwen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
