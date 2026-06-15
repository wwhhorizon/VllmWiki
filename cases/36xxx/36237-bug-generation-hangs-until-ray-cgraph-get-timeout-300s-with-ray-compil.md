# vllm-project/vllm#36237: [Bug]: Generation hangs until RAY_CGRAPH_get_timeout (300s) with Ray compiled DAG executor

| 字段 | 值 |
| --- | --- |
| Issue | [#36237](https://github.com/vllm-project/vllm/issues/36237) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Generation hangs until RAY_CGRAPH_get_timeout (300s) with Ray compiled DAG executor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vLLM's Ray executor with a compiled DAG (CGRAPH), generation hangs indefinitely. After 300 seconds (`RAY_CGRAPH_get_timeout`), a `RayChannelTimeoutError` is raised from inside `_execute_dag`: ``` ray.exceptions.RayChannelTimeoutError: System error: If the execution is expected to take a long time, increase RAY_CGRAPH_get_timeout which is currently 300 seconds. Otherwise, this may indicate that the execution is hanging. ``` The hang occurs at `refs[0].get()` in `vllm/v1/executor/ray_executor.py`, which blocks waiting on a Ray shared memory channel that never delivers output. This suggests that the underlying GPU worker(s) either hung silently or failed without the DAG detecting it, leaving rank-0 blocked indefinitely. ### Error Info ``` File "vllm/entrypoints/llm.py", line 1981, in _run_engine step_outputs = self.llm_engine.step() File "vllm/v1/engine/llm_engine.py", line 301, in step outputs = self.engine_core.get_output() File "vllm/v1/engine/core_client.py", line 283, in get_output outputs, model_executed = self.engine_core.step_fn() File "vllm/v1/engine/core.py", line 396, in step model_output = self.model_executor....

## 现有链接修复摘要

#41218 fix: convert LogprobsLists to lists for cross node Ray transport (#38602)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Generation hangs until RAY_CGRAPH_get_timeout (300s) with Ray compiled DAG executor bug ### Your current environment ### 🐛 Describe the bug When using vLLM's Ray executor with a compiled DAG (CGRAPH), generation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ll. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s at `refs[0].get()` in `vllm/v1/executor/ray_executor.py`, which blocks waiting on a Ray shared memory channel that never delivers output. This suggests that the underlying GPU worker(s) either hung silently or failed...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Additional Context This was observed when running vLLM as a generation backend inside a Ray actor (`VllmGenerationWorker`) in [NeMo-RL](https://github.com/NVIDIA-NeMo/RL). The hang is intermittent — it occurs after seve...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g occurs at `refs[0].get()` in `vllm/v1/executor/ray_executor.py`, which blocks waiting on a Ray shared memory channel that never delivers output. This suggests that the underlying GPU worker(s) either hung silently or...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41218](https://github.com/vllm-project/vllm/pull/41218) | mentioned | 0.6 | fix: convert LogprobsLists to lists for cross node Ray transport (#38602) | e work check Per `AGENTS.md` I checked open issues and PRs first: - #36237 (Generation hangs until `RAY_CGRAPH_get_timeout`): same crash class, different surface (TP only). The `R… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
