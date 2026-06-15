# vllm-project/vllm#38515: [Bug]: vLLM crashed when working with CPU offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#38515](https://github.com/vllm-project/vllm/issues/38515) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashed when working with CPU offloading

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run command ```bash #!/bin/bash # MiniMax-M2 Series Usage Guide # https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html MODEL=MiniMaxAI/MiniMax-M2.5 HF_ENDPOINT=https://hf-mirror.com NAME=minimax API_KEY=openai sudo docker stop $NAME > /dev/null 2>&1 sudo docker rm $NAME > /dev/null 2>&1 # wait for GPU release sleep 5 # parallel # requests in a single batch # --max-num-seqs 256 sudo docker run \ -d \ --restart always \ --runtime nvidia \ --gpus all \ --name $NAME \ -e HF_ENDPOINT=$HF_ENDPOINT \ -e 'NCCL_P2P_DISABLE=1' \ -v /data/hf:/root/.cache/huggingface \ -v $(pwd)/config:/config \ -p 7035:8000 \ --ipc=host \ vllm/vllm-openai:nightly \ $MODEL \ --api-key $API_KEY \ --gpu-memory-utilization 0.85 \ --tensor-parallel-size 4 \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_append_think \ --enable-auto-tool-choice \ --trust-remote-code \ --max-num-seqs 256 \ --kv-offloading-backend native \ --kv-offloading-size 512 \ --disable-hybrid-kv-cache-manager \ --enable-chunked-prefill \ --enable-prefix-caching \ --compilation-config '{"cudagraph_mode": "PIECEWISE"}' ``` Crash logs ```text (APIServer pid=1)...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: rm $NAME > /dev/null 2>&1 # wait for GPU release sleep 5 # parallel # requests in a single batch # --max-num-seqs 256 sudo docker run \ -d \ --restart always \ --runtime nvidia \ --gpus all \ --name $NAME \ -e HF_ENDPOI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html MODEL=MiniMaxAI/MiniMax-M2.5 HF_ENDPOINT=https://hf-mirror.com NAME=minimax API_KEY=openai sudo docker stop $NAME > /dev/null 2>&1 sudo docker rm $...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /bash # MiniMax-M2 Series Usage Guide # https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html MODEL=MiniMaxAI/MiniMax-M2.5 HF_ENDPOINT=https://hf-mirror.com NAME=minimax API_KEY=openai sudo docker stop...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: vLLM crashed when working with CPU offloading bug ### Your current environment ### 🐛 Describe the bug Run command ```bash #!/bin/bash # MiniMax-M2 Series Usage Guide # https://docs.vllm.ai/projects/recipes/en/lat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: \ --trust-remote-code \ --max-num-seqs 256 \ --kv-offloading-backend native \ --kv-offloading-size 512 \ --disable-hybrid-kv-cache-manager \ --enable-chunked-prefill \ --enable-prefix-caching \ --compilation-config '{"c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
