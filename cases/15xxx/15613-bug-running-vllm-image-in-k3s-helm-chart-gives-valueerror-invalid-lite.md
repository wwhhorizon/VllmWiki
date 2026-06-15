# vllm-project/vllm#15613: [Bug]: running vllm image in k3s helm chart  gives  ValueError: invalid literal for int() with base 10: 'tcp://10.43.1.39:8000'

| 字段 | 值 |
| --- | --- |
| Issue | [#15613](https://github.com/vllm-project/vllm/issues/15613) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: running vllm image in k3s helm chart  gives  ValueError: invalid literal for int() with base 10: 'tcp://10.43.1.39:8000'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug we have docker image based on vllm openai which has model Meta-Llama-3.1-8B-Instruct-Q8_0.gguf running with docker run -it --rm -p 8666:8000 --ipc=host --gpus "device=1" --name vllm1 vllm8b:2 which is working fine but same converted to helm chart gives below error: this was added as explained in https://github.com/huggingface/transformers/pull/24565 - if you loaded a llama tokenizer from a GGUF file you can ignore this message. ERROR 03-27 03:12:01 engine.py:400] invalid literal for int() with base 10: 'tcp://10.43.1.39:8000' Process SpawnProcess-1: ERROR 03-27 03:12:01 engine.py:400] Traceback (most recent call last): ERROR 03-27 03:12:01 engine.py:400] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine ERROR 03-27 03:12:01 engine.py:400] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 03-27 03:12:01 engine.py:400] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-27 03:12:01 engine.py:400] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args ERROR 03-27 03:12:01 engine.py...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 🐛 Describe the bug we have docker image based on vllm openai which has model Meta-Llama-3.1-8B-Instruct-Q8_0.gguf running with docker run -it --rm -p 8666:8000 --ipc=host --gpus "device=1" --name vllm1 vllm8b:2 which is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g;stale ### Your current environment ### 🐛 Describe the bug we have docker image based on vllm openai which has model Meta-Llama-3.1-8B-Instruct-Q8_0.gguf running with docker run -it --rm -p 8666:8000 --ipc=host --gpus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ^^^ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ror: invalid literal for int() with base 10: 'tcp://10.43.1.39:8000' bug;stale ### Your current environment ### 🐛 Describe the bug we have docker image based on vllm openai which has model Meta-Llama-3.1-8B-Instruct-Q8_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
