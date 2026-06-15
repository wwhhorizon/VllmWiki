# vllm-project/vllm#40821: [Bug]: Deepseek V4 failed to load on RTX PRO 6000

| 字段 | 值 |
| --- | --- |
| Issue | [#40821](https://github.com/vllm-project/vllm/issues/40821) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek V4 failed to load on RTX PRO 6000

### Issue 正文摘录

### Your current environment **Environment** - vLLM version: Nightly - deepseekv4-cu130 - Model: deepseek-ai/DeepSeek-V4-Flash - GPUs: 8× NVIDIA RTX PRO 6000 (Blackwell) - CUDA: 13.0 (image: vllm/vllm-openai:deepseekv4-cu130) - Python: 3.12 - PyTorch: (bundled with image) - OS: Ubuntu 24 (container) ### 🐛 Describe the bug AssertionError: auto_functionalized was not removed when serving DeepSeek-V4-Flash with DP=8 on RTX PRO 6000 ## **Reproduce** ``` services: custom_serving_0: command: --model deepseek-ai/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --data-parallel-size 8 --reasoning-parser deepseek_v4 --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' container_name: custom_openai_serving_0 deploy: resources: reservations: devices: - capabilities: - gpu device_ids: - '0' - '1' - '2' - '3' - '4' - '5' - '6' - '7' driver: nvidia environment: - HF_TOKEN=<> - VLLM_ENGINE_READY_TIMEOUT_S=3600 image: vllm/vllm-openai:deepseekv4-cu130 shm_size: 10g volumes: - /mnt/models:/root/.cache/huggingface:rw ``` ## **What happens** All 8 DP workers crash during profile_run() / _dummy_run() at startup with th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: PRO 6000 bug;DSv4 ### Your current environment **Environment** - vLLM version: Nightly - deepseekv4-cu130 - Model: deepseek-ai/DeepSeek-V4-Flash - GPUs: 8× NVIDIA RTX PRO 6000 (Blackwell) - CUDA: 13.0 (image: vllm/vllm-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Deepseek V4 failed to load on RTX PRO 6000 bug;DSv4 ### Your current environment **Environment** - vLLM version: Nightly - deepseekv4-cu130 - Model: deepseek-ai/DeepSeek-V4-Flash - GPUs: 8× NVIDIA RTX PRO 6000 (B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vironment **Environment** - vLLM version: Nightly - deepseekv4-cu130 - Model: deepseek-ai/DeepSeek-V4-Flash - GPUs: 8× NVIDIA RTX PRO 6000 (Blackwell) - CUDA: 13.0 (image: vllm/vllm-openai:deepseekv4-cu130) - Python: 3....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nd: --model deepseek-ai/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --data-parallel-size 8 --reasoning-parser deepseek_v4 --compilation-config '{"cudagraph_mode":...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ek-ai/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --data-parallel-size 8 --reasoning-parser deepseek_v4 --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWIS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
