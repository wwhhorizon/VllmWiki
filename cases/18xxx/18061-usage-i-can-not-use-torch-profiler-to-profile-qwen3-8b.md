# vllm-project/vllm#18061: [Usage]: I can not use torch.profiler to profile qwen3_8B

| 字段 | 值 |
| --- | --- |
| Issue | [#18061](https://github.com/vllm-project/vllm/issues/18061) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: I can not use torch.profiler to profile qwen3_8B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use vllm==0.8.5 and torch.profiler to profile qwen3-8B. The result txt `qwen3_8B_ops.txt` is empty, it should contain the cpu event. Is this a bug? ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams import torch # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B") # Configurae the sampling parameters (for thinking mode) sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=20, max_tokens=32768) # Initialize the vLLM engine llm = LLM(model="Qwen/Qwen3-8B") with torch.profiler.profile( activities=[ torch.profiler.ProfilerActivity.CPU, # torch.profiler.ProfilerActivity.CUDA, ], #record_shapes=True, #with_stack=True, ) as p: # Prepare the input to the model prompt = "Give me a short introduction to large language models." messages = [ {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, enable_thinking=True # True is the default value for enable_thinking ) # Generate outputs outputs = llm.generate([text], sampling_params) table_str = p.key_averages().table( sort_by="count", r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hould contain the cpu event. Is this a bug? ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams import torch # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: I can not use torch.profiler to profile qwen3_8B usage ### Your current environment ### 🐛 Describe the bug I use vllm==0.8.5 and torch.profiler to profile qwen3-8B. The result txt `qwen3_8B_ops.txt` is empty, i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: profiler.ProfilerActivity.CPU, # torch.profiler.ProfilerActivity.CUDA, ], #record_shapes=True, #with_stack=True, ) as p: # Prepare the input to the model prompt = "Give me a short introduction to large language models."...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: I can not use torch.profiler to profile qwen3_8B usage ### Your current environment ### 🐛 Describe the bug I use vllm==0.8.5 and torch.profiler to profile qwen3-8B. The result txt `qwen3_8B_ops.txt` is empty, i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
