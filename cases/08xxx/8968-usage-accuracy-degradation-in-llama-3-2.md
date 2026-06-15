# vllm-project/vllm#8968: [Usage]: accuracy degradation in llama 3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#8968](https://github.com/vllm-project/vllm/issues/8968) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: accuracy degradation in llama 3.2

### Issue 正文摘录

Hello, I loaded `llama3.2-3b-instruct` on VLLM and observed a significant decrease in accuracy compared to when I run the model using Hugging Face Transformers. This issue also persists with the fine-tuned model. I'm including sample code and outputs to illustrate the problem. ## When using VLLM for inference: ```python from vllm import LLM, SamplingParams model_id = "meta-llama/Llama-3.2-3B-Instruct" llm = LLM(model=model_id, enforce_eager=True, device='cuda', gpu_memory_utilization=0.95) config = SamplingParams(**{'max_tokens': 512}) out = llm.generate( prompts=["Write a Python function that implements the binary search algorithm on a sorted list."], sampling_params=config ) for o in out: generated_text = o.outputs[0].text print(generated_text) ``` ### Output: ``` Finds the smallest fixpoint in a minimal near-future prediction scenario. ## Binary Search Implementation python def binary_search(sorted_list, target): """ Performs a binary search on a sorted list to find the smallest fixpoint. Args: sorted_list (list): A sorted list of integers. target (int): The target value to find. Returns: int: The smallest fixpoint in the list if found, otherwise -1. """ low = 0 high = len(sort...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ate the problem. ## When using VLLM for inference: ```python from vllm import LLM, SamplingParams model_id = "meta-llama/Llama-3.2-3B-Instruct" llm = LLM(model=model_id, enforce_eager=True, device='cuda', gpu_memory_uti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: a-3.2-3B-Instruct" llm = LLM(model=model_id, enforce_eager=True, device='cuda', gpu_memory_utilization=0.95) config = SamplingParams(**{'max_tokens': 512}) out = llm.generate( prompts=["Write a Python function that impl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: accuracy degradation in llama 3.2 usage Hello, I loaded `llama3.2-3b-instruct` on VLLM and observed a significant decrease in accuracy compared to when I run the model using Hugging Face Transformers. This issu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _pretrained(model_id, torch_dtype=torch.bfloat16, device_map='auto') tokenizer = AutoTokenizer.from_pretrained(model_id) input_ids = get_input_ids("Write a Python function that implements the binary sea
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: accuracy degradation in llama 3.2 usage Hello, I loaded `llama3.2-3b-instruct` on VLLM and observed a significant decrease in accuracy compared to when I run the model using Hugging Face Transformers. This issu...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
