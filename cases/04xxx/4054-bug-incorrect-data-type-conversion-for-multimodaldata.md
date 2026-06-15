# vllm-project/vllm#4054: [Bug]: Incorrect Data Type Conversion for MultiModalData

| 字段 | 值 |
| --- | --- |
| Issue | [#4054](https://github.com/vllm-project/vllm/issues/4054) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect Data Type Conversion for MultiModalData

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I've encountered an issue with the code in the vllm project on GitHub. Specifically, at line 170 of the llm.py file https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/llm.py#L170, there is a conversion of multi_modal_data.data to torch.float16 using the statement multi_modal_data.data = multi_modal_data.data.to(torch.float16). This automatic conversion may not be suitable for all use cases, especially if the model is designed to operate with bfloat16 or other numerical precisions. If this is an issue that needs to be addressed, I would be happy to submit a pull request with a fix

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: s, especially if the model is designed to operate with bfloat16 or other numerical precisions. If this is an issue that needs to be addressed, I would be happy to submit a pull request with a fix
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Incorrect Data Type Conversion for MultiModalData bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I've encountered an issue with the code in the vllm proj...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nts/llm.py#L170, there is a conversion of multi_modal_data.data to torch.float16 using the statement multi_modal_data.data = multi_modal_data.data.to(torch.float16). This automatic conversion may not be suitable for all...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Incorrect Data Type Conversion for MultiModalData bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I've encountered an issue with the code in the vllm proj...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s an issue that needs to be addressed, I would be happy to submit a pull request with a fix

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
