# vllm-project/vllm#964: More precise memory profile

| 字段 | 值 |
| --- | --- |
| Issue | [#964](https://github.com/vllm-project/vllm/issues/964) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> More precise memory profile

### Issue 正文摘录

Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: More precise memory profile Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()` performance cuda env_dependency Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()`
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: More precise memory profile Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()` performance cuda env_dependency Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()`
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: More precise memory profile Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()` performance cuda env_dependency Use `torch.cuda.mem_get_info()` instead of `torch.cuda.max_memory_allocated()`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
