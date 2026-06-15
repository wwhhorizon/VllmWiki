# vllm-project/vllm#2339: awq compression of llama 2 70b chat got bad result

| 字段 | 值 |
| --- | --- |
| Issue | [#2339](https://github.com/vllm-project/vllm/issues/2339) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> awq compression of llama 2 70b chat got bad result

### Issue 正文摘录

I use awq to quantize llama 2 70b-chat by: ``` CUDA_VISIBLE_DEVICES="1,2,3,4,5,6,7" python quantize_llama.py ``` the codes of quantize_llama.py： ``` from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = '/nas/lili/models_hf/70B-chat' quant_path = '/nas/lili/models_hf/70B-chat-awq' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } # Load model model = AutoAWQForCausalLM.from_pretrained(model_path, **{ "low_cpu_mem_usage": True, "device_map": "auto" }) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) # Quantize model.quantize(tokenizer, quant_config=quant_config) # Save quantized model model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) ``` And I serve it with: ``` CUDA_VISIBLE_DEVICES=0,1 python api_server.py --model /nas/lili/models_hf/70B-chat-awq/ --port 8005 --tensor-parallel-size=2 ``` In my test data, orginal llama 2 70b-chat got 0.581 accuracy. But awq compressed model only got 0.094. What's wrong? my system info: autoawq 0.1.8 transformers 4.36.1 torch 2.1.2

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: awq compression of llama 2 70b chat got bad result stale I use awq to quantize llama 2 70b-chat by: ``` CUDA_VISIBLE_DEVICES="1,2,3,4,5,6,7" python quantize_llama.py ``` the codes of quantize_llama.py： ``` from awq impo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: thon quantize_llama.py ``` the codes of quantize_llama.py： ``` from awq import AutoAWQForCausalLM from transformers import AutoTokenizer model_path = '/nas/lili/models_hf/70B-chat' quant_path = '/nas/lili/models_hf/70B-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: models_hf/70B-chat-awq/ --port 8005 --tensor-parallel-size=2 ``` In my test data, orginal llama 2 70b-chat got 0.581 accuracy. But awq compressed model only got 0.094. What's wrong? my system info: autoawq 0.1.8 transfo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: parallel-size=2 ``` In my test data, orginal llama 2 70b-chat got 0.581 accuracy. But awq compressed model only got 0.094. What's wrong? my system info: autoawq 0.1.8 transformers 4.36.1 torch 2.1.2
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: awq compression of llama 2 70b chat got bad result stale I use awq to quantize llama 2 70b-chat by: ``` CUDA_VISIBLE_DEVICES="1,2,3,4,5,6,7" python quantize_llama.py ``` the codes of quantize_llama.py： ``` from awq impo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
