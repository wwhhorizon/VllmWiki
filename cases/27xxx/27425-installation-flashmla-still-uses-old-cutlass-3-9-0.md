# vllm-project/vllm#27425: [Installation]: FlashMLA still uses old cutlass 3.9.0

| 字段 | 值 |
| --- | --- |
| Issue | [#27425](https://github.com/vllm-project/vllm/issues/27425) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: FlashMLA still uses old cutlass 3.9.0

### Issue 正文摘录

### Your current environment While working on the Nix package for vLLM, I noticed that FlashMLA is embedding an old cutlass v3.9.0 as a submodule in [csrc/cutlass](https://github.com/vllm-project/FlashMLA/tree/main/csrc) while the main vLLM repo builds against the latest [v4.2.1](https://github.com/vllm-project/vllm/blob/295c7f0267010832132404760837e8dc4e0e664a/CMakeLists.txt#L285). There appear to be some API changes between cutlass 3 and 4, so it's not as simple as just changing the revision. I just wanted to note it, as from a distro packaging perspective it's annoying to have to package two versions of a dependency for a single package. ### How you are installing vllm Nix ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: FlashMLA still uses old cutlass 3.9.0 installation;stale ### Your current environment While working on the Nix package for vLLM, I noticed that FlashMLA is embedding an old cutlass v3.9.0 as a submodule i
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Installation]: FlashMLA still uses old cutlass 3.9.0 installation;stale ### Your current environment While working on the Nix package for vLLM, I noticed that FlashMLA is embedding an old cutlass v3.9.0 as a submodule...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Nix ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: FlashMLA still uses old cutlass 3.9.0 installation;stale ### Your current environment While working on the Nix package for vLLM, I noticed that FlashMLA is embedding an old cutlass v3.9.0 as a submodule...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t/FlashMLA/tree/main/csrc) while the main vLLM repo builds against the latest [v4.2.1](https://github.com/vllm-project/vllm/blob/295c7f0267010832132404760837e8dc4e0e664a/CMakeLists.txt#L285). There appear to be some API...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
