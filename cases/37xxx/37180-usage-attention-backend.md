# vllm-project/vllm#37180: [Usage]: Attention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#37180](https://github.com/vllm-project/vllm/issues/37180) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Attention backend

### Issue 正文摘录

### Your current environment ```text My current environment: - Linux ARM64 - Nvidia GH200 - Python3.11.5 ``` ### How would you like to use vllm Hello 👋 I am doing offline inference with `Qwen/Qwen3.5-35B-A3B` model. In logs it is stated that: ```bash (Worker pid=3068197) (Worker_TP0 pid=3068197) INFO 03-16 11:27:40 [cuda.py:405] Using FLASH_ATTN attention backend out of potential backends: ['FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION']. (Worker pid=3068197) (Worker_TP0 pid=3068197) INFO 03-16 11:27:40 [flash_attn.py:587] Using FlashAttention version 3 ``` However, I did not install specific `flash-attn` version. Is it possible that `vllm` is doing under-the-hood some kind of implementation or is it a bug? Below my full `.venv`: ```bash Package Version ---------------------------------------- ------------- aiohappyeyeballs 2.6.1 aiohttp 3.13.3 aiosignal 1.4.0 annotated-doc 0.0.4 annotated-types 0.7.0 anthropic 0.84.0 anyio 4.12.1 apache-tvm-ffi 0.1.9 astor 0.8.1 attrs 25.4.0 blake3 1.0.8 cachetools 7.0.5 cbor2 5.8.0 certifi 2026.2.25 cffi 2.0.0 charset-normalizer 3.4.6 click 8.3.1 cloudpickle 3.1.2 compressed-tensors 0.13.0 cryptography 46.0.5 cuda-bindings 12.9.4 cu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: id=3068197) INFO 03-16 11:27:40 [flash_attn.py:587] Using FlashAttention version 3 ``` However, I did not install specific `flash-attn` version. Is it possible that `vllm` is doing under-the-hood some kind of implementa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Usage]: Attention backend usage ### Your current environment ```text My current environment: - Linux ARM64 - Nvidia GH200 - Python3.11.5 ``` ### How would you like to use vllm Hello 👋 I am doing offline inference with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: would you like to use vllm Hello 👋 I am doing offline inference with `Qwen/Qwen3.5-35B-A3B` model. In logs it is stated that: ```bash (Worker pid=3068197) (Worker_TP0 pid=3068197) INFO 03-16 11:27:40 [cuda.py:405] Using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `bash (Worker pid=3068197) (Worker_TP0 pid=3068197) INFO 03-16 11:27:40 [cuda.py:405] Using FLASH_ATTN attention backend out of potential backends: ['FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION']. (Worker...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 3.11 ijson 3.5.0 importlib-metadata 8.7.1 interegular 0.3.3 jinja2 3.1.6 jiter 0.13.0 jmespath

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
