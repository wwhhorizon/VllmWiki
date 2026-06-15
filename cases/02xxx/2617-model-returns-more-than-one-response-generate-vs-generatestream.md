# vllm-project/vllm#2617: Model returns more than one response Generate() vs GenerateStream()

| 字段 | 值 |
| --- | --- |
| Issue | [#2617](https://github.com/vllm-project/vllm/issues/2617) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Model returns more than one response Generate() vs GenerateStream()

### Issue 正文摘录

I have running vllm with Triton using Python backend and loading the model via AsyncLLMEngine `self.llm = AsyncLLMEngine.from_engine_args(engine_args)` And I am generating the output using lm.generate() function as shown below ``` outputs = self.llm.generate( prompt=prompt, sampling_params=sampling_params, request_id=1, prompt_token_ids=self.tokens ) generated_text = '' async for output in outputs: generated_text = output.outputs[0].text ``` However, when hitting the model via Triton URL, I get this error back **> {"error":"generate expects model to produce exactly 1 response, use generate stream for model that generates various number of responses"}** Is there any other method than **generate()** to use here? My triton config file looks like ``` name: "my_model" backend: "python" max_batch_size: 0 model_transaction_policy { decoupled: True } # The usage of device is deferred to the vLLM engine instance_group [ { count: 1 kind: KIND_MODEL } ] input [ { name: "QUESTION" data_type: TYPE_STRING dims: [ 1 ] }, { name: "Param_B" data_type: TYPE_STRING dims: [ 1 ] }, { name: "Param_C" data_type: TYPE_STRING dims: [ -1 ] } ] output [ { name: "OUTPUT__0" data_type: TYPE_STRING dims: [ -1,...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: han one response Generate() vs GenerateStream() I have running vllm with Triton using Python backend and loading the model via AsyncLLMEngine `self.llm = AsyncLLMEngine.from_engine_args(engine_args)` And I am generating...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Model returns more than one response Generate() vs GenerateStream() I have running vllm with Triton using Python backend and loading the model via AsyncLLMEngine `self.llm = AsyncLLMEngine.from_engine_args(engine_args)`
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sampling_params=sampling_params, request_id=1, prompt_token_ids=self.tokens ) generated_text = '' async for output in outputs: generated_text = output.outputs[0].text ``` However, when hitting the model via Trit
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Model returns more than one response Generate() vs GenerateStream() I have running vllm with Triton using Python backend and loading the model via AsyncLLMEngine `self.llm = AsyncLLMEngine.from_engine_args(engine_args)`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
