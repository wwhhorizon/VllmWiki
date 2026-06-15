# vllm-project/vllm#33418: [Bug]: wrong error reported when len(prompt) + requested tokens > max_context_len

| 字段 | 值 |
| --- | --- |
| Issue | [#33418](https://github.com/vllm-project/vllm/issues/33418) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: wrong error reported when len(prompt) + requested tokens > max_context_len

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running `vllm serve` and sending requests where `request.max_tokens max_model_len`, the output error is wrong, with maximum context length not matching the real model context's length * Serving command: ``` vllm serve ./llama-194m --max-model-len 2048 ``` * Request where `request.max_tokens > max_model_len`: as expected ✅ ``` # Sending request curl -X 'POST' 'http://localhost:8000/v1/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "model": "./llama-194m", "prompt": "What is the capital of France?", "max_tokens": 2049 }' # Error message is as expected {"error":{"message":"'max_tokens' (2049) cannot be greater than the model's maximum context length (2048). (parameter=max_tokens, value=2049)","type":"BadRequestError","param":"max_tokens","code":400}} ``` * Request where `request.max_tokens max_model_len`: wrong model's maximum context lengths ❌ ``` # Sending request curl -X 'POST' 'http://localhost:8000/v1/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "model": "./llama-194m", "prompt": "What is the capital of France?", "max_tokens": 2045 }'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support cuda build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: unning `vllm serve` and sending requests where `request.max_tokens max_model_len`, the output error is wrong, with maximum context length not matching the real model context's length * Serving command: ``` vllm serve ./...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: wrong error reported when len(prompt) + requested tokens > max_context_len bug ### Your current environment ### 🐛 Describe the bug When running `vllm serve` and sending requests where `request.max_tokens max_mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support cuda build_error env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
