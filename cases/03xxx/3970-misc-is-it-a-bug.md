# vllm-project/vllm#3970: [Misc]: Is it a bug?

| 字段 | 值 |
| --- | --- |
| Issue | [#3970](https://github.com/vllm-project/vllm/issues/3970) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Is it a bug?

### Issue 正文摘录

### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/main/vllm/sequence.py#L343 def get_num_new_tokens(self) -> int: """Get the number of new tokens to be computed. Args: remainig_token_budget: The remaining token budgets. Returns: The new number of tokens to be computed. I.e., 1 for decode, prompt size for prefill. If there's not enough remainig_token_budget, it can return the chunked number of new tokens. """ if self.data.stage == SequenceStage.DECODE: return 1 return self.data.get_num_uncomputed_tokens()

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eturns: The new number of tokens to be computed. I.e., 1 for decode, prompt size for prefill. If there's not enough remainig_token_budget, it can return the chunked number of new tokens. """ if self.data.stage == Sequen...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
