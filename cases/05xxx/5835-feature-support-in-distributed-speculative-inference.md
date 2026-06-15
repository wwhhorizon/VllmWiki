# vllm-project/vllm#5835: [Feature]: Support in distributed speculative inference

| 字段 | 值 |
| --- | --- |
| Issue | [#5835](https://github.com/vllm-project/vllm/issues/5835) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support in distributed speculative inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi @cadedaniel, Thanks again for your awesome work on speculative inference! It was a pleasure meeting you today. As you requested, I'm posting the question we discussed as an issue. - **Feature request:** Support [distributed speculative inference](https://arxiv.org/pdf/2405.14105) (_DSI_), the fastest inference algorithm that doesn't require any additional training or architectural changes. - **Question:** What parts of the current vLLM implementation fit DSI, and what parts are missing? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support in distributed speculative inference feature request;stale ### 🚀 The feature, motivation and pitch Hi @cadedaniel, Thanks again for your awesome work on speculative inference! It was a pleasure meetin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: test inference algorithm that doesn't require any additional training or architectural changes. - **Question:** What parts of the current vLLM implementation fit DSI, and what parts are missing? ### Alternatives _No res...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: speculative inference](https://arxiv.org/pdf/2405.14105) (_DSI_), the fastest inference algorithm that doesn't require any additional training or architectural changes. - **Question:** What parts of the current vLLM imp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
