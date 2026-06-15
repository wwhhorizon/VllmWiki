# vllm-project/vllm#14941: [Performance]: Speculative Decoding vs. Standard Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#14941](https://github.com/vllm-project/vllm/issues/14941) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Speculative Decoding vs. Standard Inference

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I am testing the response time of a model using speculative decoding and comparing it to standard inference. However, I am observing that with speculative decoding enabled, the response time is 2.76 seconds, whereas without it, the response time is significantly lower at 0.5694 seconds. From my understanding, speculative decoding should improve performance, but in this case, it seems to be slowing things down. I would appreciate any insights into why this might be happening. speculative decoding ` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model facebook/opt-6.7b --seed 42 -tp 1 --speculative_model facebook/opt-125m --num_speculative_tokens 5 --gpu_memory_utilization 0.8` **Result** ![Image](https://github.com/user-attachments/assets/8c099567-8ae5-478a-9521-9363d6743f7b) standard inference ` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model facebook/opt-6.7b ` **Result** ![Image](https://github.com/user-attachments/assets/d521fd88-b79d-4884-928d-e70b0ec6c14f) This is my run.py code ``` from openai import OpenAI import time # Import tim...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ance, but in this case, it seems to be slowing things down. I would appreciate any insights into why this might be happening. speculative decoding ` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 800...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Speculative Decoding vs. Standard Inference performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I am testing the response time of a model using specula...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression I am testing the response time of a model using speculative decoding and comparing it to standard inference. However, I am observing that...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ent.models.list() model = models.data[0].id # Completion API stream = False # Start timing start_time = time.time() completion = client.completions.create( model=model, prompt="The future of AI is", echo=False, n=1, str...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
