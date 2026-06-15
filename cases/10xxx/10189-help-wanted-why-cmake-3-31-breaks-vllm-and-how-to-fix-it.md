# vllm-project/vllm#10189: [help wanted]: why cmake 3.31 breaks vllm and how to fix it 

| 字段 | 值 |
| --- | --- |
| Issue | [#10189](https://github.com/vllm-project/vllm/issues/10189) |
| 状态 | closed |
| 标签 | help wanted |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [help wanted]: why cmake 3.31 breaks vllm and how to fix it 

### Issue 正文摘录

### Anything you want to discuss about vllm. we need to figure it out and revert https://github.com/vllm-project/vllm/pull/10188 in the end. the recent cmake 3.31 release breaks the release pipeline. this successful release https://buildkite.com/vllm/release/builds/1745#019311b9-49d5-4f13-8064-df14308bd9ae uses cmake 3.30 and this failed release https://buildkite.com/vllm/release/builds/1746#01931327-c49b-4e52-8c0b-95fb95140ea4 uses cmake 3.31, and we get `CMake Error: Could not find CMAKE_ROOT !!! .` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [help wanted]: why cmake 3.31 breaks vllm and how to fix it help wanted ### Anything you want to discuss about vllm. we need to figure it out and revert https://github.com/vllm-project/vllm/pull/10188 in the end. the re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
