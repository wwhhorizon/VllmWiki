# vllm-project/vllm#28163: [RFC]: SageMaker Day-0 Compatibility with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#28163](https://github.com/vllm-project/vllm/issues/28163) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: SageMaker Day-0 Compatibility with vLLM

### Issue 正文摘录

### Motivation. This RFC proposes establishing a standardized container interface that enables vLLM to work seamlessly with Amazon SageMaker without requiring customer intervention or container rebuilds. #### SageMaker Integration Requirements Enterprise customers deploying vLLM on Amazon SageMaker need: 1. Stateful Session Management: Support for SageMaker's session-based routing via custom headers (`X-Amzn-SageMaker-Session-Id`) to enable efficient KV cache reuse across requests 2. Dynamic Multi-LoRA Serving: Integration with SageMaker's adapter management protocol for loading/unloading LoRA adapters at runtime 3. Handler Customization: Ability to override or extend SageMaker-specific endpoints (`/ping`, `/invocations`) without modifying vLLM code 1. support pre/post processing through customized script and environment variables 2. support customized middleware through customized script and environment variables with more features to come ... #### Current State vLLM already has foundational SageMaker support: * An optional vllm-sagemaker Dockerfile target with SageMaker-specific entrypoint * Basic SageMaker APIs (`/ping`, `/invocations`) in the OpenAI server * Existing LoRA adap...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Amazon SageMaker without requiring customer intervention or container rebuilds. #### SageMaker Integration Requirements Enterprise customers deploying vLLM on Amazon SageMaker need: 1. Stateful Session Management: Suppo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nup) * No integration with SageMaker's Multi-LoRA adapter management API format * Limited extensibility for customers to customize handlers without forking vLLM ### Proposed Change. #### Overview The aim is to integrate...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: package developed by AWS that is published to PyPI. #### Opt-out Mechanism A new CLI flag `--disable-sagemaker-standards` allows users to disable the bootstrap component of the integration if needed. The default value i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: amic Multi-Adapter Inference uses a specific request format with adapter metadata in headers. vLLM Integration: ```python3 # vllm/entrypoints/dynamic_lora.py @sagemaker_standards.register_load_adapter_handler( request_s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: : 1. Stateful Session Management: Support for SageMaker's session-based routing via custom headers (`X-Amzn-SageMaker-Session-Id`) to enable efficient KV cache reuse across requests 2. Dynamic Multi-LoRA Serving: Integr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
