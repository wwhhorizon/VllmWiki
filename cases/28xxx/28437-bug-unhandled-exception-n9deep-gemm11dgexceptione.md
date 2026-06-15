# vllm-project/vllm#28437: [Bug]: Unhandled exception: N9deep_gemm11DGExceptionE.

| 字段 | 值 |
| --- | --- |
| Issue | [#28437](https://github.com/vllm-project/vllm/issues/28437) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unhandled exception: N9deep_gemm11DGExceptionE.

### Issue 正文摘录

### Your current environment This was using: [nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa](https://hub.docker.com/layers/vllm/vllm-openai/nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa/images/sha256-d18513b7afb0c3ab0e4d0fb814e0c271edfb2e54a9194339e44b38e3603f92ed) docker image and DSR1 ```text - '--model=/mnt/genai/unsloth--DeepSeek-R1-0528/b8fbb38094435d23aaef169287866947247bb386' - '--disable-log-requests' - '--distributed-executor-backend=ray' - '--load-format=runai_streamer' - '--port=5000' - '--tensor-parallel-size=8' - '--served-model-name=gresearch/deepseek-r1-0528' - '--uvicorn-log-level=warning' - '--block_size=32' - '--model-loader-extra-config={"concurrency": 178, "distributed": true}' - '--enable-server-load-tracking' - '--gpu-memory-utilization=0.90' - '--max-model-len=128000' - '--max-num-seqs=1024' - '--reasoning-parser=deepseek_r1' - '--enable-expert-parallel' - '--enable-prefix-caching' ``` ``` - name: VLLM_SKIP_P2P_CHECK value: '1' - name: VLLM_DISABLE_COMPILE_CACHE value: '1' - name: RUNAI_STREAMER_DIST value: '1' - name: VLLM_USE_FLASHINFER_MOE_FP16 value: '1' - name: TORCHINDUCTOR_CACHE_DIR ``` ### 🐛 Describe the bug This is an intermittent issue discov...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 271edfb2e54a9194339e44b38e3603f92ed) docker image and DSR1 ```text - '--model=/mnt/genai/unsloth--DeepSeek-R1-0528/b8fbb38094435d23aaef169287866947247bb386' - '--disable-log-requests' - '--distributed-executor-backend=r...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Unhandled exception: N9deep_gemm11DGExceptionE. bug;stale ### Your current environment This was using: [nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa](https://hub.docker.com/layers/vllm/vllm-openai/nightly-e5e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 9287866947247bb386' - '--disable-log-requests' - '--distributed-executor-backend=ray' - '--load-format=runai_streamer' - '--port=5000' - '--tensor-parallel-size=8' - '--served-model-name=gresearch/deepseek-r1-0528' - '-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: as using: [nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa](https://hub.docker.com/layers/vllm/vllm-openai/nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa/images/sha256-d18513b7afb0c3ab0e4d0fb814e0c271edfb2e54a9194339...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e44b38e3603f92ed) docker image and DSR1 ```text - '--model=/mnt/genai/unsloth--DeepSeek-R1-0528/b8fbb38094435d23aaef169287866947247bb386' - '--disable-log-requests' - '--distributed-executor-backend=ray' - '--load-forma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
