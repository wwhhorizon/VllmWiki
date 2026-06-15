# vllm-project/vllm#22965: [Bug]: [xPyD]Abnormal results when using v1 P2pNcclConnector as KV cache transport: repeated requests for the same input produce abnormal outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#22965](https://github.com/vllm-project/vllm/issues/22965) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [xPyD]Abnormal results when using v1 P2pNcclConnector as KV cache transport: repeated requests for the same input produce abnormal outputs

### Issue 正文摘录

### Your current environment **My Environmet** 机器：2 * H20 * 8 vllm: 0.10.0 model: Qwen3-Coder-480B-A35B-Instruct-FP8 P/D：1P1D Launch Prefiller ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_USE_V1=1 vllm serve /model \ --host 0.0.0.0 \ --port 20003 \ --tensor-parallel-size 8 \ --max-model-len 131072 \ --trust-remote-code \ --gpu-memory-utilization 0.85 \ --enable-expert-parallel \ --kv-transfer-config \ "{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_producer\",\"kv_buffer_size\":\"1e1\",\"kv_port\":\"21001\",\"kv_connector_extra_config\":{\"proxy_ip\":\"0.0.0.0\",\"proxy_port\":\"30001\",\"http_port\":\"20003\",\"send_type\":\"PUT_ASYNC\",\"nccl_num_channels\":\"16\"}}" ``` Launch Deocder ``` VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve /model \ --host 0.0.0.0 \ --port 21003 \ --tensor-parallel-size 8 \ --max-model-len 131072 \ --trust-remote-code \ --gpu-memory-utilization 0.85 \ --enable-expert-parallel \ --kv-transfer-config \ "{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_consumer\",\"kv_buffer_size\":\"8e9\",\"kv_port\":\"22001\",\"kv_connector_extra_config\":{\"proxy_ip\":\"10.94.130.184\",\"proxy_port\":\"30001\",\"http_port\":\"21003\",\...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment **My Environmet** 机器：2 * H20 * 8 vllm: 0.10.0 model: Qwen3-Coder-480B-A35B-Instruct-FP8 P/D：1P1D Launch Prefiller ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_USE_V1=1 vllm serve /model \ --hos...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l results when using v1 P2pNcclConnector as KV cache transport: repeated requests for the same input produce abnormal outputs bug;stale ### Your current environment **My Environmet** 机器：2 * H20 * 8 vllm: 0.10.0 model: Q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model: Qwen3-Coder-480B-A35B-Instruct-FP8 P/D：1P1D Launch Prefiller ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_USE_V1=1 vllm serve /model \ --host 0.0.0.0 \ --port 20003 \ --tensor-parallel-size 8 \ --max-model-len 1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nmet** 机器：2 * H20 * 8 vllm: 0.10.0 model: Qwen3-Coder-480B-A35B-Instruct-FP8 P/D：1P1D Launch Prefiller ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_USE_V1=1 vllm serve /model \ --host 0.0.0.0 \ --port 20003 \ --tensor-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: [xPyD]Abnormal results when using v1 P2pNcclConnector as KV cache transport: repeated requests for the same input produce abnormal outputs bug;stale ### Your current environment **My Environmet** 机器：2 * H20 * 8 v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
