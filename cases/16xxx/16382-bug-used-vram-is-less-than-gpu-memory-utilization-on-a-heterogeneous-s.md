# vllm-project/vllm#16382: [Bug]: Used VRAM is less than GPU memory utilization on a heterogeneous setup

| 字段 | 值 |
| --- | --- |
| Issue | [#16382](https://github.com/vllm-project/vllm/issues/16382) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Used VRAM is less than GPU memory utilization on a heterogeneous setup

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Setup Info** Node A has a 3090(24G VRAM), node B has a L40S(48G). Ray cluster is ready. **Reproduce Steps** Run: ``` vllm serve /path/to/Qwen/Qwen2.5-1.5B-Instruct --max-model-len 8192 --tensor-parallel-size 1 --pipeline-parallel-size 2 --distributed-executor-backend ray --gpu-memory-utilization=0.5 ``` In node B, VRAM usage is less than `--gpu-memory-utilization=0.5`. I don't find clear explanation in the documentation. Is this expected? nvidia-smi outputs: ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA L40S On | 00000000:38:00.0 Off | 0 | | N/A 42C P0 85W / 350W | 12891MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: t find clear explanation in the documentation. Is this expected? nvidia-smi outputs: ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.90.07 Driver Version:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Ray cluster is ready. **Reproduce Steps** Run: ``` vllm serve /path/to/Qwen/Qwen2.5-1.5B-Instruct --max-model-len 8192 --tensor-parallel-size 1 --pipeline-parallel-size 2 --distributed-executor-backend ray --gpu-memory-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tensor-parallel-size 1 --pipeline-parallel-size 2 --distributed-executor-backend ray --gpu-memory-utilization=0.5 ``` In node B, VRAM usage is less than `--gpu-memory-utilization=0.5`. I don't find clear explanation in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: A has a 3090(24G VRAM), node B has a L40S(48G). Ray cluster is ready. **Reproduce Steps** Run: ``` vllm serve /path/to/Qwen/Qwen2.5-1.5B-Instruct --max-model-len 8192 --tensor-parallel-size 1 --pipeline-parallel-size 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
