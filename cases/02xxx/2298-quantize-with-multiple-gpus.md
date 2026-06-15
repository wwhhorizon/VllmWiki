# vllm-project/vllm#2298: quantize with multiple gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#2298](https://github.com/vllm-project/vllm/issues/2298) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> quantize with multiple gpus

### Issue 正文摘录

I want to quantize my fine-tuned llama 2 70b model with awq. I follow the [doc](https://docs.vllm.ai/en/latest/quantization/auto_awq.html) ``` from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = '/nas/lili/models_hf/ft-70B-chat' quant_path = '/nas/lili/models_hf/ft-70B-chat-awq' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } # Load model model = AutoAWQForCausalLM.from_pretrained(model_path, **{"low_cpu_mem_usage": True}) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # Quantize model.quantize(tokenizer, quant_config=quant_config) # Save quantized model model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) ``` I run it in a 8xA100 40GB node. It only use gpu:0 and oom. Can I use multiple gpus to quantize my model. The error messages: ``` Traceback (most recent call last): File "/nas/lili/codes/vllmtest/quantize_llama.py", line 13, in model.quantize(tokenizer, quant_config=quant_config) File "/home/ubuntu/miniconda3/envs/py39_torch21/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: quantize with multiple gpus I want to quantize my fine-tuned llama 2 70b model with awq. I follow the [doc](https://docs.vllm.ai/en/latest/quantization/auto_awq.html) ``` from awq import AutoAWQForCausalLM from transfor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: https://docs.vllm.ai/en/latest/quantization/auto_awq.html) ``` from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = '/nas/lili/models_hf/ft-70B-chat' quant_path = '/nas/lili/models_hf/f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d(quant_path) tokenizer.save_pretrained(quant_path) ``` I run it in a 8xA100 40GB node. It only use gpu:0 and oom. Can I use multiple gpus to quantize my model. The error messages: ``` Traceback (most recent call last):...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: quantize with multiple gpus I want to quantize my fine-tuned llama 2 70b model with awq. I follow the [doc](https://docs.vllm.ai/en/latest/quantization/auto_awq.html) ``` from awq import AutoAWQForCausalLM from transfor
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: d(quant_path) ``` I run it in a 8xA100 40GB node. It only use gpu:0 and oom. Can I use multiple gpus to quantize my model. The error messages: ``` Traceback (most recent call last): File "/nas/lili/codes/vllmtest/quanti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
