# vllm-project/vllm#16707: [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution. & RuntimeError: NCCL error: unhandled system error

| 字段 | 值 |
| --- | --- |
| Issue | [#16707](https://github.com/vllm-project/vllm/issues/16707) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution. & RuntimeError: NCCL error: unhandled system error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to deploy the model in a multi-machine and multi-GPU parallel manner using the **Docker (version: 0.8.4)** of vllm on three servers. Their hardware configurations are the same (8 * RTX 4090). When I deploy the model on Server 1, Server 2, and Server 3 separately, it works normally. When I deploy the model in parallel on Server 1 and Server 3, it also runs normally. However, when I try to deploy the model in a multi-machine and multi-GPU parallel manner using Server 1 and Server 3, or Server 2 and Server 3, or Server 1, Server 2 and Server 3, an error will occur. The error is as follows (**the following is the error when I tried to deploy on Server 1 and Server 2**). full log is here: [error.log](https://github.com/user-attachments/files/19773668/docker_run.log) ``` [rank0]: Traceback (most recent call last): [rank0]: File "/usr/local/bin/vllm", line 10, in [rank0]: sys.exit(main()) [rank0]: ^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 51, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: y the model in a multi-machine and multi-GPU parallel manner using the **Docker (version: 0.8.4)** of vllm on three servers. Their hardware configurations are the same (8 * RTX 4090). When I deploy the model on Server 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: f vllm on three servers. Their hardware configurations are the same (8 * RTX 4090). When I deploy the model on Server 1, Server 2, and Server 3 separately, it works normally. When I deploy the model in parallel on Serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution. & RuntimeError: NCCL error: unhandled system error bug;stale ### Your current environment ### 🐛 Describe the bug I tried t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ckages/vllm/entrypoints/cli/main.py", line 51, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd [rank0]: uvloop.run(run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ur current environment ### 🐛 Describe the bug I tried to deploy the model in a multi-machine and multi-GPU parallel manner using the **Docker (version: 0.8.4)** of vllm on three servers. Their hardware configurations ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
