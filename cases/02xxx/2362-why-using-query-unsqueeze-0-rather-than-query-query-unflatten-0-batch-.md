# vllm-project/vllm#2362: why using 'query.unsqueeze(0)' rather than 'query = query.unflatten(0, (batch_size, seq_len))' consistently

| 字段 | 值 |
| --- | --- |
| Issue | [#2362](https://github.com/vllm-project/vllm/issues/2362) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> why using 'query.unsqueeze(0)' rather than 'query = query.unflatten(0, (batch_size, seq_len))' consistently

### Issue 正文摘录

Please help me to understand that, in the forward implemention of PagedAttention In /vllm-project/vllm/tree/main/vllm/model_executor/layers/attention.py, why the tensors sent to xops.memory_efficient_attention_forward use 'query.unsqueeze(0)' rather than 'query = query.unflatten(0, (batch_size, seq_len))' which is consistent with the self.alibi_slopes branch. In my opinion, at the input moment of the forward function, query has shape [batch_size, seq_len, num_heads * head_size], tokens of different batches stay in there own batch, then after query = query.view(-1, self.num_heads, self.head_size) all tokens of all seqs of all batches flattened into the 1st dim. before feed to xops.memory_efficient_attention_forward, should the tokens be reshaped back by query.unflatten(0, (batch_size, seq_len))? otherwise query.unflatten(0, (batch_size, seq_len)) will concat seqs of different batches into an entire one, and I guess it will cause the prediction wrong. for example: when query = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] the unsqueeze(0) will feed the embedded seqs [Hello, my name is The president of the United...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el_executor/layers/attention.py, why the tensors sent to xops.memory_efficient_attention_forward use 'query.unsqueeze(0)' rather than 'query = query.unflatten(0, (batch_size, seq_len))' which is consistent with the self...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ward implemention of PagedAttention In /vllm-project/vllm/tree/main/vllm/model_executor/layers/attention.py, why the tensors sent to xops.memory_efficient_attention_forward use 'query.unsqueeze(0)' rather than 'query =...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
