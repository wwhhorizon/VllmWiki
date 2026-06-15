# vllm-project/vllm#651: cache_kernel.cu does not compile using pip install -e . on source code

| 字段 | 值 |
| --- | --- |
| Issue | [#651](https://github.com/vllm-project/vllm/issues/651) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> cache_kernel.cu does not compile using pip install -e . on source code

### Issue 正文摘录

Neither in docker (with the suggested docker), nor on my own environment, I get to compilte the cache_kernel.cu. NCVV = 11.8, also using the PyTorch 2.0.1 CUDA 11.8 package. At first, it didn't install at all because of the myproject.toml pointing towards a pytorch in pip that is not cuda enabled. After removing the toml file, I ran into these errors: vllm\csrc\cache_kernels.cu(41): error: expression must be a pointer to a complete object type vllm\csrc\cache_kernels.cu(42): error: expression must be a pointer to a complete object type vllm\csrc\cache_kernels.cu(96): error: expression must have a constant value vllm\csrc\cache_kernels.cu(96): note #2689-D: the value of variable "num_layers" (86): here cannot be used as a constant vllm\csrc\cache_kernels.cu(97): error: expression must have a constant value vllm\csrc\cache_kernels.cu(97): note #2689-D: the value of variable "num_layers" (86): here cannot be used as a constant

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cache_kernel.cu does not compile using pip install -e . on source code installation Neither in docker (with the suggested docker), nor on my own environment, I get to compilte the cache_kernel.cu. NCVV = 11.8, also usin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: compilte the cache_kernel.cu. NCVV = 11.8, also using the PyTorch 2.0.1 CUDA 11.8 package. At first, it didn't install at all because of the myproject.toml pointing towards a pytorch in pip that is not cuda enabled. Aft...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
