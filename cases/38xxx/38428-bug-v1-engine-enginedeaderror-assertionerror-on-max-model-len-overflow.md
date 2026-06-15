# vllm-project/vllm#38428: [Bug]: V1 Engine: EngineDeadError (AssertionError) on max_model_len overflow during realtime audio streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#38428](https://github.com/vllm-project/vllm/issues/38428) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;nan_inf |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine: EngineDeadError (AssertionError) on max_model_len overflow during realtime audio streaming

### Issue 正文摘录

When using the V1 engine/scheduler with a realtime audio model (e.g., `mistralai/Voxtral-Mini-4B-Realtime-2602`), reaching the `max_model_len` limit results in a hard crash (`EngineDeadError`) of the entire engine instead of a graceful termination of the stream. In a realtime audio streaming context, continuous token growth is expected. Currently, hitting the max token limit mid-stream triggers a strict token accounting assertion (`AssertionError: Sampled token IDs exceed the max model length`) in the V1 scheduler (`gpu_model_runner.py`). This brings down the engine core entirely, rather than simply stopping the generation for that specific request with a `finish_reason="length"`. **Steps to Reproduce:** 1. Start vLLM with the V1 engine and a realtime audio model. 2. Stream audio continuously from a client without explicitly closing or resetting the connection. 3. Once the context reaches `max_model_len` (in this case, 4096), the engine crashes with `EngineDeadError`. **Environment / Configuration:** * **Model:** `mistralai/Voxtral-Mini-4B-Realtime-2602` * **vLLM (v0.18.0 with V1 Engine)** via Docker on a single RTX 5060 Ti 16GB (CUDA 13.1). * **Command / Setup:** `docker build -t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ne core entirely, rather than simply stopping the generation for that specific request with a `finish_reason="length"`. **Steps to Reproduce:** 1. Start vLLM with the V1 engine and a realtime audio model. 2. Stream audi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: V1 Engine: EngineDeadError (AssertionError) on max_model_len overflow during realtime audio streaming bug When using the V1 engine/scheduler with a realtime audio model (e.g., `mistralai/Voxtral-Mini-4B-Realtime-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ealtime-2602` * **vLLM (v0.18.0 with V1 Engine)** via Docker on a single RTX 5060 Ti 16GB (CUDA 13.1). * **Command / Setup:** `docker build -t vllm-voxtral-audio .` Dockerfile ```dockerfile FROM vllm/vllm-openai:v0.18.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: en overflow during realtime audio streaming bug When using the V1 engine/scheduler with a realtime audio model (e.g., `mistralai/Voxtral-Mini-4B-Realtime-2602`), reaching the `max_model_len` limit results in a hard cras...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n for that specific request with a `finish_reason="length"`. **Steps to Reproduce:** 1. Start vLLM with the V1 engine and a realtime audio model. 2. Stream audio continuously from a client without explicitly closing or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
