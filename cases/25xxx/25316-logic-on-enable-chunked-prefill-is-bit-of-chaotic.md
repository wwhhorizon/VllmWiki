# vllm-project/vllm#25316: logic on `enable_chunked_prefill` is bit of chaotic

| 字段 | 值 |
| --- | --- |
| Issue | [#25316](https://github.com/vllm-project/vllm/issues/25316) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> logic on `enable_chunked_prefill` is bit of chaotic

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/d88918e4c2d189eb25724a6cff9a9028c67daa07/vllm/engine/arg_utils.py#L1178-L1188 L1179 function `self._set_default_args_v1` relys on `self.enable_chunked_prefill`, which is partially determined by L1188 for env of `POWER (ppc64le)/ARM CPUs in V1`, inside function `self._set_default_args_v1`, it may take `self.enable_chunked_prefill` as True, but after that function `self.enable_chunked_prefill` would be set to False.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: logic on `enable_chunked_prefill` is bit of chaotic stale https://github.com/vllm-project/vllm/blob/d88918e4c2d189eb25724a6cff9a9028c67daa07/vllm/engine/arg_utils.py#L1178-L1188 L1179 function `self._set_default_args_v1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: but after that function `self.enable_chunked_prefill` would be set to False.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
