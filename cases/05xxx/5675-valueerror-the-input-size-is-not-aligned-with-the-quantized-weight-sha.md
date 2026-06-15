# vllm-project/vllm#5675: ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.[Bug]: 

| 字段 | 值 |
| --- | --- |
| Issue | [#5675](https://github.com/vllm-project/vllm/issues/5675) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.[Bug]: 

### Issue 正文摘录

@youkaichao ### Your current environment My environment: Name: vllm Version: 0.4.2+cu117 ### 🐛 Describe the bug I quantified the model(Qwen2_72B) using AWQ myself, when i wanna to set api service by using two gpus it doesn't work. but using one gpu is fine, but in some situation i have to use two gpus to set this service. Is there anyone could give me some suggestions? ![1718781017940](https://github.com/vllm-project/vllm/assets/110730393/10f55a57-44da-4719-a259-a37c5daf4653)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Name: vllm Version: 0.4.2+cu117 ### 🐛 Describe the bug I quantified the model(Qwen2_72B) using AWQ myself, when i wanna to set api service by using two gpus it doesn't work. but using one gpu is fine, but in some situat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ug @youkaichao ### Your current environment My environment: Name: vllm Version: 0.4.2+cu117 ### 🐛 Describe the bug I quantified the model(Qwen2_72B) using AWQ myself, when i wanna to set api service by using two gpus it...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.[Bug]: bug @youkaichao ### Your current environment My environment: Name: vllm Version: 0.4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
