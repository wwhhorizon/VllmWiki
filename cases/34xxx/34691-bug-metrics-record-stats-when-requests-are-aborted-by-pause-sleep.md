# vllm-project/vllm#34691: [Bug][Metrics] - record stats when requests are aborted by pause/sleep

| 字段 | 值 |
| --- | --- |
| Issue | [#34691](https://github.com/vllm-project/vllm/issues/34691) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Metrics] - record stats when requests are aborted by pause/sleep

### Issue 正文摘录

From https://github.com/vllm-project/vllm/pull/34528#discussion_r2813379522 In engine core, we do: ``` @staticmethod def _send_abort_outputs( output_queue: queue.Queue[tuple[int, EngineCoreOutputs] | bytes], aborted_reqs: list[tuple[str, int]], ) -> None: ... outputs = [ EngineCoreOutput(req_id, [], finish_reason=FinishReason.ABORT) for req_id in req_ids ] eco = EngineCoreOutputs(finished_requests=req_ids, outputs=outputs) output_queue.put_nowait((client_index, eco)) ``` The lack of e.g. `num_cached_tokens` or `trace_headers` will cause metrics and tracing problems See also #30587 and #32162

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug][Metrics] - record stats when requests are aborted by pause/sleep bug From https://github.com/vllm-project/vllm/pull/34528#discussion_r2813379522 In engine core, we do: ``` @staticmethod def _send_abort_outputs( ou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: of e.g. `num_cached_tokens` or `trace_headers` will cause metrics and tracing problems See also #30587 and #32162

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
