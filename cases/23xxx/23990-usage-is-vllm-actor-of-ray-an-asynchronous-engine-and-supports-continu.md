# vllm-project/vllm#23990: [Usage]: Is vllm actor of ray an asynchronous engine and supports continuous batching when RLHF?

| 字段 | 值 |
| --- | --- |
| Issue | [#23990](https://github.com/vllm-project/vllm/issues/23990) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is vllm actor of ray an asynchronous engine and supports continuous batching when RLHF?

### Issue 正文摘录

https://github.com/janelu9/EasyLLM/blob/431e33cbd614fb255e8a36e2cd11476cd61d348d/jllm/vllm.py#L198 ``` @app.post("/generate") async def generate(request: GenerationRequest): token_prompts = [TokensPrompt(prompt_token_ids=p) for p in request.prompts] actor = actor_pool[request.rank] outputs = await actor.generate.remote( prompts=token_prompts, sampling_params=SamplingParams(**request.sampling_params)) text = [oi.text for o in outputs for oi in o.outputs] token_ids = [oi.token_ids for o in outputs for oi in o.outputs] return JSONResponse({'text':text,'token_ids':token_ids}) ``` The speed I tested supported that it's a synchronous engine. How to make it an asynchronous engine and support continuous batching? - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s engine and support continuous batching? - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: or of ray an asynchronous engine and supports continuous batching when RLHF? usage https://github.com/janelu9/EasyLLM/blob/431e33cbd614fb255e8a36e2cd11476cd61d348d/jllm/vllm.py#L198 ``` @app.post("/generate") async def...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d61d348d/jllm/vllm.py#L198 ``` @app.post("/generate") async def generate(request: GenerationRequest): token_prompts = [TokensPrompt(prompt_token_ids=p) for p in request.prompts] actor = actor_pool[request.rank] outputs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: return JSONResponse({'text':text,'token_ids':token_ids}) ``` The speed I tested supported that it's a synchronous engine. How to make it an asynchronous engine and support continuous batching? - [x] Make sure you alread...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
