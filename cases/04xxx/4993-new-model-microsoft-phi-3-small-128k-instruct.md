# vllm-project/vllm#4993: [New Model]: microsoft/Phi-3-small-128k-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#4993](https://github.com/vllm-project/vllm/issues/4993) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: microsoft/Phi-3-small-128k-instruct

### Issue 正文摘录

### The model to consider. https://huggingface.co/microsoft/Phi-3-small-128k-instruct ### The closest model vllm already supports. Phi3ForCausalLM ### What's your difficulty of supporting the model you want? (RayWorkerWrapper pid=46639) ERROR 05-23 00:00:58 worker_base.py:145] ValueError: Model architectures ['Phi3SmallForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LlavaForConditionalGeneration', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'Phi3ForCausalLM', 'QWenLMHeadModel', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'RWForCausalLM', 'Stable...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [New Model]: microsoft/Phi-3-small-128k-instruct new-model ### The model to consider. https://huggingface.co/microsoft/Phi-3-small-128k-instruct ### The closest model vllm already supports. Phi3ForCausalLM ### What's yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [New Model]: microsoft/Phi-3-small-128k-instruct new-model ### The model to consider. https://huggingface.co/microsoft/Phi-3-small-128k-instruct ### The closest model vllm already supports. Phi3ForCausalLM ### What's yo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', '...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiF...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
