# vllm-project/vllm#11775: [Bug]: data_parallel_size=4 or 2 not working for lighteval with vllm backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#11775](https://github.com/vllm-project/vllm/issues/11775) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: data_parallel_size=4 or 2 not working for lighteval with vllm backend.

### Issue 正文摘录

### Your current environment ### Model Input Dumps -rw-rw-rw- 1 ubuntu ubuntu 0 Jan 6 15:24 /tmp/9211bcadcfd6a7699ff787bebf5af3cbe779d1ffd33c8d68dcc65336c467745cmeta-llama-Llama-2-7b-chat-hf.lock for other errors, it was able to create pkl file, not for this one. -- Error Snip-- │ │ │ LoglikelihoodRequest( │ │ │ │ │ │ task_name='leaderboard|truthfulqa:mc|0', │ │ │ │ │ │ sample_index='1_0', │ │ │ │ │ │ request_index=1, │ │ │ │ │ │ context='Q: What is human life expectancy in the United │ │ │ │ States?\nA: Human life expectancy '+535, │ │ │ │ │ │ metric_categories=[ ], │ │ │ │ │ │ choice=' All French people are sophisticated.', │ │ │ │ │ │ tokenized_context=[ │ │ │ │ │ │ │ 1, │ │ │ │ │ │ │ 660, │ │ │ │ │ │ │ 29901, │ │ │ │ │ │ │ 1724, │ │ │ │ │ │ │ 338, │ │ │ │ │ │ │ 5199, │ │ │ │ │ │ │ 2834, │ │ │ │ │ │ │ 2149, │ │ │ │ │ │ │ 6906, │ │ │ │ │ │ │ 297, │ │ │ │ │ │ │ ... +185 │ │ │ │ │ │ ], │ │ │ │ │ │ tokenized_continuation=[ │ │ │ │ │ │ │ 2178, │ │ │ │ │ │ │ 5176, │ │ │ │ │ │ │ 2305, │ │ │ │ │ │ │ 526, │ │ │ │ │ │ │ 269, │ │ │ │ │ │ │ 3021, │ │ │ │ │ │ │ 4695, │ │ │ │ │ │ │ 630, │ │ │ │ │ │ │ 29889 │ │ │ │ │ │ ] │ │ │ │ │ ), │ │ │ │ │ ... +9986 │ │ │ │ ] │ │ │ │ res = [] │ │ │ │ retu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hteval with vllm backend. bug;stale ### Your current environment ### Model Input Dumps -rw-rw-rw- 1 ubuntu ubuntu 0 Jan 6 15:24 /tmp/9211bcadcfd6a7699ff787bebf5af3cbe779d1ffd33c8d68dcc65336c467745cmeta-llama-Llama-2-7b-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ta_parallel_size=4 or 2 not working for lighteval with vllm backend. bug;stale ### Your current environment ### Model Input Dumps -rw-rw-rw- 1 ubuntu ubuntu 0 Jan 6 15:24 /tmp/9211bcadcfd6a7699ff787bebf5af3cbe779d1ffd33...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: data_parallel_size=4 or 2 not working for lighteval with vllm backend. bug;stale ### Your current environment ### Model Input Dumps -rw-rw-rw- 1 ubuntu ubuntu 0 Jan 6 15:24 /tmp/9211bcadcfd6a7699ff787bebf5af3cbe7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: OD=spawn && lighteval vllm "pretrained=meta-llama/Llama-2-7b-chat-hf,dtype=float16,data_parallel_size=4" "leaderboard|truthfulqa:mc|0|0" tensor_parallel_size=4 works, is it because of the model/GPU the data_parallel_siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
