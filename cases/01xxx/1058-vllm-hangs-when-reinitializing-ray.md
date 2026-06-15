# vllm-project/vllm#1058: vllm hangs when reinitializing ray

| 字段 | 值 |
| --- | --- |
| Issue | [#1058](https://github.com/vllm-project/vllm/issues/1058) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vllm hangs when reinitializing ray

### Issue 正文摘录

I'd like to be able to unload a vllm model and re-load it later, in the same script. However, the following (on 0.1.7) causes the script to hang (disclaimer: this isn't my particular workload, but a minimal reproducible example): ```python from vllm import LLM, SamplingParams def process_prompts(prompts): llm = LLM( model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=2, trust_remote_code=True, load_format="pt") sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=500) return llm.generate(prompts, sampling_params) prompt_batch_1 = ["Hello, my name is", "The president of the United States is"] prompt_batch_2 = ["The capital of France is", "The future of AI is"] batch_1_output = process_prompts(prompt_batch_1) batch_2_output = process_prompts(prompt_batch_2) ``` Results in: ``` 2023-09-15 11:43:25,943 INFO worker.py:1621 -- Started a local Ray instance. INFO 09-15 11:43:51 llm_engine.py:72] Initializing an LLM engine with config: model='meta-llama/Llama-2 -70b-chat-hf', tokenizer='meta-llama/Llama-2-70b-chat-hf', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, download_dir='/scr/biggest/nfliu/cache/huggingface/', load_format=pt, tensor_pa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: m hangs when reinitializing ray bug I'd like to be able to unload a vllm model and re-load it later, in the same script. However, the following (on 0.1.7) causes the script to hang (disclaimer: this isn't my particular...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ang (disclaimer: this isn't my particular workload, but a minimal reproducible example): ```python from vllm import LLM, SamplingParams def process_prompts(prompts): llm = LLM( model="meta-llama/Llama-2-70b-chat-hf", te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --------------------------------------------------------------+ | NVIDIA-SMI 535.54.03 Driver Version: 535.54.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+-------------------...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lama/Llama-2-70b-chat-hf', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, download_dir='/scr/biggest/nfliu/cache/huggingface/', load_format=pt, tensor_para llel_size=2, seed=0) INFO 09-15 11:43:51 tok...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pt to hang (disclaimer: this isn't my particular workload, but a minimal reproducible example): ```python from vllm import LLM, SamplingParams def process_prompts(prompts): llm = LLM( model="meta-llama/Llama-2-70b-chat-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
