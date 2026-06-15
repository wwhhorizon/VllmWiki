# vllm-project/vllm#19628: [Bug]: I am traing to run unsloth/phi-4-bnb-4bit but I am getting always the same error Validation Error:1 validatiopn error for modelconfig Infer_schema(func): Parameter block_size has unsupported type list[int]

| 字段 | 值 |
| --- | --- |
| Issue | [#19628](https://github.com/vllm-project/vllm/issues/19628) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: I am traing to run unsloth/phi-4-bnb-4bit but I am getting always the same error Validation Error:1 validatiopn error for modelconfig Infer_schema(func): Parameter block_size has unsupported type list[int]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am traing to run unsloth/phi-4-bnb-4bit but I am getting always the same error Validation Error:1 validatiopn error for modelconfig Infer_schema(func): Parameter block_size has unsupported type list[int]: The valid type are: dict_keys class 'torch.tensor' typing.Optional[torch.Tensor]... I have used --block_size 32 and I have even changed block_size=32 in vllm/vllm/config .py They used unsloth/tinyllama-bnb-4bit in docs but I can't see the difference of this model with unsloth/phi-4-bnb-4bit Could some one help me to run a quantized model in vllm? thanks ### Before submitting a new issue... - [x] #19629

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m getting always the same error Validation Error:1 validatiopn error for modelconfig Infer_schema(func): Parameter block_size has unsupported type list[int] bug;stale ### Your current environment ### 🐛 Describe the bug...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: I am traing to run unsloth/phi-4-bnb-4bit but I am getting always the same error Validation Error:1 validatiopn error for modelconfig Infer_schema(func): Parameter block_size has unsupported type list[int] bug;st...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: this model with unsloth/phi-4-bnb-4bit Could some one help me to run a quantized model in vllm? thanks ### Before submitting a new issue... - [x] #19629
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: er_schema(func): Parameter block_size has unsupported type list[int] bug;stale ### Your current environment ### 🐛 Describe the bug I am traing to run unsloth/phi-4-bnb-4bit but I am getting always the same error Validat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
