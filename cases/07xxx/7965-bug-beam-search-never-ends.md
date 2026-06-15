# vllm-project/vllm#7965: [Bug]: beam search never ends

| 字段 | 值 |
| --- | --- |
| Issue | [#7965](https://github.com/vllm-project/vllm/issues/7965) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: beam search never ends

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Generation with Beam Sampling never terminates. Sample code: ``` python from transformers import AutoTokenizer from vllm import LLM, SamplingParams repo_name = 'meta-llama/Meta-Llama-3.1-8B' llm = LLM(model=repo_name, tokenizer=repo_name, # quantization='awq', dtype="float16", gpu_memory_utilization=0.25, max_model_len=16000, max_num_seqs=1 ) print('llm:', llm) sampling_params = SamplingParams( max_tokens=10, use_beam_search=True, best_of=2, temperature=0.0, repetition_penalty=1.0, top_p=1.0, top_k=-1, early_stopping=True, stop=['###'], ) print('sampling_type:', sampling_params.sampling_type) text = "Hi" outputs = llm.generate([text], sampling_params) for output in outputs: generated_text = output.outputs[0].text print(generated_text) # print(generate_vLLM(text)) ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: m Sampling never terminates. Sample code: ``` python from transformers import AutoTokenizer from vllm import LLM, SamplingParams repo_name = 'meta-llama/Meta-Llama-3.1-8B' llm = LLM(model=repo_name, tokenizer=repo_name,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ' llm = LLM(model=repo_name, tokenizer=repo_name, # quantization='awq', dtype="float16", gpu_memory_utilization=0.25, max_model_len=16000, max_num_seqs=1 ) print('llm:', llm) sampling_params = SamplingParams(
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: beam search never ends bug;stale ### Your current environment ### 🐛 Describe the bug Generation with Beam Sampling never terminates. Sample code: ``` python from transformers import AutoTokenizer from vllm import...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rt AutoTokenizer from vllm import LLM, SamplingParams repo_name = 'meta-llama/Meta-Llama-3.1-8B' llm = LLM(model=repo_name, tokenizer=repo_name, # quantization='awq', dtype="float16", gpu_memory_utilization=0.25, max_mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: beam search never ends bug;stale ### Your current environment ### 🐛 Describe the bug Generation with Beam Sampling never terminates. Sample code: ``` python from transformers import AutoTokenizer from vllm import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
