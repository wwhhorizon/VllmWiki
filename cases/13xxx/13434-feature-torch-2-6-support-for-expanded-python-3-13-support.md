# vllm-project/vllm#13434: [Feature]: `torch>=2.6` support for expanded Python 3.13 support

| 字段 | 值 |
| --- | --- |
| Issue | [#13434](https://github.com/vllm-project/vllm/issues/13434) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `torch>=2.6` support for expanded Python 3.13 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Trying `pip install vllm>=0.7 torch>=2.6` fails since `vllm` v0.7 seems to require `torch==2.5.1`. Can we allow `torch==2.6`? Something like `torch>=2.5.1<2.7` can work too. ### Alternatives n/a ### Additional context https://pytorch.org/blog/pytorch2-6/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ort feature request ### 🚀 The feature, motivation and pitch Trying `pip install vllm>=0.7 torch>=2.6` fails since `vllm` v0.7 seems to require `torch==2.5.1`. Can we allow `torch==2.6`? Something like `torch>=2.5.1<2.7`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -6/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: `torch>=2.6` support for expanded Python 3.13 support feature request ### 🚀 The feature, motivation and pitch Trying `pip install vllm>=0.7 torch>=2.6` fails since `vllm` v0.7 seems to require `torch==2.5.1`....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
