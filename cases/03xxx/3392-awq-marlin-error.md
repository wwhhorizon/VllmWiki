# vllm-project/vllm#3392: AWQ + Marlin Error

| 字段 | 值 |
| --- | --- |
| Issue | [#3392](https://github.com/vllm-project/vllm/issues/3392) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;gemm_linear;model_support;quantization |
| 子分类 | debug |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AWQ + Marlin Error

### Issue 正文摘录

I convert model follow AutoAWQ library as follow script. 1. Quantize with Marlin ```python from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = 'mistralai/Mistral-7B-Instruct-v0.2' quant_path = 'mistral-instruct-v0.2-awq-marlin' quant_config = { "zero_point": False, "q_group_size": 128, "w_bit": 4, "version": "Marlin" } # Load model model = AutoAWQForCausalLM.from_pretrained( model_path, **{"low_cpu_mem_usage": True, "use_cache": False} ) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # Quantize model.quantize(tokenizer, quant_config=quant_config) # Save quantized model model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) print(f'Model is quantized and saved at "{quant_path}"') ``` 2. Generate ```python from awq import AutoAWQForCausalLM from transformers import AutoTokenizer, TextStreamer quant_path = "./mistral-instruct-v0.2-awq-marlin" # Load model model = AutoAWQForCausalLM.from_quantized(quant_path, fuse_layers=False) tokenizer = AutoTokenizer.from_pretrained(quant_path, trust_remote_code=True) streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True) # Convert prompt to to...

## 现有链接修复摘要

#3751 [Bugfix] Support AutoAWQ Models Serialized in Marlin Format

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: WQ library as follow script. 1. Quantize with Marlin ```python from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = 'mistralai/Mistral-7B-Instruct-v0.2' quant_path = 'mistral-instruct-v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: AWQ + Marlin Error I convert model follow AutoAWQ library as follow script. 1. Quantize with Marlin ```python from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = 'mistralai/Mistral-7B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: arlin Error I convert model follow AutoAWQ library as follow script. 1. Quantize with Marlin ```python from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = 'mistralai/Mistral-7B-Instruc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mpt_template.format(prompt=prompt), return_tensors='pt' ).input_ids.cuda() # Generate output generation_output = model.generate( tokens, streamer=streamer, max_new_tokens=512 ) ``` 2 steps above work perfectly. But when...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: th = 'mistral-instruct-v0.2-awq-marlin' quant_config = { "zero_point": False, "q_group_size": 128, "w_bit": 4, "version": "Marlin" } # Load model model = AutoAWQForCausalLM.from_pretrained( model_path, **{"low_cpu_mem_u...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3751](https://github.com/vllm-project/vllm/pull/3751) | closes_keyword | 0.95 | [Bugfix] Support AutoAWQ Models Serialized in Marlin Format | FIX #3392 ```python from vllm import LLM, SamplingParams quant_path = "hllj/mistral-instruct-v0.2-awq-marlin" # Load model model = LLM(quant_path) sampling_params = Sam |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
