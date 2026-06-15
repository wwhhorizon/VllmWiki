# vllm-project/vllm#22931: [Feature]: FP8 e4m3fn->fnuz KV cache conversion

| 字段 | 值 |
| --- | --- |
| Issue | [#22931](https://github.com/vllm-project/vllm/issues/22931) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FP8 e4m3fn->fnuz KV cache conversion

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We would like to be able to use FP8 KV cache quantization while disagg serving across hardwares: NVIDIA-based prefill (e4m3fn) and AMD-based decode (e4m3fnuz). VLLM appears to already support conversion of hardware-specfic FP8 format variants during weight loading through `normalize_e4m3fn_to_e4m3fnuz`, which has two basic components: 1. Replacing -0 values with +0 in the weight itself 2. Multiplying existing scales by 2.0 to account for exponent bias difference I have been investigating how we can add support for the same operation for the KV cache entries, but there are some key differences: - It appears k/v scale values are stored on a per-layer basis, and have a default value created during init. They can also be dynamically calculated per-layer on the first forward pass if the `--calc-kv-scales` option is passed. Finally, they may be loaded during weight loading if specified by the checkpoint. - KV cache entries arrive via a connector, which unified attention waits upon. It seems reasonable to me to modify the attention layer to apply *2.0 multiplier to the k/v scales if and only if the current platform is fnuz, fp8 kv cache type enable...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: FP8 e4m3fn->fnuz KV cache conversion feature request;stale ### 🚀 The feature, motivation and pitch We would like to be able to use FP8 KV cache quantization while disagg serving across hardwares: NVIDIA-based...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: FP8 e4m3fn->fnuz KV cache conversion feature request;stale ### 🚀 The feature, motivation and pitch We would like to be able to use FP8 KV cache quantization while disagg serving across hardwares: NVIDIA-based...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: FP8 e4m3fn->fnuz KV cache conversion feature request;stale ### 🚀 The feature, motivation and pitch We would like to be able to use FP8 KV cache quantization while disagg serving across hardwares: NVIDIA-based...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: FP8 e4m3fn->fnuz KV cache conversion feature request;stale ### 🚀 The feature, motivation and pitch We would like to be able to use FP8 KV cache quantization while disagg serving across hardwares: NVIDIA-based...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
