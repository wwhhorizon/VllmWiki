# vllm-project/vllm#27886: [Bug]: vLLM 0.10.2/0.11.0 bench serve deadlocks when benchmarking DeepSeek-R1-BF16 (sglang 0.4.7), with processes hanging indefinitely during script execution

| 字段 | 值 |
| --- | --- |
| Issue | [#27886](https://github.com/vllm-project/vllm/issues/27886) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.10.2/0.11.0 bench serve deadlocks when benchmarking DeepSeek-R1-BF16 (sglang 0.4.7), with processes hanging indefinitely during script execution

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Test Script： `vllm bench serve --header Authorization=X --backend openai-chat --base-url X --endpoint /v1/chat/completions --tokenizer X/tokenizer/deepseek --percentile-metrics ttft,tpot,itl,e2el --save-result --result-filename X.json --ignore-eos --trust-remote-code --model DeepSeek-R1 --dataset-name random --random-output-len 1024 --random-input-len 1024 --num-prompts 1 --metric-percentiles 99 --max-concurrency 1 --request-rate 1 --random-range-ratio 0.2` Sglang Deploy Script： `"script": "python3 -m sglang.launch_server --model-path /model/DeepSeek-R1-bf16 --host 0.0.0.0 --port 8000 --tp 16 --context-length 56000 --trust-remote-code --mem-fraction-static 0.9 --enable-metrics --served-model-name DeepSeek-R1" ` Now： `DEBUG 10-31 23:23:20 [plugins/__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 10-31 23:23:20 [platforms/__init__.py:34] Checking if TPU platform is available. DEBUG 10-31 23:23:20 [platforms/__init__.py:52] TPU platform is not available because: No module named 'libtpu' DEBUG 10-31 23:23:20 [platforms/__init__.py:58] Checking if CUDA platform is available. DEBUG 10-31 23:23:20 [platforms/__ini...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: med 'libtpu' DEBUG 10-31 23:23:20 [platforms/__init__.py:58] Checking if CUDA platform is available. DEBUG 10-31 23:23:20 [platforms/__init__.py:78] Confirmed CUDA platform is available. DEBUG 10-31 23:23:20 [platforms/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM 0.10.2/0.11.0 bench serve deadlocks when benchmarking DeepSeek-R1-BF16 (sglang 0.4.7), with processes hanging indefinitely during script execution bug;stale ### Your current environment ### 🐛 Describe the bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: vLLM 0.10.2/0.11.0 bench serve deadlocks when benchmarking DeepSeek-R1-BF16 (sglang 0.4.7), with processes hanging indefinitely during script execution bug;stale ### Your current environment ### 🐛 Describe the bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -save-result --result-filename X.json --ignore-eos --trust-remote-code --model DeepSeek-R1 --dataset-name random --random-output-len 1024 --random-input-len 1024 --num-prompts 1 --metric-percentiles 99 --max-concurrency...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: cribe the bug Test Script： `vllm bench serve --header Authorization=X --backend openai-chat --base-url X --endpoint /v1/chat/completions --tokenizer X/tokenizer/deepseek --percentile-metrics ttft,tpot,itl,e2el --save-re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
