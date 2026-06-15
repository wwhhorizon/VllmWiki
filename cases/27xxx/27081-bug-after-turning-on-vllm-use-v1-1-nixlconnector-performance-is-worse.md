# vllm-project/vllm#27081: [Bug]: After turning on VLLM_USE_V1=1, NixlConnector performance is worse！

| 字段 | 值 |
| --- | --- |
| Issue | [#27081](https://github.com/vllm-project/vllm/issues/27081) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After turning on VLLM_USE_V1=1, NixlConnector performance is worse！

### Issue 正文摘录

### Your current environment In the PD separation experiment on the 4090 machine, it was found that after turning on VLLM_USE_V1=1 in the 1P1D task, the performance of NixlConnector was worse. ### 🐛 Describe the bug ``` # without VLLM_USE_V1 # P CUDA_VISIBLE_DEVICES=4 \ UCX_NET_DEVICES=all \ VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \ VLLM_USE_MODELSCOPE=true \ python3 -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --model /qwen \ --served-model-name Qwen3-30B-A3B-GPTQ-Int4 \ --gpu-memory-utilization 0.8 \ --max-model-len 10240 \ --enable-chunked-prefill \ --port 8100 \ --trust-remote-code \ --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' # D CUDA_VISIBLE_DEVICES=5 \ UCX_NET_DEVICES=all \ VLLM_NIXL_SIDE_CHANNEL_PORT=5601 \ VLLM_USE_MODELSCOPE=true \ python3 -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --model /qwen \ --served-model-name Qwen3-30B-A3B-GPTQ-Int4 \ --gpu-memory-utilization 0.8 \ --max-model-len 10240 \ --enable-chunked-prefill \ --port 8200 \ --trust-remote-code \ --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' # 代理 python3 tests/v1/kv_connector/nixl_integration/toy_proxy_server....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ES=4 \ UCX_NET_DEVICES=all \ VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \ VLLM_USE_MODELSCOPE=true \ python3 -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --model /qwen \ --served-model-name Qwen3-30B-A3B-GPT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: After turning on VLLM_USE_V1=1, NixlConnector performance is worse！ bug;stale ### Your current environment In the PD separation experiment on the 4090 machine, it was found that after turning on VLLM_USE_V1=1 in the 1P1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nector was worse. ### 🐛 Describe the bug ``` # without VLLM_USE_V1 # P CUDA_VISIBLE_DEVICES=4 \ UCX_NET_DEVICES=all \ VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \ VLLM_USE_MODELSCOPE=true \ python3 -m vllm.entrypoints.openai.api_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oder-ports 8200 ``` without VLLM_USE_V1=1： with VLLM_USE_V1=1 vllm version：v0.10.2 nixl： 0.6.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: llel-size 1 \ --model /qwen \ --served-model-name Qwen3-30B-A3B-GPTQ-Int4 \ --gpu-memory-utilization 0.8 \ --max-model-len 10240 \ --enable-chunked-prefill \ --port 8100 \ --trust-remote-code \ --kv-transfer-config '{"k...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
