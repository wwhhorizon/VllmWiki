# vllm-project/vllm#1321: memory leak when running mistralai/Mistral-7B-Instruct-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#1321](https://github.com/vllm-project/vllm/issues/1321) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> memory leak when running mistralai/Mistral-7B-Instruct-v0.1

### Issue 正文摘录

I have an error suggesting memory leak when running ```llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=0.80, max_model_len=8000) sampling_params = SamplingParams(best_of=3, temperature=0.8, top_p=0.95, max_tokens=450, presence_penalty = 1.0, frequency_penalty=1.) outputs = llm.generate(prompts, sampling_params) ``` ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=415, ref_count=0) is already freed. Any suggestions on what to look into would be most appreciated!

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: LLM(model="mistralai/Mistral-7B-Instruct-v0.1", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=0.80, max_model_len=8000) sampling_params = SamplingParams(best_of=3, temperature=0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: already freed. Any suggestions on what to look into would be most appreciated!
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ate(prompts, sampling_params) ``` ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=415, ref_count=0) is already freed. Any suggestions on what to look into would be most appreciated!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .1 bug I have an error suggesting memory leak when running ```llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=0.80, max_model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
