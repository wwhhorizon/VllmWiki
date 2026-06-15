# vllm-project/vllm#38472: [Bug]: [xPyD]Potential OOM when using v1 P2pNcclConnector as KV cache transport: KV cache accumulation on decode instance.

| 字段 | 值 |
| --- | --- |
| Issue | [#38472](https://github.com/vllm-project/vllm/issues/38472) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [xPyD]Potential OOM when using v1 P2pNcclConnector as KV cache transport: KV cache accumulation on decode instance.

### Issue 正文摘录

### Your current environment My Environmet gpu A800 80GB * 2 vllm: 0.11.0 model: meta-llama/Meta-Llama-3-8B-Instruct P/D：1P1D Prefill Instance ```shell CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 vllm serve $MODEL \ --enforce-eager \ --host 127.0.0.1 \ --port 20003 \ --tensor-parallel-size 1 \ --seed 1024 \ --dtype float16 \ --max-model-len 8192 \ --max-num-batched-tokens 32768 \ --max-num-seqs 1024 \ --trust-remote-code \ --gpu-memory-utilization 0.8 \ --kv-transfer-config \ "{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_producer\",\"kv_buffer_size\":\"1e1\",\"kv_port\":\"21001\",\"kv_connector_extra_config\":{\"proxy_ip\":\"127.0.0.1\",\"proxy_port\":\"30001\",\"http_port\":\"20003\",\"send_type\":\"PUT_ASYNC\",\"nccl_num_channels\":\"16\",\"mem_pool_size_gb\":\"16\"}}" ``` Decode Instance ```shell CUDA_VISIBLE_DEVICES=1 VLLM_USE_V1=1 vllm serve $MODEL \ --enforce-eager \ --host 127.0.0.1 \ --port 20005 \ --tensor-parallel-size 1 \ --seed 1024 \ --dtype float16 \ --max-model-len 8192 \ --max-num-batched-tokens 10000 \ --max-num-seqs 1024 \ --trust-remote-code \ --gpu-memory-utilization 0.8 \ --kv-transfer-config \ "{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_consu...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: meta-llama/Meta-Llama-3-8B-Instruct P/D：1P1D Prefill Instance ```shell CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 vllm serve $MODEL \ --enforce-eager \ --host 127.0.0.1 \ --port 20003 \ --tensor-parallel-size 1 \ --seed 1024...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: [xPyD]Potential OOM when using v1 P2pNcclConnector as KV cache transport: KV cache accumulation on decode instance. bug ### Your current environment My Environmet gpu A800 80GB * 2 vllm: 0.11.0 model: meta-llama/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment My Environmet gpu A800 80GB * 2 vllm: 0.11.0 model: meta-llama/Meta-Llama-3-8B-Instruct P/D：1P1D Prefill Instance ```shell CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 vllm serve $MODEL \ --enforce-eage...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: sing v1 P2pNcclConnector as KV cache transport: KV cache accumulation on decode instance. bug ### Your current environment My Environmet gpu A800 80GB * 2 vllm: 0.11.0 model: meta-llama/Meta-Llama-3-8B-Instruct P/D：1P1D...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 003 \ --tensor-parallel-size 1 \ --seed 1024 \ --dtype float16 \ --max-model-len 8192 \ --max-num-batched-tokens 32768 \ --max-num-seqs 1024 \ --trust-remote-code \ --gpu-memory-utilization 0.8 \ --kv-transfer-config \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
