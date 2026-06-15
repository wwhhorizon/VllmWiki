# vllm-project/vllm#10743: [Bug]: Making a request to the OpenAI API server with n=2 and best_of=2 fails

| 字段 | 值 |
| --- | --- |
| Issue | [#10743](https://github.com/vllm-project/vllm/issues/10743) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Making a request to the OpenAI API server with n=2 and best_of=2 fails

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When trying to make a streamed request for 2 samples with a best_of value of 2, I get an error telling me that `n` should be equal to `best_of` for streaming to be enabled (which it is). This can be worked around by not setting `best_of` in the request, which will give me what I want, but the error message is confusing. It should likely suggest setting `best_of` to 0 when you want to stream. Beyond the unintuitive API behaviour, I believe there is a slightly weird bug with best_of. I dug into the code to try and understand what was going on and I found that the problem is in `ParallelSampleSequenceGroup.add_request`: ```python class ParallelSampleSequenceGroup(SequenceGroupBase): @staticmethod def add_request(request_id: str, engine, params, **kwargs): original_params = params params = copy.deepcopy(original_params) params.n = 1 group = ParallelSampleSequenceGroup(request_id) seqs = [] for i in range(original_params.n): request_id_i = f"{request_id}_parallel_sample_{i}" group.seq_id_to_index[request_id_i] = i seq_group = engine._add_processed_request( request_id_i, params=params, **kwargs, ) #...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Making a request to the OpenAI API server with n=2 and best_of=2 fails bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When trying to make a streamed request for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e it would be the right behaviour for `best_of>n>1` cases. I would appreciate your thoughts on the correct approach to fix this issue. ## Reproducing the error Start a server on port 8000 with a model called `model`: ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h n=2 and best_of=2 fails bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When trying to make a streamed request for 2 samples with a best_of value of 2, I get an error...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
