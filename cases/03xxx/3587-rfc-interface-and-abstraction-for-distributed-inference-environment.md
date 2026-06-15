# vllm-project/vllm#3587: [RFC]: Interface and Abstraction for Distributed Inference Environment

| 字段 | 值 |
| --- | --- |
| Issue | [#3587](https://github.com/vllm-project/vllm/issues/3587) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;hardware_porting |
| 子分类 | race_cond |
| Operator 关键词 | kernel;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Interface and Abstraction for Distributed Inference Environment

### Issue 正文摘录

This RFC describes a proposal for interfaces and abstractions for distributed inference environments. I plan to solicit discussions for a week (until March 31st) before I begin to actually refactor the code. # Motivation The current distributed inference environment in `vllm` is quite tangled, and we often see deadlocks and hangs (see https://github.com/vllm-project/vllm/issues/3455 , https://github.com/vllm-project/vllm/issues/2770 , https://github.com/vllm-project/vllm/issues/3559 , to name a few). The problem becomes prominent when we try to upgrade to pytorch 2.2.0 (see https://github.com/vllm-project/vllm/pull/3442 , https://github.com/vllm-project/vllm/pull/3442 ), because `pytorch 2.2.0` upgrades from `nccl==2.18.1` to `2.19.3` (see https://pypi.org/pypi/torch/2.1.2/json and https://pypi.org/pypi/torch/2.2.0/json to compare the dependency), and `nccl==2.19.3` breaks `vllm` due to increased memory cost during cudagraph capture (from 10MB per graph to 100MB per graph, adds up to several GBs because we have dozens of cudagraph). TL,DR; distributed inference in current codebase is a headache. If it works, hooray; if not, don't be surprised. # Proposal ## Abstraction I think we...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s and abstractions for distributed inference environments. I plan to solicit discussions for a week (until March 31st) before I begin to actually refactor the code. # Motivation The current distributed inference environ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: inference environments. I plan to solicit discussions for a week (until March 31st) before I begin to actually refactor the code. # Motivation The current distributed inference environment in `vllm` is quite tangled, an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mplementation of Coordinator can be `torch.distributed`, with the `gloo` backend designed to communicate CPU tensors. Other considerations include MPI and custom-implemented TCP store. However, since we live in `torch`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: n-place allreduce function: `allreduce(char* input, size_t count, size_t dtype, size_t op)`. More functionality would be better (e.g. out-of-place allreduce, broadcast/reduce/scatter etc.), but inplace allreduce is all...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: The semantic is standard, no need for more explanation. 4. `barrier()`: block until all processes reaches here. Also standard communication primitive. Note: very often than not, we want to execute something in just one...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
