# vllm-project/vllm#2176: Quantizing 'lmsys/vicuna-7b-v1.5' model (vllm  AutoAWQ example code)  giving cuda error

| 字段 | 值 |
| --- | --- |
| Issue | [#2176](https://github.com/vllm-project/vllm/issues/2176) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Quantizing 'lmsys/vicuna-7b-v1.5' model (vllm  AutoAWQ example code)  giving cuda error

### Issue 正文摘录

The example code for Quantizing on vllm documentation was working before few days, but now same code on same machine giving cuda error. ## CODE : ``` from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = 'lmsys/vicuna-7b-v1.5' quant_path = 'vicuna-7b-v1.5-awq' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } # Load model model = AutoAWQForCausalLM.from_pretrained(model_path, **{"low_cpu_mem_usage": True}) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # Quantize model.quantize(tokenizer, quant_config=quant_config) # Save quantized model model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) ``` ## MACHINE CONFIG(GPU) : AWS sagemaker ml.g5.8xlarge NVIDIA A10G ## ERROR OUTPUT: ---> 1 model.quantize(tokenizer, quant_config=quant_config) File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/torch/utils/_contextlib.py:115, in context_decorator. .decorate_context(*args, **kwargs) 112 @functools.wraps(func) 113 def decorate_context(*args, **kwargs): 114 with ctx_factory(): --> 115 return func(*args, **kwargs) File ~/anaconda3/envs/pytorch_p310/lib/python3.10/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: now same code on same machine giving cuda error. ## CODE : ``` from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = 'lmsys/vicuna-7b-v1.5' quant_path = 'vicuna-7b-v1.5-awq' quant_config...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Quantizing 'lmsys/vicuna-7b-v1.5' model (vllm AutoAWQ example code) giving cuda error The example code for Quantizing on vllm documentation was working before few days, but now same code on same machine giving cuda erro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Quantizing 'lmsys/vicuna-7b-v1.5' model (vllm AutoAWQ example code) giving cuda error The example code for Quantizing on vllm documentation was working before few days, but now same code on same machine giving cuda err
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tizing 'lmsys/vicuna-7b-v1.5' model (vllm AutoAWQ example code) giving cuda error The example code for Quantizing on vllm documentation was working before few days, but now same code on same machine giving cuda error. #...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: inear;model_support;quantization;scheduler_memory cuda;gemm;quantization oom env_dependency;shape The example code for Quantizing on vllm documentation was working before few days, but now same code on same machine givi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
