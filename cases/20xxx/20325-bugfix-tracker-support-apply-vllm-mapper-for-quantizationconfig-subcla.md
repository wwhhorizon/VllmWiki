# vllm-project/vllm#20325: [Bugfix] [Tracker]: Support `apply_vllm_mapper` for `QuantizationConfig` subclasses

| 字段 | 值 |
| --- | --- |
| Issue | [#20325](https://github.com/vllm-project/vllm/issues/20325) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bugfix] [Tracker]: Support `apply_vllm_mapper` for `QuantizationConfig` subclasses

### Issue 正文摘录

It was noticed that many quantization configs do not account for `hf_to_vllm_mapper` when matching modules to quantize. #20046 introduced `QuantizationConfig.apply_vllm_mapper` which is an abstract method which should be implemented by subclasses. This issue tracks the implementation of these subclass methods - [ ] aqlm - [ ] deepspeedfp - [ ] gptq_bitblas - [ ] modelopt - [ ] qqq - [ ] auto_round - [ ] bitblas - [ ] experts_int8 - [ ] gptq_marlin_24 - [ ] ipex_quant - [ ] moe_wna16 - [ ] quark - [ ] awq_marlin - [ ] bitsandbytes - [ ] fbgemm_fp8 - [ ] gptq_marlin - [ ] neuron_quant - [ ] awq - [x] compressed_tensors - [x] fp8 - [ ] gptq - [ ] ptpc_fp8 - [ ] torchao - [ ] awq_triton - [ ] deepgemm - [ ] gguf - [ ] hqq_marlin - [ ] marlin - [ ] tpu_int8 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bugfix] [Tracker]: Support `apply_vllm_mapper` for `QuantizationConfig` subclasses feature request;stale It was noticed that many quantization configs do not account for `hf_to_vllm_mapper` when matching modules to qua...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: tq_bitblas - [ ] modelopt - [ ] qqq - [ ] auto_round - [ ] bitblas - [ ] experts_int8 - [ ] gptq_marlin_24 - [ ] ipex_quant - [ ] moe_wna16 - [ ] quark - [ ] awq_marlin - [ ] bitsandbytes - [ ] fbgemm_fp8 - [ ] gptq_mar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bugfix] [Tracker]: Support `apply_vllm_mapper` for `QuantizationConfig` subclasses feature request;stale It was noticed that many quantization configs do not account for `hf_to_vllm_mapper` when matching modules to qua...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Support `apply_vllm_mapper` for `QuantizationConfig` subclasses feature request;stale It was noticed that many quantization configs do not account for `hf_to_vllm_mapper` when matching modules to quantize. #20046 introd...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ssed_tensors - [x] fp8 - [ ] gptq - [ ] ptpc_fp8 - [ ] torchao - [ ] awq_triton - [ ] deepgemm - [ ] gguf - [ ] hqq_marlin - [ ] marlin - [ ] tpu_int8 ### Alternatives _No response_ ### Additional context _No response_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
