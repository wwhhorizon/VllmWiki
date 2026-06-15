# vllm-project/vllm#30136: [RFC]: Deprecate Legacy Quantization Formats

| 字段 | 值 |
| --- | --- |
| Issue | [#30136](https://github.com/vllm-project/vllm/issues/30136) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecate Legacy Quantization Formats

### Issue 正文摘录

### Motivation. * vLLM supports a large variety of quantization formats. This is hard to maintain and makes the codebase complex * Many mature frameworks (`llm-compressor`, `modelopt`, `quark`, `torchao`) have emerged which are general purpose implementations of various quantization schemes * we have limited usage of older formats per usage stats ### Proposed Change. * deprecate many of the legacy formats Kept: - compressed-tensors - quark - awq.py (to be deprecated later, too many models exist though --- autoawq no longer maintained) - bitsandbytes.py - fp8.py - inc.py (all of auto_round consolidated here) # <<< UPDATED - quark - mxfp4.py - modelopt.py - gguf.py - gptq.py (to be deprecated later, too many models exists though) --- autogptq no longer maintained) - torchao.py Proposed to be removed (per usage stats): - auto_round - awq_marlin (consolidate to awq.py) - awq_triton (consolidate to awq.py) - bitblas.py - cpu_wna16.py - deepseepfp8.py - experts_int8.py - fbgemm_fp8.py - fp_quant.py - gptq_bitblas.py - gptq_marlin.py (consolidate to gptq.py) - gptq_marlin_24.py - hqq_marlin.py - input_quant_fp8.py - ipex_quant.py - moe_wna16.py - petit.py - ptpc_fp8.py - rtn.py - tpu_int...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: Deprecate Legacy Quantization Formats RFC ### Motivation. * vLLM supports a large variety of quantization formats. This is hard to maintain and makes the codebase complex * Many mature frameworks (`llm-compressor...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: n (consolidate to awq.py) - bitblas.py - cpu_wna16.py - deepseepfp8.py - experts_int8.py - fbgemm_fp8.py - fp_quant.py - gptq_bitblas.py - gptq_marlin.py (consolidate to gptq.py) - gptq_marlin_24.py - hqq_marlin.py - in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Deprecate Legacy Quantization Formats RFC ### Motivation. * vLLM supports a large variety of quantization formats. This is hard to maintain and makes the codebase complex * Many mature frameworks (`llm-compressor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: er usage stats): - auto_round - awq_marlin (consolidate to awq.py) - awq_triton (consolidate to awq.py) - bitblas.py - cpu_wna16.py - deepseepfp8.py - experts_int8.py - fbgemm_fp8.py - fp_quant.py - gptq_bitblas.py - gp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
