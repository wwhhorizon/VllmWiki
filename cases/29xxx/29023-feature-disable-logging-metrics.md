# vllm-project/vllm#29023: [Feature]: Disable logging `/metrics`

| 字段 | 值 |
| --- | --- |
| Issue | [#29023](https://github.com/vllm-project/vllm/issues/29023) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Disable logging `/metrics`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - IGW hits `/metrics` continuously to understand the current load on the system - This leads to an overload of logs - We can disable this with `--disable-uvicorn-access-log`, but lose access to all access logs We should have `--disable-uvicorn-metrics-access-log` to avoid logging * just * metrics. Per Gemini, we can do this with something like: ```python # Define the routes for which access logs should be disabled EXCLUDE_PATHS = ["/health", "/metrics"] class EndpointFilter(logging.Filter): def filter(self, record: logging.LogRecord) -> bool: # Check if the log record contains arguments and if the path matches an excluded path if record.args and len(record.args) >= 3: path = record.args[2] # The path is typically the third argument in uvicorn access logs if path in EXCLUDE_PATHS: return False # Exclude this log record return True # Include all other log records ``` Create a command line arg like `--disable-uvicorn-metrics-access-log`which selectively disables logging hits to `/metrics` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: Disable logging `/metrics` help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch - IGW hits `/metrics` continuously to understand the current load on the system - This leads...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cess logs if path in EXCLUDE_PATHS: return False # Exclude this log record return True # Include all other log records ``` Create a command line arg like `--disable-uvicorn-metrics-access-log`which selectively disables...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
