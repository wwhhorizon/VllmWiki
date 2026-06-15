# vllm-project/vllm#13545: [Bug]: Make https://wheels.vllm.ai/nightly inspectable

| 字段 | 值 |
| --- | --- |
| Issue | [#13545](https://github.com/vllm-project/vllm/issues/13545) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Make https://wheels.vllm.ai/nightly inspectable

### Issue 正文摘录

### Your current environment / ### 🐛 Describe the bug For example, with torch, we can inspect and choose a version from https://download.pytorch.org/whl/nightly/torch/. It is not possible with vllm's https://wheels.vllm.ai/nightly which gives `This XML file does not appear to have any style information associated with it. The document tree is shown below.`. An alternative is `pip index versions vllm --pre --extra-index-url https://wheels.vllm.ai/nightly`, which gives `0.7.3.dev228+g42333026, 0.7.2, 0.7.1, 0.7.0, 0.6.6.post1, 0.6.6, 0.6.5, 0.6.4.post1, 0.6.4, 0.6.3.post1, 0.6.3, 0.6.2, 0.6.1.post2, 0.6.1.post1, 0.6.1, 0.6.0, 0.5.5, 0.5.4, 0.5.3.post1, 0.5.3, 0.5.2, 0.5.1, 0.5.0.post1, 0.5.0, 0.4.3, 0.4.2, 0.4.1, 0.4.0.post1, 0.4.0, 0.3.3, 0.3.2, 0.3.1, 0.3.0, 0.2.7, 0.2.6, 0.2.5, 0.2.4, 0.2.3, 0.2.2, 0.2.1.post1, 0.2.0, 0.1.7, 0.1.6, 0.1.5, 0.1.4, 0.1.3, 0.1.2, 0.1.1, 0.1.0, 0.0.1` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Make https://wheels.vllm.ai/nightly inspectable bug;stale ### Your current environment / ### 🐛 Describe the bug For example, with torch, we can inspect and choose a version from https://download.pytorch.org/whl/n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .1` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i/nightly which gives `This XML file does not appear to have any style information associated with it. The document tree is shown below.`. An alternative is `pip index versions vllm --pre --extra-index-url https://wheel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Make https://wheels.vllm.ai/nightly inspectable bug;stale ### Your current environment / ### 🐛 Describe the bug For example, with torch, we can inspect and choose a version from https://download.pytorch.org/whl/n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
