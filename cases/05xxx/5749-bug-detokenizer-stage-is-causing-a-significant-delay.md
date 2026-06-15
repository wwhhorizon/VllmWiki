# vllm-project/vllm#5749: [Bug]: Detokenizer stage is causing a significant delay

| 字段 | 值 |
| --- | --- |
| Issue | [#5749](https://github.com/vllm-project/vllm/issues/5749) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Detokenizer stage is causing a significant delay

### Issue 正文摘录

### Your current environment ``` Latest code from the main branch. ``` ### 🐛 Describe the bug **Description** This issue reports a significant latency increase when invoking the Detokenizer.detokenize_incrementally function. **Root Cause:** The current implementation in detokenizer.py [detokenizer.py](https://github.com/vllm-project/vllm/blob/main/vllm/transformers_utils/detokenizer.py#L269) performs a length calculation using the len(tokenizer) function call. This appears to be the source of the latency spike. **Data Points:** Inference with large batch size and big models experiences an additional ~15ms to ~20ms overhead per token generated. **Questions:** I would appreciate any insights into why the tokenizer is passed as a parameter to all the functions instead of being a class variable within Detokenizer. Is there a specific reason for this design choice?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e is causing a significant delay bug ### Your current environment ``` Latest code from the main branch. ``` ### 🐛 Describe the bug **Description** This issue reports a significant latency increase when invoking the Deto...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 15ms to ~20ms overhead per token generated. **Questions:** I would appreciate any insights into why the tokenizer is passed as a parameter to all the functions instead of being a class variable within Detokenizer. Is th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: latency spike. **Data Points:** Inference with large batch size and big models experiences an additional ~15ms to ~20ms overhead per token generated. **Questions:** I would appreciate any insights into why the tokenizer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
