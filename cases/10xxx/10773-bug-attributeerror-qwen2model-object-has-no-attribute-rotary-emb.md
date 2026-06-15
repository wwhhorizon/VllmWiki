# vllm-project/vllm#10773: [Bug]: AttributeError: 'Qwen2Model' object has no attribute 'rotary_emb'

| 字段 | 值 |
| --- | --- |
| Issue | [#10773](https://github.com/vllm-project/vllm/issues/10773) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen2Model' object has no attribute 'rotary_emb'

### Issue 正文摘录

### Your current environment ### Model Input Dumps from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = '/home/root123/workspace/model/qwen2-0-5/' quant_path = '/home/root123/workspace/model/qwen2-0-5-awq-4/' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } # Load model model = AutoAWQForCausalLM.from_pretrained( model_path, **{"low_cpu_mem_usage": True, "use_cache": False} ) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # Quantize model.quantize(tokenizer, quant_config=quant_config) # Save quantized model model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) print(f'Model is quantized at "{quant_path}"') ### 🐛 Describe the bug 在进行awq模型量化时报错 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AttributeError: 'Qwen2Model' object has no attribute 'rotary_emb' bug;stale ### Your current environment ### Model Input Dumps from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g;stale ### Your current environment ### Model Input Dumps from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = '/home/root123/workspace/model/qwen2-0-5/' quant_path = '/home/root123/wo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: AutoTokenizer model_path = '/home/root123/workspace/model/qwen2-0-5/' quant_path = '/home/root123/workspace/model/qwen2-0-5-awq-4/' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 时报错 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pretrained( model_path, **{"low_cpu_mem_usage": True, "use_cache": False} ) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # Quantize model.quantize(tokenizer, quant_config=quant_config) #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
