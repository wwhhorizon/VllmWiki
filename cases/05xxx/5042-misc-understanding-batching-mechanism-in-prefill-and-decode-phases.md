# vllm-project/vllm#5042: [Misc]: Understanding Batching Mechanism in Prefill and Decode Phases

| 字段 | 值 |
| --- | --- |
| Issue | [#5042](https://github.com/vllm-project/vllm/issues/5042) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Understanding Batching Mechanism in Prefill and Decode Phases

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi, I want to understand how vLLM batches requests and generates output tokens. I know it uses continuous batching, but does it also batch in the decode phase? Sample codes for stream mode show it returning tokens for each request in order. For example, when all tokens for request 1 are generated, request 2 starts to output tokens (in async). I would be grateful if anyone could shed some light on how batching works in both the prefill and decode phases. Thanks.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: Understanding Batching Mechanism in Prefill and Decode Phases ### Anything you want to discuss about vllm. Hi, I want to understand how vLLM batches requests and generates output tokens. I know it uses continuou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Misc]: Understanding Batching Mechanism in Prefill and Decode Phases ### Anything you want to discuss about vllm. Hi, I want to understand how vLLM batches requests and generates output tokens. I know it uses continuou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
