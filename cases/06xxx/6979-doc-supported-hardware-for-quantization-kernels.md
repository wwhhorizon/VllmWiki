# vllm-project/vllm#6979: [Doc]: Supported Hardware for Quantization Kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#6979](https://github.com/vllm-project/vllm/issues/6979) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Supported Hardware for Quantization Kernels

### Issue 正文摘录

### 📚 The doc issue I'm confused what "the quantization method is supported" mean? Ampere arch doesn't support FP8, according to Nvidia. So does this mean the FP8 operation is supported on A100/A800 GPU? Or just we can conver the weight parameters form FP16 to FP8? ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: c issue I'm confused what "the quantization method is supported" mean? Ampere arch doesn't support FP8, according to Nvidia. So does this mean the FP8 operation is supported on A100/A800 GPU? Or just we can conver the w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Doc]: Supported Hardware for Quantization Kernels documentation ### 📚 The doc issue I'm confused what "the quantization method is supported" mean? Ampere arch doesn't support FP8, according to Nvidia. So does this mean...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
