# vllm-project/vllm#11011: [Bug]: Qwen2ForSequenceClassification does not work.

| 字段 | 值 |
| --- | --- |
| Issue | [#11011](https://github.com/vllm-project/vllm/issues/11011) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2ForSequenceClassification does not work.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to run the following example code for the embedding generation (Sequence Classification) with vllm=v0.6.4.post1, ``` python from vllm import LLM # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create an LLM. model = LLM(model="jason9693/Qwen2.5-1.5B-apeach") # Generate embedding. The output is a list of PoolingRequestOutputs. outputs = model.encode(prompts) # Print the outputs. for output in outputs: print(output.outputs.embedding) # list of 4096 floats ``` The error occurs. I have tested on multiple devices, they show the same error message: ``` aiscuser@node-0:~$ ./.conda/envs/vllm/bin/python /home/aiscuser/vllm_test.py config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 950/950 [00:00 32K. Currently, chunked prefill might not work with some features or models. If you encounter any issues, please disable chunked prefill by...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n (Sequence Classification) with vllm=v0.6.4.post1, ``` python from vllm import LLM # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: es, please disable chunked prefill by setting --enable-chunked-prefill=False. INFO 12-09 08:55:21 config.py:1136] Chunked prefill is enabled with max_num_batched_tokens=32768. INFO 12-09 08:55:21 llm_engine.py:249] Init...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2ForSequenceClassification does not work. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to run the following example code for the embedding generati
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: en2.5-1.5B-apeach") # Generate embedding. The output is a list of PoolingRequestOutputs. outputs = model.encode(prompts) # Print the outputs. for output in outputs: print(output.outputs.embedding) # list of 4096 floats...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
