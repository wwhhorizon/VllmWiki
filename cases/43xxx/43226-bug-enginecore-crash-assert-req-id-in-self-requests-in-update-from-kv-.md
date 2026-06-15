# vllm-project/vllm#43226: [Bug]: EngineCore crash — assert req_id in self.requests in _update_from_kv_xfer_finished when an async KV connector reports a finished transfer for an aborted/freed request

| 字段 | 值 |
| --- | --- |
| Issue | [#43226](https://github.com/vllm-project/vllm/issues/43226) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8 |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineCore crash — assert req_id in self.requests in _update_from_kv_xfer_finished when an async KV connector reports a finished transfer for an aborted/freed request

### Issue 正文摘录

### 🐛 Describe the bug `Scheduler._update_from_kv_xfer_finished` asserts that every connector-reported finished transfer still belongs to a live request: ```python # vllm/v1/core/sched/scheduler.py (present on main as of 2026-05-20) for req_id in kv_connector_output.finished_recving or (): logger.debug("Finished recving KV transfer for request %s", req_id) assert req_id in self.requests # vllm.v1.engine.exceptions.EngineDeadError ``` This is the classic "abort races an in-flight async KV transfer" double-free/stale-id scenario. ### Why #33377 does not fully fix this PR #33377 ("avoid vllm-side double free during async scheduling + request abort + async KV cache transfer", merged 2026-02-03) addressed exactly this class of race — but **only in `update_from_output`**, which now tolerates already-gone requests: ```python # update_from_output (post-#33377) request = self.requests.get(req_id) if request is None or request.is_finished(): # The request is already finished. This can happen if the # request is aborted while the model is executing it ... # NOTE: When delay_free_blocks=True (for async KV cache transfer # in KV connector) ... continue ``` The sibling path **`_update_from_kv_x...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: EngineCore crash — assert req_id in self.requests in _update_from_kv_xfer_finished when an async KV connector reports a finished transfer for an aborted/freed request ### 🐛 Describe the bug `Scheduler._update_fro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: routing transfers to non-owning sub-connectors. That fix is connector-specific and does not cover a single async connector reporting a finished transfer for an already-freed request. This issue is the general scheduler-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uction with `LMCacheMPConnector` (LMCache multi-process mode) on GLM-5.1-FP8, TP=8, vLLM v0.20.1 — ~9.5h MTBF under real traffic (the crash needs an abort to coincide with an in-flight async KV transfer, so it's a low-r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eady finished. This can happen if the # request is aborted while the model is executing it ... # NOTE: When delay_free_blocks=True (for async KV cache transfer # in KV connector) ... continue ``` The sibling path **`_up...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: shed sets from completing async futures without re-checking engine ownership, but per the analysis above the robust, connector-agnostic fix belongs in the scheduler. ### Environment vLLM v0.20.1 (assert also present unc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
