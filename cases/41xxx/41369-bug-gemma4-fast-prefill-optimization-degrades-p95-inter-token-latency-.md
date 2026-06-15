# vllm-project/vllm#41369: [Bug]: Gemma4 Fast Prefill Optimization degrades p95 inter-token latency significantly

| 字段 | 值 |
| --- | --- |
| Issue | [#41369](https://github.com/vllm-project/vllm/issues/41369) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 Fast Prefill Optimization degrades p95 inter-token latency significantly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug p95 inter-token latency went up significantly after enabling `--kv-sharing-fast-prefill` on Gemma4 model (contrary to https://github.com/vllm-project/vllm/pull/38879). The following is a graph showing p50, p95, p99 on metric `prometheus/vllm:inter_token_latency_seconds/histogram`. You can see where I enabled the new flag. There are no meaningful improvements in E2E request latency or time to first token. The VMs are deployed on Google Compute Engine. The way we use it is just this `docker run` command in a Linux startup script: ```bash docker run -d \ --gpus all \ --restart=on-failure \ --log-driver=gcplogs \ --log-opt gcp-log-cmd=true \ --log-opt mode=non-blocking \ --log-opt max-buffer-size=5m \ -e VLLM_HTTP_TIMEOUT_KEEP_ALIVE=620 \ -p 8080:8080 \ -v "$MIDDLEWARE_HOST_PATH":/workspace/request_middleware.py:ro \ --name $CONTAINER_NAME \ "$IMAGE" \ --port 8080 \ --model google/gemma-4-E4B-it \ --served-model-name google/gemma-4-E4B-it google/gemma-3n-E4B-it \ --max-model-len 3072 \ --max-num-seqs 16 \ --gpu-memory-utilization 0.9 \ --api-key XXX \ --disable-access-log-for-endpoints "/health,/metrics,/ping,/ready" \ --limit-mm-per...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s are deployed on Google Compute Engine. The way we use it is just this `docker run` command in a Linux startup script: ```bash docker run -d \ --gpus all \ --restart=on-failure \ --log-driver=gcplogs \ --log-opt gcp-lo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /ping,/ready" \ --limit-mm-per-prompt '{"image": 0, "audio": 0}' \ --dtype bfloat16 \ --no-enable-log-requests \ --middleware XXX \ --structured-outputs-config '{"backend":"guidance"}' \ --async-scheduling \ --enable-pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 Fast Prefill Optimization degrades p95 inter-token latency significantly bug ### Your current environment ### 🐛 Describe the bug p95 inter-token latency went up significantly after enabling `--kv-sharing-f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Gemma4 Fast Prefill Optimization degrades p95 inter-token latency significantly bug ### Your current environment ### 🐛 Describe the bug p95 inter-token latency went up significantly after enabling `--kv-sharing-f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ble-log-requests \ --middleware XXX \ --structured-outputs-config '{"backend":"guidance"}' \ --async-scheduling \ --enable-prefix-caching \ --kv-sharing-fast-prefill ``` Our Docker image is based on `vllm/vllm-openai:v0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
