# vllm-project/vllm#3886: [Bug]: Error When Using quantized Jais on Specific Layers with vLLM (GPTQ is used for quantization)

| 字段 | 值 |
| --- | --- |
| Issue | [#3886](https://github.com/vllm-project/vllm/issues/3886) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error When Using quantized Jais on Specific Layers with vLLM (GPTQ is used for quantization)

### Issue 正文摘录

### Your current environment Hello everyone, I need some help here, please. I tried to quantize the JAIS model using GPTQ. Here is my code: ``` from auto_gptq.modeling._base import BaseGPTQForCausalLM from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig import auto_gptq from transformers import AutoModel, AutoTokenizer # define model auto_gptq.modeling._base.SUPPORTED_MODELS = ["jais"] class JAISLMHeadModelGPTQ(BaseGPTQForCausalLM): layer_type = "JAISBlock" layers_block_name = "transformer.h" outside_layer_modules = ["transformer.ln_f", "transformer.relative_pe", "transformer.wte"] inside_layer_modules = [ ["attn.c_attn"], # ["attn.c_proj"], # ["mlp.c_fc", "mlp.c_fc2"], # ["mlp.c_proj"], ] quantized_model_dir = "/sdb-disk/LlmsModels/jais-13b-chat-4bit" # load quantized model to the first GPU tokenizer = AutoTokenizer.from_pretrained(quantized_model_dir, use_fast=True, trust_remote_code=True) model = JAISLMHeadModelGPTQ.from_quantized(quantized_model_dir, device="cuda:0", trust_remote_code=True, ) # download quantized model from Hugging Face Hub and load to the first GPU # model = AutoGPTQForCausalLM.from_quantized(repo_id, device="cuda:0", use_safetensors=True, use_triton...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: lo everyone, I need some help here, please. I tried to quantize the JAIS model using GPTQ. Here is my code: ``` from auto_gptq.modeling._base import BaseGPTQForCausalLM from auto_gptq import AutoGPTQForCausalLM, BaseQua...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Error When Using quantized Jais on Specific Layers with vLLM (GPTQ is used for quantization) bug;stale ### Your current environment Hello everyone, I need some help here, please. I tried to quantize the JAIS mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Error When Using quantized Jais on Specific Layers with vLLM (GPTQ is used for quantization) bug;stale ### Your current environment Hello everyone, I need some help here, please. I tried to quantize the JAIS mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ["mlp.c_proj"], ] quantized_model_dir = "/sdb-disk/LlmsModels/jais-13b-chat-4bit" # load quantized model to the first GPU tokenizer = AutoTokenizer.from_pretrained(quantized_model_dir, use_fast=True, trust_remote_code=T...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: class JAISLMHeadModelGPTQ(BaseGPTQForCausalLM): layer_type = "JAISBlock" layers_block_name = "transformer.h" outside_layer_modules = ["transformer.ln_f", "transformer.relative_pe", "transformer.wte"] inside_layer_module...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
