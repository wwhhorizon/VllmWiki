# vllm-project/vllm#1859: 使用vllm运行Yi-34B-Chat-4bit错误

| 字段 | 值 |
| --- | --- |
| Issue | [#1859](https://github.com/vllm-project/vllm/issues/1859) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 使用vllm运行Yi-34B-Chat-4bit错误

### Issue 正文摘录

使用vllm运行Yi-34B-Chat-4bit，python -m vllm.entrypoints.apiserver --model /media/data/Yi-34B-Chat-4bit --tensor-parallel-size 4 --quantization awq不能运行， --tensor-parallel-size 2可以运行，输出满max_tokens才会停止，短回答就重复到max_tokens停止。

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: piserver --model /media/data/Yi-34B-Chat-4bit --tensor-parallel-size 4 --quantization awq不能运行， --tensor-parallel-size 2可以运行，输出满max_tokens才会停止，短回答就重复到max_tokens停止。
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t-4bit错误 使用vllm运行Yi-34B-Chat-4bit，python -m vllm.entrypoints.apiserver --model /media/data/Yi-34B-Chat-4bit --tensor-parallel-size 4 --quantization awq不能运行， --tensor-parallel-size 2可以运行，输出满max_tokens才会停止，短回答就重复到max_toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
