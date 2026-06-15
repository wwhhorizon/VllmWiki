# vllm-project/vllm#12682: [Bug]: AssertionError on loading unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#12682](https://github.com/vllm-project/vllm/issues/12682) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError on loading unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assertion error on loading mistral small 2501 with unsloth weights ``` python3 -m vllm.entrypoints.openai.api_server --model unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit --tool-call-parser mistral --enable-auto-tool-choice --max-model-len 8192 --gpu-memory-utilization 0.98 --download-dir ./models_cache --host 0.0.0.0 --port 8000 --quantization bitsandbytes --load-format bitsandbytes ``` Error trace - ``` File "/home/ubuntu/.pyenv/versions/3.12.0/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubuntu/.pyenv/versions/3.12.0/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args return cls(ipc_path=ipc_path, ^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubuntu/.pyenv/versions/3.12.0/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 73, in __init__ self.engine = LLMEngine(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubuntu/.pyenv/versions/3.12.0/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oad-format bitsandbytes ``` Error trace - ``` File "/home/ubuntu/.pyenv/versions/3.12.0/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine engine = MQLLMEngine.from_engine_ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: uct-2501-unsloth-bnb-4bit bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assertion error on loading mistral small 2501 with unsloth weights ``` python3 -m vllm.entrypoi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: AssertionError on loading unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assertion error on loading mist...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: on loading unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Assertion error on loading mistral small 2501 with un...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
