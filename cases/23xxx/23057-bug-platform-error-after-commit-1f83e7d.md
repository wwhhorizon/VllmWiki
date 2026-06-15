# vllm-project/vllm#23057: [Bug]: Platform error after Commit 1f83e7d.

| 字段 | 值 |
| --- | --- |
| Issue | [#23057](https://github.com/vllm-project/vllm/issues/23057) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Platform error after Commit 1f83e7d.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I got a platform error after [this pr](https://github.com/vllm-project/vllm/pull/22971) when I installed the nightly wheel using `uv sync`. ``` error: Distribution `vllm==0.10.1.dev699+g1f83e7d84 @ registry+https://wheels.vllm.ai/1f83e7d849ccb03990bb896f49df20343a2828b9` can't be installed because it doesn't have a source distribution or wheel for the current platform hint: You're on Linux (`manylinux_2_31_x86_64`), but `vllm` (v0.10.1.dev699+g1f83e7d84) only has wheels for the following platform: `manylinux1_aarch64`; consider adding your platform to `tool.uv.required-environments` to ensure uv resolves to a version with compatible wheels ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: after [this pr](https://github.com/vllm-project/vllm/pull/22971) when I installed the nightly wheel using `uv sync`. ``` error: Distribution `vllm==0.10.1.dev699+g1f83e7d84 @ registry+https://wheels.vllm.ai/1f83e7d849cc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 699+g1f83e7d84) only has wheels for the following platform: `manylinux1_aarch64`; consider adding your platform to `tool.uv.required-environments` to ensure uv resolves to a version with compatible wheels ``` ### Before...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
