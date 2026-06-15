# vllm-project/vllm#40374: [Bug]: vllm does not use all of the available RAM

| 字段 | 值 |
| --- | --- |
| Issue | [#40374](https://github.com/vllm-project/vllm/issues/40374) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm does not use all of the available RAM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On Raspberry PI 5 (4Go), the following command fails due to insufficient memory. ```bash vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 ``` => Available memory on node 0 (0.01/0.47 GiB) on startup is less than desired CPU memory utilization (0.9, 0.43 GiB). Decrease --gpu-memory-utilization or reduce CPU memory used by other processes. [vllm_serve_output.txt](https://github.com/user-attachments/files/26901628/vllm_serve_output.txt) **Additional information** ```bash numactl --hardware ``` [numactl_output.txt](https://github.com/user-attachments/files/26901629/numactl_output.txt) I tried without numa by defining `VLLM_NUMA_DISABLED` but it does not work too.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: bug On Raspberry PI 5 (4Go), the following command fails due to insufficient memory. ```bash vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 ``` => Available memory on node 0 (0.01/0.47 GiB) on startup is less than d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m/user-attachments/files/26901628/vllm_serve_output.txt) **Additional information** ```bash numactl --hardware ``` [numactl_output.txt](https://github.com/user-attachments/files/26901629/numactl_output.txt) I tried with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: uild;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: too. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
