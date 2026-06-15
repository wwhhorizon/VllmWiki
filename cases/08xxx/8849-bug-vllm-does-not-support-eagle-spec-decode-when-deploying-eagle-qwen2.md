# vllm-project/vllm#8849: [Bug]: VLLM does not support EAGLE Spec Decode when deploying EAGLE-Qwen2-7B-Instruct model 

| 字段 | 值 |
| --- | --- |
| Issue | [#8849](https://github.com/vllm-project/vllm/issues/8849) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM does not support EAGLE Spec Decode when deploying EAGLE-Qwen2-7B-Instruct model 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can successfully deploy llama3-8b-instruct with EAGLE. But there is a problem when deploying qwen2-7b-instruct with EAGLE. I have converted the EAGLE-Qwen2-7B-Instruct model according to[[vllm/model_executor/models/eagle.py:L126](https://github.com/vllm-project/vllm/blob/8fae5ed7f6bfd63b81310fcb24b310d9205c9687/vllm/model_executor/models/eagle.py#L126)](https://github.com/vllm-project/vllm/blob/8fae5ed7f6bfd63b81310fcb24b310d9205c9687/vllm/model_executor/models/eagle.py#L126). I tried the python code below ``` llm = LLM( model="/models/Qwen2-7B-Instruct", dtype='bfloat16', tensor_parallel_size=4, speculative_model="/models/EAGLE-Qwen2-7B-Instruct-vllm", speculative_draft_tensor_parallel_size=1, num_speculative_tokens=1, use_v2_block_manager=True, ) ``` I encountered another error below: `AssertionError: Attempted to load weight (torch.Size([3584])) into parameter (torch.Size([3584, 7168]))` I lookup to the code [[vllm/model_executor/models/eagle.py:L139](https://github.com/vllm-project/vllm/blob/8fae5ed7f6bfd63b81310fcb24b310d9205c9687/vllm/model_executor/models/eagle.py#L139)](https://github...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: VLLM does not support EAGLE Spec Decode when deploying EAGLE-Qwen2-7B-Instruct model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can successfully deploy llama3-8b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: hon code below ``` llm = LLM( model="/models/Qwen2-7B-Instruct", dtype='bfloat16', tensor_parallel_size=4, speculative_model="/models/EAGLE-Qwen2-7B-Instruct-vllm", speculative_draft_tensor_parallel_size=1, num_speculat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: VLLM does not support EAGLE Spec Decode when deploying EAGLE-Qwen2-7B-Instruct model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can successfully deploy llama3-8b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: de! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
