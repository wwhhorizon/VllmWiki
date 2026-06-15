# vllm-project/vllm#2554: CUDA out of memory error despite having enough memory

| 字段 | 值 |
| --- | --- |
| Issue | [#2554](https://github.com/vllm-project/vllm/issues/2554) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA out of memory error despite having enough memory

### Issue 正文摘录

I am trying to run [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on server with two A100s (a total of 80GB of GPU RAM). ``` $ python -m vllm.entrypoints.openai.api_server \ --model mistralai/Mixtral-8x7B-Instruct-v0.1 \ --tensor-parallel-size 2 ``` vLLM seems to fully utilize the memory of the GPUs and thus a `CUDA out of memory` error is thrown. Here is the output of `nvidia-smi`. ``` +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 545.23.08 Driver Version: 545.23.08 CUDA Version: 12.3 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA A100-PCIE-40GB On | 00000000:65:00.0 Off | 0 | | N/A 25C P0 54W / 250W | 40327MiB / 40960MiB | 0% Default | | | | Disabled | +-----------------------------------------+----------------------+----------------------+ | 1 NVIDIA A100-PCIE-40GB On | 00000000:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 545.23.08 Driver Version: 545.23.08 CUDA Version: 12.3 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: stale I am trying to run [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on server with two A100s (a total of 80GB of GPU RAM). ``` $ python -m vllm.entrypoints.openai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: CUDA out of memory error despite having enough memory stale I am trying to run [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on server with two A100s (a total of 80G
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | 0 N/A N/A 209623
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: CUDA out of memory error despite having enough memory stale I am trying to run [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on server with two A100s (a total of 80G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
