# vllm-project/vllm#887: GPTQ support

| 字段 | 值 |
| --- | --- |
| Issue | [#887](https://github.com/vllm-project/vllm/issues/887) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPTQ support

### Issue 正文摘录

Can I run a model with GPTQ quantization like this one from hugging face? https://huggingface.co/TheBloke/CodeLlama-13B-oasst-sft-v10-GGUF ``` from transformers import AutoTokenizer, pipeline, logging from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig model_name_or_path = "TheBloke/Llama-2-13B-chat-GPTQ" model_basename = "model" use_triton = False tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True) model = AutoGPTQForCausalLM.from_quantized(model_name_or_path, model_basename=model_basename, use_safetensors=True, trust_remote_code=True, device="cuda:0", use_triton=use_triton, quantize_config=None) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: GPTQ support Can I run a model with GPTQ quantization like this one from hugging face? https://huggingface.co/TheBloke/CodeLlama-13B-oasst-sft-v10-GGUF ``` from transformers import AutoTokenizer, pipeline, logging from...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: or_path = "TheBloke/Llama-2-13B-chat-GPTQ" model_basename = "model" use_triton = False tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True) model = AutoGPTQForCausalLM.from_quantized(model_name_o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: face.co/TheBloke/CodeLlama-13B-oasst-sft-v10-GGUF ``` from transformers import AutoTokenizer, pipeline, logging from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig model_name_or_path = "TheBloke/Llama-2-13B-ch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: GPTQ support Can I run a model with GPTQ quantization like this one from hugging face? https://huggingface.co/TheBloke/CodeLlama-13B-oasst-sft-v10-GGUF ``` from transformers import AutoTokenizer, pipeline, logging from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: use_safetensors=True, trust_remote_code=True, device="cuda:0", use_triton=use_triton, quantize_config=None) ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
