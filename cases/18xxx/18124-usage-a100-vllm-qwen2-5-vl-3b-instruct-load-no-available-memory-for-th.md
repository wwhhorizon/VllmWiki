# vllm-project/vllm#18124: [Usage]: A100 vllm部署Qwen2.5-VL-3B-Instruct，load模型之后报错No available memory for the cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#18124](https://github.com/vllm-project/vllm/issues/18124) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: A100 vllm部署Qwen2.5-VL-3B-Instruct，load模型之后报错No available memory for the cache blocks

### Issue 正文摘录

### Your current environment 命令：vllm serve Qwen/Qwen2.5-VL-3B-Instruct --gpu-memory-utilization 0.3，80G的显卡--gpu-memory-utilization 0.3是24G 环境： aiohappyeyeballs 2.6.1 aiohttp 3.11.18 aiosignal 1.3.2 airportsdata 20250224 annotated-types 0.7.0 anyio 4.9.0 astor 0.8.1 async-timeout 5.0.1 attrs 25.3.0 blake3 1.0.4 cachetools 5.5.2 certifi 2025.4.26 charset-normalizer 3.4.2 click 8.2.0 cloudpickle 3.1.1 compressed-tensors 0.9.2 cupy-cuda12x 13.4.1 depyf 0.18.0 dill 0.4.0 diskcache 5.6.3 distro 1.9.0 dnspython 2.7.0 einops 0.8.1 email_validator 2.2.0 exceptiongroup 1.3.0 fastapi 0.115.12 fastapi-cli 0.0.7 fastrlock 0.8.3 filelock 3.18.0 frozenlist 1.6.0 fsspec 2024.6.1 gguf 0.10.0 h11 0.16.0 httpcore 1.0.9 httptools 0.6.4 httpx 0.28.1 huggingface-hub 0.31.2 idna 3.10 importlib_metadata 8.7.0 interegular 0.3.3 Jinja2 3.1.6 jiter 0.9.0 jsonschema 4.23.0 jsonschema-specifications 2025.4.1 lark 1.2.2 llguidance 0.7.19 llvmlite 0.43.0 lm-format-enforcer 0.10.11 markdown-it-py 3.0.0 MarkupSafe 2.1.5 mdurl 0.1.2 mistral_common 1.5.4 mpmath 1.3.0 msgpack 1.1.0 msgspec 0.19.0 multidict 6.4.3 nest-asyncio 1.6.0 networkx 3.3 ninja 1.11.1.4 numba 0.60.0 numpy 1.26.4 nvidia-cublas-cu11 11.11.3.6 nvi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: core 1.0.9 httptools 0.6.4 httpx 0.28.1 huggingface-hub 0.31.2 idna 3.10 importlib_metadata 8.7.0 interegular 0.3.3 Jinja2 3.1.6 jiter 0.9.0 jsonschema 4.23.0 jsonschema-specifications 2025.4.1 lark 1.2.2 llguidance 0.7...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: A100 vllm部署Qwen2.5-VL-3B-Instruct，load模型之后报错No available memory for the cache blocks usage ### Your current environment 命令：vllm serve Qwen/Qwen2.5-VL-3B-Instruct --gpu-memory-utilization 0.3，80G的显卡--gpu-memory-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: A100 vllm部署Qwen2.5-VL-3B-Instruct，load模型之后报错No available memory for the cache blocks usage ### Your current environment 命令：vllm serve Qwen/Qwen2.5-VL-3B-Instruct --gpu-memory-utilization 0.3，80G的显卡--gpu-memory-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: vllm部署Qwen2.5-VL-3B-Instruct，load模型之后报错No available memory for the cache blocks usage ### Your current environment 命令：vllm serve Qwen/Qwen2.5-VL-3B-Instruct --gpu-memory-utilization 0.3，80G的显卡--gpu-memory-utilization 0....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio 2.6.0+cu118 torchvision 0.21.0+cu118 tqdm 4.67.1 transformers 4.51.3 triton 3.2.0 typer 0.15.3 typing_extensions 4.12.2 typing-inspection 0.4.0 urllib3 2.4.0 uvicorn 0.34.2 uvloop 0.21.0 vllm 0.8.2+cu118 watchfiles...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
