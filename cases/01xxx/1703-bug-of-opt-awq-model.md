# vllm-project/vllm#1703: bug of opt awq model

| 字段 | 值 |
| --- | --- |
| Issue | [#1703](https://github.com/vllm-project/vllm/issues/1703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> bug of opt awq model

### Issue 正文摘录

Hi @zhuohan123, I found two bugs of opt awq model in the latest code because of the code refactor. 1. in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L215, some opt model may not use quantized linear in project_in/project_out, 2. in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L254, project_in/project_out have two return value

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /main/vllm/model_executor/models/opt.py#L215, some opt model may not use quantized linear in project_in/project_out, 2. in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L254, project_i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug of opt awq model bug Hi @zhuohan123, I found two bugs of opt awq model in the latest code because of the code refactor. 1. in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L215, so...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: awq model bug Hi @zhuohan123, I found two bugs of opt awq model in the latest code because of the code refactor. 1. in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py#L215, some opt mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
