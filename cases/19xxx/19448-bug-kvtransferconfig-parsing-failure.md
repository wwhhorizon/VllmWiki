# vllm-project/vllm#19448: [Bug]: KVTransferConfig Parsing Failure

| 字段 | 值 |
| --- | --- |
| Issue | [#19448](https://github.com/vllm-project/vllm/issues/19448) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KVTransferConfig Parsing Failure

### Issue 正文摘录

### Your current environment My docker cannot download collect_env.py. The vLLM version is 0.9.0.1. ### 🐛 Describe the bug When running ``` VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=1 vllm serve /data/models/Qwen3-32B --tensor_parallel-size 1 --port 8101 --max-model-len 40960 --swap-space 0 --trust-remote-code --kv-cache-dtype 'fp8' --kv-transfer-config '{"kv_connector":"Connector"}' --no-enable-chunked-prefill ``` I got an error `vllm serve: error: argument --kv-transfer-config: Value {"kv_connector":"Connector"} cannot be converted to ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: KVTransferConfig Parsing Failure bug ### Your current environment My docker cannot download collect_env.py. The vLLM version is 0.9.0.1. ### 🐛 Describe the bug When running ``` VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ]: KVTransferConfig Parsing Failure bug ### Your current environment My docker cannot download collect_env.py. The vLLM version is 0.9.0.1. ### 🐛 Describe the bug When running ``` VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=1 vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 101 --max-model-len 40960 --swap-space 0 --trust-remote-code --kv-cache-dtype 'fp8' --kv-transfer-config '{"kv_connector":"Connector"}' --no-enable-chunked-prefill ``` I got an error `vllm serve: error: argument --kv-tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sion is 0.9.0.1. ### 🐛 Describe the bug When running ``` VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=1 vllm serve /data/models/Qwen3-32B --tensor_parallel-size 1 --port 8101 --max-model-len 40960 --swap-space 0 --trust-remote-co...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: --port 8101 --max-model-len 40960 --swap-space 0 --trust-remote-code --kv-cache-dtype 'fp8' --kv-transfer-config '{"kv_connector":"Connector"}' --no-enable-chunked-prefill ``` I got an error `vllm serve: error: argument...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
