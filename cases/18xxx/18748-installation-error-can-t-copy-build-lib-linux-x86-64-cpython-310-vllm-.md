# vllm-project/vllm#18748: [Installation]: error: can't copy 'build/lib.linux-x86_64-cpython-310/vllm/_C.abi3.so': doesn't exist or not a regular file

| 字段 | 值 |
| --- | --- |
| Issue | [#18748](https://github.com/vllm-project/vllm/issues/18748) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: error: can't copy 'build/lib.linux-x86_64-cpython-310/vllm/_C.abi3.so': doesn't exist or not a regular file

### Issue 正文摘录

### Your current environment python 3.10.13 torch2.6 gcc 12.3.0 ### How you are installing vllm When I install from source, encounter a this error: `error: can't copy 'build/lib.linux-x86_64-cpython-310/vllm/_C.abi3.so': doesn't exist or not a regular file`. I can't find useful answer in issue base. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: error: can't copy 'build/lib.linux-x86_64-cpython-310/vllm/_C.abi3.so': doesn't exist or not a regular file installation ### Your current environment python 3.10.13 torch2.6 gcc 12.3.0 ### How you are in
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
