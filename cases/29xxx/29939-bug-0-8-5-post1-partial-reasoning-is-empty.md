# vllm-project/vllm#29939: [Bug]: 0.8.5.post1 Partial reasoning is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#29939](https://github.com/vllm-project/vllm/issues/29939) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.8.5.post1 Partial reasoning is empty

### Issue 正文摘录

### Your current environment I am using Verl0.6.0 for reinforcement learning, and the inference engine is VLLM0.8.5.Post1 absl-py 2.3.1 accelerate 1.11.0 addict 2.4.0 aiofiles 25.1.0 aiohappyeyeballs 2.6.1 aiohttp 3.13.2 aiohttp-cors 0.8.1 aiosignal 1.4.0 airportsdata 20250909 annotated-doc 0.0.3 annotated-types 0.7.0 antlr4-python3-runtime 4.9.3 anyio 4.11.0 astor 0.8.1 async-timeout 5.0.1 attrs 25.4.0 av 16.0.1 bitsandbytes 0.45.0 blake3 1.0.8 boto3 1.40.64 botocore 1.40.64 cachetools 6.2.1 certifi 2025.10.5 cfgv 3.4.0 charset-normalizer 3.4.4 click 8.2.1 cloudpickle 3.1.1 codetiming 1.4.0 colorful 0.5.8 compressed-tensors 0.9.3 contourpy 1.3.2 cupy-cuda12x 13.6.0 cycler 0.12.1 datasets 4.3.0 Deprecated 1.3.1 depyf 0.18.0 dill 0.4.0 diskcache 5.6.3 distlib 0.4.0 distro 1.9.0 dnspython 2.8.0 einops 0.8.1 email-validator 2.3.0 et_xmlfile 2.0.0 exceptiongroup 1.3.0 fastapi 0.120.4 fastapi-cli 0.0.14 fastapi-cloud-cli 0.3.1 fastrlock 0.8.3 filelock 3.20.0 flash_attn 2.7.4.post1 flashinfer-python 0.2.2.post1+cu124torch2.6 fonttools 4.60.1 frozenlist 1.8.0 fsspec 2025.9.0 gguf 0.17.1 gitdb 4.0.12 GitPython 3.1.45 google-api-core 2.28.1 google-auth 2.42.1 googleapis-common-protos 1.71....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: 1.76.0 h11 0.16.0 hf_transfer 0.1.9 hf-xet 1.2.0 httpcore 1.0.9 httptools 0.7.1 httpx
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 2.42.1 googleapis-common-protos 1.71.0 grpcio 1.76.0 h11 0.16.0 hf_transfer 0.1.9 hf-xet 1.2.0 httpcore
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0.9.3 contourpy 1.3.2 cupy-cuda12x 13.6.0 cycler 0.12.1 datasets 4.3.0 Deprecated 1.3.1 depyf
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: 0.8.5.post1 Partial reasoning is empty bug;stale ### Your current environment I am using Verl0.6.0 for reinforcement learning, and the inference engine is VLLM0.8.5.Post1 absl-py 2.3.1 accelerate 1.1
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 3.20.0 flash_attn 2.7.4.post1 flashinfer-python 0.2.2.post1+cu124torch2.6 fonttools 4.60.1 frozenlist 1.8.0 fsspec 2025.9.0 gguf

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
