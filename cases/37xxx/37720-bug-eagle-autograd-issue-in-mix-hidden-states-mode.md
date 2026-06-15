# vllm-project/vllm#37720: [Bug]: EAGLE Autograd issue in Mix Hidden States mode

| 字段 | 值 |
| --- | --- |
| Issue | [#37720](https://github.com/vllm-project/vllm/issues/37720) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: EAGLE Autograd issue in Mix Hidden States mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When training EAGLE3 with mix hidden states enabled, I get this error: ``` [rank1]: RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [CUDABFloat16Type [2, 4096, 2880]], which is output 0 of IndexPutBackward0, is at version 3; expected version 2 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autograd.set_detect_anomaly(True). ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: for gradient computation has been modified by an inplace operation: [CUDABFloat16Type [2, 4096, 2880]], which is output 0 of IndexPutBackward0, is at version 3; expected version 2 instead. Hint: enable anomaly detection...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ded for gradient computation has been modified by an inplace operation: [CUDABFloat16Type [2, 4096, 2880]], which is output 0 of IndexPutBackward0, is at version 3; expected version 2 instead. Hint: enable anomaly detec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: at16Type [2, 4096, 2880]], which is output 0 of IndexPutBackward0, is at version 3; expected version 2 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autogr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
