# vllm-project/vllm#17652: [Bug]: Degradation of Qwen/Qwen3-30B-A3B performance depending on batch size

| 字段 | 值 |
| --- | --- |
| Issue | [#17652](https://github.com/vllm-project/vllm/issues/17652) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Degradation of Qwen/Qwen3-30B-A3B performance depending on batch size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained( 'Qwen/Qwen3-30B-A3B' ) sampling_params = SamplingParams( temperature=0, max_tokens=16000, ) llm = LLM( model='Qwen/Qwen3-30B-A3B', gpu_memory_utilization=0.95, max_model_len=32000, max_num_seqs=50, tensor_parallel_size=1, ) input_prompts = [] for message in messages: prompt = tokenizer.apply_chat_template(message, add_generation_prompt=True, enable_thinking=False) input_prompts.append(prompt) output = llm.generate(input_prompts, self.sampling_params) ``` `input_prompts` contains `batch_size` prompts. The model performs well with `batch_size=1` or `10`, but output gets worse and unreadable if `batch_size = 50`. E.g. The LLM's output with `batch_size=50`: 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug ``` from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained( 'Qwen/Qwen3-30B-A3B' ) sampling_params = SamplingParams( temperature=0, max_tokens=1600...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Degradation of Qwen/Qwen3-30B-A3B performance depending on batch size bug;stale ### Your current environment ### 🐛 Describe the bug ``` from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ply_chat_template(message, add_generation_prompt=True, enable_thinking=False) input_prompts.append(prompt) output = llm.generate(input_prompts, self.sampling_params) ``` `input_prompts` contains `batch_size` prompts. Th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
