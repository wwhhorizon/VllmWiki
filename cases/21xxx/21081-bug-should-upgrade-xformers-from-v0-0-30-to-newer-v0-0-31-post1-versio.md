# vllm-project/vllm#21081: [Bug]: Should upgrade xformers from v0.0.30 to newer v0.0.31.post1 version

| 字段 | 值 |
| --- | --- |
| Issue | [#21081](https://github.com/vllm-project/vllm/issues/21081) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Should upgrade xformers from v0.0.30 to newer v0.0.31.post1 version

### Issue 正文摘录

### 🐛 Describe the bug l am using [verl](https://github.com/vllm-project/vllm/tree/main) library, which is built on `vllm` (0.9.0+ release). According to `requirements/cuda.txt`, vllm requires `xformers==0.0.30`. However, this version is incompatible with flash-attention 2.8.0.post2. Based on the release notes for flash-attention, only versions >=2.8.0 support torch==2.7, which is a mandatory requirement for vllm (0.9.0+ release). For more details, see the relevant update from the xformers repository: https://github.com/facebookresearch/xformers/issues/1267 File need to change: https://github.com/vllm-project/vllm/blob/main/requirements/cuda.txt ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y, which is built on `vllm` (0.9.0+ release). According to `requirements/cuda.txt`, vllm requires `xformers==0.0.30`. However, this version is incompatible with flash-attention 2.8.0.post2. Based on the release notes fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Should upgrade xformers from v0.0.30 to newer v0.0.31.post1 version bug;stale ### 🐛 Describe the bug l am using [verl](https://github.com/vllm-project/vllm/tree/main) library, which is built on `vllm` (0.9.0+ rel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Should upgrade xformers from v0.0.30 to newer v0.0.31.post1 version bug;stale ### 🐛 Describe the bug l am using [verl](https://github.com/vllm-project/vllm/tree/main) library, which is built on `vllm` (0.9.0+ release)....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
