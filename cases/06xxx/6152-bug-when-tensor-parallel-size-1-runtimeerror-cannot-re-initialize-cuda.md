# vllm-project/vllm#6152: [Bug]: When tensor_parallel_size>1,  RuntimeError: Cannot re-initialize CUDA in forked subprocess.

| 字段 | 值 |
| --- | --- |
| Issue | [#6152](https://github.com/vllm-project/vllm/issues/6152) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When tensor_parallel_size>1,  RuntimeError: Cannot re-initialize CUDA in forked subprocess.

### Issue 正文摘录

### Your current environment vllm version: '0.5.0.post1' ### 🐛 Describe the bug When I set tensor_parallel_size=1, it works well. But, if I set tensor_parallel_size>1, below error occurs: RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method. After I add ``` import torch import multiprocessing torch.multiprocessing.set_start_method('spawn') ``` the same RuntimeError still occurs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ialize CUDA in forked subprocess. bug ### Your current environment vllm version: '0.5.0.post1' ### 🐛 Describe the bug When I set tensor_parallel_size=1, it works well. But, if I set tensor_parallel_size>1, below error o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: When tensor_parallel_size>1, RuntimeError: Cannot re-initialize CUDA in forked subprocess. bug ### Your current environment vllm version: '0.5.0.post1' ### 🐛 Describe the bug When I set tensor_parallel_size=1, it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
