# vllm-project/vllm#20175: [Bug]: No throughput stats logging in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#20175](https://github.com/vllm-project/vllm/issues/20175) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: No throughput stats logging in V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using a V1 async engine we do not get any log output on the console regarding the throughput metrics of the engine even though the engines `stat_loggers` (by default) contain a `LoggingStatLogger`. The reason for this is that `LoggingStatLogger.log` is only called in `AsyncLLM.do_log_stats` which in turn is never called while the engine is running. I don't think this is actually desired behaviour. Relevant files: [v1/engine/async_llm.py](https://github.com/vllm-project/vllm/blob/main/vllm/v1/engine/async_llm.py) [v1/metrics/loggers.py](https://github.com/vllm-project/vllm/blob/main/vllm/v1/metrics/loggers.py) We currently use a patched version of the `LoggingStatLogger` like this: ```python class V1LoggingStatLoggerFixed(V1LoggingStatLogger): """ A fixed version of V1LoggingStatLogger actually logs during the record method. The log method is otherwise not called in the VLLM codebase. """ def __init__(self, *args: Any, **kwargs: Any) -> None: super().__init__(*args, **kwargs) self.log_interval = 5 def record(self, *args: Any, **kwargs: Any) -> None: super().record(*args, **kwargs) now = time.monotonic() if now - self.last_log...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: No throughput stats logging in V1 bug ### Your current environment ### 🐛 Describe the bug When using a V1 async engine we do not get any log output on the console regarding the throughput metrics of the engine ev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t/vllm/blob/main/vllm/v1/metrics/loggers.py) We currently use a patched version of the `LoggingStatLogger` like this: ```python class V1LoggingStatLoggerFixed(V1LoggingStatLogger): """ A fixed version of V1LoggingStatLo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: uld probably be preferable if `log` is eventually called from somewhere else). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom ri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
