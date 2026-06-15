# vllm-project/vllm#19214: [Usage]: Is the service interface exposed by PD separation compatible with the service API of OpenAPI?

| 字段 | 值 |
| --- | --- |
| Issue | [#19214](https://github.com/vllm-project/vllm/issues/19214) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is the service interface exposed by PD separation compatible with the service API of OpenAPI?

### Issue 正文摘录

### Your current environment ```bash export IMAGE="registry.intsig.net/yongshuai_wang/docker.io/vllm/vllm-openai:v0.9.0" export WK_DIR=`pwd` docker run -it --rm --gpus all \ --shm-size 32g \ --network host \ --privileged \ --entrypoint bash \ -v /juicefs-algorithm:/juicefs-algorithm \ -w ${WK_DIR} \ ${IMAGE} ``` ```bash #!/bin/bash MODEL_NAME=/juicefs-algorithm/workspace/vision/yongshuai_wang/models/qwen/Qwen2.5-3B-Instruct export VLLM_USE_V1=0 # 当前vllm 0.9.0的PD分离支持V0 CUDA_VISIBLE_DEVICES=6 vllm serve $MODEL_NAME \ --port 8100 \ --max-model-len 9126 \ --gpu-memory-utilization 0.5 \ --trust-remote-code \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2}' & # decoding instance, which is the KV consumer CUDA_VISIBLE_DEVICES=7 vllm serve $MODEL_NAME \ --port 8200 \ --max-model-len 9126 \ --gpu-memory-utilization 0.5 \ --trust-remote-code \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":"kv_consumer","kv_rank":1,"kv_parallel_size":2}' & ``` ### disagg_prefill_proxy_server.py ```python import os import aiohttp from quart import Quart, make_response, request AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(tota...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: fs-algorithm \ -w ${WK_DIR} \ ${IMAGE} ``` ```bash #!/bin/bash MODEL_NAME=/juicefs-algorithm/workspace/vision/yongshuai_wang/models/qwen/Qwen2.5-3B-Instruct export VLLM_USE_V1=0 # 当前vllm 0.9.0的PD分离支持V0 CUDA_VISIBLE_DEVI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: posed by PD separation compatible with the service API of OpenAPI? usage;stale ### Your current environment ```bash export IMAGE="registry.intsig.net/yongshuai_wang/docker.io/vllm/vllm-openai:v0.9.0" export WK_DIR=`pwd`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nt environment ```bash export IMAGE="registry.intsig.net/yongshuai_wang/docker.io/vllm/vllm-openai:v0.9.0" export WK_DIR=`pwd` docker run -it --rm --gpus all \ --shm-size 32g \ --network host \ --privileged \ --entrypoi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: qwen/Qwen2.5-3B-Instruct export VLLM_USE_V1=0 # 当前vllm 0.9.0的PD分离支持V0 CUDA_VISIBLE_DEVICES=6 vllm serve $MODEL_NAME \ --port 8100 \ --max-model-len 9126 \ --gpu-memory-utilization 0.5 \ --trust-remote-code \ --kv-transf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: hunked(1024): yield chunk_bytes else: content = await response.read() yield content @app.route("/v1/completions", methods=["POST"]) async def handle_request(): try: original_request_data = await reque

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
