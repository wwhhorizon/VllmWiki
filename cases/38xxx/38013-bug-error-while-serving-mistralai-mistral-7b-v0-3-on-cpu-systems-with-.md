# vllm-project/vllm#38013: [Bug]: Error while serving mistralai/Mistral-7B-v0.3 on CPU systems with Docker build

| 字段 | 值 |
| --- | --- |
| Issue | [#38013](https://github.com/vllm-project/vllm/issues/38013) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while serving mistralai/Mistral-7B-v0.3 on CPU systems with Docker build

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Docker build # -------------- git clone https://github.com/vllm-project/vllm.git cd vllm docker build -f docker/Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . # Starting the docker container # -------------------------------- docker run --rm \ --net=host \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --privileged=true \ --shm-size=16g \ -e VLLM_CPU_KVCACHE_SPACE=40 \ -e VLLM_CPU_OMP_THREADS_BIND="0-63" \ -e VLLM_CPU_SGL_KERNEL=1 \ vllm-cpu-env \ --model=mistralai/Mistral-7B-v0.3 \ --dtype=bfloat16 \ -tp=1 \ --enable-chunked-prefill \ --enable-prefix-caching # Client side testing using curl and error observed # ----------------------------------------------------- curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "mistralai/Mistral-7B-v0.3", "prompt": "Explain what is AI in one sentence.", "max_tokens": 50, "temperature": 0.0 }' {"error":{"message":"EngineCore encountered an issue. See stack trace (above) for the root cause.","type":"InternalServerError","param":null,"code":500}} # Docker log displayed # ----------------------- INFO 03-24 14:38:33 [__init__.py:44] Available pl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Error while serving mistralai/Mistral-7B-v0.3 on CPU systems with Docker build bug ### Your current environment ### 🐛 Describe the bug # Docker build # -------------- git clone https://github.com/vllm-project/vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 3 \ --dtype=bfloat16 \ -tp=1 \ --enable-chunked-prefill \ --enable-prefix-caching # Client side testing using curl and error observed # ----------------------------------------------------- curl http://localhost:8000/v1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pu-env \ --model=mistralai/Mistral-7B-v0.3 \ --dtype=bfloat16 \ -tp=1 \ --enable-chunked-prefill \ --enable-prefix-caching # Client side testing using curl and error observed # ------------------------------------------...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ed an issue. See stack trace (above) for the root cause.","type":"InternalServerError","param":null,"code":500}} # Docker log displayed # ----------------------- INFO 03-24 14:38:33 [__init__.py:44] Available plugins fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ----------------- docker run --rm \ --net=host \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --privileged=true \ --shm-size=16g \ -e VLLM_CPU_KVCACHE_SPACE=40 \ -e VLLM_CPU_OMP_THREADS_BIND="0-63" \ -e VLLM_CPU_S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
