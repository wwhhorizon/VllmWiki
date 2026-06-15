# vllm-project/vllm#40340: [Bug]: MoRI Connector hangs at >=128 concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#40340](https://github.com/vllm-project/vllm/issues/40340) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;moe |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoRI Connector hangs at >=128 concurrency

### Issue 正文摘录

### Your current environment Running `vllm bench serve` with `--max-concurrency 128` or 256 @ 1k/1k ISL/OSL on a 1P1D deployment of DSR1 TP8EP8 on two 8xMI300X nodes hangs indefinitely after a while. ```shell # Set on both nodes before running any command export PREFILL_IP= export DECODE_IP= # Node 1 (prefill node) — command 1: start toy proxy docker run -d \ --name moriio-toy-proxy \ --network host \ --rm \ --entrypoint bash \ vllm/vllm-openai-rocm:v0.19.1 \ -c "pip install --quiet --ignore-installed quart aiohttp msgpack && \ python3 -u /app/vllm/examples/online_serving/disaggregated_serving/moriio_toy_proxy_server.py" # Node 1 (prefill node) — command 2: start prefill instance docker run -d \ --rm \ --name moriio-prefill \ --init --network host --ipc host --privileged \ --cap-add SYS_PTRACE --security-opt seccomp=unconfined \ --ulimit memlock=-1 --ulimit stack=67108864 \ --shm-size 256G \ --group-add video --group-add render \ --device /dev/kfd --device /dev/dri --device /dev/infiniband \ -v /sys:/sys \ -v "${HOME}/.cache/huggingface:/root/.cache/huggingface" \ -e HF_HOME=/root/.cache/huggingface \ -e HF_HUB_ENABLE_HF_TRANSFER=0 \ -e VLLM_MORIIO_CONNECTOR_READ_MODE=1 \ -e NCCL_...

## 现有链接修复摘要

#40344 [Bugfix][ROCm] Resolve MoRI connector hangs at high concurrency

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: export DECODE_IP= # Node 1 (prefill node) — command 1: start toy proxy docker run -d \ --name moriio-toy-proxy \ --network host \ --rm \ --entrypoint bash \ vllm/vllm-openai-rocm:v0.19.1 \ -c "pip install --quiet --igno...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: MoRI Connector hangs at >=128 concurrency bug;rocm ### Your current environment Running `vllm bench serve` with `--max-concurrency 128` or 256 @ 1k/1k ISL/OSL on a 1P1D deployment of DSR1 TP8EP8 on two 8xMI300X n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: dev/dri --device /dev/infiniband \ -v /sys:/sys \ -v "${HOME}/.cache/huggingface:/root/.cache/huggingface" \ -e HF_HOME=/root/.cache/huggingface \ -e HF_HUB_ENABLE_HF_TRANSFER=0 \ -e VLLM_MORIIO_CONNECTOR_READ_MODE=1 \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: hile. ```shell # Set on both nodes before running any command export PREFILL_IP= export DECODE_IP= # Node 1 (prefill node) — command 1: start toy proxy docker run -d \ --name moriio-toy-proxy \ --network host \ --rm \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _READY_TIMEOUT_S=3600 \ -e VLLM_SERVER_DEV_MODE=1 \ -e VLLM_ROCM_USE_AITER=1 \ -e VLLM_ROCM_USE_AITER_PAGED_ATTN=0 \ -e VLLM_ROCM_USE_AITER_RMSNORM=1 \ -e VLLM_USE_AITER_TRITON_SILU_MUL=0 \ vllm/vllm-openai-rocm:v0.19.1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40344](https://github.com/vllm-project/vllm/pull/40344) | closes_keyword | 0.95 | [Bugfix][ROCm] Resolve MoRI connector hangs at high concurrency | Fixes #40340. There are a few parts of the MoRI-IO connector code that can cause indefinite hangs of the connector. This PR resolves them so we can run at least 512 concurrency |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
