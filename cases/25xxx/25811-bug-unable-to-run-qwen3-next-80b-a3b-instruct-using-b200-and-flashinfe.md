# vllm-project/vllm#25811: [Bug]: Unable to run Qwen3-Next-80B-A3B-Instruct  using B200 and Flashinfer backend

| 字段 | 值 |
| --- | --- |
| Issue | [#25811](https://github.com/vllm-project/vllm/issues/25811) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run Qwen3-Next-80B-A3B-Instruct  using B200 and Flashinfer backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I get the following error when i run the folllowing code, note that when i change the attention backend from flashinfer to something else i dont get this error: ``` base_model = "Qwen/Qwen3-Next-80B-A3B-Instruct" model = LLM(model=base_model, tensor_parallel_size=num_gpus, max_model_len=None) # st() # Define sampling parameters sampling_params = SamplingParams( # temperature=0.7, # top_p=0.95, max_tokens=2048, #stop=[" ", "\n\n"] # Common stop tokens ) # Example prompt prompt = [{"role": "user", "content": "Who is the president of US?"}] # Generate response outputs = model.chat([prompt], sampling_params) ``` Full Error: ```text (EngineCore_DP0 pid=3339204) RuntimeError: Expect (32 > (EngineCore_DP0 pid=3339204) Traceback (most recent call last): (EngineCore_DP0 pid=3339204) File "/home/ubuntu/.local/share/mamba/envs/pho/lib/python3.12/weakref.py", line 666, in _exitfunc (EngineCore_DP0 pid=3339204) f() (EngineCore_DP0 pid=3339204) File "/home/ubuntu/.local/share/mamba/envs/pho/lib/python3.12/weakref.py", line 590, in __call__ (EngineCore_DP0 pid=3339204) return info.func(*info.args, **(info.kwargs or {})) (EngineCore_DP0 pid=3339...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Unable to run Qwen3-Next-80B-A3B-Instruct using B200 and Flashinfer backend bug;stale ### Your current environment ### 🐛 Describe the bug I get the following error when i run the folllowing code, note that when i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Unable to run Qwen3-Next-80B-A3B-Instruct using B200 and Flashinfer backend bug;stale ### Your current environment ### 🐛 Describe the bug I get the following error when i run the folllowing code, note that when i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unable to run Qwen3-Next-80B-A3B-Instruct using B200 and Flashinfer backend bug;stale ### Your current environment ### 🐛 Describe the bug I get the following error when i run the folllowing code, note that when i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: o run Qwen3-Next-80B-A3B-Instruct using B200 and Flashinfer backend bug;stale ### Your current environment ### 🐛 Describe the bug I get the following error when i run the folllowing code, note that when i change the att...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
