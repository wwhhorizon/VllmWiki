# vllm-project/vllm#13429: [Bug]: [V1][Core] Structured decoding - Decouple Json from Json Object

| 字段 | 值 |
| --- | --- |
| Issue | [#13429](https://github.com/vllm-project/vllm/issues/13429) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1][Core] Structured decoding - Decouple Json from Json Object

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using json_object = True for guided decoding (as per V0 guidelines), V1 (based on #12388 ) expects us to have a json_schema present for it as well. In nature both json_object and json need to be decoupled as per this [code snippet](https://github.com/vllm-project/vllm/pull/12388/files#diff-35f85e99eae8897d78a45f6a8d21bb69f9d8fe4a51e072bf299118dadac612f3R160) since json_object would inherently use the JsonGrammar compiled by xgrammar backend and would not require a Json Schema for it. ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, guided_decoding=GuidedDecodingParams( json_object=True, backend="xgrammar")) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Error : ```ERROR 02-17 22:27:52 core.py:235] File "/host/vllm/vllm/v1/request.py", l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 18dadac612f3R160) since json_object would inherently use the JsonGrammar compiled by xgrammar backend and would not require a Json Schema for it. ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: [V1][Core] Structured decoding - Decouple Json from Json Object bug;stale ### Your current environment ### 🐛 Describe the bug When using json_object = True for guided decoding (as per V0 guidelines), V1 (based on #...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ce json_object would inherently use the JsonGrammar compiled by xgrammar backend and would not require a Json Schema for it. ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: backend="xgrammar")) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
