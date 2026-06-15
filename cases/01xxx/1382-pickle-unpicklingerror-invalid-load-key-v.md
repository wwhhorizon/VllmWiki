# vllm-project/vllm#1382: _pickle.UnpicklingError: invalid load key, 'v'.

| 字段 | 值 |
| --- | --- |
| Issue | [#1382](https://github.com/vllm-project/vllm/issues/1382) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> _pickle.UnpicklingError: invalid load key, 'v'.

### Issue 正文摘录

Hello team, i am trying to use vllm to inference Llama2-70b-chat-hf on 8 *v100 (32G, 4 nodes ,each node with 2 gpu) . The model was manually downloaded from huggingface , and saved to /mnt/share_dir/models/Llama-2-70b-chat-hf which is a shared directory across 4 nodes `vllm: 0.2.0` And i encountered the error Here are the code ```python from vllm import LLM,SamplingParams num_gpus=8 llm = LLM("/mnt/share_dir/models/Llama-2-70b-chat-hf", tensor_parallel_size=num_gpus,load_format="pt") sampling_params = SamplingParams(temperature=0.8, top_p=0.95) system_prompt="You are a helpful assistant. " query= "Hello" template1 = f""" >{system_prompt} >\n\n [INST] {query} [INST] """ outputs = llm.generate([template1],sampling_params) # Print the outputs. print(outputs) ``` ``` 2023-10-16 21:31:12,187 INFO worker.py:1458 -- Connecting to existing Ray cluster at address: xxx.xxx.xxx.xxx:6379... 2023-10-16 21:31:12,195 INFO worker.py:1642 -- Connected to Ray cluster. INFO 10-16 21:31:12 llm_engine.py:72] Initializing an LLM engine with config: model='/mnt/share_dir/models/Llama-2-70b-chat-hf', tokenizer='/mnt/share_dir/models/Llama-2-70b-chat-hf', tokenizer_mode=auto, revision=None, trust_remote_c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: invalid load key, 'v'. Hello team, i am trying to use vllm to inference Llama2-70b-chat-hf on 8 *v100 (32G, 4 nodes ,each node with 2 gpu) . The model was manually downloaded from huggingface , and saved to /mnt/share_d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: b-chat-hf', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=8, quantization=None, seed=0) INFO 10-16 21:31:12...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: And i encountered the error Here are the code ```python from vllm import LLM,SamplingParams num_gpus=8 llm = LLM("/mnt/share_dir/models/Llama-2-70b-chat-hf", tensor_parallel_size=num_gpus,load_format="pt") sampling_para...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -2-70b-chat-hf', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=8, quantization=None, seed=0) INFO 10-16 21:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ong time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Traceback (most recent call last): File "/mnt/share_dir/code/inference/distributed/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
