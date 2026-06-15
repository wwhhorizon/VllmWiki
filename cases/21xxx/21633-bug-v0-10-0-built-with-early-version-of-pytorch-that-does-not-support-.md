# vllm-project/vllm#21633: [Bug]: v0.10.0 built with early version of pytorch that does not support sm-120

| 字段 | 值 |
| --- | --- |
| Issue | [#21633](https://github.com/vllm-project/vllm/issues/21633) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.10.0 built with early version of pytorch that does not support sm-120

### Issue 正文摘录

### Your current environment vllm-1 | /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:287: UserWarning: vllm-1 | NVIDIA GeForce RTX 5070 Ti with CUDA capability sm_120 is not compatible with the current PyTorch installation. vllm-1 | The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. vllm-1 | If you want to use the NVIDIA GeForce RTX 5070 Ti GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/ vllm-1 | v0.9.2 works with SM-120, i.e. Blackwell on RTX 5000 series. v0.10.0 does not. Suggest rebuilding and forcing pytorch to be >=2.7.1 ### 🐛 Describe the bug vllm-1 | /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:287: UserWarning: vllm-1 | NVIDIA GeForce RTX 5070 Ti with CUDA capability sm_120 is not compatible with the current PyTorch installation. vllm-1 | The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. vllm-1 | If you want to use the NVIDIA GeForce RTX 5070 Ti GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/ vllm-1 | v0.9.2 works with SM-120, i.e. Blackwell on RTX 5000 series...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: v0.10.0 built with early version of pytorch that does not support sm-120 bug ### Your current environment vllm-1 | /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:287: UserWarning: vllm-1 | NVIDIA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: v0.10.0 built with early version of pytorch that does not support sm-120 bug ### Your current environment vllm-1 | /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:287: UserWarning: vllm-1 | NVIDIA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development hardware_porting cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
