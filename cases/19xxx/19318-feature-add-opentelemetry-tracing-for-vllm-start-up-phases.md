# vllm-project/vllm#19318: [Feature]: Add opentelemetry tracing for vLLM start up phases

| 字段 | 值 |
| --- | --- |
| Issue | [#19318](https://github.com/vllm-project/vllm/issues/19318) |
| 状态 | closed |
| 标签 | feature request;stale;startup-ux |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;operator |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add opentelemetry tracing for vLLM start up phases

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This FR asks for tracing through vLLM cold starts. This would include key phases, as trace spans, leading up to the FastAPI HTTP server is up and running. #17794 is related but asks for tracing requests. Why would this be useful? * To facilitate cold start optimizations, both for vLLM users and contributors. This is important for quick auto scaling of inference workloads in cloud environments. * Users may want to tweak vLLM settings based on which phase is contributig to high latency, e.g. changing how the model is loaded using `--load-format runai_streamer`. * Contributors interested in performance optimization need this data to know which area to focus on and the visual phase breakdown provided by traces is much easier to interpret quickly than logs. This is how I noticed #19317. The set of key spans and their attributes could be iterated on over time but I think it'd be interesting to include at least * Python import time (which is non-trivial) * Model config loading * (Async)LLM init, including setting up tokenizer, output processor, etc. * Setting up the engine core * Loading the model * torch.compile * CUDA graph capture * KV cache ini...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Feature]: Add opentelemetry tracing for vLLM start up phases feature request;stale;startup-ux ### 🚀 The feature, motivation and pitch This FR asks for tracing through vLLM cold starts. This would include key phases, as...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d on which phase is contributig to high latency, e.g. changing how the model is loaded using `--load-format runai_streamer`. * Contributors interested in performance optimization need this data to know which area to foc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ant to tweak vLLM settings based on which phase is contributig to high latency, e.g. changing how the model is loaded using `--load-format runai_streamer`. * Contributors interested in performance optimization need this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: * Setting up the engine core * Loading the model * torch.compile * CUDA graph capture * KV cache init and profile run(s) Similar to existing request tracing in v0 this feature could be opt-in toggled by a flag or enviro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add opentelemetry tracing for vLLM start up phases feature request;stale;startup-ux ### 🚀 The feature, motivation and pitch This FR asks for tracing through vLLM cold starts. This would include key phases, as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
