# vllm-project/vllm#28440: [Bug]: Failed to generate Cutlass kernels: [Errno 13] Permission denied in Docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#28440](https://github.com/vllm-project/vllm/issues/28440) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to generate Cutlass kernels: [Errno 13] Permission denied in Docker image

### Issue 正文摘录

### Your current environment Running [nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa](https://hub.docker.com/layers/vllm/vllm-openai/nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa/images/sha256-d18513b7afb0c3ab0e4d0fb814e0c271edfb2e54a9194339e44b38e3603f92ed) with qwen3-coder-480b-a35b ``` - '--model=/mnt/genai/Qwen--Qwen3-Coder-480B-A35B-Instruct/9d90cf8fca1bf7b7acca42d3fc9ae694a2194069' - '--disable-log-requests' - '--distributed-executor-backend=ray' - '--load-format=runai_streamer' - '--port=5000' - '--tensor-parallel-size=8' - '--served-model-name=gresearch/qwen3-coder-480b-a35b' - '--uvicorn-log-level=warning' - '--block_size=32' - '--model-loader-extra-config={"concurrency": 178, "distributed": true}' - '--enable-server-load-tracking' - '--gpu-memory-utilization=0.90' - '--max-model-len=262144' - '--max-num-seqs=1024' - '--enable-expert-parallel' - '--enable-auto-tool-choice' - '--tool-call-parser=qwen3_coder' - '--enable-prefix-caching' - '--max-num-batched-tokens=4096' - '--dtype=bfloat16' ``` ``` - name: VLLM_SKIP_P2P_CHECK value: '1' - name: VLLM_DISABLE_COMPILE_CACHE value: '1' - name: RUNAI_STREAMER_DIST value: '1' - name: RUNAI_STREAMER_CHUNK_BYTESIZE value: '419...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 6-d18513b7afb0c3ab0e4d0fb814e0c271edfb2e54a9194339e44b38e3603f92ed) with qwen3-coder-480b-a35b ``` - '--model=/mnt/genai/Qwen--Qwen3-Coder-480B-A35B-Instruct/9d90cf8fca1bf7b7acca42d3fc9ae694a2194069' - '--disable-log-re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Failed to generate Cutlass kernels: [Errno 13] Permission denied in Docker image bug;stale ### Your current environment Running [nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa](https://hub.docker.com/layers/vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oder' - '--enable-prefix-caching' - '--max-num-batched-tokens=4096' - '--dtype=bfloat16' ``` ``` - name: VLLM_SKIP_P2P_CHECK value: '1' - name: VLLM_DISABLE_COMPILE_CACHE value: '1' - name: RUNAI_STREAMER_DIST value: '1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug]: Failed to generate Cutlass kernels: [Errno 13] Permission denied in Docker image bug;stale ### Your current environment Running [nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa](https://hub.docker.com/layers/vllm/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ion=0.90' - '--max-model-len=262144' - '--max-num-seqs=1024' - '--enable-expert-parallel' - '--enable-auto-tool-choice' - '--tool-call-parser=qwen3_coder' - '--enable-prefix-caching' - '--max-num-batched-tokens=4096' -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
