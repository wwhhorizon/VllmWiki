# vllm-project/vllm#20440: [Bug]: PD disaggregation using NixlConnector failed with long prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#20440](https://github.com/vllm-project/vllm/issues/20440) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PD disaggregation using NixlConnector failed with long prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying pd disaggregation using NixlConnector. Everything is ok when I send a short prompt, but I got a `Segmentation fault` when sending a prompt with about 500 tokens. Here is the script I used to start the pd disaggregation service: ``` MODEL="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" CONNECTOR="NixlConnector" trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT trap 'kill $(jobs -pr)' EXIT wait_for_server() { local port=$1 timeout 1200 bash -c " until curl -s localhost:${port}/v1/chat/completions > /dev/null; do sleep 1 done" && return 0 || return 1 } run() { local model_name=$1 local connector=$2 echo "================================" echo "Testing model: $model_name" echo "Using connector: $connector" echo "================================" # prefilling instance, which is the KV producer PREFILL_PORT=8100 CUDA_VISIBLE_DEVICES=0 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve ../../data/huggingface.co/$model_name \ --port $PREFILL_PORT \ --max-model-len 5000 \ --max-num-batched-tokens=8192 \ --disable-log-requests \ --gpu-memory-utilization 0.95 \ --trust-remote-code \ --kv-transfer-config \ "{\"kv_connector\":\"$connector\",\"kv_rol...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: for decode instance to start..." wait_for_server $DECODE_PORT # Build the command for the proxy server with all the hosts and ports PROXY_PORT=8000 PROXY_CMD="python3 toy_proxy_server.py --port $PROXY_PORT" PROXY_CMD+="...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: onnector: $connector" echo "================================" # prefilling instance, which is the KV producer PREFILL_PORT=8100 CUDA_VISIBLE_DEVICES=0 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve ../../data/huggingface.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: . Here is the script I used to start the pd disaggregation service: ``` MODEL="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" CONNECTOR="NixlConnector" trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT trap 'kill $(jobs -pr)' EXIT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=5000, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
