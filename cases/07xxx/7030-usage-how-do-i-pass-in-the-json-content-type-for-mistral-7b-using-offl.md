# vllm-project/vllm#7030: [Usage]: how do I pass in the JSON content-type for Mistral 7B using offline inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#7030](https://github.com/vllm-project/vllm/issues/7030) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how do I pass in the JSON content-type for Mistral 7B using offline inference?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to use the [JSON mode](https://docs.mistral.ai/capabilities/json_mode/) for Mistral 7B while doing offline inference using the `generate` method as below. Is that possible somehow? Just using the prompt doesn't seem to produce JSON output as requested. If this is not possible, is the only solution to use something like [Outlines](https://github.com/outlines-dev/outlines)? Would love some details on that, if so. ``` llm = LLM(model="mistralai/Mistral-7B-v0.3") prompt = "Please name the biggest and smallest continent in JSON using the following schema: {biggest: , smallest: }" sampling_params = SamplingParams(temperature=temperature, top_p=1.0) response = self.llm.generate(prompt, sampling_params) ```

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: model="mistralai/Mistral-7B-v0.3") prompt = "Please name the biggest and smallest continent in JSON using the following schema: {biggest: , smallest: }" sampling_params = SamplingParams(temperature=temperature, top_p=1....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: es-dev/outlines)? Would love some details on that, if so. ``` llm = LLM(model="mistralai/Mistral-7B-v0.3") prompt = "Please name the biggest and smallest continent in JSON using the following schema: {biggest: , smalles...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: le somehow? Just using the prompt doesn't seem to produce JSON output as requested. If this is not possible, is the only solution to use something like [Outlines](https://github.com/outlines-dev/outlines)? Would love so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
