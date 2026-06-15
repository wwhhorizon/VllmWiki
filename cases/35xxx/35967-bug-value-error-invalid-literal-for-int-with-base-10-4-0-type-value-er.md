# vllm-project/vllm#35967: [Bug]: Value error, invalid literal for int() with base 10: '4.0' [type=value_error, input_value=ArgsKwargs((), {'model_co...transfer_config': None}), input_type=ArgsKwargs]

| 字段 | 值 |
| --- | --- |
| Issue | [#35967](https://github.com/vllm-project/vllm/issues/35967) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Value error, invalid literal for int() with base 10: '4.0' [type=value_error, input_value=ArgsKwargs((), {'model_co...transfer_config': None}), input_type=ArgsKwargs]

### Issue 正文摘录

### Your current environment I'm using a Mac laptop with the M4 Apple Silicon chip, and I encountered an error when running it. My environment dependencies are as follows. (vllm-run) wendell@Wendell-Mac Qwen3.5-2B % pip list Package Version Build ---------------------------------------- --------------------------- ----- accelerate 1.12.0 aiohappyeyeballs 2.6.1 aiohttp 3.13.3 aiosignal 1.4.0 annotated-doc 0.0.4 annotated-types 0.7.0 anthropic 0.84.0 anyio 4.12.1 astor 0.8.1 attrs 25.4.0 blake3 1.0.8 cachetools 7.0.2 cbor2 5.8.0 certifi 2026.2.25 cffi 2.0.0 charset-normalizer 3.4.4 click 8.3.1 cloudpickle 3.1.2 compressed-tensors 0.13.0 cryptography 46.0.5 depyf 0.20.0 dill 0.4.1 diskcache 5.6.3 distro 1.9.0 dnspython 2.8.0 docstring_parser 0.17.0 einops 0.8.2 email-validator 2.3.0 fastapi 0.135.1 fastapi-cli 0.0.24 fastapi-cloud-cli 0.14.0 fastar 0.8.0 filelock 3.25.0 frozenlist 1.8.0 fsspec 2026.2.0 gguf 0.18.0 googleapis-common-protos 1.72.0 grpcio 1.78.0 grpcio-reflection 1.78.0 h11 0.16.0 hf-xet 1.3.2 httpcore 1.0.9 httptools 0.7.1 httpx 0.28.1 httpx-sse 0.4.3 huggingface_hub 0.36.2 idna 3.11 ijson 3.5.0 importlib_metadata 8.7.1 interegular 0.3.3 Jinja2 3.1.6 jiter 0.13.0 jmesp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: chip, and I encountered an error when running it. My environment dependencies are as follows. (vllm-run) wendell@Wendell-Mac Qwen3.5-2B % pip list Package Version Build ---------------------------------------- ---------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: nt() with base 10: '4.0' [type=value_error, input_value=ArgsKwargs((), {'model_co...transfer_config': None}), input_type=ArgsKwargs] bug ### Your current environment I'm using a Mac laptop with the M4 Apple Silicon chip...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: r current environment I'm using a Mac laptop with the M4 Apple Silicon chip, and I encountered an error when running it. My environment dependencies are as follows. (vllm-run) wendell@Wendell-Mac Qwen3.5-2B % pip list P...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 3.11 ijson 3.5.0 importlib_metadata 8.7.1 interegular 0.3.3 Jinja2 3.1.6 jiter 0.13.0 jmespath
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 0.37.0 regex 2026.2.28 requests 2.32.5 rich 14.3.3 rich-toolkit 0.19.7 rignore 0.7.6 rpds-py

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
