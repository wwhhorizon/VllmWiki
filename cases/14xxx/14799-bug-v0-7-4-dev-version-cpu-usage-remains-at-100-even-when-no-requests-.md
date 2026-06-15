# vllm-project/vllm#14799: [Bug]: v0.7.4 dev version CPU usage remains at 100% even when no requests are being processed.

| 字段 | 值 |
| --- | --- |
| Issue | [#14799](https://github.com/vllm-project/vllm/issues/14799) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.7.4 dev version CPU usage remains at 100% even when no requests are being processed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Start the vLLM service using the following command. ```bash VLLM_ATTENTION_BACKEND=FLASHMLA VLLM_USE_V1=1 OMP_NUM_THREADS=12 /opt/vllm-0.7.4-dev/bin/vllm serve DeepSeek-R1 --max-model-len 131072 --max-num-batched-tokens 8192 --enable-reasoning --reasoning-parser deepseek_r1 --api_key ${VLLM_API_KEY} --tensor-parallel-size 8 --trust-remote-code --disable-log-requests --enable-prefix-caching --enable-chunked-prefill --gpu_memory_utilization=0.95 -O3 ``` ``` Package Version --------------------------------- ---------------------- aiohappyeyeballs 2.6.1 aiohttp 3.11.13 aiosignal 1.3.2 airportsdata 20250224 annotated-types 0.7.0 anyio 4.8.0 astor 0.8.1 attrs 25.3.0 blake3 1.0.4 certifi 2025.1.31 charset-normalizer 3.4.1 click 8.1.8 cloudpickle 3.1.1 compressed-tensors 0.9.2 cupy-cuda12x 13.4.0 depyf 0.18.0 dill 0.3.9 diskcache 5.6.3 distro 1.9.0 dnspython 2.7.0 einops 0.8.1 email_validator 2.2.0 fastapi 0.115.11 fastapi-cli 0.0.7 fastrlock 0.8.3 filelock 3.17.0 flashinfer-python 0.2.2+cu124torch2.5 frozenlist 1.5.0 fsspec 2025.3.0 gguf 0.10.0 h11 0.14.0 httpcore 1.0.7 httptools 0.6.4 httpx 0.28.1 huggingface-hub 0.29.3 idna 3.10 impor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: v0.7.4 dev version CPU usage remains at 100% even when no requests are being processed. bug ### Your current environment ### 🐛 Describe the bug Start the vLLM service using the following command. ```bash VLLM_ATT...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: THREADS=12 /opt/vllm-0.7.4-dev/bin/vllm serve DeepSeek-R1 --max-model-len 131072 --max-num-batched-tokens 8192 --enable-reasoning --reasoning-parser deepseek_r1 --api_key ${VLLM_API_KEY} --tensor-parallel-size 8 --trust...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rt the vLLM service using the following command. ```bash VLLM_ATTENTION_BACKEND=FLASHMLA VLLM_USE_V1=1 OMP_NUM_THREADS=12 /opt/vllm-0.7.4-dev/bin/vllm serve DeepSeek-R1 --max-model-len 131072 --max-num-batched-tokens 81...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 3.1.1 compressed-tensors 0.9.2 cupy-cuda12x 13.4.0 depyf 0.18.0 dill 0.3.9 diskcache 5.6.3 distro 1.9.0 dnspython
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v0.7.4 dev version CPU usage remains at 100% even when no requests are being processed. bug ### Your current environment ### 🐛 Describe the bug Start the vLLM service using the following command. ```bash VLLM_ATT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
