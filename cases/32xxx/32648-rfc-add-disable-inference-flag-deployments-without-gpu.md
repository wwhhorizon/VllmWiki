# vllm-project/vllm#32648: [RFC]: Add --disable-inference flag deployments without GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#32648](https://github.com/vllm-project/vllm/issues/32648) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add --disable-inference flag deployments without GPU

### Issue 正文摘录

### Motivation. When deploying vLLM as a sidecar (e.g., in llm-d), there are cases where only the render API (#32473) is needed for preprocessing/tokenization, while inference is handled by separate GPU pods. Currently, vLLM requires GPU initialization even when inference is not used. ## Related RFCs This proposal is related to the following RFCs: - https://github.com/vllm-project/vllm/issues/22817 - https://github.com/vllm-project/vllm/issues/22880 While those RFCs propose a comprehensive architectural redesign, this proposal offers a minimal, short-term solution that can be used until the full disaggregation is implemented. ### Proposed Change. Add a `--disable-inference` flag that: - Skips engine core initialization - Uses a no-op client (`AsyncMPClientNoInference`) instead of `AsyncMPClient` - Allows running vLLM frontend without GPU ## Use Case - llm-d sidecar deployments that only use [render API](https://github.com/vllm-project/vllm/pull/32473) (`/v1/chat/completions/render`, `/v1/completions/render`) for preprocessing/tokenization - Inference is handled by separate GPU pods, so the sidecar doesn't need GPU ## Proposed Implementation ### 1. Add config field (`vllm/config/vl...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vllm-project/vllm/issues/22880 While those RFCs propose a comprehensive architectural redesign, this proposal offers a minimal, short-term solution that can be used until the full disaggregation is implemented. ### Prop...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ient.py`) ```python class AsyncMPClientNoInference(MPClient): """Asyncio-compatible client that skips engine core for no-inference mode.""" def __init__( self, vllm_config: VllmConfig, executor_class: type[Executor], lo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: python @config class VllmConfig: ... disable_inference: bool = False """Disable inference and use a no-op engine client.""" ``` ### 2. Add CLI argument (`vllm/engine/arg_utils.py`) ```python vllm_group.add_argument( "--...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: so the sidecar doesn't need GPU ## Proposed Implementation ### 1. Add config field (`vllm/config/vllm.py`) ```python @config class VllmConfig: ... disable_inference: bool = False """Disable inference and use a no-op eng...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Add --disable-inference flag deployments without GPU RFC;stale ### Motivation. When deploying vLLM as a sidecar (e.g., in llm-d), there are cases where only the render API (#32473) is needed for preprocessing/tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
