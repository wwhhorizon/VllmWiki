# vllm-project/vllm#20431: [Bug]: some error when training in ray

| 字段 | 值 |
| --- | --- |
| Issue | [#20431](https://github.com/vllm-project/vllm/issues/20431) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: some error when training in ray

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I use the verl to for training, sometimes a error occured: ``` Fatal Python error: none_dealloc: deallocating None [36m(WorkerDict pid=494481)[0m Python runtime state: initialized [36m(WorkerDict pid=494481)[0m [36m(WorkerDict pid=494481)[0m Thread 0x00007f36860ff640 (most recent call first): [36m(WorkerDict pid=494481)[0m [36m(WorkerDict pid=494481)[0m [36m(WorkerDict pid=494481)[0m Thread 0x00007f3687bfd640 (most recent call first): [36m(WorkerDict pid=494481)[0m File "/home/linxiang/miniconda3/envs/DAPO/lib/python3.10/site-packages/vllm/usage/usage_lib.py", line 229 in _report_continous_usage [36m(WorkerDict pid=494481)[0m File "/home/linxiang/miniconda3/envs/DAPO/lib/python3.10/site-packages/vllm/usage/usage_lib.py", line 164 in _report_usage_worker [36m(WorkerDict pid=494481)[0m File "/home/linxiang/miniconda3/envs/DAPO/lib/python3.10/threading.py", line 946 in run [36m(WorkerDict pid=494481)[0m File "/home/linxiang/miniconda3/envs/DAPO/lib/python3.10/threading.py", line 1009 in _bootstrap_inner [36m(WorkerDict pid=494481)[0m File "/home/linxiang/miniconda3/envs/DAPO/lib/python3.10/threading.py", l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nxiang/miniconda3/envs/DAPO/lib/python3.10/site-packages/torch/_inductor/compile_worker/subproc_pool.py", line 53 in _recv_msg [36m(WorkerDict pid=494481)[0m File "/home/linxiang/miniconda3/envs/DAPO/lib/python3.10/si...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ', 'algorithm.filter_groups.metric=seq_final_reward', 'actor_rollout_ref.model.use_remove_padding=False', 'actor_rollout_ref.actor.use_dynamic_bsz=False', 'actor_rollout_ref.ref.log_prob_use_dynamic_bsz=False', 'actor_r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: as._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.lib, pyarrow._compute, pandas._lib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0.5.6 compressed-tensors 0.9.2 cupy-cuda12x 13.4.1 datasets 3.6.0 Deprecated 1.2.18 depyf 0.18.0 dill
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: , psutil._psutil_posix, setproctitle, yaml._yaml, charset_normalizer.md, requests.packages.charset_normalizer.md, requests.packages.chardet.md, uvloop.loop, ray._raylet, numpy._core._multiarray_umath, numpy.linalg._umat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
