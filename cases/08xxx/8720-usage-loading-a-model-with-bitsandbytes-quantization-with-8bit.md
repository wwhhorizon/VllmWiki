# vllm-project/vllm#8720: [Usage]: Loading a model with bitsandbytes quantization with 8bit

| 字段 | 值 |
| --- | --- |
| Issue | [#8720](https://github.com/vllm-project/vllm/issues/8720) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Loading a model with bitsandbytes quantization with 8bit

### Issue 正文摘录

How can I load a model using bitsandbytes quantization in 8-bit format? I'm currently loading the model with the following code: ```python model_id = "path/to/model" llm = LLM(model=model_id, dtype=torch.bfloat16, trust_remote_code=True, \ quantization="bitsandbytes", load_format="bitsandbytes") ``` This loads the model in 4-bit format, but I can't figure out how to load it in 8-bit. What should I change to load the model in 8-bit instead?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: Loading a model with bitsandbytes quantization with 8bit usage;stale How can I load a model using bitsandbytes quantization in 8-bit format? I'm currently loading the model with the following code: ```python mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Loading a model with bitsandbytes quantization with 8bit usage;stale How can I load a model using bitsandbytes quantization in 8-bit format? I'm currently loading the model with the following code: ```python mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Loading a model with bitsandbytes quantization with 8bit usage;stale How can I load a model using bitsandbytes quantization in 8-bit format? I'm currently loading the model with the following code: ```python mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
