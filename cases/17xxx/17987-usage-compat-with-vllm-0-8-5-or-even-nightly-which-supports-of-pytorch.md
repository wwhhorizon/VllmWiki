# vllm-project/vllm#17987: [Usage]: Compat with vllm 0.8.5 or even nightly (which supports of PyTorch 2.7.0) and support for PyTorch 2.7.0

| 字段 | 值 |
| --- | --- |
| Issue | [#17987](https://github.com/vllm-project/vllm/issues/17987) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Compat with vllm 0.8.5 or even nightly (which supports of PyTorch 2.7.0) and support for PyTorch 2.7.0

### Issue 正文摘录

### Your current environment This vllm PR introduces support for PyTorch 2.7.0: - https://github.com/vllm-project/vllm/pull/16859 this nightly vllm version can be installed as `pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` In `requirements.txt` still 0.8.3 version is mentioned: https://github.com/volcengine/verl/blob/17f283b1e818a102bfa799c7c906d95e81fba11b/requirements.txt#L20 Does verl support the nightly vllm / PyTorch 2.7.0? Thanks! ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0: - https://github.com/vllm-project/vllm/pull/16859 this nightly vllm version can be installed as `pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` In `requirements.txt` still 0.8.3 version i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
