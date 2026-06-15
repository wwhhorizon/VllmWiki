# vllm-project/vllm#34519: [Feature]: Quality of life - expose model name / custom label in GPU process name

| 字段 | 值 |
| --- | --- |
| Issue | [#34519](https://github.com/vllm-project/vllm/issues/34519) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Quality of life - expose model name / custom label in GPU process name

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When running multiple models with vLLM across several GPUs, I rely on `nvidia-smi` (or tools like [nvitop](https://github.com/XuehaiPan/nvitop) ) to monitor GPU allocation and usage. Currently, vLLM processes appear with a generic name such as: ``` VLLM::EngineCore ``` This makes it hard to identify which GPU corresponds to which deployed model when multiple vLLM instances are running at the same time. Example `nvidia-smi` output: ``` $ nvidia-smi Fri Feb 13 15:04:06 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 590.44.01 Driver Version: 590.44.01 CUDA Version: 13.1 | +-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA A100-SXM4-80GB Off | 00000000:07:00.0 Off | 0 | | N/A 39C P0 70W / 400W | 4266MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+-------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 590.44.01 Driver Version: 590.44.01 CUDA Version: 13.1 | +-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: running multiple models with vLLM across several GPUs, I rely on `nvidia-smi` (or tools like [nvitop](https://github.com/XuehaiPan/nvitop) ) to monitor GPU allocation and usage. Currently, vLLM processes appear with a g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Quality of life - expose model name / custom label in GPU process name feature request ### 🚀 The feature, motivation and pitch When running multiple models with vLLM across several GPUs, I rely on `nvidia-smi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: y of life - expose model name / custom label in GPU process name feature request ### 🚀 The feature, motivation and pitch When running multiple models with vLLM across several GPUs, I rely on `nvidia-smi` (or tools like...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | 0 N/A N/A

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
