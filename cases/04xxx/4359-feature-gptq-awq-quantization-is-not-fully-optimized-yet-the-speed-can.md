# vllm-project/vllm#4359: [Feature]: GPTQ/AWQ quantization is not fully optimized yet. The speed can be slower than non-quantized models.

| 字段 | 值 |
| --- | --- |
| Issue | [#4359](https://github.com/vllm-project/vllm/issues/4359) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GPTQ/AWQ quantization is not fully optimized yet. The speed can be slower than non-quantized models.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch While running the vLLM server with quantized models specifying the quantization type, the below mentioned Warning is shown: ``` WARNING 04-25 12:26:07 config.py:169] gptq quantization is not fully optimized yet. The speed can be slower than non-quantized models. ``` Is the a feature in progress or is there any workaround that can be done to handle the same. Let me know if any more details are required from my end. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n is not fully optimized yet. The speed can be slower than non-quantized models. feature request ### 🚀 The feature, motivation and pitch While running the vLLM server with quantized models specifying the quantization ty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vation and pitch While running the vLLM server with quantized models specifying the quantization type, the below mentioned Warning is shown: ``` WARNING 04-25 12:26:07 config.py:169] gptq quantization is not fully optim...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: GPTQ/AWQ quantization is not fully optimized yet. The speed can be slower than non-quantized models. feature request ### 🚀 The feature, motivation and pitch While running the vLLM server with quantized models...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ptimized yet. The speed can be slower than non-quantized models. feature request ### 🚀 The feature, motivation and pitch While running the vLLM server with quantized models specifying the quantization type, the below me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
