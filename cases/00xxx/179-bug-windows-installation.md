# vllm-project/vllm#179: Bug: Windows installation

| 字段 | 值 |
| --- | --- |
| Issue | [#179](https://github.com/vllm-project/vllm/issues/179) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug: Windows installation

### Issue 正文摘录

I got this message when trying out vllm with windows; `No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin'` Cuda is installed and available in the directory. Does vllm support windows installation now? Thanks for great work

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Bug: Windows installation installation I got this message when trying out vllm with windows; `No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin'` Cuda is installed a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: installation I got this message when trying out vllm with windows; `No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin'` Cuda is installed and available in the direct...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
