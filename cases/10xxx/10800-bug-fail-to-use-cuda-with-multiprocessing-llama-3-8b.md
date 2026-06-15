# vllm-project/vllm#10800: [Bug]: Fail to use CUDA with multiprocessing (llama_3_8b)

| 字段 | 值 |
| --- | --- |
| Issue | [#10800](https://github.com/vllm-project/vllm/issues/10800) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to use CUDA with multiprocessing (llama_3_8b)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I load LLM as: `llm = LLM( model= model_id, tokenizer= model_id, download_dir = cache_dir, dtype='half', tensor_parallel_size = 2, gpu_memory_utilization=0.75, enable_lora = False)` I get error as `RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method` I tried loading llama_3_8b using huggingface, llm generation can be completed using 2 GPU, I just try vllm to speed up the generation process. Can anyone help me with this error? Thanks a lot! Best, Yi Nov 30th, 2024 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Fail to use CUDA with multiprocessing (llama_3_8b) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I load LLM as: `llm = LLM( model= model_id, tokenizer= mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Fail to use CUDA with multiprocessing (llama_3_8b) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I load LLM as: `llm = LLM( model= model_id, tokenizer=
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y asked questions. performance frontend_api;model_support cuda dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , tokenizer= model_id, download_dir = cache_dir, dtype='half', tensor_parallel_size = 2, gpu_memory_utilization=0.75, enable_lora = False)` I get error as `RuntimeError: Cannot re-initialize CUDA in forked subprocess. T...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: l_size = 2, gpu_memory_utilization=0.75, enable_lora = False)` I get error as `RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method` I tri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
