# vllm-project/vllm#3209: IMPORTANT Bug: Model return empty response (output len = 0), when recieved multiple concurrent request.

| 字段 | 值 |
| --- | --- |
| Issue | [#3209](https://github.com/vllm-project/vllm/issues/3209) |
| 状态 | closed |
| 标签 |  |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | nan_inf |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> IMPORTANT Bug: Model return empty response (output len = 0), when recieved multiple concurrent request.

### Issue 正文摘录

When I did a bunch of load test the vLLM endpoint with OpenAI API, I see that the server will return 20% to 50% empty responses when it recieved multiple concurrent request. Configuration: ``` vLLM==0.3.0 Model: Zephyr-7b-beta, although it even worse with bigger model like Llama-2-70b and Mixtral 8x7b Cuda 12.2 1 x A100 80GB GPU ``` Number of concurrent request: 100, request rate set as default = "inf", meaning 100 request will be send concurrently. How to replicate: I'm using latest benchmark_serving.py (5.3.2024) with following modification: I comment out L69-L72: https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py#L69 and modify following: - Line 88 to: ``` if prompt_len MAX_PROMPT_LEN or output_len > MAX_OUTPUT_LEN: ``` and set the params like that: ``` MIN_PROMPT_LEN = 400 MAX_PROMPT_LEN = 700 MAX_OUTPUT_LEN= 300 MIN_OUTPUT_LEN= 100 ``` Moreover, since in the current code of https://github.com/vllm-project/vllm/blob/main/benchmarks/backend_request_func.py#L265 doesn't check for the output len, I need to add 2 more line of code like this: ``` if generated_text=="": output.success = False else: output.success = True ``` With above configuration, the s...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: though it even worse with bigger model like Llama-2-70b and Mixtral 8x7b Cuda 12.2 1 x A100 80GB GPU ``` Number of concurrent request: 100, request rate set as default = "inf", meaning 100 request will be send concurren...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: IMPORTANT Bug: Model return empty response (output len = 0), when recieved multiple concurrent request. When I did a bunch of load test the vLLM endpoint with OpenAI API, I see that the server will return 20% to 50% emp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: IMPORTANT Bug: Model return empty response (output len = 0), when recieved multiple concurrent request. When I did a bunch of load test the vLLM endpoint with OpenAI API, I see that the server will return 20% to 50% empt
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ), when recieved multiple concurrent request. When I did a bunch of load test the vLLM endpoint with OpenAI API, I see that the server will return 20% to 50% empty responses when it recieved multiple concurrent request....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: urrent code of https://github.com/vllm-project/vllm/blob/main/benchmarks/backend_request_func.py#L265 doesn't check for the output len, I need to add 2 more line of code like this: ``` if generated_text=="": output.succ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
