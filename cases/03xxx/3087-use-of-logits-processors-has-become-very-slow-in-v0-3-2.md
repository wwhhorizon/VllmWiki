# vllm-project/vllm#3087: Use of `logits_processors` has become very slow in v0.3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#3087](https://github.com/vllm-project/vllm/issues/3087) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Use of `logits_processors` has become very slow in v0.3.2

### Issue 正文摘录

I am using vLLM together with [`outlines`](https://github.com/outlines-dev/outlines) for structured generation. After having upgraded from v0.3.2, generation became very slow, and the RAM usage leads to OOM crashes now. Here is a minimal example: ```python from vllm import LLM, SamplingParams from outlines.serve.vllm import JSONLogitsProcessor from pydantic import BaseModel, conlist import datetime as dt class Output(BaseModel): names: conlist(str, max_length=5) organizations: conlist(str, max_length=5) locations: conlist(str, max_length=5) miscellanous: conlist(str, max_length=5) llm = LLM('mistralai/Mistral-7B-v0.1', max_model_len=10_000, gpu_memory_utilization=0.9) logits_processor = JSONLogitsProcessor(schema=Output, llm=llm.llm_engine) logits_processor.fsm.vocabulary = list(logits_processor.fsm.vocabulary) prompt = """ Locate all the names, organizations, locations and other miscellaneous entities in the following sentence: "Charles went and saw Anna at the coffee shop Starbucks, which was based in a small town in Germany called Essen." """ sampling_params = SamplingParams(max_tokens=128, temperature=0, logits_processors=[logits_processor]) t0 = dt.datetime.now() llm.generate...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ads to OOM crashes now. Here is a minimal example: ```python from vllm import LLM, SamplingParams from outlines.serve.vllm import JSONLogitsProcessor from pydantic import BaseModel, conlist import datetime as dt class O...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: JSONLogitsProcessor(schema=Output, llm=llm.llm_engine) logits_processor.fsm.vocabulary = list(logits_processor.fsm.vocabulary) prompt = """ Locate all the names, organizations, locations and other miscellaneous entities...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ded from v0.3.2, generation became very slow, and the RAM usage leads to OOM crashes now. Here is a minimal example: ```python from vllm import LLM, SamplingParams from outlines.serve.vllm import JSONLogitsProcessor fro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: outlines.serve.vllm import JSONLogitsProcessor from pydantic import BaseModel, conlist import datetime as dt class Output(BaseModel): names: conlist(str, max_length=5) organizations: conlist(str, max_length=5) locations...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
