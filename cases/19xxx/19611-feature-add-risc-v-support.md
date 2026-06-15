# vllm-project/vllm#19611: [Feature]: Add RISC-V support

| 字段 | 值 |
| --- | --- |
| Issue | [#19611](https://github.com/vllm-project/vllm/issues/19611) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add RISC-V support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch RISC-V is an open ISA and its system software ecosystem is growing stable and much ready for serious high performance computing scenarios. We are a RISC-V CPU chip vendor and have experimented with `llama.cpp + vulkan + AMD7900` to achieve ~27tokens/s for 32B DeepSeek. As desktop- and server-grade RISC-V CPUs (improved single core performance and sufficient PCIe lanes) become available, we receive lots of demands to run vLLM on RISC-V with flagship GPUs. We believe it is time. As https://github.com/vllm-project/vllm/issues/8996 points out @mgoin , RISC-V support is straightforward with pytorch support. We could contribute the following pieces: - [ ] arch tests and risc-v related shims - [ ] a RISC-V scalar backend in `csrc/cpu/`, as most off-the-shelf RISC-V chips do not have standard-compliant vector support. This backend will allow vLLM to run on most RISC-V chips. - [ ] a RISC-V vector backend, to run vLLM with qemu (emulating a vector capable RISC-V CPU and future chips). - [ ] CI tests that involve RISC-V backends We are open to comments of any kind and more than happy to follow-up RISC-V + vLLM and more GPU backends in the future. ###...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y for serious high performance computing scenarios. We are a RISC-V CPU chip vendor and have experimented with `llama.cpp + vulkan + AMD7900` to achieve ~27tokens/s for 32B DeepSeek. As desktop- and server-grade RISC-V...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add RISC-V support feature request;stale ### 🚀 The feature, motivation and pitch RISC-V is an open ISA and its system software ecosystem is growing stable and much ready for serious high performance computing...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pieces: - [ ] arch tests and risc-v related shims - [ ] a RISC-V scalar backend in `csrc/cpu/`, as most off-the-shelf RISC-V chips do not have standard-compliant vector support. This backend will allow vLLM to run on mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and server-grade RISC-V CPUs (improved single core performance and sufficient PCIe lanes) become available, we receive lots of demands to run vLLM on RISC-V with flagship GPUs. We believe it is time. As https://github.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g scenarios. We are a RISC-V CPU chip vendor and have experimented with `llama.cpp + vulkan + AMD7900` to achieve ~27tokens/s for 32B DeepSeek. As desktop- and server-grade RISC-V CPUs (improved single core performance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
