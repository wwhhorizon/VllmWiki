# vllm-project/vllm#25759: [Usage]: run Qwen2.5-VL with PD disaggregation raise ValueError("Insufficient memory")

| 字段 | 值 |
| --- | --- |
| Issue | [#25759](https://github.com/vllm-project/vllm/issues/25759) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: run Qwen2.5-VL with PD disaggregation raise ValueError("Insufficient memory")

### Issue 正文摘录

### Your current environment I start the P and D services with the following parameters. ``` # kv_producer VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 vllm serve /opt/work/Qwen2.5-VL-7B-Instruct-20250829-FP8-Dynamic --host 0.0.0.0 --port 8100 --tensor-parallel-size 1 --served-model-name base_model --dtype auto --max-model-len 10000 --limit-mm-per-prompt '{"image":12}' --compilation-config '{"level": 3,"compilation_mode":"default","compiler":"vllm-compiler","configs":{"model":{"vision_language":{"enable":true,"vision_encoder_compilation_mode":"disable","llm_compilation_mode":"enable"}}}}' --max-num-seqs 20 --gpu-memory-utilization 0.7 --kv-transfer-config '{"kv_connector":"P2pNcclConnector","kv_role":"kv_producer","kv_buffer_size":"2e9","kv_port":"21001","kv_connector_extra_config":{"proxy_ip":"0.0.0.0","proxy_port":"30001","http_port":"8100","send_type":"PUT_ASYNC"}}' # kv_consumer VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 vllm serve /opt/work/Qwen2.5-VL-7B-Instruct-20250829-FP8-Dynamic --port 8200 --served-model-name base_model --tensor-parallel-size 1 --dtype auto --enable-prefix-caching --enable-chunked-prefill --max-model-len 8000 --limit-mm-per-prompt '{"image":12}' --compilation-config...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: A_VISIBLE_DEVICES=0 vllm serve /opt/work/Qwen2.5-VL-7B-Instruct-20250829-FP8-Dynamic --host 0.0.0.0 --port 8100 --tensor-parallel-size 1 --served-model-name base_model --dtype auto --max-model-len 10000 --limit-mm-per-p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: run Qwen2.5-VL with PD disaggregation raise ValueError("Insufficient memory") usage ### Your current environment I start the P and D services with the following parameters. ``` # kv_producer VLLM_USE_V1=1 CUDA_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: run Qwen2.5-VL with PD disaggregation raise ValueError("Insufficient memory") usage ### Your current environment I start the P and D services with the following parameters. ``` # kv_producer VLLM_USE_V1=1 CUDA_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: or-parallel-size 1 --dtype auto --enable-prefix-caching --enable-chunked-prefill --max-model-len 8000 --limit-mm-per-prompt '{"image":12}' --compilation-config '{"level": 3,"compilation_mode":"default","compiler":"vllm-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ervices with the following parameters. ``` # kv_producer VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 vllm serve /opt/work/Qwen2.5-VL-7B-Instruct-20250829-FP8-Dynamic --host 0.0.0.0 --port 8100 --tensor-parallel-size 1 --served...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
