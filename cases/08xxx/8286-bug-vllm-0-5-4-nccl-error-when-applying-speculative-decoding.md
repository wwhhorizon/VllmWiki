# vllm-project/vllm#8286: [Bug]: vllm 0.5.4 NCCL error when applying speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#8286](https://github.com/vllm-project/vllm/issues/8286) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.5.4 NCCL error when applying speculative decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed the inference service for the Qwen2 72B model using VLLM on 4 GPUs in the server. When I try to enable speculative decoding, I always encounter an NCCL error. I attempted to run the debug test code and found that the code cannot run properly. However, when I do not use speculative decoding, the service starts normally here is the output when running debug test code by `NCCL_DEBUG=TRACE VLLM_LOGGING_LEVEL=DEBUG torchrun --nproc-per-node=2 test.py`: ``` W0909 07:11:11.638000 140533383049856 torch/distributed/run.py:779] W0909 07:11:11.638000 140533383049856 torch/distributed/run.py:779] ***************************************** W0909 07:11:11.638000 140533383049856 torch/distributed/run.py:779] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. W0909 07:11:11.638000 140533383049856 torch/distributed/run.py:779] ***************************************** 0f139cc8454d:9292:9292 [0] NCCL INFO Bootstrap : Using eth0:172.17.0.15 0f139cc8454d:9292:9292 [0] NCCL INFO NET/Pl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g internal implementation 0f139cc8454d:9292:9292 [0] NCCL INFO cudaDriverVersion 12040 NCCL version 2.20.5+cuda12.4 0f139cc8454d:9293:9293 [1] NCCL INFO cudaDriverVersion 12040 0f139cc8454d:9293:9293 [1] NCCL INFO Boots...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ent ### 🐛 Describe the bug I deployed the inference service for the Qwen2 72B model using VLLM on 4 GPUs in the server. When I try to enable speculative decoding, I always encounter an NCCL error. I attempted to run the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .so), using internal implementation 0f139cc8454d:9292:9292 [0] NCCL INFO cudaDriverVersion 12040 NCCL version 2.20.5+cuda12.4 0f139cc8454d:9293:9293 [1] NCCL INFO cudaDriverVersion 12040 0f139cc8454d:9293:9293 [1] NCCL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm 0.5.4 NCCL error when applying speculative decoding bug ### Your current environment ### 🐛 Describe the bug I deployed the inference service for the Qwen2 72B model using VLLM on 4 GPUs in the server. When I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
