# vllm-project/vllm#19746: [Usage]: embed prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#19746](https://github.com/vllm-project/vllm/issues/19746) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: embed prompts

### Issue 正文摘录

### Your current environment I'm running vllm on my laptop with no gpu (laster master branch version). I'm using the same library versions used by vllm's requirements files on a linux machine. ```text [W617 09:11:14.826998707 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Tensor registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: AutocastCPU previous kernel: registered at /pytorch/aten/src/ATen/autocast_mode.cpp:327 new kernel: registered at /opt/workspace/ipex-cpu-dev/csrc/cpu/autocast/autocast_mode.cpp:112 (function operator()) INFO 06-17 09:11:16 [__init__.py:244] Automatically detected platform cpu. Collecting environment information... ============================== System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version : (GCC) 15.1.1 20250521 (Red Hat 15.1.1-2) Clang version : 20.1.6 (Fedora 20.1.6-1.fc42) CMake version...

## 现有链接修复摘要

#24278 [CORE] Prompt Embeddings Support for v1 Engine

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ronment I'm running vllm on my laptop with no gpu (laster master branch version). I'm using the same library versions used by vllm's requirements files on a linux machine. ```text [W617 09:11:14.826998707 OperatorEntry....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ch version : 2.7.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: __.py:244] Automatically detected platform cpu. Collecting environment information... ============================== System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack overf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Te...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24278](https://github.com/vllm-project/vllm/pull/24278) | closes_keyword | 0.95 | [CORE] Prompt Embeddings Support for v1 Engine | Fixes #19746. Prompt Embedding inputs are a niche, but frequently asked for feature in vLLM. https://github.com/vllm-project/vllm/pull/15428 introduced them in the v0 engine, but |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
