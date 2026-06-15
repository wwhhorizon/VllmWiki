# vllm-project/vllm#6989: [Usage]: internVL2 推理不支持

| 字段 | 值 |
| --- | --- |
| Issue | [#6989](https://github.com/vllm-project/vllm/issues/6989) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: internVL2 推理不支持

### Issue 正文摘录

### Your current environment 版本： vllm 0.5.3.post1 vllm-flash-attn 2.5.9.post1 代码： from vllm import LLM llm = LLM(model="OpenGVLab/InternVL2-8B", trust_remote_code=True) # Name or path of your model output = llm.generate("Hello, my name is") print(output) 报错 ValueError: Model architectures ['InternVLChatModel'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChameleonForCausalLM', 'ChameleonForConditionalGeneration', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'FalconForCausalLM', 'FuyuForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LlavaForConditionalGeneration', 'LlavaNextForConditionalGeneration', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'Or...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: internVL2 推理不支持 usage ### Your current environment 版本： vllm 0.5.3.post1 vllm-flash-attn 2.5.9.post1 代码： from vllm import LLM llm = LLM(model="OpenGVLab/InternVL2-8B", trus
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0.5.3.post1 vllm-flash-attn 2.5.9.post1 代码： from vllm import LLM llm = LLM(model="OpenGVLab/InternVL2-8B", trust_remote_code=True) # Name or path of your model output = llm.generate("Hello, my name is") print(output) 报错...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: = llm.generate("Hello, my name is") print(output) 报错 ValueError: Model architectures ['InternVLChatModel'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM',...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM', 'DeepseekV2ForCausalLM', 'FalconForCausalLM', 'FuyuForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'Pers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
