# vllm-project/vllm#19352: [Bug]: v1 performs worse than v0 at high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#19352](https://github.com/vllm-project/vllm/issues/19352) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v1 performs worse than v0 at high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found that v1 has a worse rps than v0 at 64 concurrency, and I'm really curious about the reason. Here is the script I used to start vllm serve: ``` vllm serve ../../data/huggingface.co/Qwen/Qwen3-32B \ --max-model-len=16384 \ -tp 2 \ --disable-log-requests \ --no-enable-prefix-caching \ ``` And I used `genai-perf` to test the performance: ``` genai-perf profile -m ../../data/huggingface.co/Qwen/Qwen3-32B \ --url http://127.0.0.1:8000 \ --endpoint-type chat \ --streaming \ --tokenizer ../../data/huggingface.co/Qwen/Qwen3-32B \ --endpoint v1/chat/completions \ -H 'Content-Type: application/json' \ --stability-percentage 999 \ --warmup-request-count 5 \ --artifact-dir ./outputs/genai-perf/v1 \ --request-count 128 \ --concurrency 64 \ --input-file ./dataset/allinput_genai_perf.jsonl \ --output-tokens-mean 500 \ --output-tokens-stddev 0 ``` Here is the result I got: v1: ``` Model: qwen3-32b rps: 0.457 TTFT mean (ms): 48302.740 TPOT mean (ms): 146.232 Model: deepseek-r1-distilled-qwen-32b rps: 0.376 TTFT mean (ms): 57105.977 TPOT mean (ms): 214.476 ``` v0 (--no-enable-chunked-prefill): ``` Model: qwen3-32b rps: 0.472 TTFT mean (ms):...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: is the script I used to start vllm serve: ``` vllm serve ../../data/huggingface.co/Qwen/Qwen3-32B \ --max-model-len=16384 \ -tp 2 \ --disable-log-requests \ --no-enable-prefix-caching \ ``` And I used `genai-perf` to te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: s \ --no-enable-prefix-caching \ ``` And I used `genai-perf` to test the performance: ``` genai-perf profile -m ../../data/huggingface.co/Qwen/Qwen3-32B \ --url http://127.0.0.1:8000 \ --endpoint-type chat \ --streaming...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: \ --max-model-len=16384 \ -tp 2 \ --disable-log-requests \ --no-enable-prefix-caching \ ``` And I used `genai-perf` to test the performance: ``` genai-perf profile -m ../../data/huggingface.co/Qwen/Qwen3-32B \ --url htt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
