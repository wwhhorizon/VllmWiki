# vllm-project/vllm#13424: [Installation]: flash-attention internal "git submodule update" problematic for offline-install

| 字段 | 值 |
| --- | --- |
| Issue | [#13424](https://github.com/vllm-project/vllm/issues/13424) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: flash-attention internal "git submodule update" problematic for offline-install

### Issue 正文摘录

### Your current environment N/A ### How you are installing vllm pip install . I was building vllm off-line with clones of CUTLASS and flash-attention. flash-attention (setup.py) does a "git submodule update" to populate the CUTLASS include files it needs. This is problematic for an off-line install. It would be better if it payed attention to VLLM_CUTLASS_SRC_DIR or something like that. A simple work around is to just copy the CUTLASS include tree into flash-attention csrc/cutlass subdirectory before building vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: flash-attention internal "git submodule update" problematic for offline-install installation;stale ### Your current environment N/A ### How you are installing vllm pip install . I was building vllm off
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: talling vllm pip install . I was building vllm off-line with clones of CUTLASS and flash-attention. flash-attention (setup.py) does a "git submodule update" to populate the CUTLASS include files it needs. This is proble...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rnal "git submodule update" problematic for offline-install installation;stale ### Your current environment N/A ### How you are installing vllm pip install . I was building vllm off-line with clones of CUTLASS and flash...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
