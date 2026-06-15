# vllm-project/vllm#25504: [Feature]: Priority based scheduling policy

| 字段 | 值 |
| --- | --- |
| Issue | [#25504](https://github.com/vllm-project/vllm/issues/25504) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Priority based scheduling policy

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Problems: - For some applications, it's important to be able to set task priority in a queue especially given how team working on different priority projects on the same server. For example: some jobs might be cron based, some Agent tasks might have different priority versus the chatbot aplication. Having SLO-aware priority queue helps with latency, fairness and resource efficiency Proposed design: New Scheduler where clients can send request with different priority and the scheduler can schedule accordingly Examples: class _AgentSJFRequestQueue(PriorityRequestQueue): """Priority queue that re-computes job priority on every enqueue.""" def __init__(self, priority_fn: Callable[[Request], float]) -> None: super().__init__() self._priority_fn = priority_fn def add_request(self, request: Request) -> None: # type: ignore[override] request.priority = self._priority_fn(request) super().add_request(request) class AgentSJFScheduler(Scheduler): """Scheduler that prioritizes short jobs with optional SLO hints.""" _PRIORITY_HEADER_KEYS = ("x-slo", "x-slo-ms", "x-deadline-ms") _DEFAULT_SLO_MS = 60_000 _MAX_SLO_MS = 86_400_000 # 24 hours in milliseconds....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Priority based scheduling policy feature request ### 🚀 The feature, motivation and pitch Problems: - For some applications, it's important to be able to set task priority in a queue especially given how team...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: def get_priority(self, request: Request) -> float: """ return numerical score act as composite score of priority mutiplier, remaining_tokens and slow message (in ms) ### Alternatives _No response_ ### Additional context...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: feature, motivation and pitch Problems: - For some applications, it's important to be able to set task priority in a queue especially given how team working on different priority projects on the same server. For example...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ersus the chatbot aplication. Having SLO-aware priority queue helps with latency, fairness and resource efficiency Proposed design: New Scheduler where clients can send request with different priority and the scheduler...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
