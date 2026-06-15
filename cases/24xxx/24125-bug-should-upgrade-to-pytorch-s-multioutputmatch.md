# vllm-project/vllm#24125: [Bug]: Should upgrade to PyTorch's MultiOutputMatch

| 字段 | 值 |
| --- | --- |
| Issue | [#24125](https://github.com/vllm-project/vllm/issues/24125) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Should upgrade to PyTorch's MultiOutputMatch

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/d328f7894f140fdc643dc1aa5fe80f4596e6f418/vllm/compilation/multi_output_match.py#L19-L24 This should be supported in torch >= 2.6 now, so we should be able to delete the code in vLLM (or at least add a guard to only use said code in older versions of pytorch ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Should upgrade to PyTorch's MultiOutputMatch bug;torch.compile ### Your current environment n/a ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/d328f7894f140fdc643dc1aa5fe80f4596e6f418/vllm/compi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rch ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
