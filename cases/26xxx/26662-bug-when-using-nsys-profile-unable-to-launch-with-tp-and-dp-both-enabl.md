# vllm-project/vllm#26662: [Bug]: When using `nsys profile`, unable to launch with `TP` and `DP` both enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#26662](https://github.com/vllm-project/vllm/issues/26662) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using `nsys profile`, unable to launch with `TP` and `DP` both enabled

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/user-attachments/files/22872934/env.txt) ### 🐛 Describe the bug When launching vLLM server with the following command (the same as [documentation's instructs](https://docs.vllm.ai/en/latest/contributing/profiling.html#openai-server_1)), vllm failed to start: ```shell nsys profile -o ./my_report.nsys-rep --trace-fork-before-exec=true --cuda-graph-trace=node \ --delay 300 --duration 30 \ vllm serve ../../models/Qwen3-30B-A3B --dtype auto \ --no-disable-nccl-for-dp-synchronization \ --no-enable-prefix-caching --trust-remote-code \ --tensor-parallel-size 2 --data-parallel-size 2 --enable-expert-parallel \ --max-num-seqs 120 \ --max-model-len 9600 \ --port 10086 ``` Facing an assertion in `cuda_communicator.py`: ``` File "vllm/vllm/distributed/device_communicators/cuda_communicator.py", line 285, in all_gatherv assert pynccl_comm is not None and not pynccl_comm.disabled ``` However, when disabling `DP` with setting `--data-parallel-size 1` or disabling `TP` with setting `--tensor-parallel-size 1`, vLLM could run successfully. Also, when launching vllm without using `nsys profile`, enabling `DP` and `TP` at the same time doesn't...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: When using `nsys profile`, unable to launch with `TP` and `DP` both enabled bug;stale ### Your current environment [env.txt](https://github.com/user-attachments/files/22872934/env.txt) ### 🐛 Describe the bug When...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ell nsys profile -o ./my_report.nsys-rep --trace-fork-before-exec=true --cuda-graph-trace=node \ --delay 300 --duration 30 \ vllm serve ../../models/Qwen3-30B-A3B --dtype auto \ --no-disable-nccl-for-dp-synchronization...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cuda-graph-trace=node \ --delay 300 --duration 30 \ vllm serve ../../models/Qwen3-30B-A3B --dtype auto \ --no-disable-nccl-for-dp-synchronization \ --no-enable-prefix-caching --trust-remote-code \ --tensor-parallel-size...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: remote-code \ --tensor-parallel-size 2 --data-parallel-size 2 --enable-expert-parallel \ --max-num-seqs 120 \ --max-model-len 9600 \ --port 10086 ``` Facing an assertion in `cuda_communicator.py`: ``` File "vllm/vllm/di...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: \ --max-num-seqs 120 \ --max-model-len 9600 \ --port 10086 ``` Facing an assertion in `cuda_communicator.py`: ``` File "vllm/vllm/distributed/device_communicators/cuda_communicator.py", line 285, in all_gatherv assert p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
