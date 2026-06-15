# vllm-project/vllm#24218: [Feature]: Propose in docs a complete example of `pyproject.toml` to be used directly with `uv sync`

| 字段 | 值 |
| --- | --- |
| Issue | [#24218](https://github.com/vllm-project/vllm/issues/24218) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Propose in docs a complete example of `pyproject.toml` to be used directly with `uv sync`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This should allow instant and reliable starting of a new project using vllm. Currently in the docs are only `uv pip install` examples which do not produce `pyproject.toml` 1. One tricky part is pinning vllm to a nightly wheel 2. Another is using correct github release wheel path for flash-attn for avoiding compilation from sources (as on pypi only a source package is available, for some reasons wheels are not pushed there and only published on github releases) My take is at https://gist.github.com/vadimkantorov/fe63f8628ff6cad460e934e1d7ed650b An improvement would also pin FlashInfer and any other optional dependencies in a correct way ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ting of a new project using vllm. Currently in the docs are only `uv pip install` examples which do not produce `pyproject.toml` 1. One tricky part is pinning vllm to a nightly wheel 2. Another is using correct github r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e example of `pyproject.toml` to be used directly with `uv sync` feature request;unstale ### 🚀 The feature, motivation and pitch This should allow instant and reliable starting of a new project using vllm. Currently in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: kantorov/fe63f8628ff6cad460e934e1d7ed650b An improvement would also pin FlashInfer and any other optional dependencies in a correct way ### Alternatives _No response_ ### Additional context _No response_ ### Before subm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
