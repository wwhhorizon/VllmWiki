# vllm-project/vllm#2701: how to get sentence prob, no generation needed, it seems very slow

| 字段 | 值 |
| --- | --- |
| Issue | [#2701](https://github.com/vllm-project/vllm/issues/2701) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to get sentence prob, no generation needed, it seems very slow

### Issue 正文摘录

```python sp = SamplingParams() sp.max_tokens = 0 sp.prompt_logprobs = 0 texts = [ "vllm is awesome", "how to get this sentence probability.", ] outputs = llm.generate(texts, sp, use_tqdm=False) res = [] for i, output in enumerate(outputs): sum_log_prob = 0.0 for item in output.prompt_logprobs: if item is not None: sum_log_prob += next(iter(item.values())) res.append(sum_log_prob) print(res) ```

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s sentence probability.", ] outputs = llm.generate(texts, sp, use_tqdm=False) res = [] for i, output in enumerate(outputs): sum_log_prob = 0.0 for item in output.prompt_logprobs: if item is not None: sum_log_prob += nex...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
