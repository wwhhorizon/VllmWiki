# vllm-project/vllm#12225: [Usage]: Guided choice not working as expected

| 字段 | 值 |
| --- | --- |
| Issue | [#12225](https://github.com/vllm-project/vllm/issues/12225) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Guided choice not working as expected

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.5.1 Versions of relevant libraries: [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-ml-py==12.560.30 [pip3] onnxruntime==1.20.1 [pip3] pyzmq==26.2.0 [pip3] sentence-transformers==3.3.1 [pip3] torch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.0 [conda] Could not collect vLLM Version: 0.6.6.post1 vLLM Build Flags: ``` ### How would you like to use vllm I am using a hosted vLLM model for inference. I would like to be able to use the `guided_choice` param to constrain my outputs. I was using the example provided on the vLLM documentation [here](https://docs.vllm.ai/en/latest/features/structured_outputs.html). This is my current setup: ```python from openai import OpenAI api_key = " " hosted_url = " " client = OpenAI( base_url=hosted_url, api_key=api_key ) completion = client.chat.completions.create( model=" ", messages=[ {"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"} ], extra_body={"guided_choice": ["positive", "negative"]}, ) print(completion.choices[0].message.content) ``` This is the output that I get: ``` The sentiment of the statement "vLLM is wonderful!" is positive....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: orking as expected usage;stale ### Your current environment ``` PyTorch version: 2.5.1 Versions of relevant libraries: [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-ml-py==12.560.30 [pip3] onnxruntime...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Flags: ``` ### How would you like to use vllm I am using a hosted vLLM model for inference. I would like to be able to use the `guided_choice` param to constrain my outputs. I was using the example provided on the vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Guided choice not working as expected usage;stale ### Your current environment ``` PyTorch version: 2.5.1 Versions of relevant libraries: [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-ml-py==...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: mple provided on the vLLM documentation [here](https://docs.vllm.ai/en/latest/features/structured_outputs.html). This is my current setup: ```python from openai import OpenAI api_key = " " hosted_url = " " client = Open...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
