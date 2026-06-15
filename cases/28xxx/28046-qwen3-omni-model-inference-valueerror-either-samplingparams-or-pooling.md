# vllm-project/vllm#28046: Qwen3-Omni model inference : ValueError: Either SamplingParams or PoolingParams must be provided.

| 字段 | 值 |
| --- | --- |
| Issue | [#28046](https://github.com/vllm-project/vllm/issues/28046) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen3-Omni model inference : ValueError: Either SamplingParams or PoolingParams must be provided.

### Issue 正文摘录

### Your current environment ```text The output of `python web_demo.py` ``` The above mentioned method provides the error below ``` qwen/Qwen3-Omni/collect_env.py", line 287, in get_vllm_version from vllm import __version__, __version_tuple__ ImportError: cannot import name '__version__' from 'vllm' (unknown location) ``` while the envs installed are below: ``` pip list Package Version Editable project location --------------------------------- --------------------------------- ---------------------------------------------------------- accelerate 1.11.0 aiofiles 24.1.0 aiohappyeyeballs 2.6.1 aiohttp 3.13.2 aiosignal 1.4.0 airportsdata 20250909 annotated-doc 0.0.3 annotated-types 0.7.0 anyio 4.11.0 astor 0.8.1 async-timeout 5.0.1 attrs 25.4.0 audioread 3.1.0 av 16.0.1 blake3 1.0.8 Brotli 1.1.0 cachetools 6.2.1 certifi 2025.10.5 cffi 2.0.0 charset-normalizer 3.4.4 click 8.2.1 cloudpickle 3.1.2 cmake 4.1.2 compressed-tensors 0.10.2 cupy-cuda12x 13.6.0 decorator 5.2.1 depyf 0.18.0 dill 0.4.0 diskcache 5.6.3 distro 1.9.0 dnspython 2.8.0 einops 0.8.1 email-validator 2.3.0 exceptiongroup 1.3.0 fastapi 0.121.0 fastapi-cli 0.0.14 fastapi-cloud-cli 0.3.1 fastrlock 0.8.3 ffmpy 0.6.4 filelock...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: error below ``` qwen/Qwen3-Omni/collect_env.py", line 287, in get_vllm_version from vllm import __version__, __version_tuple__ ImportError: cannot import name '__version__' from 'vllm' (unknown location) ``` while the e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Qwen3-Omni model inference : ValueError: Either SamplingParams or PoolingParams must be provided. usage ### Your current environment ```text The output of `python web_demo.py` ``` The above mentioned method provides th
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4.1.2 compressed-tensors 0.10.2 cupy-cuda12x 13.6.0 decorator 5.2.1 depyf 0.18.0 dill 0.4.0 diskcache 5.6.3 distro
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 4.67.1 transformers 4.57.0 triton 3.3.0 typer 0.20.0 typer-slim 0.20.0 typing_extensions 4.15.0 typing-inspection 0.4.2 tzdata
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 0.37.0 regex 2025.11.3 requests 2.32.5 rich 14.2.0 rich-toolkit 0.15.1 rignore 0.7.4 rpds-py 0.28.0 ruff

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
