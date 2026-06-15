# vllm-project/vllm#6218: [Feature]: FlashInfer + Gemma 2 for AMD GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#6218](https://github.com/vllm-project/vllm/issues/6218) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 | import_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: FlashInfer + Gemma 2 for AMD GPU

### Issue 正文摘录

This could be question rather than a feature request. flashinfer is not supported for AMD GPUs and it's not currently planned until a [later version](https://github.com/flashinfer-ai/flashinfer/issues/19), Is there a way to run Gemma 2 models on AMD (I'm getting `ValueError: Please use Flashinfer backend for models withlogits_soft_cap (i.e., Gemma-2). Otherwise, the output might be wrong. Set Flashinfer backend by export VLLM_ATTENTION_BACKEND=FLASHINFER.` even though I set the env var. I wanted to give it a try and remove the [validation](https://github.com/vllm-project/vllm/blob/v0.5.1/vllm/attention/selector.py#L137-L147) but it fails with None type because of [import error](https://github.com/vllm-project/vllm/blob/v0.5.1/vllm/attention/backends/flashinfer.py#L4-L11)) ? Or is there an alternative that can be used? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: FlashInfer + Gemma 2 for AMD GPU feature request;rocm;stale This could be question rather than a feature request. flashinfer is not supported for AMD GPUs and it's not currently planned until a [later version...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: not supported for AMD GPUs and it's not currently planned until a [later version](https://github.com/flashinfer-ai/flashinfer/issues/19), Is there a way to run Gemma 2 models on AMD (I'm getting `ValueError: Please use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: FlashInfer + Gemma 2 for AMD GPU feature request;rocm;stale This could be question rather than a feature request. flashinfer is not supported for AMD GPUs and it's not currently planned until a [later version...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: FlashInfer + Gemma 2 for AMD GPU feature request;rocm;stale This could be question rather than a feature request. flashinfer is not supported for AMD GPUs and it's not currently planned until a [later version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: FlashInfer + Gemma 2 for AMD GPU feature request;rocm;stale This could be question rather than a feature request. flashinfer is not supported for AMD GPUs and it's not currently planned until a [later version...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
