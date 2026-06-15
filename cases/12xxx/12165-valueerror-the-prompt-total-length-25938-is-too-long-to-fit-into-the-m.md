# vllm-project/vllm#12165: ValueError: The prompt (total length 25938) is too long to fit into the model (context length 4096). Make sure that `max_model_len` is no smaller than the number of text tokens plus multimodal tokens.

| 字段 | 值 |
| --- | --- |
| Issue | [#12165](https://github.com/vllm-project/vllm/issues/12165) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ValueError: The prompt (total length 25938) is too long to fit into the model (context length 4096). Make sure that `max_model_len` is no smaller than the number of text tokens plus multimodal tokens.

### Issue 正文摘录

### Your current environment # Name Version Build Channel _libgcc_mutex 0.1 main defaults _openmp_mutex 5.1 1_gnu defaults accelerate 1.0.1 pypi_0 pypi aiofiles 23.2.1 pypi_0 pypi aiohappyeyeballs 2.4.4 pypi_0 pypi aiohttp 3.11.11 pypi_0 pypi aiohttp-cors 0.7.0 pypi_0 pypi aiosignal 1.3.2 pypi_0 pypi airportsdata 20241001 pypi_0 pypi annotated-types 0.7.0 pypi_0 pypi anyio 4.8.0 pypi_0 pypi astor 0.8.1 pypi_0 pypi attrs 24.3.0 pypi_0 pypi av 14.0.1 pypi_0 pypi blake3 1.0.2 pypi_0 pypi bzip2 1.0.8 h5eee18b_6 defaults ca-certificates 2024.12.31 h06a4308_0 defaults cachetools 5.5.0 pypi_0 pypi certifi 2024.12.14 pypi_0 pypi charset-normalizer 3.4.1 pypi_0 pypi click 8.1.8 pypi_0 pypi cloudpickle 3.1.1 pypi_0 pypi colorful 0.5.6 pypi_0 pypi compressed-tensors 0.8.1 pypi_0 pypi contourpy 1.3.1 pypi_0 pypi cycler 0.12.1 pypi_0 pypi datasets 3.1.0 pypi_0 pypi depyf 0.18.0 pypi_0 pypi dill 0.3.8 pypi_0 pypi diskcache 5.6.3 pypi_0 pypi distlib 0.3.9 pypi_0 pypi distro 1.9.0 pypi_0 pypi docstring-parser 0.16 pypi_0 pypi einops 0.8.0 pypi_0 pypi fastapi 0.115.6 pypi_0 pypi ffmpy 0.5.0 pypi_0 pypi filelock 3.16.1 pypi_0 pypi fire 0.7.0 pypi_0 pypi fonttools 4.55.3 pypi_0 pypi frozenlist 1.5.0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: ValueError: The prompt (total length 25938) is too long to fit into the model (context length 4096). Make sure that `max_model_len` is no smaller than the number of text tokens plus multimodal tokens. bug ### Your curre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: odal tokens. bug ### Your current environment # Name Version Build Channel _libgcc_mutex 0.1 main defaults _openmp_mutex 5.1 1_gnu defaults accelerate 1.0.1
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: to the model (context length 4096). Make sure that `max_model_len` is no smaller than the number of text tokens plus multimodal tokens. bug ### Your current environment # Name Version Build Channel _libgcc_mutex 0.1 mai
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pypi transformers 4.46.1 pypi_0 pypi triton 3.1.0 pypi_0 pypi trl 0.9.6 pypi_0 pypi typer 0.15.1 pypi_0 pypi typing-extensions
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a 3.10 pypi_0 pypi importlib-metadata 8.5.0 pypi_0 pypi importlib-resources 6.5.2 pypi_0 pypi iniconfig 2.0.0 pypi_0 pypi interegular 0.3.3

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
