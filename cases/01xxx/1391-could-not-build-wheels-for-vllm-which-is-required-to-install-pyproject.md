# vllm-project/vllm#1391:  Could not build wheels for vllm, which is required to install pyproject.toml-based projects

| 字段 | 值 |
| --- | --- |
| Issue | [#1391](https://github.com/vllm-project/vllm/issues/1391) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |
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

>  Could not build wheels for vllm, which is required to install pyproject.toml-based projects

### Issue 正文摘录

This appears to be an issue with CUDA version requiring 11.7. However, there are security concerns with this version of CUDA requiring me to use version 12.2 is there any intention of updating vLLM to work with the latest version of CUDA?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Could not build wheels for vllm, which is required to install pyproject.toml-based projects installation;stale This appears to be an issue with CUDA version requiring 11.7. However, there are security concerns with this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .toml-based projects installation;stale This appears to be an issue with CUDA version requiring 11.7. However, there are security concerns with this version of CUDA requiring me to use version 12.2 is there any intentio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: which is required to install pyproject.toml-based projects installation;stale This appears to be an issue with CUDA version requiring 11.7. However, there are security concerns with this version of CUDA requiring me to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: version 12.2 is there any intention of updating vLLM to work with the latest version of CUDA? development ci_build cuda build_error env_dependency This appears to be an issue with CUDA version requiring 11.7. However, t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
