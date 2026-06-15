# vllm-project/vllm#41519: [Bug]: Xiaomi MiMo v2.5 broken on SM12x

| 字段 | 值 |
| --- | --- |
| Issue | [#41519](https://github.com/vllm-project/vllm/issues/41519) |
| 状态 | open |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Xiaomi MiMo v2.5 broken on SM12x

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launching Xiaomi MiMo v2.5 Flash on 4x RTX 6000 Pro Blackwell in fp8 precision or on 2x DGX Sparks nvfp4 precision with the following command: ```bash vllm serve XiaomiMiMo/MiMo-V2.5 --host 0.0.0.0 --port 8000 --tensor-parallel-size 4 --gpu-memory-utilization 0.80 --trust-remote-code --tool-call-parser qwen3_xml --reasoning-parser qwen3 --enable-expert-parallel --served-model-name XiaomiMiMo/MiMo-V2-Flash --attention-backend FLASH_ATTN --attention-config.flash_attn_version=3 ``` spits out the error: `AssertionError: Sinks are only supported in FlashAttention 3` [full error trace.txt](https://github.com/user-attachments/files/27309124/full.error.trace.txt) It looks like this might be the case because during the model load, the model seems to fallback to `FlashAttentionDiffKVBackend`, which possibly doesn't get overridden by the explicit flag to use flash attention v3. See [`vllm/model_executor/models/mimo_v2.py` at line 296-302](https://github.com/vllm-project/vllm/blob/0a9362d6ab88eed6fe7b52ed8424794cd492f888/vllm/model_executor/models/mimo_v2.py#L296-L302). The model seems to override whatever attention version I am utilizing at...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: allel --served-model-name XiaomiMiMo/MiMo-V2-Flash --attention-backend FLASH_ATTN --attention-config.flash_attn_version=3 ``` spits out the error: `AssertionError: Sinks are only supported in FlashAttention 3` [full err...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: he bug Launching Xiaomi MiMo v2.5 Flash on 4x RTX 6000 Pro Blackwell in fp8 precision or on 2x DGX Sparks nvfp4 precision with the following command: ```bash vllm serve XiaomiMiMo/MiMo-V2.5 --host 0.0.0.0 --port 8000 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Xiaomi MiMo v2.5 broken on SM12x bug ### Your current environment ### 🐛 Describe the bug Launching Xiaomi MiMo v2.5 Flash on 4x RTX 6000 Pro Blackwell in fp8 precision or on 2x DGX Sparks nvfp4 precision with the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Launching Xiaomi MiMo v2.5 Flash on 4x RTX 6000 Pro Blackwell in fp8 precision or on 2x DGX Sparks nvfp4 precision with the following command: ```bash vllm serve XiaomiMiMo/MiMo-V2.5 --host 0.0.0.0 --port 8000 --tensor-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: memory-utilization 0.80 --trust-remote-code --tool-call-parser qwen3_xml --reasoning-parser qwen3 --enable-expert-parallel --served-model-name XiaomiMiMo/MiMo-V2-Flash --attention-backend FLASH_ATTN --attention-config.f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
