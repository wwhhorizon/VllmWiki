# vllm-project/vllm#6815: [Bug]: Llama3.1-70B-FP8 Prompt insufficient computing power

| 字段 | 值 |
| --- | --- |
| Issue | [#6815](https://github.com/vllm-project/vllm/issues/6815) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama3.1-70B-FP8 Prompt insufficient computing power

### Issue 正文摘录

### Your current environment ![2](https://github.com/user-attachments/assets/8967ff30-871b-4e63-9e64-4e821b3a3c54) ![xxx](https://github.com/user-attachments/assets/ef267444-fa79-447e-a92e-9808186c40c1) The computing power of 3090 is 8.6, and the computing power of 4090 is 8.9. Does it mean that 3090 no longer supports FP8? ### 🐛 Describe the bug ![2](https://github.com/user-attachments/assets/8967ff30-871b-4e63-9e64-4e821b3a3c54) ![xxx](https://github.com/user-attachments/assets/ef267444-fa79-447e-a92e-9808186c40c1) The computing power of 3090 is 8.6, and the computing power of 4090 is 8.9. Does it mean that 3090 no longer supports FP8?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Llama3.1-70B-FP8 Prompt insufficient computing power bug ### Your current environment ![2](https://github.com/user-attachments/assets/8967ff30-871b-4e63-9e64-4e821b3a3c54) ![xxx](https://github.com/user-attachmen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Llama3.1-70B-FP8 Prompt insufficient computing power bug ### Your current environment ![2](https://github.com/user-attachments/assets/8967ff30-871b-4e63-9e64-4e821b3a3c54) ![xxx](https://github.com/user-attachmen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Llama3.1-70B-FP8 Prompt insufficient computing power bug ### Your current environment ![2](https://github.com/user-attachments/assets/8967ff30-871b-4e63-9e64-4e821b3a3c54) ![xxx](https://github.com/user-attachmen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
