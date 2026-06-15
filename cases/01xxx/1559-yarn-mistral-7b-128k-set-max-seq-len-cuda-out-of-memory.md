# vllm-project/vllm#1559: Yarn-Mistral-7b-128k  set max_seq_len, CUDA OUT OF MEMORY....

| 字段 | 值 |
| --- | --- |
| Issue | [#1559](https://github.com/vllm-project/vllm/issues/1559) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Yarn-Mistral-7b-128k  set max_seq_len, CUDA OUT OF MEMORY....

### Issue 正文摘录

Does it take up more than 40GB memory to be able to modify the length of the tokens before loading the model? ```Python from vllm import LLM, SamplingParams#, set_tokenizer, get_tokenizer import torch import time import gc # max_seq_len=2028, model= "NousResearch/Yarn-Mistral-7b-128k" llm = LLM(model=model,dtype="bfloat16", gpu_memory_utilization=.5, tensor_parallel_size=1, quantization=None, seed=0,) ``` set max_seq_len how? ``` INFO 11-04 06:25:50 llm_engine.py:72] Initializing an LLM engine with config: model='NousResearch/Yarn-Mistral-7b-128k', tokenizer='NousResearch/Yarn-Mistral-7b-128k', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=524288, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) ``` ![image](https://github.com/vllm-project/vllm/assets/123802672/41b8b386-14b0-4a97-9b87-77351f2274b6)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =2028, model= "NousResearch/Yarn-Mistral-7b-128k" llm = LLM(model=model,dtype="bfloat16", gpu_memory_utilization=.5, tensor_parallel_size=1, quantization=None, seed=0,) ``` set max_seq_len how? ``` INFO 11-04 06:25:50 l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: memory to be able to modify the length of the tokens before loading the model? ```Python from vllm import LLM, SamplingParams#, set_tokenizer, get_tokenizer import torch import time import gc # max_seq_len=2028, model=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: the length of the tokens before loading the model? ```Python from vllm import LLM, SamplingParams#, set_tokenizer, get_tokenizer import torch import time import gc # max_seq_len=2028, model= "NousResearch/Yarn-Mistral-7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Yarn-Mistral-7b-128k set max_seq_len, CUDA OUT OF MEMORY.... Does it take up more than 40GB memory to be able to modify the length of the tokens before loading the model? ```Python from vllm import LLM, SamplingParams#,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 6) performance frontend_api;model_support;quantization cuda;quantization oom dtype;env_dependency Does it take up more than 40GB memory to be able to modify the length of the tokens before loading the model?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
