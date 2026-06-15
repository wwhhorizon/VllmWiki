# vllm-project/vllm#21828: [Bug]: When the service is pulled up, there is enough video memory but a service pull up error occurs

| 字段 | 值 |
| --- | --- |
| Issue | [#21828](https://github.com/vllm-project/vllm/issues/21828) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When the service is pulled up, there is enough video memory but a service pull up error occurs

### Issue 正文摘录

### Your current environment but i only start a serve 32B model A800 80G（60G Free） ### 🐛 Describe the bug This is my seeting cuda_visible_devices:str = os.getenv(key="DEVICE_ID",default="0") model = os.getenv(key="MODEL_NAME", default="llm") max_tokens = int(os.getenv(key="MAX_TOKENS", default="8192")) tp_size = int(os.getenv(key="TP", default="1")) pp_size = int(os.getenv(key="PP", default="1")) gpus = float(os.getenv(key="GPUS", default="0.4")) token = os.getenv(key="API_KEY", default="na") weight_format = os.getenv(key="WEIGHT_FORMAT", default="awq_marlin") reason_format = os.getenv(key="REASON_FORMAT", default="none") while i start the server by vllm v1 engine engine_args = AsyncEngineArgs( model="/app/model", served_model_name=env.model, quantization=env.weight_format if env.weight_format != "full" else None, max_model_len=env.max_tokens, tensor_parallel_size=env.tp_size, pipeline_parallel_size=env.pp_size, gpu_memory_utilization=env.gpus, trust_remote_code=True, enforce_eager=True, enable_reasoning=env.reason_format if env.reason_format != "none" else None, reasoning_parser= env.reasoning_parser if env.reason_format !="none" else None, distributed_executor_backend="ray" if e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urs bug;stale ### Your current environment but i only start a serve 32B model A800 80G（60G Free） ### 🐛 Describe the bug This is my seeting cuda_visible_devices:str = os.getenv(key="DEVICE_ID",default="0") model = os.get...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model A800 80G（60G Free） ### 🐛 Describe the bug This is my seeting cuda_visible_devices:str = os.getenv(key="DEVICE_ID",default="0") model = os.getenv(key="MODEL_NAME", default="llm") max_tokens = int(os.getenv(key="MAX...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , quantization=env.weight_format if env.weight_format != "full" else None, max_model_len=env.max_tokens, tensor_parallel_size=env.tp_size, pipeline_parallel_size=env.pp_size, gpu_memory_utilization=env.gpus, trust_remot...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: up, there is enough video memory but a service pull up error occurs bug;stale ### Your current environment but i only start a serve 32B model A800 80G（60G Free） ### 🐛 Describe the bug This is my seeting cuda_visible_dev...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: er if env.reason_format !="none" else None, distributed_executor_backend="ray" if env.tp_size >=2 else None, guided_decoding_backend="auto", tokenizer_pool_size=1, tokenizer_pool_type="ray", disable_log_requests=True )...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
