# vllm-project/vllm#30633: [Installation]: How to install vLLM 0.11.0 with CUDA < 12.9 (Driver 535)? No matching wheels found

| 字段 | 值 |
| --- | --- |
| Issue | [#30633](https://github.com/vllm-project/vllm/issues/30633) |
| 状态 | open |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: How to install vLLM 0.11.0 with CUDA < 12.9 (Driver 535)? No matching wheels found

### Issue 正文摘录

### Your current environment I’m trying to install vLLM 0.11.0 on a machine with NVIDIA Driver 535, and I ran into issues related to CUDA version compatibility. Environment OS: Linux (Ubuntu 20.04 / 22.04) GPU: NVIDIA GPU H20 NVIDIA Driver: 535.xx Python: 3.10 vLLM version: 0.11.0 Problem According to the release information for vLLM 0.11.0, the available prebuilt wheels appear to target CUDA 12.9+. However, with Driver 535, CUDA 12.9 is not supported, and I cannot find any official wheels for CUDA 12.1 / 12.2 / 12.4 or lower. This leads to the following questions: Is vLLM 0.11.0 officially compatible with CUDA versions < 12.9? If yes, what is the recommended way to install it on systems with Driver 535? Build from source with a specific CUDA version? Use a specific Docker image? Pin to an older vLLM release? Are there plans to provide prebuilt wheels for CUDA 12.1 / 12.4, or is CUDA 12.9+ now a hard requirement going forward? What I’ve tried Checked the GitHub Releases page for vLLM 0.11.0 — no wheels for CUDA < 12.9 Verified that upgrading CUDA to 12.9 is not possible with Driver 535 Looked for documentation on source builds for older CUDA versions, but didn’t find clear guidanc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: How to install vLLM 0.11.0 with CUDA < 12.9 (Driver 535)? No matching wheels found installation ### Your current environment I’m trying to install vLLM 0.11.0 on a machine with NVIDIA Driver 535, and I ra
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: How to install vLLM 0.11.0 with CUDA < 12.9 (Driver 535)? No matching wheels found installation ### Your current environment I’m trying to install vLLM 0.11.0 on a machine with NVIDIA Driver 535, and I r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Python: 3.10 vLLM version: 0.11.0 Problem According to the release information for vLLM 0.11.0, the available prebuilt wheels appear to target CUDA 12.9+. However, with Driver 535, CUDA 12.9 is not supported, and I cann...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
