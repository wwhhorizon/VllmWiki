# vllm-project/vllm#24827: [Bug]: v0.10.2 no longer supports Qwen/Qwen3-Embedding-0.6B

| 字段 | 值 |
| --- | --- |
| Issue | [#24827](https://github.com/vllm-project/vllm/issues/24827) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | install |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.10.2 no longer supports Qwen/Qwen3-Embedding-0.6B

### Issue 正文摘录

### Your current environment v0.10.2 does work for other models Qwen/Qwen3-Embedding-0.6B used to work under v0.10.1.1 docker compose up [+] Running 2/2 ✔ Network vllm-embed_default Created 0.1s ✔ Container vllm-embed-vllm-1 Created 0.0s Attaching to vllm-1 vllm-1 | /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. vllm-1 | import pynvml # type: ignore[import] vllm-1 | INFO 09-14 02:33:54 [__init__.py:216] Automatically detected platform cuda. vllm-1 | WARNING 09-14 02:33:57 [__init__.py:1766] argument 'task' is deprecated vllm-1 | (APIServer pid=1) INFO 09-14 02:33:57 [api_server.py:1896] vLLM API server version 0.10.2 vllm-1 | (APIServer pid=1) INFO 09-14 02:33:57 [utils.py:328] non-default args: {'host': '0.0.0.0', 'port': 8002, 'model': 'Qwen/Qwen3-Embedding-0.6B', 'task': 'embed', 'max_model_len': 8192} vllm-1 | (APIServer pid=1) INFO 09-14 02:34:08 [__init__.py:742] Resolved architecture: Qwen3ForCausalLM vllm-1 | (APIServer pid=1) INFO 09-14 02:34:08...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: for other models Qwen/Qwen3-Embedding-0.6B used to work under v0.10.1.1 docker compose up [+] Running 2/2 ✔ Network vllm-embed_default Created 0.1s ✔ Container vllm-embed-vllm-1 Created
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: v0.10.2 no longer supports Qwen/Qwen3-Embedding-0.6B bug ### Your current environment v0.10.2 does work for other models Qwen/Qwen3-Embedding-0.6B used to work under v0.10.1.1 docker compose up [+] Running 2/2 ✔...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .py:728] Found pooling configuration. vllm-1 | (APIServer pid=1) `torch_dtype` is deprecated! Use `dtype` instead! vllm-1 | (APIServer pid=1) INFO 09-14 02:34:08 [__init__.py:1815] Using max model len 8192 vllm-1 | (API...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: aching to vllm-1 vllm-1 | /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
