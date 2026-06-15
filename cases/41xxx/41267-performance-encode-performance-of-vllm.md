# vllm-project/vllm#41267: [Performance]: Encode performance of vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#41267](https://github.com/vllm-project/vllm/issues/41267) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | sampling |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Encode performance of vLLM

### Issue 正文摘录

### Discussion on performance I am running vLLM with open telemetry tracing enabled to measure time taken in encode. Though vLLM doesn't export spans for encode phase, I assumed that the remaining time during a request processing which is not accounted for in any of the steps. I set max_tokens as 1 so the decode time is almost 0 **Setup** vLLM: v0.19.1 Model/hardware: Qwen-vl 2.5 7B deployed on a h100 80 GB node **Sample Trace** Here is an example trace while processing a 1080p image: gen_ai.latency.e2e | 0.293 seconds -- | -- gen_ai.latency.time_in_model_decode | 0.000 seconds gen_ai.latency.time_in_model_inference | 0.126 seconds gen_ai.latency.time_in_model_prefill | 0.126 seconds gen_ai.latency.time_in_queue | 0.000 seconds gen_ai.latency.time_to_first_token | 0.293 seconds gen_ai.request.max_tokens | 1 gen_ai.request.n | 1 gen_ai.request.temperature | 0.01 gen_ai.request.top_p | 1 gen_ai.usage.completion_tokens | 1 gen_ai.usage.prompt_tokens | 2718 Time taken by encoder | 0.167 seconds **Observations** The time taken to encode is more than prefill, I expected the time to be lower. In general for different image sizes, I found that the encode time is similar order of magnitude...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: max_tokens as 1 so the decode time is almost 0 **Setup** vLLM: v0.19.1 Model/hardware: Qwen-vl 2.5 7B deployed on a h100 80 GB node **Sample Trace** Here is an example trace while processing a 1080p image: gen_ai.latenc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: xport spans for encode phase, I assumed that the remaining time during a request processing which is not accounted for in any of the steps. I set max_tokens as 1 so the decode time is almost 0 **Setup** vLLM: v0.19.1 Mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0 **Setup** vLLM: v0.19.1 Model/hardware: Qwen-vl 2.5 7B deployed on a h100 80 GB node **Sample Trace** Here is an example trace while processing a 1080p image: gen_ai.latency.e2e | 0.293 seconds -- | -- gen_ai.latency....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ce** Here is an example trace while processing a 1080p image: gen_ai.latency.e2e | 0.293 seconds -- | -- gen_ai.latency.time_in_model_decode | 0.000 seconds gen_ai.latency.time_in_model_inference | 0.126 seconds gen_ai....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Discussion on performance I am running vLLM with open telemetry tracing enabled to measure time taken in encode. Though vLLM doesn't export spans for encode phase, I assumed that the remaining time during a request...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
