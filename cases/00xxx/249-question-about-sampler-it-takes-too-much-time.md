# vllm-project/vllm#249: Question about sampler. It takes too much time

| 字段 | 值 |
| --- | --- |
| Issue | [#249](https://github.com/vllm-project/vllm/issues/249) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Question about sampler. It takes too much time

### Issue 正文摘录

I noticed that, the sampler stage uses lots of repeated cuda kernels. Seems you do sampling in a for loop, launch each kernel for a sequence? Why is this? BTW, do you compare the performance with FasterTransformer? I didn't see about this. Thank you! below is my code: ``` path = '/data/llm/hf-llama-7b/' llm = LLM(model=path) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) sampling_params.max_tokens = 1 cnt = 1 start = time.time() for i in range(cnt): with nvtx.annotate("generate", color="red"): outputs = llm.generate(prompt_token_ids = input_ids, sampling_params = sampling_params) end = time.time() prefill_ticks = (end - start) / cnt ```

## 现有链接修复摘要

#6442 [Core] Use numpy to speed up padded token processing

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: see about this. Thank you! below is my code: ``` path = '/data/llm/hf-llama-7b/' llm = LLM(model=path) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) sampling_params.max_tokens = 1 cnt = 1 start = time.ti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es too much time I noticed that, the sampler stage uses lots of repeated cuda kernels. Seems you do sampling in a for loop, launch each kernel for a sequence? Why is this? BTW, do you compare the performance with Faster...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: en_ids = input_ids, sampling_params = sampling_params) end = time.time() prefill_ticks = (end - start) / cnt ``` performance model_support;sampling_logits cuda;kernel;sampling #6442 [Core] Use numpy to speed up padded t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6442](https://github.com/vllm-project/vllm/pull/6442) | mentioned | 0.6 | [Core] Use numpy to speed up padded token processing | when running small models. (See benchmark results below) Related: #249 #5289 ## Benchmarks The following test was conducted on an NVIDIA A100 80GB GPU. ### Sampler latency |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
