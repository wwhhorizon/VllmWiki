# vllm-project/vllm#14759: [Bug]: sampling_params.n > 1, after reset_state_for_recompute() will meet 'AssertionError: seq_len: 2701, context_len: 0, query_len: 2701'

| 字段 | 值 |
| --- | --- |
| Issue | [#14759](https://github.com/vllm-project/vllm/issues/14759) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sampling_params.n > 1, after reset_state_for_recompute() will meet 'AssertionError: seq_len: 2701, context_len: 0, query_len: 2701'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from transformers import AutoTokenizer, AutoModelForCausalLM import torch import random from vllm import LLM, SamplingParams model_path="a 7b model" llm = LLM( model=model_path, dtype='auto', enable_chunked_prefill=False, gpu_memory_utilization=0.6, max_model_len=5120, enforce_eager=True, enable_prefix_caching=False, trust_remote_code=True, # max_num_batched_tokens=40960, tensor_parallel_size=2, swap_space=32, ) def generate_lists(num_lists=256, list_length=250, min_value=1, max_value=19999, seed=1234): random.seed(seed) lists = [] for _ in range(num_lists): lst = [0] lst.extend(random.randint(min_value, max_value) for _ in range(list_length - 1)) lists.append(lst) return lists random_lists = generate_lists() kwargs = {'n': 8, 'logprobs': 1, 'max_tokens': 4096, 'detokenize': False, 'temperature': 1.0, 'top_k': -1, 'top_p': 1, 'ignore_eos': False} s = SamplingParams(**kwargs) outputs = llm.generate( prompt_token_ids=random_lists, # because we have already convert it to prompt token id sampling_params=s, use_tqdm=False) print("======finish=======") print(len(outputs)) print(len(outputs[0].outputs)) ``` vLLM version is 0.6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rent environment ### 🐛 Describe the bug ```python from transformers import AutoTokenizer, AutoModelForCausalLM import torch import random from vllm import LLM, SamplingParams model_path="a 7b model" llm = LLM( model=mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: eet 'AssertionError: seq_len: 2701, context_len: 0, query_len: 2701' bug;stale ### Your current environment ### 🐛 Describe the bug ```python from transformers import AutoTokenizer, AutoModelForCausalLM import torch impo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ror. By the way, this error is in n=8 and large batch_size. When use a small batch_size, like 16, `reset_state_for_recompute` will not be called, and works. Another right case is n=1 and large batch_size, `reset_state_f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tils.py](https://github.com/vllm-project/vllm/blob/v0.6.3/vllm/attention/backends/utils.py#L163). I debug the code, find a seq will call `reset_state_for_recompute` in [sequence.py](https://github.com/vllm-project/vllm/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ingParams model_path="a 7b model" llm = LLM( model=model_path, dtype='auto', enable_chunked_prefill=False, gpu_memory_utilization=0.6, max_model_len=5120, enforce_eager=True, enable_prefix_caching=False, trust_remote_co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
