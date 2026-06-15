# vllm-project/vllm#27628: [Bug]: nccl can't use NET plugin Socket after update to torch 2.9

| 字段 | 值 |
| --- | --- |
| Issue | [#27628](https://github.com/vllm-project/vllm/issues/27628) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nccl can't use NET plugin Socket after update to torch 2.9

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tensor Parallel works well before torch 2.9 commit (for example `250fb1b8ea836ab4cdd2890581815a9c19b8b8ed`). It can use socket connection. ``` INFO 10-28 11:44:15 [pynccl.py:111] vLLM is using nccl==2.27.3 idc-st-mad-gpu-004:3125165:3125165 [0] NCCL INFO cudaDriverVersion 12010 idc-st-mad-gpu-004:3125165:3125165 [0] NCCL INFO NCCL version 2.27.3+cuda12.9 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL INFO cudaDriverVersion 12010 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL INFO Bootstrap: Using bond0:192.168.12.70 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL INFO NCCL version 2.27.3+cuda12.9 idc-st-mad-gpu-004:3125166:3125166 [1] NCCL INFO cudaDriverVersion 12010 idc-st-mad-gpu-004:3125166:3125166 [1] NCCL INFO Bootstrap: Using bond0:192.168.12.70 idc-st-mad-gpu-004:3125166:3125166 [1] NCCL INFO NCCL version 2.27.3+cuda12.9 idc-st-mad-gpu-004:3125168:3125168 [3] NCCL INFO cudaDriverVersion 12010 idc-st-mad-gpu-004:3125168:3125168 [3] NCCL INFO Bootstrap: Using bond0:192.168.12.70 idc-st-mad-gpu-004:3125168:3125168 [3] NCCL INFO NCCL version 2.27.3+cuda12.9 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL INFO NET/Plugin: Could not find: li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nccl==2.27.3 idc-st-mad-gpu-004:3125165:3125165 [0] NCCL INFO cudaDriverVersion 12010 idc-st-mad-gpu-004:3125165:3125165 [0] NCCL INFO NCCL version 2.27.3+cuda12.9 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL INFO cudaDr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: M is using nccl==2.27.3 idc-st-mad-gpu-004:3125165:3125165 [0] NCCL INFO cudaDriverVersion 12010 idc-st-mad-gpu-004:3125165:3125165 [0] NCCL INFO NCCL version 2.27.3+cuda12.9 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: nccl can't use NET plugin Socket after update to torch 2.9 bug;stale ### Your current environment ### 🐛 Describe the bug Tensor Parallel works well before torch 2.9 commit (for example `250fb1b8ea836ab4cdd2890581...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;speculative_decoding cuda;kernel;operator;triton build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Chunksize set to 131072 idc-st-mad-gpu-004:3125167:3125167 [2] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. idc-st-mad-gpu-004:3125166:3125166 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
