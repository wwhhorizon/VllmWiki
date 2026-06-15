# vllm-project/vllm#36443: [Bug]: qwen3.5-27b ValueError: Tokenizer class TokenizersBackendFast does not exist or is not currently imported.

| 字段 | 值 |
| --- | --- |
| Issue | [#36443](https://github.com/vllm-project/vllm/issues/36443) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3.5-27b ValueError: Tokenizer class TokenizersBackendFast does not exist or is not currently imported.

### Issue 正文摘录

### Your current environment An error occurred when deploying qwen3-5-27b-gptq-int8 on vllm 0.17.0 Traceback (most recent call last): File "/ssd4/workspace/1_test/webserver_new2.py", line 1136, in infer = QwenInfer(args) ^^^^^^^^^^^^^^^ File "/ssd4/workspace/1_test/qwen_infer_vllm.py", line 38, in __init__ self.tokenizer = AutoTokenizer.from_pretrained(args.model_path, \ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/ssd4/.conda/envs/vllm0170_py312/lib/python3.12/site-packages/transformers/models/auto/tokenization_auto.py", line 1153, in from_pretrained raise ValueError( ValueError: Tokenizer class TokenizersBackendFast does not exist or is not currently imported. addict 2.4.0 aiofiles 23.2.1 aiohappyeyeballs 2.6.1 aiohttp 3.13.3 aiosignal 1.4.0 annotated-doc 0.0.4 annotated-types 0.7.0 anthropic 0.84.0 anyio 4.9.0 apache-tvm-ffi 0.1.9 astor 0.8.1 async-timeout 3.0.1 attrs 25.4.0 babel 2.17.0 baidubce 0.8.3 bce-python-sdk 0.9.42 black 22.8.0 blake3 1.0.8 Brotli 1.1.0 cachetools 7.0.4 cbor2 5.8.0 certifi 2025.7.9 cffi 2.0.0 chardet 3.0.4 charset-normalizer 3.4.5 click 8.3.1 cloudpickle 3.1.2 colorlog 6.9.0 compressed-tensors 0.13.0 cryptography 46.0.5 cuda-bindings 12.9.4...

## 现有链接修复摘要

#36448 fix(tokenizer): handle TokenizersBackendFast class for Qwen3.5 GPTQ models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Tokenizer class TokenizersBackendFast does not exist or is not currently imported. bug ### Your current environment An error occurred when deploying qwen3-5-27b-gptq-int8 on vllm 0.17.0 Traceback (most recent call last)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: qwen3.5-27b ValueError: Tokenizer class TokenizersBackendFast does not exist or is not currently imported. bug ### Your current environment An error occurred when deploying qwen3-5-27b-gptq-int8 on vllm 0.17.0 Tr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: qwen3.5-27b ValueError: Tokenizer class TokenizersBackendFast does not exist or is not currently imported. bug ### Your current environment An error occurred when deploying qwen3-5-27b-gptq-int8 on vllm 0.17.0 Tr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ent ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization cuda;kernel;quantization;triton build_error;crash dtype;env_dependency #36448 fix(tokenizer): handle TokenizersBackendFast class for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.13.0 cryptography 46.0.5 cuda-bindings 12.9.4 cuda-pathfinder 1.4.1 cuda-python 12.9.4 cupy-cuda12x 14.0.1 datasets

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36448](https://github.com/vllm-project/vllm/pull/36448) | closes_keyword | 0.95 | fix(tokenizer): handle TokenizersBackendFast class for Qwen3.5 GPTQ models | Fixes #36443 When loading models whose `tokenizer_config.json` references the `TokenizersBackendFast` class (e.g. Qwen3.5-27B GPTQ), `AutoTokenizer.from_pretrained()` raises: ``` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
