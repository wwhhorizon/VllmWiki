# vllm-project/vllm#13686: [Bug]: OLMo 2 does not split qkv correctly for grouped query attention

| 字段 | 值 |
| --- | --- |
| Issue | [#13686](https://github.com/vllm-project/vllm/issues/13686) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OLMo 2 does not split qkv correctly for grouped query attention

### Issue 正文摘录

### Your current environment I do not have access to the environment anymore, but the bug and its fix are straightforward. ### 🐛 Describe the bug OLMo 2 does not correctly do attention when the number of heads is not the same as the number of kv heads (i.e. GQA or MQA is used instead of MHA). Specifically, it splits qkv into equal chunks rather than chunks based on q, k, v size. The fix is a 1-liner. I don't have a minimal repro, but below is the stack trace caused by using OLMo 2 for GQA. ``` Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks. Traceback (most recent call last): File "/opt/conda/lib/python3.11/site-packages/vllm/executor/multiproc_worker_utils.py", line 236, in _run_worker_process output = run_method(worker, method, args, kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/site-packages/vllm/utils.py", line 2220, in run_method return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/site-packages/vllm/worker/worker....

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py", line 229, in determine_num_available_blocks self.model_runner.profile_run() File "/opt/conda/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) ^^...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e as the number of kv heads (i.e. GQA or MQA is used instead of MHA). Specifically, it splits qkv into equal chunks rather than chunks based on q, k, v size. The fix is a 1-liner. I don't have a minimal repro, but below...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: worker VllmWorkerProcess while processing method determine_num_available_blocks. Traceback (most recent call last): File "/opt/conda/lib/python3.11/site-packages/vllm/executor/multiproc_worker_utils.py", line 236, in _r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /worker/worker.py", line 229, in determine_num_available_blocks self.model_runner.profile_run() File "/opt/conda/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args,...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
