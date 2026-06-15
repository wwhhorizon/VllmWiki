# vllm-project/vllm#21576: [Bug]: [P/D] NIXLConnector does not support P TP > D TP

| 字段 | 值 |
| --- | --- |
| Issue | [#21576](https://github.com/vllm-project/vllm/issues/21576) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [P/D] NIXLConnector does not support P TP > D TP

### Issue 正文摘录

### Your current environment vllm on h200 ### 🐛 Describe the bug A use case is lama-scout/qwen: - TP for P workers - DP for D workers This currently crashes with ```bash (EngineCore_0 pid=286) ERROR 07-25 03:33:23 [nixl_connector.py:548] p_remote_rank = self.tp_rank // tp_ratio (EngineCore_0 pid=286) ERROR 07-25 03:33:23 [nixl_connector.py:548] ~~~~~~~~~~~~~^^~~~~~~~~~ (EngineCore_0 pid=286) ERROR 07-25 03:33:23 [nixl_connector.py:548] ZeroDivisionError: integer division or modulo by zero (EngineCore_1 pid=289) ERROR 07-25 03:33:23 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=0, num_waiting_reqs=1, kv_cache_usage=0.0016330974414806576, prefix_cache_stats=PrefixCacheStats(reset=False, requests=1, queries=758, hits=0), spec_decoding_stats=None, num_corrupted_reqs=0) ``` We should support D TP>P TP? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: [P/D] NIXLConnector does not support P TP > D TP bug;stale ### Your current environment vllm on h200 ### 🐛 Describe the bug A use case is lama-scout/qwen: - TP for P workers - DP for D workers This currently cras...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: TP? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: usage=0.0016330974414806576, prefix_cache_stats=PrefixCacheStats(reset=False, requests=1, queries=758, hits=0), spec_decoding_stats=None, num_corrupted_reqs=0) ``` We should support D TP>P TP? ### Before submitting a ne...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ironment vllm on h200 ### 🐛 Describe the bug A use case is lama-scout/qwen: - TP for P workers - DP for D workers This currently crashes with ```bash (EngineCore_0 pid=286) ERROR 07-25 03:33:23 [nixl_connector.py:548] p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
