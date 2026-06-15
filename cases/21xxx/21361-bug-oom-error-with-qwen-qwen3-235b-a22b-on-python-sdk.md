# vllm-project/vllm#21361: [Bug]: OOM Error with Qwen/Qwen3-235B-A22B on Python SDK

| 字段 | 值 |
| --- | --- |
| Issue | [#21361](https://github.com/vllm-project/vllm/issues/21361) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM Error with Qwen/Qwen3-235B-A22B on Python SDK

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I start the service using the command: ```shell vllm serve /data/model/Qwen/Qwen3-235B-A22B --host 0.0.0.0 --port 4000 --enable-auto-tool-choice --tool-call-parser hermes --tensor-parallel-size 8 --served-model-name Qwen3-235B-A22B --gpu-memory-utilization 0.9 --max-model-len 25000 ``` it runs successfully. However, when I try to launch it programmatically using the following code: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("/data/model/Qwen/Qwen3-235B-A22B") # Configurae the sampling parameters (for thinking mode) sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=20, max_tokens=16384) # Initialize the vLLM engine llm = LLM(model="/data/model/Qwen/Qwen3-235B-A22B", tensor_parallel_size=8, swap_space=4, , max_num_seqs=128) # Prepare the input to the model prompt = "Give me a short introduction to large language models." messages = [ {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, enable_thinking=True, # Set to False t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: t programmatically using the following code: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("/data/model/Qwen/Q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: in __init__ (VllmWorker rank=4 pid=4103128) self.model = TransformersModel(vllm_config=vllm_config, prefix=prefix) (VllmWorker rank=4 pid=4103128) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker ra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: OOM Error with Qwen/Qwen3-235B-A22B on Python SDK bug ### Your current environment ### 🐛 Describe the bug When I start the service using the command: ```shell vllm serve /data/model/Qwen/Qwen3-235B-A22B --host 0....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: OOM Error with Qwen/Qwen3-235B-A22B on Python SDK bug ### Your current environment ### 🐛 Describe the bug When I start the service using the command: ```shell vllm serve /data/model/Qwen/Qwen3-235B-A22B --host 0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, enable_thinking=True, # Set to False to strictly disable thinking ) # Generate outputs outputs = llm.generate([text], sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
