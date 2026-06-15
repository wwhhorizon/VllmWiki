# vllm-project/vllm#194: Ubuntu pip installation issue

| 字段 | 值 |
| --- | --- |
| Issue | [#194](https://github.com/vllm-project/vllm/issues/194) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Ubuntu pip installation issue

### Issue 正文摘录

On ubuntu 20.04, Python 3.10, pip 23.1.2 Issue persisting with Python 3.8 and pip 21.2.4 ``` Collecting vllm Using cached vllm-0.1.0.tar.gz (83 kB) Running command pip subprocess to install build dependencies Collecting ninja Using cached ninja-1.11.1-py2.py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (145 kB) Collecting packaging Using cached packaging-23.1-py3-none-any.whl (48 kB) Collecting setuptools Using cached setuptools-68.0.0-py3-none-any.whl (804 kB) Collecting torch>=2.0.0 Using cached torch-2.0.1-cp310-cp310-manylinux1_x86_64.whl (619.9 MB) Collecting wheel Using cached wheel-0.40.0-py3-none-any.whl (64 kB) Collecting filelock (from torch>=2.0.0) Using cached filelock-3.12.2-py3-none-any.whl (10 kB) Collecting typing-extensions (from torch>=2.0.0) Using cached typing_extensions-4.6.3-py3-none-any.whl (31 kB) Collecting sympy (from torch>=2.0.0) Using cached sympy-1.12-py3-none-any.whl (5.7 MB) Collecting networkx (from torch>=2.0.0) Using cached networkx-3.1-py3-none-any.whl (2.1 MB) Collecting jinja2 (from torch>=2.0.0) Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB) Collecting nvidia-cuda-nvrtc-cu11==11.7.99 (from torch>=2.0.0) Using cached nvidia_cuda_n...

## 现有链接修复摘要

#12446 [Bugfix] Fix Granite 3.0 MoE model loading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Ubuntu pip installation issue installation On ubuntu 20.04, Python 3.10, pip 23.1.2 Issue persisting with Python 3.8 and pip 21.2.4 ``` Collecting vllm Using cached vllm-0.1.0.tar.gz (83 kB) Running command pip subproce...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d. This behaviour is the source of the following dependency conflicts. llama-index 0.6.29 requires typing-extensions==4.5.0, but you have typing-extensions 4.6.3 which is incompatible. Successfully installed MarkupSafe-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ia_nvtx_cu11-11.7.91-py3-none-manylinux1_x86_64.whl (98 kB) Collecting triton==2.0.0 (from torch>=2.0.0) Using cached triton-2.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (63.3 MB) Collecting cmake...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB) Collecting nvidia-cuda-nvrtc-cu11==11.7.99 (from torch>=2.0.0) Using cached nvidia_cuda_nvrtc_cu11-11.7.99-2-py3-none-manylinux1_x86_64.whl (21.0 MB) Collecting nvidia...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ;triton build_error;crash env_dependency #12446 [Bugfix] Fix Granite 3.0 MoE model loading On ubuntu 20.04, Python 3.10, pip 23.1.2

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12446](https://github.com/vllm-project/vllm/pull/12446) | closes_keyword | 0.95 | [Bugfix] Fix Granite 3.0 MoE model loading | fixes the failure in Granite model tests (https://buildkite.com/vllm/ci/builds/12467#0194a0fc-112d-48fd-a0d4-099edd508fef). The problem was introduced by https://github.com/vllm-pr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
