# vllm-project/vllm#16183: [Bug]: ValueError: ChatGLMForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#16183](https://github.com/vllm-project/vllm/issues/16183) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: ChatGLMForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` model_path = "ShieldLM-6B-chatglm3/" model = LLM(model=model_path, trust_remote_code=True) outputs = self.model.generate(formatted_prompts, sampling_params) ``` when I try to run the above example code the HF link of this model is: https://huggingface.co/thu-coai/ShieldLM-6B-chatglm3 and I download the model to my local space. but it didn't work, I got the value error INFO 04-07 11:30:34 [cpu.py:40] Using Torch SDPA backend. INFO 04-07 11:30:44 [parallel_state.py:948] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0 [rank0]: Traceback (most recent call last): [rank0]: File "/workspace/inference_cpu_vllm.py", line 579, in [rank0]: safety_eval = SafetyEval_VLLM(model_path=model_path) [rank0]: File "/workspace/inference_cpu_vllm.py", line 200, in __init__ [rank0]: self.model = LLM(model=model_path, trust_remote_code=True) [rank0]: File "/usr/local/lib/python3.10/site-packages/vllm/utils.py", line 1049, in inner [rank0]: return fn(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 240, in __init__ [rank0]: self.llm_engine = self.engine_class.from_engine_args...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: h vLLM. bug ### Your current environment ### 🐛 Describe the bug ``` model_path = "ShieldLM-6B-chatglm3/" model = LLM(model=model_path, trust_remote_code=True) outputs = self.model.generate(formatted_prompts, sampling_pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s, sampling_params) ``` when I try to run the above example code the HF link of this model is: https://huggingface.co/thu-coai/ShieldLM-6B-chatglm3 and I download the model to my local space. but it didn't work, I got t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: I got the value error INFO 04-07 11:30:34 [cpu.py:40] Using Torch SDPA backend. INFO 04-07 11:30:44 [parallel_state.py:948] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0 [rank0]: Traceback (most...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , line 116, in _initialize_model [rank0]: model_class, _ = get_model_architecture(model_config) [rank0]: File "/usr/local/lib/python3.10/site-packages/vllm/model_executor/model_loader/utils.py", line 106, in get_model_a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e "/workspace/inference_cpu_vllm.py", line 579, in [rank0]: safety_eval = SafetyEval_VLLM(model_path=model_path) [rank0]: File "/workspace/inference_cpu_vllm.py", line 200, in __init__ [rank0]: self.model = LLM(model=mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
