# vllm-project/vllm#4599: [Bug]: I used vllm=0.4.1 to run the squeezellm, I meet the bug RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED at "/opt/hostedtoolcache/Python/3.10.14/x64/lib/python3.10/site-packages/torch/include/c10/cuda/impl/CUDAGuardImpl.h":25, please report a bug to PyTorch. 

| 字段 | 值 |
| --- | --- |
| Issue | [#4599](https://github.com/vllm-project/vllm/issues/4599) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: I used vllm=0.4.1 to run the squeezellm, I meet the bug RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED at "/opt/hostedtoolcache/Python/3.10.14/x64/lib/python3.10/site-packages/torch/include/c10/cuda/impl/CUDAGuardImpl.h":25, please report a bug to PyTorch. 

### Issue 正文摘录

### Your current environment [Bug]: I used vllm=0.4.1 to run the squeezellm, I meet the bug RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED at "/opt/hostedtoolcache/Python/3.10.14/x64/lib/python3.10/site-packages/torch/include/c10/cuda/impl/CUDAGuardImpl.h":25, please report a bug to PyTorch. ### 🐛 Describe the bug [Bug]: I used vllm=0.4.1 to run the squeezellm, I meet the bug RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED at "/opt/hostedtoolcache/Python/3.10.14/x64/lib/python3.10/site-packages/torch/include/c10/cuda/impl/CUDAGuardImpl.h":25, please report a bug to PyTorch.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: UDAGuardImpl.h":25, please report a bug to PyTorch. development cuda env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 4.1 to run the squeezellm, I meet the bug RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED at "/opt/hostedtoolcache/Python/3.10.14/x64/lib/python3.10/site-packages/torch/include/c10/cuda/impl/CUDAGuardImpl.h":...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /c10/cuda/impl/CUDAGuardImpl.h":25, please report a bug to PyTorch. bug;stale ### Your current environment [Bug]: I used vllm=0.4.1 to run the squeezellm, I meet the bug RuntimeError: t == DeviceType::CUDA INTERNAL ASSE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
