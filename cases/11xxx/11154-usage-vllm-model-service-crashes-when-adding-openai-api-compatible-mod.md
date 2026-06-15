# vllm-project/vllm#11154: [Usage]: vLLM model service crashes when adding OpenAI-API-compatible model in dify， model id:  Qwen/Qwen2-VL-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#11154](https://github.com/vllm-project/vllm/issues/11154) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM model service crashes when adding OpenAI-API-compatible model in dify， model id:  Qwen/Qwen2-VL-7B-Instruct

### Issue 正文摘录

### Your current environment vLLM API server version 0.6.4.post2 docker vllm-cpu-env model "Qwen/Qwen2-VL-7B-Instruct" ### How would you like to use vllm vLLM model service crashes when adding OpenAI-API-compatible model in dify， model id: Qwen/Qwen2-VL-7B-Instruct ---------------------------------------------------------------- Error message： INFO 12-13 01:12:19 engine.py:267] Added request chatcmpl-093873b3235846bfb6500cd5807b39be. ERROR 12-13 01:12:19 engine.py:135] RuntimeError("shape '[0, -1, 128]' is invalid for input of size 71680") ERROR 12-13 01:12:19 engine.py:135] Traceback (most recent call last): ERROR 12-13 01:12:19 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 133, in start ERROR 12-13 01:12:19 engine.py:135] self.run_engine_loop() ...... ERROR 12-13 01:12:19 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1747, in _call_impl ERROR 12-13 01:12:19 engine.py:135] return forward_call(*args, **kwargs) ERROR 12-13 01:12:19 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 825, in forward ERROR 12-13 01...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Qwen2-VL-7B-Instruct usage ### Your current environment vLLM API server version 0.6.4.post2 docker vllm-cpu-env model "Qwen/Qwen2-VL-7B-Instruct" ### How would you like to use vllm vLLM model service crashes when adding...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: vLLM model service crashes when adding OpenAI-API-compatible model in dify， model id: Qwen/Qwen2-VL-7B-Instruct usage ### Your current environment vLLM API server version 0.6.4.post2 docker vllm-cpu-env model "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: own ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --------------- Error message： INFO 12-13 01:12:19 engine.py:267] Added request chatcmpl-093873b3235846bfb6500cd5807b39be. ERROR 12-13 01:12:19 engine.py:135] RuntimeError("shape '[0, -1, 128]' is invalid for input of s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
