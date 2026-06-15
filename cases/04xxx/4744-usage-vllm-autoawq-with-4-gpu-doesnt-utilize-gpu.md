# vllm-project/vllm#4744: [Usage]: Vllm AutoAWQ with 4-GPU doesnt utilize GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#4744](https://github.com/vllm-project/vllm/issues/4744) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Vllm AutoAWQ with 4-GPU doesnt utilize GPU

### Issue 正文摘录

### Your current environment ... ### How would you like to use vllm I have downloaded a model. Now on my 4 GPU instance I attempt to quantize it using AutoAWQ. Whenever I run the script below I get 0% GPU utilization. Can anyone assist why can this be happening? ```py import json from huggingface_hub import snapshot_download from awq import AutoAWQForCausalLM from transformers import AutoTokenizer import os # some other code here # //////////////// # some code here # Load model model = AutoAWQForCausalLM.from_pretrained(args.model_path, device_map="auto", **{"low_cpu_mem_usage": True}) tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True) # Load quantization config from file if args.quant_config: quant_config = json.loads(args.config) else: # Default quantization config print("Using default quantization config") quant_config = {"zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM"} # Quantize print("Quantizing the model") model.quantize(tokenizer, quant_config=quant_config) # Save quantized model and tokenizer if args.quant_path: print("Saving the model") model.save_quantized(args.quant_path) tokenizer.save_pretrained(args.quant_path)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nvironment ... ### How would you like to use vllm I have downloaded a model. Now on my 4 GPU instance I attempt to quantize it using AutoAWQ. Whenever I run the script below I get 0% GPU utilization. Can anyone assist w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 0% GPU utilization. Can anyone assist why can this be happening? ```py import json from huggingface_hub import snapshot_download from awq import AutoAWQForCausalLM from transformers import AutoTokenizer import os # some...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e vllm I have downloaded a model. Now on my 4 GPU instance I attempt to quantize it using AutoAWQ. Whenever I run the script below I get 0% GPU utilization. Can anyone assist why can this be happening? ```py import json...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: m file if args.quant_config: quant_config = json.loads(args.config) else: # Default quantization config print("Using default quantization config") quant_config = {"zero_point": True, "q_group_size": 128, "w_bit": 4, "ve...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nfig = {"zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM"} # Quantize print("Quantizing the model") model.quantize(tokenizer, quant_config=quant_config) # Save quantized model and tokenizer if args....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
