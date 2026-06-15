# vllm-project/vllm#17489: [Bug]:  VisionArena Benchmark for Vision Language Models (with `benchmark_serving.py`) crashes with `Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Forbidden`

| 字段 | 值 |
| --- | --- |
| Issue | [#17489](https://github.com/vllm-project/vllm/issues/17489) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  VisionArena Benchmark for Vision Language Models (with `benchmark_serving.py`) crashes with `Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Forbidden`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary tldr; the benchmark example [VisionArena Benchmark for Vision Language Models](https://github.com/vllm-project/vllm/tree/main/benchmarks#visionarena-benchmark-for-vision-language-models), leads to `ValueError: Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Forbidden` when running the benchmark script. ## Reproducer taken from here: https://github.com/vllm-project/vllm/tree/main/benchmarks#visionarena-benchmark-for-vision-language-models ``` vllm serve Qwen/Qwen2-VL-7B-Instruct --disable-log-requests --trust-remote-code . . . INFO 04-30 17:52:42 [serving_chat.py:118] Using default chat sampling params from model: {'temperature': 0.01, 'top_k': 1, 'top_p': 0.001} INFO 04-30 17:52:43 [serving_completion.py:61] Using default completion sampling params from model: {'temperature': 0.01, 'top_k': 1, 'top_p': 0.001} INFO 04-30 17:52:43 [api_server.py:1090] Starting vLLM API server on http://0.0.0.0:8000 INFO 04-30 17:52:43 [launcher.py:28] Available routes are: INFO 04-30 17:52:43 [launcher.py:36] Route: /openapi.json, Methods: HEAD, GET INFO 04-30 17:52:43 [launcher.py:36] Route...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: VisionArena Benchmark for Vision Language Models (with `benchmark_serving.py`) crashes with `Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Forbidden` bug;stale ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: test run failed - Please make sure benchmark arguments are correctly specified. Error: Forbidden` bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary tldr; the benchmark example [VisionArena Benchma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: sure benchmark arguments are correctly specified. Error: Forbidden` bug;stale ### Your current environment ### 🐛 Describe the bug ## Summary tldr; the benchmark example [VisionArena Benchmark for Vision Language Models]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: VisionArena Benchmark for Vision Language Models (with `benchmark_serving.py`) crashes with `Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Forbidden` bug;stale ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lete. ``` benchmark ``` python3 vllm/benchmarks/benchmark_serving.py --backend openai-chat --model Qwen/Qwen2-VL-7B-Instruct --endpoint /v1/chat/completions --dataset-name hf --dataset-path lmarena-ai/VisionArena-Chat -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
