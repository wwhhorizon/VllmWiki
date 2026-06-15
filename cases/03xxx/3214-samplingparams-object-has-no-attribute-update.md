# vllm-project/vllm#3214: 'SamplingParams' object has no attribute update

| 字段 | 值 |
| --- | --- |
| Issue | [#3214](https://github.com/vllm-project/vllm/issues/3214) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 'SamplingParams' object has no attribute update

### Issue 正文摘录

Hi, I got this error after updating `vllm` and `transformers`: ``` Traceback (most recent call last): File "/user/work/ad20999/1lm-rephrase/evaluate_gpt_rephrase_vllm.py", line 576, in main() File "/user/work/ad20999/1lm-rephrase/evaluate_gpt_rephrase_vllm.py", line 480, in main outputs = model.generate(inputs, sampling_params) File "/user/work/ad20999/anaconda3/envs/vltm/lib/python3.10/site-packages/awq/models/base.py", line 110, in generate return self.model.generate(*args, **kwargs) File "/user/work/ad20999/anaconda3/envs/vltm/lib/python3.10/site-packages/torch/utils/contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/user/work/ad20999/anaconda3/envs/vltm/lib/python3.10/site-packages/transformers/generation/utils.py", line 1349, in generate model_kwargs = generation_config.update(**kwargs) # All unused kwargs must be model kwargs AttributeError: 'SamplingParams' object has no attribute 'update' ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rephrase/evaluate_gpt_rephrase_vllm.py", line 480, in main outputs = model.generate(inputs, sampling_params) File "/user/work/ad20999/anaconda3/envs/vltm/lib/python3.10/site-packages/awq/models/base.py", line 110, in ge...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 'SamplingParams' object has no attribute update stale Hi, I got this error after updating `vllm` and `transformers`: ``` Traceback (most recent call last): File "/user/work/ad20999/1lm-rephrase/evaluate_gpt_rephrase_vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Traceback (most recent call last): File "/user/work/ad20999/1lm-rephrase/evaluate_gpt_rephrase_vllm.py", line 576, in main() File "/user/work/ad20999/1lm-rephrase/evaluate_gpt_rephrase_vllm.py", line 480, in main output...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
