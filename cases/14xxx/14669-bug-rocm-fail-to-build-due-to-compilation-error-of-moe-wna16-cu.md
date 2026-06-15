# vllm-project/vllm#14669: [Bug]: ROCm fail to build due to compilation error of `moe_wna16.cu`

| 字段 | 值 |
| --- | --- |
| Issue | [#14669](https://github.com/vllm-project/vllm/issues/14669) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm fail to build due to compilation error of `moe_wna16.cu`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When compiling the latest vLLM commit on ROCm, it gives the following error. ![Image](https://github.com/user-attachments/assets/7e950073-9dae-4918-8e0f-ec7881ed76d0) The error comes from the compilation of CUDA only kernels, introduced in https://github.com/vllm-project/vllm/commit/90e88ab75632745c137647bf710d63997529fb89. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#14671 [ROCm][Bugfix] Fix ROCm build failure

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: ROCm fail to build due to compilation error of `moe_wna16.cu` bug;stale ### Your current environment ### 🐛 Describe the bug When compiling the latest vLLM commit on ROCm, it gives the following error. ![Image](ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ROCm fail to build due to compilation error of `moe_wna16.cu` bug;stale ### Your current environment ### 🐛 Describe the bug When compiling the latest vLLM commit on ROCm, it gives the following error. ![Image](ht...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: ROCm fail to build due to compilation error of `moe_wna16.cu` bug;stale ### Your current environment ### 🐛 Describe the bug When compiling the latest vLLM commit on ROCm, it gives the following error. ![Image](ht...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: ROCm fail to build due to compilation error of `moe_wna16.cu` bug;stale ### Your current environment ### 🐛 Describe the bug When compiling the latest vLLM commit on ROCm, it gives the following error. ![Image](ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: our current environment ### 🐛 Describe the bug When compiling the latest vLLM commit on ROCm, it gives the following error. ![Image](https://github.com/user-attachments/assets/7e950073-9dae-4918-8e0f-ec7881ed76d0) The e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14671](https://github.com/vllm-project/vllm/pull/14671) | closes_keyword | 0.95 |  [ROCm][Bugfix] Fix ROCm build failure | FIX #14669 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
