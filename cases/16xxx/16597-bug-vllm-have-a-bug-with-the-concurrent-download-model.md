# vllm-project/vllm#16597: [Bug]: vllm have a bug with the concurrent download model

| 字段 | 值 |
| --- | --- |
| Issue | [#16597](https://github.com/vllm-project/vllm/issues/16597) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm have a bug with the concurrent download model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When i run `bash examples/online_serving/disaggregated_prefill.sh` this examples. got a error. ``` + echo '🚧🚧 Warning: The usage of disaggregated prefill is experimental and subject to change 🚧🚧' 🚧🚧 Warning: The usage of disaggregated prefill is experimental and subject to change 🚧🚧 + sleep 1 + MODEL_NAME=Qwen/Qwen2.5-0.5B + trap cleanup INT ++ hostname -I ++ awk '{print $1}' + export VLLM_HOST_IP=172.64.130.224 + VLLM_HOST_IP=172.64.130.224 + python3 -c 'import quart' + echo 'Quart is already installed.' Quart is already installed. + CUDA_VISIBLE_DEVICES=0 + vllm serve Qwen/Qwen2.5-0.5B --port 8100 --max-model-len 100 --gpu-memory-utilization 0.8 --trust-remote-code --kv-transfer-config '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2}' + wait_for_server 8100 + local port=8100 + timeout 1200 bash -c ' until curl -s localhost:8100/v1/completions > /dev/null; do sleep 1 done' + CUDA_VISIBLE_DEVICES=1 + vllm serve Qwen/Qwen2.5-0.5B --port 8200 --max-model-len 100 --gpu-memory-utilization 0.8 --trust-remote-code --kv-transfer-config '{"kv_connector":"PyNcclConnector","kv_role":"kv_consumer"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: VLLM_HOST_IP=172.64.130.224 + VLLM_HOST_IP=172.64.130.224 + python3 -c 'import quart' + echo 'Quart is already installed.' Quart is already installed. + CUDA_VISIBLE_DEVICES=0 + vllm serve Qwen/Qwen2.5-0.5B --port 8100...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm have a bug with the concurrent download model bug;stale ### Your current environment ### 🐛 Describe the bug When i run `bash examples/online_serving/disaggregated_prefill.sh` this examples. got a error. ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm have a bug with the concurrent download model bug;stale ### Your current environment ### 🐛 Describe the bug When i run `bash examples/online_serving/disaggregated_prefill.sh` this examples. got a error. ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dtype='auto', kv_cache_dtype='auto', max_model_len=100, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=100, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dist...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
