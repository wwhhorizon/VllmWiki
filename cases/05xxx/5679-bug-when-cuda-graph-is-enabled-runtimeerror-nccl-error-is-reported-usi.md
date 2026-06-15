# vllm-project/vllm#5679: [Bug]: When cuda_graph is enabled, RunTimeError:NCCL error is reported using nvidia-nccl-cu11

| 字段 | 值 |
| --- | --- |
| Issue | [#5679](https://github.com/vllm-project/vllm/issues/5679) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When cuda_graph is enabled, RunTimeError:NCCL error is reported using nvidia-nccl-cu11

### Issue 正文摘录

### Your current environment 1、 torch 2.3.0+cu118 vllm 0.4.3+cu118 2、 [root@master1 v2]# pip show torch Name: torch Version: 2.3.0+cu118 Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration Home-page: https://pytorch.org/ Author: PyTorch Team Author-email: [packages@pytorch.org](mailto:packages@pytorch.org) License: BSD-3 Location: /opt/anaconda3/envs/vllm4/lib/python3.10/site-packages Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu11, nvidia-cuda-cupti-cu11, nvidia-cuda-nvrtc-cu11, nvidia-cuda-runtime-cu11, nvidia-cudnn-cu11, nvidia-cufft-cu11, nvidia-curand-cu11, nvidia-cusolver-cu11, nvidia-cusparse-cu11, nvidia-nccl-cu11, nvidia-nvtx-cu11, sympy, triton, typing-extensions 3、(vllm4) [root@master1 v2]# pip list |grep nccl nvidia-nccl-cu11 2.20.5 ### 🐛 Describe the bug When cuda_graph is enabled, RunTimeError:NCCL error is reported using nvidia-nccl-cu11 pip install nvidia-nccl-cu12 is ok.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: +cu118 vllm 0.4.3+cu118 2、 [root@master1 v2]# pip show torch Name: torch Version: 2.3.0+cu118 Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration Home-page: https://pytorch.org/ Author: P...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: r-cu11, nvidia-cusparse-cu11, nvidia-nccl-cu11, nvidia-nvtx-cu11, sympy, triton, typing-extensions 3、(vllm4) [root@master1 v2]# pip list |grep nccl nvidia-nccl-cu11 2.20.5 ### 🐛 Describe the bug When cuda_graph is enabl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: When cuda_graph is enabled, RunTimeError:NCCL error is reported using nvidia-nccl-cu11 bug;stale ### Your current environment 1、 torch 2.3.0+cu118 vllm 0.4.3+cu118 2、 [root@master1 v2]# pip show torch Name: torch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: enabled, RunTimeError:NCCL error is reported using nvidia-nccl-cu11 bug;stale ### Your current environment 1、 torch 2.3.0+cu118 vllm 0.4.3+cu118 2、 [root@master1 v2]# pip show torch Name: torch Version: 2.3.0+cu118 Summ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
