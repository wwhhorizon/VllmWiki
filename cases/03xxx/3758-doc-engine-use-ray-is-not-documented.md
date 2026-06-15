# vllm-project/vllm#3758: [Doc]: `--engine-use-ray` is not documented

| 字段 | 值 |
| --- | --- |
| Issue | [#3758](https://github.com/vllm-project/vllm/issues/3758) |
| 状态 | closed |
| 标签 | documentation;good first issue |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: `--engine-use-ray` is not documented

### Issue 正文摘录

### 📚 The doc issue It looks like `AsyncEngineArgs` are not documented in https://docs.vllm.ai/en/latest/models/engine_args.html, meaning that `--engine-use-ray` is undocumented: https://github.com/vllm-project/vllm/blob/563c1d7ec56aa0f9fdc28720f3517bf9297f5476/vllm/engine/arg_utils.py#L441-L464

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e `AsyncEngineArgs` are not documented in https://docs.vllm.ai/en/latest/models/engine_args.html, meaning that `--engine-use-ray` is undocumented: https://github.com/vllm-project/vllm/blob/563c1d7ec56aa0f9fdc28720f3517b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s like `AsyncEngineArgs` are not documented in https://docs.vllm.ai/en/latest/models/engine_args.html, meaning that `--engine-use-ray` is undocumented: https://github.com/vllm-project/vllm/blob/563c1d7ec56aa0f9fdc28720f...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
