# vllm-project/vllm#13387: [Bug]: Chunk Prefill feature fails for ppc64le (IBM POWER)

| 字段 | 值 |
| --- | --- |
| Issue | [#13387](https://github.com/vllm-project/vllm/issues/13387) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chunk Prefill feature fails for ppc64le (IBM POWER)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When we run chunked prefill enabled on ppc64le, it fails with an ipex dependency. As ipex does not work for ppc64le, we are seeing this error. ### Test script ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-1.3b", enable_chunked_prefill=True) # Enable chunked prefill long_prompt = """Once upon a time in a faraway land, there was a wise old owl who lived in a hollow tree. This owl had seen many seasons pass and had gathered knowledge from all corners of the world...""" sampling_params = SamplingParams(temperature=0.7, max_tokens=100) outputs = llm.generate([long_prompt], sampling_params) for output in outputs: print("Generated Text:", output.outputs[0].text) ``` ### Error Log ``` INFO 02-16 08:18:58 __init__.py:183] Automatically detected platform cpu. config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 653/653 [00:00 [rank0]: outputs = llm.generate([long_prompt], sampling_params) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g When we run chunked prefill enabled on ppc64le, it fails with an ipex dependency. As ipex does not work for ppc64le, we are seeing this error. ### Test script ```python from vllm import LLM, SamplingParams llm = LLM(m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Chunk Prefill feature fails for ppc64le (IBM POWER) bug;stale ### Your current environment ### 🐛 Describe the bug When we run chunked prefill enabled on ppc64le, it fails with an ipex dependency. As ipex does not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1.dev4356+gb02fd28.d20250129.cpu-py3.11-linux-ppc64le.egg/vllm/attention/backends/torch_sdpa.py", line 536, in forward [rank0]: import intel_extension_for_pytorch.llm.modules as ipex_modules [rank0]: ModuleNotFoundError...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;import_error;nan_inf dtype;env_dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
