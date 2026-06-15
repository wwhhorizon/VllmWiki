# vllm-project/vllm#34296: [Usage]:  vllm/vllm-openai:v0.15.1  No CUDA GPUs are available,0.10.1.1 is ok

| 字段 | 值 |
| --- | --- |
| Issue | [#34296](https://github.com/vllm-project/vllm/issues/34296) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  vllm/vllm-openai:v0.15.1  No CUDA GPUs are available,0.10.1.1 is ok

### Issue 正文摘录

### Your current environment wsl nvidia-smi ``` root@DESKTOP-G31254H:/mnt/c/Users/CTOS# nvidia-smi Wed Feb 11 09:04:50 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 575.51.02 Driver Version: 576.02 CUDA Version: 12.9 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA GeForce RTX 4090 On | 00000000:65:00.0 Off | Off | | 30% 35C P8 17W / 450W | 40838MiB / 49140MiB | 1% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA GeForce RTX 4090 On | 00000000:B3:00.0 Off | Off | | 30% 39C P8 5W / 450W | 42388MiB / 49140MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type P...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ----------------------------+ | NVIDIA-SMI 575.51.02 Driver Version: 576.02 CUDA Version: 12.9 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: vllm/vllm-openai:v0.15.1 No CUDA GPUs are available,0.10.1.1 is ok usage ### Your current environment wsl nvidia-smi ``` root@DESKTOP-G31254H:/mnt/c/Users/CTOS# nvidia-smi Wed Feb 11 09:04:50 2026 +------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ckages/vllm/collect_env.py", line 831, in main Collecting environment information... output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/collect_env.py", line 826, in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /dist-packages/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/collect_env.py", line 24, in cmd collect_env_main() File "/u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; IBRS Vu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
