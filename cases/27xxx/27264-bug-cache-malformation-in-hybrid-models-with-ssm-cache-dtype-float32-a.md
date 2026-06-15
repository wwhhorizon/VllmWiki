# vllm-project/vllm#27264: [Bug]: Cache malformation in hybrid models with SSM cache dtype float32 and block allocation wrap around

| 字段 | 值 |
| --- | --- |
| Issue | [#27264](https://github.com/vllm-project/vllm/issues/27264) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Cache malformation in hybrid models with SSM cache dtype float32 and block allocation wrap around

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hey, We're running a hybrid model, and are running into an issue when turning prefix caching on. After a few requests where processed, the model starts returning 0s. After some debugging, we've found that the issue starts happening in the first full attention layer in the model, which comes after some Mamba2 layers, where at some point the attention output started including NaNs, which quickly spread and turned the entire hidden states into NaNs. Looking deeper, we saw that the block tables that were input into the attention computation were wrapping around the cache buffer when the issue started occurring. The prompt in the script below lead to an increase of 5 in the attention layer's single allocated page (5, 10, 15, ...), until it reached the end of the buffer, and then it started again at (2, 7, 12, ...). The issue started the moment the block table included page 2, and happened consistently after that. Further debugging revealed that this happens only when setting `mamba_ssm_cache_dtype="float32"` in the model initialization. We've found that the issue only occurs in main after #25103, which doesn't concern the KV cache dir...

## 现有链接修复摘要

#25752 [V1] [Hybrid] Mamba2 Automatic Prefix Caching

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ay, and doesn't happen before. We didn't manage to get the issue reproducing inside any of the currently running hybrid model tests at this time, unfortunately. We are looking into the areas of the code which write to t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Cache malformation in hybrid models with SSM cache dtype float32 and block allocation wrap around bug ### Your current environment ### 🐛 Describe the bug Hey, We're running a hybrid model, and are running into an...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Cache malformation in hybrid models with SSM cache dtype float32 and block allocation wrap around bug ### Your current environment ### 🐛 Describe the bug Hey, We're running a hybrid model, and are running into an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Cache malformation in hybrid models with SSM cache dtype float32 and block allocation wrap around bug ### Your current environment ### 🐛 Describe the bug Hey, We're running a hybrid model, and are running into an...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Cache malformation in hybrid models with SSM cache dtype float32 and block allocation wrap around bug ### Your current environment ### 🐛 Describe the bug Hey, We're running a hybrid model, and are running into an...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25752](https://github.com/vllm-project/vllm/pull/25752) | mentioned | 0.45 | [V1] [Hybrid] Mamba2 Automatic Prefix Caching | med that this issue also happens all the way back to the original pr (#25752) that introduced apc for mamba2 caches, when the kv cache spec keys are sorted in the same way, and do… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
