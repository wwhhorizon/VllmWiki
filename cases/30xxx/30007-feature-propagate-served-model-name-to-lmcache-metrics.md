# vllm-project/vllm#30007: [Feature]: Propagate served-model-name to LMCache metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#30007](https://github.com/vllm-project/vllm/issues/30007) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Propagate served-model-name to LMCache metrics

### Issue 正文摘录

## **Feature Request: Propagate `served-model-name` to LMCache metrics** ### **Summary** When running vLLM using the OpenAI-compatible API, the `--served-model-name` parameter is not propagated to LMCache-related Prometheus metrics. Instead, the internal `model_name` label reflects the underlying model path (e.g. `/huggingface/cache/.../DeepSeek-V3-0324`). This makes it difficult to correlate metrics with the externally-exposed model name, especially when multiple served aliases point to the same model or when deployments rely on logical model names rather than filesystem paths. ### **Current Behavior** Running vLLM with: ``` --served-model-name deepseek-v3-0324-longrunning --kv-transfer-config='{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' ``` Yields metrics such as: ``` lmcache_local_cache_usage{ model_name="/huggingface/cache/hub/deepseek-ai/DeepSeek-V3-0324", ... } ``` The `model_name` label is always the internal model path, not the served alias. ### **Requested Behavior** Expose `served-model-name` in LMCache-related metrics, such as: * Replace `model_name` with the served name **or** * Add a second label, e.g. `served_model_name`, while preserving the internal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Propagate served-model-name to LMCache metrics feature request;stale ## **Feature Request: Propagate `served-model-name` to LMCache metrics** ### **Summary** When running vLLM using the OpenAI-compatible API,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Propagate served-model-name to LMCache metrics feature request;stale ## **Feature Request: Propagate `served-model-name` to LMCache metrics** ### **Summary** When running vLLM using the OpenAI-compatible API,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fficult to correlate metrics with the externally-exposed model name, especially when multiple served aliases point to the same model or when deployments rely on logical model names rather than filesystem paths. ### **Cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sed Implementation** * Inject `served-model-name` into the worker model metadata. * When generating LMCache metrics, add it as an additional Prometheus label. * Backward-compatible: existing label values unchanged. ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
