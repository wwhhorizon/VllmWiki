# vllm-project/vllm#41125: [Bug]: DeepSeek V4 hangs when input length exceeds 64k tokens (vLLM deepseekv4-cu129 image)

| 字段 | 值 |
| --- | --- |
| Issue | [#41125](https://github.com/vllm-project/vllm/issues/41125) |
| 状态 | closed |
| 标签 | bug;DSv4 |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | build_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 hangs when input length exceeds 64k tokens (vLLM deepseekv4-cu129 image)

### Issue 正文摘录

### Your current environment ## Environment - Model: `deepseek-ai/DeepSeek-V4-Flash` - Docker Image: `vllm/vllm-openai:deepseekv4-cu129` - Deployment Mode: multi-node / multi-GPU (data parallel = 4, expert parallel enabled) - GPU: H800 - CUDA: 12.9 (from image) --- ## Deployment Command ```bash server vllm serve deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 4 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --speculative_config '{"method":"mtp","num_speculative_tokens":1}' \ --reasoning-parser deepseek_v4 ``` client command ```sh vllm bench serve \ --random-input-len 64000 \ --random-output-len 10 ``` ## Issue Description - When input length is around 32k tokens, the service works normally and returns responses. - When input length increases to 64k tokens or above, the service hangs and does not return any response. - No explicit error is observed; the request appears to be stuck indefinitely. ### 🐛 Describe the bug When input length is around 32k tokens,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t environment ## Environment - Model: `deepseek-ai/DeepSeek-V4-Flash` - Docker Image: `vllm/vllm-openai:deepseekv4-cu129` - Deployment Mode: multi-node / multi-GPU (data parallel = 4, expert parallel enabled) - GPU: H80...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rve deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 4 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "cust...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: / multi-GPU (data parallel = 4, expert parallel enabled) - GPU: H800 - CUDA: 12.9 (from image) --- ## Deployment Command ```bash server vllm serve deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 4 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: kv4-cu129 image) bug;DSv4 ### Your current environment ## Environment - Model: `deepseek-ai/DeepSeek-V4-Flash` - Docker Image: `vllm/vllm-openai:deepseekv4-cu129` - Deployment Mode: multi-node / multi-GPU (data parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
