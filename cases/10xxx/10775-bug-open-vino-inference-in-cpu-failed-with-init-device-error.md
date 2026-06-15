# vllm-project/vllm#10775: [Bug]: [Open-VINO] inference in CPU failed with "init_device" error

| 字段 | 值 |
| --- | --- |
| Issue | [#10775](https://github.com/vllm-project/vllm/issues/10775) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Open-VINO] inference in CPU failed with "init_device" error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 1. convert qwen2.5-7b-instruct into int4 format using `optimum`: `optimum-cli export openvino -m ./qwen2.5-7b-instruct --task text-generation-with-past --weight-format int4 ./qwen2.5-7b-int4` 2. deploy the model using vllm: `vllm serve ./qwen2.5-7b-int4 --max-model-len 8192 --enable-chunked-prefill --max-num-batched-tokens 256`. additional parameters follow vllm docs' performance tips, environment variables are provided in `collect_env.py` output 3. error occurs: ```text Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/orion/.local/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 368, in run_mp_engine raise e File "/home/orion/.local/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, File "/home/orion/.local/lib/python3.10/site-packages/vllm/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: failed with "init_device" error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 1. convert qwen2.5-7b-instruct into int4 format using `optimum`: `optimum-cli export openvino -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding atten...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: o response_ ### 🐛 Describe the bug 1. convert qwen2.5-7b-instruct into int4 format using `optimum`: `optimum-cli export openvino -m ./qwen2.5-7b-instruct --task text-generation-with-past --weight-format int4 ./qwen2.5-7...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: llm: `vllm serve ./qwen2.5-7b-int4 --max-model-len 8192 --enable-chunked-prefill --max-num-batched-tokens 256`. additional parameters follow vllm docs' performance tips, environment variables are provided in `collect_en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
