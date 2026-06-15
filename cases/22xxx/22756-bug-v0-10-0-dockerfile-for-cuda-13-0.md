# vllm-project/vllm#22756: [Bug]: v0.10.0 Dockerfile for CUDA 13.0?

| 字段 | 值 |
| --- | --- |
| Issue | [#22756](https://github.com/vllm-project/vllm/issues/22756) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.10.0 Dockerfile for CUDA 13.0?

### Issue 正文摘录

### Your current environment Anyone have a Dockerfile for v0.10.0 vLLM for CUDA 13 and PyTorch >= 2.7.1 (preferably 2.8.0+) that works with Blackwell? Or is there a nightly build that works? v0.9.2 was the last release that worked without a custom Dockerfile. ### 🐛 Describe the bug releases after 0.92.0 only support CUDA 12.4, nothing later. I did see a Dockerfile that worked for 12.8. For other reasons, I'm on CUDA 13.0 and looking for a way to get v0.10.0 to work. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: v0.10.0 Dockerfile for CUDA 13.0? bug ### Your current environment Anyone have a Dockerfile for v0.10.0 vLLM for CUDA 13 and PyTorch >= 2.7.1 (preferably 2.8.0+) that works with Blackwell? Or is there a nightly b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: v0.10.0 Dockerfile for CUDA 13.0? bug ### Your current environment Anyone have a Dockerfile for v0.10.0 vLLM for CUDA 13 and PyTorch >= 2.7.1 (preferably 2.8.0+) that works with Blackwell? Or is there a nightly b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
