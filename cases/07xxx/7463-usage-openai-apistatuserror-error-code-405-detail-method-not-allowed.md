# vllm-project/vllm#7463: [Usage]: openai.APIStatusError: Error code: 405 - {'detail': 'Method Not Allowed'}

| 字段 | 值 |
| --- | --- |
| Issue | [#7463](https://github.com/vllm-project/vllm/issues/7463) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: openai.APIStatusError: Error code: 405 - {'detail': 'Method Not Allowed'}

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I run `vllm serve /mnt/datastore/shared/model-fp8 --max-model-len 16384 --tensor-parallel-size 8 --gpu-memory-utilization 0.95 --served-model-name model-v2-405b-e4` But then I get `openai.APIStatusError: Error code: 405 - {'detail': 'Method Not Allowed'}` I get this only with the chat.completions api from oai lib. Text completion api works fine..

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ould you like to use vllm I run `vllm serve /mnt/datastore/shared/model-fp8 --max-model-len 16384 --tensor-parallel-size 8 --gpu-memory-utilization 0.95 --served-model-name model-v2-405b-e4` But then I get `openai.APISt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How would you like to use vllm I run `vllm serve /mnt/datastore/shared/model-fp8 --max-model-len 16384 --tensor-parallel-size 8 --gpu-memory-utilization 0.95 --served-model-name model-v2-405b-e4` But then I get `openai....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
