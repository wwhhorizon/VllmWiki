# vllm-project/vllm#7456: [Misc]: I want to run Llama 3.1 405B using speculative. Can you give me a guide?

| 字段 | 值 |
| --- | --- |
| Issue | [#7456](https://github.com/vllm-project/vllm/issues/7456) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: I want to run Llama 3.1 405B using speculative. Can you give me a guide?

### Issue 正文摘录

### Anything you want to discuss about vllm. I am trying to perform a serving performance test using pipeline parallelism with the LLAMA 3.1 405B model as a draft model with 8b, but the model fails to load after being loaded. Could you please guide me on this issue? $ vllm serve /models/Meta-Llama-3.1-405B-Instruct -tp 8 -pp 2 --speculative-model /models/Meta-Llama-3.1-8B-Instruct --use-v2-block-manager --num-speculative-tokens 5 $Logs mngc-001:7118:7118 [0] NCCL INFO comm 0x134fcb60 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1b000 commId 0x2d7e114b994d6072 - Init COMPLETE [rank0]: Traceback (most recent call last): [rank0]: File "/usr/local/bin/vllm", line 8, in [rank0]: sys.exit(main()) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 149, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 29, in serve [rank0]: asyncio.run(run_server(args)) [rank0]: File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run [rank0]: return loop.run_until_complete(main) [rank0]: File "/usr/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete [rank0]: return future.result() [...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Misc]: I want to run Llama 3.1 405B using speculative. Can you give me a guide? stale ### Anything you want to discuss about vllm. I am trying to perform a serving performance test using pipeline parallelism with the L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n3.10/dist-packages/vllm/scripts.py", line 29, in serve [rank0]: asyncio.run(run_server(args)) [rank0]: File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run [rank0]: return loop.run_until_complete(main) [rank0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 8 -pp 2 --speculative-model /models/Meta-Llama-3.1-8B-Instruct --use-v2-block-manager --num-speculative-tokens 5 $Logs mngc-001:7118:7118 [0] NCCL INFO comm 0x134fcb60 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1b000 com...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Misc]: I want to run Llama 3.1 405B using speculative. Can you give me a guide? stale ### Anything you want to discuss about vllm. I am trying to perform a serving performance test using pipeline parallelism with the L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: am trying to perform a serving performance test using pipeline parallelism with the LLAMA 3.1 405B model as a draft model with 8b, but the model fails to load after being loaded. Could you please guide me on this issue?...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
