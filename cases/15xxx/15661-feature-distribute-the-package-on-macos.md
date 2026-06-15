# vllm-project/vllm#15661: [Feature]: distribute the package on macos

| 字段 | 值 |
| --- | --- |
| Issue | [#15661](https://github.com/vllm-project/vllm/issues/15661) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: distribute the package on macos

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now that vLLM can be built directly in macos with `pip install -e .` , we can build the wheel and publish it to pypi, so that users can directly install it. This is mostly for testing and development, so that people can develop some pure python code without spinning up a gpu server. This will help lower the barrier of developing vllm. Along with it, we should also have some nightly ci to have basic smoke test to make sure it is not broken. cc @simon-mo for release, and @khluu for ci. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vation and pitch Now that vLLM can be built directly in macos with `pip install -e .` , we can build the wheel and publish it to pypi, so that users can directly install it. This is mostly for testing and development, s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vllm. Along with it, we should also have some nightly ci to have basic smoke test to make sure it is not broken. cc @simon-mo for release, and @khluu for ci. ### Alternatives _No response_ ### Additional context _No res...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: distribute the package on macos feature request;stale ### 🚀 The feature, motivation and pitch Now that vLLM can be built directly in macos with `pip install -e .` , we can build the wheel and publish it to py...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: h it to pypi, so that users can directly install it. This is mostly for testing and development, so that people can develop some pure python code without spinning up a gpu server. This will help lower the barrier of dev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
