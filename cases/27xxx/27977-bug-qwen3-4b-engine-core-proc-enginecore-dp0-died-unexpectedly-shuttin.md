# vllm-project/vllm#27977: [Bug]: Qwen3-4B  Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

| 字段 | 值 |
| --- | --- |
| Issue | [#27977](https://github.com/vllm-project/vllm/issues/27977) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-4B  Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "1,2" from vllm import LLM, SamplingParams from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained("/home/resource/model/Qwen3-4B-Thinking-2507") llm = LLM( model="/home/resource/model/Qwen3-4B-Thinking-2507", gpu_memory_utilization=0.95, max_model_len=10000, ) sampling_params = SamplingParams( max_tokens=8192, temperature=0.6, top_p=0.95, top_k=20, min_p=0 ) instruction = """ You are a helpful assistant that can solve the given question step by step. Given a question, you need to first think about the reasoning process in the mind and then provide the answer. The reasoning process and answer are enclosed within and tags respectively. Format example: This is the reasoning process. The final answer is \\boxed{answer here} In the last part of the answer, the final exact answer is enclosed within \\boxed{} with latex format.""" prompt = "The normal shock wave in the airflow occurs at $P_{1}=10 \\mathrm{Pa}$ (70Pa abs), $T_{1}=40 \\mathrm{~ °F ~} \\ (5 \\mathrm{~ °C ~})$, $V_{1}= 1400 \\mathrm{ft/sec \\left(425 \\ m/s \\right)}$, what is the temperature...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "1,2" from vllm import LLM, SamplingParams from transformers import AutoTokenizer tokenizer = AutoTokeni...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ne core proc EngineCore_DP0 died unexpectedly, shutting down client. bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "1,2" from vllm import LLM, Sam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 3 18:58:32 [model.py:547] Resolved architecture: Qwen3ForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! INFO 11-03 18:58:32 [model.py:1510] Using max model len 10000 INFO 11-03 18:58:32 [scheduler.py:205] Ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-4B Engine core proc EngineCore_DP0 died unexpectedly, shutting down client. bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "1,2" from v

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
