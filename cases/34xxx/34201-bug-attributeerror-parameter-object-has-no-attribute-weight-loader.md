# vllm-project/vllm#34201: [Bug]: AttributeError: 'Parameter' object has no attribute 'weight_loader'

| 字段 | 值 |
| --- | --- |
| Issue | [#34201](https://github.com/vllm-project/vllm/issues/34201) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;kernel;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Parameter' object has no attribute 'weight_loader'

### Issue 正文摘录

### Your current environment ➜ wsl --version WSL version: 2.6.1.0 Kernel version: 6.6.87.2-1 WSLg version: 1.0.66 MSRDC version: 1.2.6353 Direct3D version: 1.611.1-81528511 DXCore version: 10.0.26100.1-240331-1435.ge-release Windows version: 10.0.19045.4780 ➜ python3 --version Python 3.12.10 ➜ vllm -v 0.15.1 ➜ nvidia-smi ```plaintext Tue Feb 10 10:08:55 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 580.82.10 Driver Version: 581.29 CUDA Version: 13.0 | +-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA GeForce RTX 3080 On | 00000000:01:00.0 On | N/A | | 0% 30C P8 23W / 320W | 19054MiB / 20480MiB | 2% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI P...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ttribute 'weight_loader' bug;stale ### Your current environment ➜ wsl --version WSL version: 2.6.1.0 Kernel version: 6.6.87.2-1 WSLg version: 1.0.66 MSRDC version: 1.2.6353 Direct3D version: 1.611.1-81528511 DXCore vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: .19045.4780 ➜ python3 --version Python 3.12.10 ➜ vllm -v 0.15.1 ➜ nvidia-smi ```plaintext Tue Feb 10 10:08:55 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e the bug ➜ export PYTORCH_ALLOC_CONF=expandable_segments:True ➜ export HF_HUB_OFFLINE=1 ➜ VLLM_SERVER_DEV_MODE=1 vllm serve \ cyankiwi/Ministral-3-14B-Instruct-2512-AWQ-4bit \ --served-model-name Ministral-3-14B-Instru...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | No running processes
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AttributeError: 'Parameter' object has no attribute 'weight_loader' bug;stale ### Your current environment ➜ wsl --version WSL version: 2.6.1.0 Kernel version: 6.6.87.2-1 WSLg version: 1.0.66 MSRDC version: 1.2.6353 Dir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
