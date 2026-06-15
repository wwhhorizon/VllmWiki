# vllm-project/vllm#8972: [New Model]: Add support for Ovis models

| 字段 | 值 |
| --- | --- |
| Issue | [#8972](https://github.com/vllm-project/vllm/issues/8972) |
| 状态 | closed |
| 标签 | new-model;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Add support for Ovis models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I wanted to try the model AIDC-AI/Ovis1.6-Gemma2-9B but I´m getting the error "Model architectures ['Ovis'] are not supported for now". Is it planned for the future or is there some workaround? ### Alternatives _No response_ ### Additional context The full error that I´m getting is: ValueError: Model architectures ['Ovis'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMM odel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCau salLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LLaM AForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalL M', 'OlmoeForCausalLM', 'OPTForCausalLM', 'Orio...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Add support for Ovis models new-model;unstale ### 🚀 The feature, motivation and pitch Hi, I wanted to try the model AIDC-AI/Ovis1.6-Gemma2-9B but I´m getting the error "Model architectures ['Ovis'] are not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: try the model AIDC-AI/Ovis1.6-Gemma2-9B but I´m getting the error "Model architectures ['Ovis'] are not supported for now". Is it planned for the future or is there some workaround? ### Alternatives _No response_ ### Ad...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ure, motivation and pitch Hi, I wanted to try the model AIDC-AI/Ovis1.6-Gemma2-9B but I´m getting the error "Model architectures ['Ovis'] are not supported for now". Is it planned for the future or is there some workaro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCau salLM', 'Gemma2ForCausalL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: AForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalL M', 'OlmoeFor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
