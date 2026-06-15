# vllm-project/vllm#6641: [Usage]: What do max_num_seqs and max_model_len do

| 字段 | 值 |
| --- | --- |
| Issue | [#6641](https://github.com/vllm-project/vllm/issues/6641) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What do max_num_seqs and max_model_len do

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Can someone help me explain what the max_num_seqs and max_model_len parameters do? At what stage do these two parameters operate? When I set the following engine parameters: { "model": "/model", "tensor_parallel_size": 8, "tokenizer_mode": "auto", "trust_remote_code": true, "dtype": "auto", "gpu_memory_utilization": 0.95, "max_num_seqs": 256, "max_model_len": 8192, "enforce_eager": true } The model can still handle an input length of around 16291, calculated using len(prompt)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: parallel_size": 8, "tokenizer_mode": "auto", "trust_remote_code": true, "dtype": "auto", "gpu_memory_utilization": 0.95, "max_num_seqs": 256, "max_model_len": 8192, "enforce_eager": true } The model can still handle an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: What do max_num_seqs and max_model_len do usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Can someone help me explain what the max_num_seq...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
