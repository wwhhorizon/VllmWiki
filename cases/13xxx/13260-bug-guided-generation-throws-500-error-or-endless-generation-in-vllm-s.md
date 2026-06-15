# vllm-project/vllm#13260: [Bug]: Guided generation throws 500 error or endless generation in vllm serve for mistral small 2501

| 字段 | 值 |
| --- | --- |
| Issue | [#13260](https://github.com/vllm-project/vllm/issues/13260) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Guided generation throws 500 error or endless generation in vllm serve for mistral small 2501

### Issue 正文摘录

### Your current environment docker image `vllm/vllm-openai:v0.7.2`, running on 1 H100 GPU. ### 🐛 Describe the bug Running structured output generation results in a 500 server error, but running offline inference is ok. Running json structured generation will cause an endless generation of whitespace. ## vllm serve error ```sh vllm serve mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --revision 20b2ed1c4e9af44b9ad125f79f713301e27737e2 ``` ```python from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) completion = client.chat.completions.create( model="mistralai/Mistral-Small-24B-Instruct-2501", messages=[ { "role": "user", "content": "Classify this sentiment: vLLM is wonderful!", } ], extra_body={"guided_choice": ['positive', 'negative']}, ) content = completion.choices[0].message.content print(completion.choices[0].message.content) ``` ![Image](https://github.com/user-attachments/assets/3cd613aa-f2cb-4040-a8fe-f498fc7d061c) ```python from pydantic import BaseModel from enum import Enum class CarType(str, Enum): sedan = "s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rve mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --revision 20b2ed1c4e9af44b9ad125f79f713301e27737...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eration throws 500 error or endless generation in vllm serve for mistral small 2501 bug;stale ### Your current environment docker image `vllm/vllm-openai:v0.7.2`, running on 1 H100 GPU. ### 🐛 Describe the bug Running st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: llm serve for mistral small 2501 bug;stale ### Your current environment docker image `vllm/vllm-openai:v0.7.2`, running on 1 H100 GPU. ### 🐛 Describe the bug Running structured output generation results in a 500 server...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 500 error or endless generation in vllm serve for mistral small 2501 bug;stale ### Your current environment docker image `vllm/vllm-openai:v0.7.2`, running on 1 H100 GPU. ### 🐛 Describe the bug Running structured output...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
