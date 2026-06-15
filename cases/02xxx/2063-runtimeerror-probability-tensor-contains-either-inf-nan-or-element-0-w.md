# vllm-project/vllm#2063: RuntimeError: probability tensor contains either inf, nan or element < 0, when using Falcon 7B with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#2063](https://github.com/vllm-project/vllm/issues/2063) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: probability tensor contains either inf, nan or element < 0, when using Falcon 7B with vLLM

### Issue 正文摘录

Hi, I'm looking to quantize Falcon-instruct models with AutoAWQ and serve them with vLLM. Below are my package versions and my e2e code snippet. AutoAWQ version: 0.1.7 vLLM version: 0.2.3 ``` # Generate quantized model from awq import AutoAWQForCausalLM from transformers import AutoTokenizer pretrained_model_id="tiiuae/falcon-7b-instruct" model = AutoAWQForCausalLM.from_pretrained( model_path=pretrained_model_id, trust_remote_code=True, device_map="cpu", low_cpu_mem_usage=True, ) tokenizer = AutoTokenizer.from_pretrained( pretrained_model_id, trust_remote_code=True ) quant_config = { "zero_point": True, "q_group_size": 64, "w_bit": 4, "version": "GEMM", } model.quantize( tokenizer, quant_config=quant_config, calib_data="pileval", text_column="text", ) quant_path = "/tmp/model" model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) # VLLM from vllm import LLM, SamplingParams prompts = [ "What is a car?", ] sampling_params = SamplingParams(temperature=0, max_tokens=300) llm = LLM(model=quant_path, trust_remote_code=True, tensor_parallel_size=1) outputs = llm.generate(prompts, sampling_params) ``` This results in the following stack trace upon trying to initialize the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: truct models with AutoAWQ and serve them with vLLM. Below are my package versions and my e2e code snippet. AutoAWQ version: 0.1.7 vLLM version: 0.2.3 ``` # Generate quantized model from awq import AutoAWQForCausalLM fro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: te-packages/vllm/engine/llm_engine.py", line 208, in _init_cache num_blocks = self._run_workers( ^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 750, in _run_workers sel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n using Falcon 7B with vLLM Hi, I'm looking to quantize Falcon-instruct models with AutoAWQ and serve them with vLLM. Below are my package versions and my e2e code snippet. AutoAWQ version: 0.1.7 vLLM version: 0.2.3 ```...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: antize( tokenizer, quant_config=quant_config, calib_data="pileval", text_column="text", ) quant_path = "/tmp/model" model.save_quantized(quant_path) tokenizer.save_pretrained(quant_path) # VLLM from vllm import LLM, Sam...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , nan or element < 0, when using Falcon 7B with vLLM Hi, I'm looking to quantize Falcon-instruct models with AutoAWQ and serve them with vLLM. Below are my package versions and my e2e code snippet. AutoAWQ version: 0.1....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
