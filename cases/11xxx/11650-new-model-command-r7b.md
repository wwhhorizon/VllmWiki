# vllm-project/vllm#11650: [New Model]: command-r7b

| 字段 | 值 |
| --- | --- |
| Issue | [#11650](https://github.com/vllm-project/vllm/issues/11650) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: command-r7b

### Issue 正文摘录

### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-r7b-12-2024 ### The closest model vllm already supports. I don‘t know，but i had installe the newest transformers and newest vllm,and I had to see the history of Cohere2ForCausalLM,but it still error after i tried again ### What's your difficulty of supporting the model you want? ValueError: Model architectures ['CohereForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHeadModel', 'Qwen2ForCausalLM', 'RWForCausalLM', 'StableLMEpochForCausalLM', 'StableLmForCausalLM', 'Starcoder2ForCausalLM'] ### Before su...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [New Model]: command-r7b new-model ### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-r7b-12-2024 ### The closest model vllm already supports. I don‘t know，but i had installe the newest transform...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 24 ### The closest model vllm already supports. I don‘t know，but i had installe the newest transformers and newest vllm,and I had to see the history of Cohere2ForCausalLM,but it still error after i tried again ### What'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: salLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t's your difficulty of supporting the model you want? ValueError: Model architectures ['CohereForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM',...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCaus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
