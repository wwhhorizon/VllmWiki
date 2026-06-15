# vllm-project/vllm#24160: [Bug]: [AMD GPU][OOM][RCCL Allreduce][NCCL error: unhandled cuda error] Got RCCL allreduce OOM error when running Llama405B TP8 on AMD GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#24160](https://github.com/vllm-project/vllm/issues/24160) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [AMD GPU][OOM][RCCL Allreduce][NCCL error: unhandled cuda error] Got RCCL allreduce OOM error when running Llama405B TP8 on AMD GPUs

### Issue 正文摘录

### Your current environment torch: 2.8.0+rocm7.0.0.lw.git3b41cb56 vllm: 0.10.1rc2.dev110+g31282401b.rocm700 aiter: 0.1.5.dev80+g86ba52753 device: MI355*8, single node ### 🐛 Describe the bug Hi, All We have got the NCCL Error when running the Llama 405B on single AMD node of 8*MI355 cards. Here is the log of failure. It comes from the NCCL. The detailed underlying error is OOM. Here is the log we got by add the debug log of RCCL: ``` 6507:[2025-09-02 05:37:31] smci355-ccs-aus-m01-25:441048:441048 [4] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04/22.04/build/rccl/hipify/src/include/alloc.h:317 NCCL WARN Cuda failure 'out of memory' 6784:[2025-09-02 05:37:31] smci355-ccs-aus-m01-25:441045:441045 [1] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04/22.04/build/rccl/hipify/src/include/alloc.h:317 NCCL WARN Cuda failure 'out of memory' 6899:[2025-09-02 05:37:31] smci355-ccs-aus-m01-25:441051:441051 [7] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04/22.04/build/rccl/hipify/src/include/alloc.h:317 NCCL WARN C...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: [AMD GPU][OOM][RCCL Allreduce][NCCL error: unhandled cuda error] Got RCCL allreduce OOM error when running Llama405B TP8 on AMD GPUs bug;rocm ### Your current environment torch: 2.8.0+rocm7.0.0.lw.git3b41cb56 vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: og we got by add the debug log of RCCL: ``` 6507:[2025-09-02 05:37:31] smci355-ccs-aus-m01-25:441048:441048 [4] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: L error: unhandled cuda error] Got RCCL allreduce OOM error when running Llama405B TP8 on AMD GPUs bug;rocm ### Your current environment torch: 2.8.0+rocm7.0.0.lw.git3b41cb56 vllm: 0.10.1rc2.dev110+g31282401b.rocm700 ai...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.8.0+rocm7.0.0.lw.git3b41cb56 vllm: 0.10.1rc2.dev110+g31282401b.rocm700 aiter: 0.1.5.dev80+g86ba52753 device: MI355*8, single node ### 🐛 Describe the bug Hi, All We have got the NCCL Error when running the Llama 405B o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: [AMD GPU][OOM][RCCL Allreduce][NCCL error: unhandled cuda error] Got RCCL allreduce OOM error when running Llama405B TP8 on AMD GPUs bug;rocm ### Your current environment torch: 2.8.0+rocm7.0.0.lw.git3b41cb56 vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
