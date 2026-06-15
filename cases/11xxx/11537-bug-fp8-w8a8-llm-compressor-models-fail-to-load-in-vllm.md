# vllm-project/vllm#11537: [Bug]: FP8 W8A8 LLM Compressor Models fail to load in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#11537](https://github.com/vllm-project/vllm/issues/11537) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 W8A8 LLM Compressor Models fail to load in vLLM

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running `vllm serve mistralai/mistral-123B-instruct --host 0.0.0.0 --port 8000 --enable-chunked-prefill False --max-seq-len-to-capture 16384 --num-scheduler-steps 10` fails with a raised exception after the model is loaded Model llm-compressor recipe: DEFAULT_stage: DEFAULT_modifiers: QuantizationModifier: ignore: [lm_head] targets: [Linear] scheme: FP8_DYNAMIC Traceback: ERROR 12-27 00:09:08 engine.py:366] 'QKVParallelLinear' object has no attribute 'input_scale' ERROR 12-27 00:09:08 engine.py:366] Traceback (most recent call last): ERROR 12-27 00:09:08 engine.py:366] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine ERROR 12-27 00:09:08 engine.py:366] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 12-27 00:09:08 engine.py:366] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args ERROR 12-27 00:09:08 engine.py:366] return cls(ipc_path=ipc_path, ERROR 12-27 00:09:08 engine.py:366] File "/workspace/vllm/vllm/engine/multiprocessing/engine.py", line 71, in __init__ ERROR 12-27 00:09:08 engine.py:366...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ith a raised exception after the model is loaded Model llm-compressor recipe: DEFAULT_stage: DEFAULT_modifiers: QuantizationModifier: ignore: [lm_head] targets: [Linear] scheme: FP8_DYNAMIC Traceback: ERROR 12-27
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: FP8 W8A8 LLM Compressor Models fail to load in vLLM bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running `vllm serve mistralai/mistral-123B-instruct --host 0.0.0.0 --
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tralai/mistral-123B-instruct --host 0.0.0.0 --port 8000 --enable-chunked-prefill False --max-seq-len-to-capture 16384 --num-scheduler-steps 10` fails with a raised exception after the model is loaded Model llm-compresso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: FP8 W8A8 LLM Compressor Models fail to load in vLLM bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running `vllm serve mistralai/mistral-123B-instruct --host 0.0.0.0 -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
