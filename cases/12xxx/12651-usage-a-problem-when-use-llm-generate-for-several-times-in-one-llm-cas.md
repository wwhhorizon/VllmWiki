# vllm-project/vllm#12651: [Usage]: A problem when use llm.generate() for several times in one LLM case

| 字段 | 值 |
| --- | --- |
| Issue | [#12651](https://github.com/vllm-project/vllm/issues/12651) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: A problem when use llm.generate() for several times in one LLM case

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I' m trying to test the performance of vllm so I need to test the time need for vllm when the input and output tokens numbers are fixed. Here I tried to run each situation for 20 times and get the average. But I got a problems that the answer returned after the first round become very strange(they are not nature language any more). It seems that the returns after the first round were interfered. What' s the problem here, what should I do to solve the problem? Thank! **### Here's my code:** ``` import time import os from vllm import LLM, SamplingParams import torch os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" os.environ["CUDA_VISIBLE_DEVICES"] = "3" prompt1 = """ """ prompt2 = """ """ prompt3 = """ """ prompt4 = """ """ prompt5 = """ """ prompt6 = """ """ prompt_list = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6] def count_tokens(text, tokenizer): input_ids = tokenizer.encode(text, add_special_tokens=False) return len(input_ids) def get_generation_time(prompts, required_tokens): sampling_params = SamplingParams(temperature=1, max_tokens=required_tokens, min_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: at should I do to solve the problem? Thank! **### Here's my code:** ``` import time import os from vllm import LLM, SamplingParams import torch os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" os.environ["CUDA_VISIBLE_DEV...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tokenizer): input_ids = tokenizer.encode(text, add_special_tokens=False) return len(input_ids) def get_generation_time(prompts, required_tokens): sampling_params = SamplingParams(temperature=1, max_tokens=required_token...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: import os from vllm import LLM, SamplingParams import torch os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" os.environ["CUDA_VISIBLE_DEVICES"] = "3" prompt1 = """ """ prompt2 = """ """ prompt3 = """ """ prompt4 = """ """...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 512] timing = [[0 for _ in range(6)] for _ in range(3)] llm = LLM( model = 'qwen2.5-3B/Qwen2.5-3B-Instruct', gpu_memory_utilization = 0.9, enable_prefix_caching = False, enforce_eager=True # # tensor_parallel_size=tenso...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: problem when use llm.generate() for several times in one LLM case usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I' m trying to test the per...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
