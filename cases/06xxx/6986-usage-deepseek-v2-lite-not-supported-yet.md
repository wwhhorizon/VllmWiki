# vllm-project/vllm#6986: [Usage]: deepseek-v2-lite  not supported yet?

| 字段 | 值 |
| --- | --- |
| Issue | [#6986](https://github.com/vllm-project/vllm/issues/6986) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: deepseek-v2-lite  not supported yet?

### Issue 正文摘录

### Your current environment docker: v0.5.0post1 model: DeepSeek-Coder-V2-Lite-Instruct, DeepSeek-V2-Lite-Chat/ which version support these models??? ### How would you like to use vllm 2024-07-31T17:09:32.375215459+08:00 [rank0]: ValueError: Model architectures ['DeepseekV2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LlavaForConditionalGeneration', 'LlavaNextForConditionalGeneration', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'Phi3ForCausalLM', 'QWenLMHeadModel', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'RWForCausalLM', 'StableLMEpochFor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: supported yet? usage ### Your current environment docker: v0.5.0post1 model: DeepSeek-Coder-V2-Lite-Instruct, DeepSeek-V2-Lite-Chat/ which version support these models??? ### How would you like to use vllm 2024-07-31T17...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: deepseek-v2-lite not supported yet? usage ### Your current environment docker: v0.5.0post1 model: DeepSeek-Coder-V2-Lite-Instruct, DeepSeek-V2-Lite-Chat/ which version support these models??? ### How would you like to u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: use vllm 2024-07-31T17:09:32.375215459+08:00 [rank0]: ValueError: Model architectures ['DeepseekV2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausal...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausal...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiF...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
