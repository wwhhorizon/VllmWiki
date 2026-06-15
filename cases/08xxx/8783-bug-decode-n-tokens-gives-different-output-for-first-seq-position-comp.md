# vllm-project/vllm#8783: [Bug]: Decode n tokens gives different output for first seq position compared to decode 1 token

| 字段 | 值 |
| --- | --- |
| Issue | [#8783](https://github.com/vllm-project/vllm/issues/8783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Decode n tokens gives different output for first seq position compared to decode 1 token

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running speculative decoding with the same model as the draft and the target. We should expect to see 100% acceptance rate, and logits that are the same. Here is the minimal script I run. ```python from vllm import LLM, SamplingParams import time import torch import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' llm = LLM( model="meta-llama/Meta-Llama-3.1-8b", dtype='bfloat16', tensor_parallel_size=1, enforce_eager=True, speculative_model="meta-llama/Meta-Llama-3.1-8b", num_speculative_tokens=1, use_v2_block_manager=True, seed=0, disable_log_stats=False, ) max_gen_tokens = 2 sampling_params = SamplingParams(temperature=1.0, min_tokens=max_gen_tokens, max_tokens=max_gen_tokens) bsz = 1 warmup_prompts = [ "The future of AI is ", ] warmup_prompts = warmup_prompts * bsz start = time.perf_counter() outputs = llm.generate(warmup_prompts, sampling_params) torch.cuda.synchronize() end = time.perf_counter() print(f"elapsed time: {end - start:.2f} s") ``` And I get the following output. The tensors are hidden_states. Note that I modified the llama.py file so that these would be printed. I replace `compu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: at are the same. Here is the minimal script I run. ```python from vllm import LLM, SamplingParams import time import torch import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' llm = LLM( model="meta-llama/Meta-Llama-3.1-8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Decode n tokens gives different output for first seq position compared to decode 1 token bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running speculative d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: EVICES'] = '0' llm = LLM( model="meta-llama/Meta-Llama-3.1-8b", dtype='bfloat16', tensor_parallel_size=1, enforce_eager=True, speculative_model="meta-llama/Meta-Llama-3.1-8b", num_speculative_tokens=1, use_v2_block_mana...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: "meta-llama/Meta-Llama-3.1-8b", num_speculative_tokens=1, use_v2_block_manager=True, seed=0, disable_log_stats=False, ) max_gen_tokens = 2 sampling_params = SamplingParams(temperature=1.0, min_tokens=max_gen_tokens, max...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mport LLM, SamplingParams import time import torch import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' llm = LLM( model="meta-llama/Meta-Llama-3.1-8b", dtype='bfloat16', tensor_parallel_size=1, enforce_eager=True, specul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
