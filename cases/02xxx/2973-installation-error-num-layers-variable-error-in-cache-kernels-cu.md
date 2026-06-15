# vllm-project/vllm#2973: Installation error -- "num_layers" variable error in cache_kernels.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#2973](https://github.com/vllm-project/vllm/issues/2973) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Installation error -- "num_layers" variable error in cache_kernels.cu

### Issue 正文摘录

I saw a prior post that was a similar issue, but it received no responses so I am trying fresh. I saw posts about the issues with the pyproject.toml file and I self-edited it to point to my CUDA capable version of pytorch. But upon running the setup.py install, I am getting this error: C:\Users\sekle\VLLM\vllm\csrc\cache_kernels.cu(109): error: expression must have a constant value int64_t key_cache_ptrs[num_layers]; ^ C:\Users\sekle\VLLM\vllm\csrc\cache_kernels.cu(109): note #2689-D: the value of variable "num_layers" (declared at line 99) cannot be used as a constant int64_t key_cache_ptrs[num_layers]; ^ C:\Users\sekle\VLLM\vllm\csrc\cache_kernels.cu(110): error: expression must have a constant value int64_t value_cache_ptrs[num_layers]; ^ C:\Users\sekle\VLLM\vllm\csrc\cache_kernels.cu(110): note #2689-D: the value of variable "num_layers" (declared at line 99) cannot be used as a constant int64_t value_cache_ptrs[num_layers]; ^ 2 errors detected in the compilation of "csrc/cache_kernels.cu". I am extremely new to programming, and once I got through my troubleshooting to where this was the only error left, I have no idea where to go next. Any help is extremely appreciated!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Installation error -- "num_layers" variable error in cache_kernels.cu I saw a prior post that was a similar issue, but it received no responses so I am trying fresh. I saw posts about the issues with the pyproject.toml
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: issues with the pyproject.toml file and I self-edited it to point to my CUDA capable version of pytorch. But upon running the setup.py install, I am getting this error: C:\Users\sekle\VLLM\vllm\csrc\cache_kernels.cu(109...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
