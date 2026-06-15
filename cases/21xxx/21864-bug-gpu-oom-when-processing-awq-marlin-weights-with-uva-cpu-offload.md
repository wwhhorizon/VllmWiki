# vllm-project/vllm#21864: [Bug]: GPU OOM when processing AWQ Marlin weights with UVA CPU Offload

| 字段 | 值 |
| --- | --- |
| Issue | [#21864](https://github.com/vllm-project/vllm/issues/21864) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU OOM when processing AWQ Marlin weights with UVA CPU Offload

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## CPU Offloading When using CPU Offloading in V1, UVA (Pin Memory) is required. https://github.com/vllm-project/vllm/blob/9025a9a7050253678431b2c20e6dd0be55f0dcc2/vllm/model_executor/models/utils.py#L579-L600 This makes the tensors to be virtually allocated on the GPU. i.e. `p.device.type == 'cuda'`, but physically on the CPU. ## Quant Processing Some quant methods requires processing after loading the weights. https://github.com/vllm-project/vllm/blob/86ae693f207fc9433f0b6d2c4331ef021dad50fe/vllm/model_executor/model_loader/utils.py#L96-L112 In AWQ, the Tensors are repacked. https://github.com/vllm-project/vllm/blob/e0e58f9729e739d857a5ed0d11fc80ea9aa21087/vllm/_custom_ops.py#L1029-L1040 However, because the loaded tensors are virtually allocated on the GPU, the repacked tensors will be physically allocated on GPU. Later, when the repacking is done and the repacked tensors should be moving back to the CPU, it isn't actually moved back because the loaded tensor was never in the CPU from VLLM's perspective. This causes the GPU's memory to fill up with the repacked tensors and causes OOM. https://github.com/vllm-project/vllm/blob/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: GPU OOM when processing AWQ Marlin weights with UVA CPU Offload bug;stale ### Your current environment ### 🐛 Describe the bug ## CPU Offloading When using CPU Offloading in V1, UVA (Pin Memory) is required. https:/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: the GPU. i.e. `p.device.type == 'cuda'`, but physically on the CPU. ## Quant Processing Some quant methods requires processing after loading the weights. https://github.com/vllm-project/vllm/blob/86ae693f207fc9433f0b6d2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he tensors to be virtually allocated on the GPU. i.e. `p.device.type == 'cuda'`, but physically on the CPU. ## Quant Processing Some quant methods requires processing after loading the weights. https://github.com/vllm-p...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: GPU OOM when processing AWQ Marlin weights with UVA CPU Offload bug;stale ### Your current environment ### 🐛 Describe the bug ## CPU Offloading When using CPU Offloading in V1, UVA (Pin Memory) is required. http

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
