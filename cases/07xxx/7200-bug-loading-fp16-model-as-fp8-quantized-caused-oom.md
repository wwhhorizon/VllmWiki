# vllm-project/vllm#7200: [Bug]: loading fp16 model as fp8 quantized caused OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#7200](https://github.com/vllm-project/vllm/issues/7200) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: loading fp16 model as fp8 quantized caused OOM

### Issue 正文摘录

### Your current environment (venv-vllm-54) (base) root@I1ba088648b009018e4:/hy-tmp# nvidia-smi Tue Aug 6 10:29:16 2024 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA A800 80GB PCIe Off | 00000000:6B:00.0 Off | 0 | | N/A 31C P0 42W / 300W | 4MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes found | +--------------------------------------------------------------------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ----------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: loading fp16 model as fp8 quantized caused OOM bug;stale ### Your current environment (venv-vllm-54) (base) root@I1ba088648b009018e4:/hy-tmp# nvidia-smi Tue Aug 6 10:29:16 2024 +----------------------------------...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: loading fp16 model as fp8 quantized caused OOM bug;stale ### Your current environment (venv-vllm-54) (base) root@I1ba088648b009018e4:/hy-tmp# nvidia-smi Tue Aug 6 10:29:16 2024 +----------------------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ironment (venv-vllm-54) (base) root@I1ba088648b009018e4:/hy-tmp# nvidia-smi Tue Aug 6 10:29:16 2024 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.104.05 Drive...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: loading fp16 model as fp8 quantized caused OOM bug;stale ### Your current environment (venv-vllm-54) (base) root@I1ba088648b009018e4:/hy-tmp# nvidia-smi Tue Aug 6 10:29:16 2024 +----------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
