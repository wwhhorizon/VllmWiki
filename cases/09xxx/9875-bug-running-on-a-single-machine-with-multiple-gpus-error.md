# vllm-project/vllm#9875: [Bug]:  Running on a single machine with multiple GPUs error

| 字段 | 值 |
| --- | --- |
| Issue | [#9875](https://github.com/vllm-project/vllm/issues/9875) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Running on a single machine with multiple GPUs error

### Issue 正文摘录

### Your current environment Name: vllm Version: 0.6.3.post2.dev171+g890ca360 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the interface from this vllm repository to load the model and ran eval scripts on vlmevalkit(https://github.com/open-compass/VLMEvalKit) ```bash torchrun --nproc-per-node=8 run.py --data Video-MME --model Qwen2_VL-M-RoPE-80k ``` for evaluation, but I got the error ```bash RuntimeError: world_size (8) is not equal to tensor_model_parallel_size (1) x pipeline_model_parallel_size (1). ``` Could you please advise on how to resolve this? Here is the interface ``` from vllm import LLM llm = LLM("/mnt/hwfile/mllm/weixilin/cache/Qwen2-VL-7B-Instruct", max_model_len=100000, limit_mm_per_prompt={"video": 10}, ) ``` https://github.com/vllm-project/vllm/blob/3ea2dc2ec49d1ddd7875045e2397ae76a8f50b38/vllm/distributed/parallel_state.py#L1025 Seems that the error occur at this assertion, so what change should I make to fit the assertion, thanks. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rrent environment Name: vllm Version: 0.6.3.post2.dev171+g890ca360 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the interface from this vllm repository to load the model and ran eval scripts on vlme...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: h multiple GPUs error bug;stale ### Your current environment Name: vllm Version: 0.6.3.post2.dev171+g890ca360 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the interface from this vllm repository to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I used the interface from this vllm repository to load the model and ran eval scripts on vlmevalkit(https://github.com/open-compass/VLMEvalKit) ```bash torchrun --nproc-per-node=8 run.py --data Video-MME --model Qwen2_V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Running on a single machine with multiple GPUs error bug;stale ### Your current environment Name: vllm Version: 0.6.3.post2.dev171+g890ca360 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
