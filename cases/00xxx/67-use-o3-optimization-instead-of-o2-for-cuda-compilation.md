# vllm-project/vllm#67: Use O3 optimization instead of O2 for CUDA compilation?

| 字段 | 值 |
| --- | --- |
| Issue | [#67](https://github.com/vllm-project/vllm/issues/67) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Use O3 optimization instead of O2 for CUDA compilation?

### Issue 正文摘录

We are currently using the `-O2` flag in compiling our CUDA kernels. We need to investigate whether/how changing it to `-O3` affects the system performance and compilation time.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cts the system performance and compilation time. performance cuda;kernel build_error We are currently using the `-O2` flag in compiling our CUDA kernels. We need to investigate whether/how changing it to `-O3` affects t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Use O3 optimization instead of O2 for CUDA compilation? performance We are currently using the `-O2` flag in compiling our CUDA kernels. We need to investigate whether/how changing it to `-O3` affects the system perform...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
