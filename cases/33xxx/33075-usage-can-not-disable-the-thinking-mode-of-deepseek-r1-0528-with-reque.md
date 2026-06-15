# vllm-project/vllm#33075: [Usage]: Can not disable the thinking mode of deepseek-r1-0528 with request-level chat_template_kwargs

| 字段 | 值 |
| --- | --- |
| Issue | [#33075](https://github.com/vllm-project/vllm/issues/33075) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can not disable the thinking mode of deepseek-r1-0528 with request-level chat_template_kwargs

### Issue 正文摘录

### Your current environment ```text vLLM Version: 0.10.0 NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 CUDA_MODULE_LOADING=LAZY ``` request: completion = client.chat.completions.create( model="deepseek-r1-0528", messages=messages, stream=stream, extra_body={"chat_template_kwargs": {"enable_thinking": False}} # Overrides server default ) response: data: {"id":"chatcmpl-241d0a3723fb5324434b72851d0462ff","object":"chat.completion.chunk","created":1769419920,"model":"deepseek-r1-0528","choices":[{"index":0,"delta":{"reasoning_content":" multiple"},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-241d0a3723fb5324434b72851d0462ff","object":"chat.completion.chunk","created":1769419920,"model":"deepseek-r1-0528","choices":[{"index":0,"delta":{"reasoning_content":" possibilities"},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-241d0a3723fb5324434b72851d0462ff","object":"chat.completion.chunk","created":1769419920,"model":"deepseek-r1-0528","choices":[{"index":0,"delta":{"rea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t_template_kwargs usage;stale ### Your current environment ```text vLLM Version: 0.10.0 NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Can not disable the thinking mode of deepseek-r1-0528 with request-level chat_template_kwargs usage;stale ### Your current environment ```text vLLM Version: 0.10.0 NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITI...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: m, extra_body={"chat_template_kwargs": {"enable_thinking": False}} # Overrides server default ) response: data: {"id":"chatcmpl-241d0a3723fb5324434b72851d0462ff","object":"chat.completion.chunk","created":1769419920,"mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ``` request: completion = client.chat.completions.create( model="deepseek-r1-0528", messages=messages, stream=stream, extra_body={"chat_template_kwargs": {"enable_thinking": False}} # Overrides server default ) response...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
