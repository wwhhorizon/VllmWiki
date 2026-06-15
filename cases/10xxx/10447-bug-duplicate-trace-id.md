# vllm-project/vllm#10447: [Bug]: Duplicate trace Id

| 字段 | 值 |
| --- | --- |
| Issue | [#10447](https://github.com/vllm-project/vllm/issues/10447) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Duplicate trace Id

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The traces from vLLM have duplicate trace Id's. It generates the same sequence of trace and span Id's every time the application is executed. ```text import os from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM( model="ibm-granite/granite-3.0-2b-instruct", # Set the OpenTelemetry endpoint from the environment variable. otlp_traces_endpoint=os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"], ) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` The above application was executed twice. The 2 spans in the image are from 2 different executions where vLLM generated duplicate trace Id's. The spans are tag...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: of trace and span Id's every time the application is executed. ```text import os from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The future of AI is", ] # Create a sampling param...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 's. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Duplicate trace Id bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The traces from vLLM have duplicate trace Id's. It generates the same sequence of trace and span Id's...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: NDPOINT"], ) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
