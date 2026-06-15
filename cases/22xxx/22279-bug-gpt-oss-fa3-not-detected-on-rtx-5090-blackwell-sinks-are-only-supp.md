# vllm-project/vllm#22279: [Bug]: gpt-oss -> FA3 not detected on RTX 5090 (Blackwell) – Sinks are only supported in FlashAttention 3

| 字段 | 值 |
| --- | --- |
| Issue | [#22279](https://github.com/vllm-project/vllm/issues/22279) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 97; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss -> FA3 not detected on RTX 5090 (Blackwell) – Sinks are only supported in FlashAttention 3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug docker run --rm --gpus all --ipc=host -p 8000:8000 \ -e VLLM_FLASH_ATTN_VERSION=3 \ -v /var/models/gpt-oss-20b:/model \ vllm/vllm-openai:gptoss \ --model /model \ --served-model-name gpt-oss-20b \ --max-model-len 16384 result: INFO 08-05 14:51:00 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 08-05 14:51:02 [api_server.py:1787] vLLM API server version 0.10.2.dev2+gf5635d62e.d20250805 (APIServer pid=1) INFO 08-05 14:51:02 [utils.py:326] non-default args: {'model': '/model', 'max_model_len': 16384, 'served_model_name': ['gpt-oss-20b']} (APIServer pid=1) INFO 08-05 14:51:05 [config.py:726] Resolved architecture: GptOssForCausalLM (APIServer pid=1) ERROR 08-05 14:51:05 [config.py:123] Error retrieving safetensors: Repo id must use alphanumeric chars or '-', '_', '.', '--' and '..' are forbidden, '-' and '.' cannot start or end the name, max length is 96: '/model'., retrying 1 of 2 (APIServer pid=1) ERROR 08-05 14:51:07 [config.py:121] Error retrieving safetensors: Repo id must use alphanumeric chars or '-', '_', '.', '--' and '..' are forbidden, '-' and '.' cannot start or end the name, max length is 9...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: (APIServer pid=1) INFO 08-05 14:51:07 [config.py:3628] Downcasting torch.float32 to torch.bfloat16. (APIServer pid=1) INFO 08-05 14:51:07 [config.py:1759] Using max model len 16384 (APIServer pid=1) WARNING 08-05 14:51:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Bug]: gpt-oss -> FA3 not detected on RTX 5090 (Blackwell) – Sinks are only supported in FlashAttention 3 bug ### Your current environment ### 🐛 Describe the bug docker run --rm --gpus all --ipc=host -p 8000:8000 \ -e V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Attention 3 bug ### Your current environment ### 🐛 Describe the bug docker run --rm --gpus all --ipc=host -p 8000:8000 \ -e VLLM_FLASH_ATTN_VERSION=3 \ -v /var/models/gpt-oss-20b:/model \ vllm/vllm-openai:gptoss \ --mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: gpt-oss -> FA3 not detected on RTX 5090 (Blackwell) – Sinks are only supported in FlashAttention 3 bug ### Your current environment ### 🐛 Describe the bug docker run --rm --gpus all --ipc=host -p 8000:8000 \ -e V...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gpt-oss -> FA3 not detected on RTX 5090 (Blackwell) – Sinks are only supported in FlashAttention 3 bug ### Your current environment ### 🐛 Describe the bug docker run --rm --gpus all --ipc=host -p 8000:8000 \ -e VL

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
