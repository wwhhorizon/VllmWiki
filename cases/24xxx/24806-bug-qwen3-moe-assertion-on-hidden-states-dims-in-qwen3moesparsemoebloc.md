# vllm-project/vllm#24806: [Bug]: Qwen3-moe assertion on hidden_states dims in Qwen3MoeSparseMoeBlock

| 字段 | 值 |
| --- | --- |
| Issue | [#24806](https://github.com/vllm-project/vllm/issues/24806) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3-moe assertion on hidden_states dims in Qwen3MoeSparseMoeBlock

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Assertion introduced in #24772 is problematic for 3d `hidden_states`: [qwen3_moe.py#L173-174](https://github.com/vllm-project/vllm/blob/3beadc2f25d1111db6a5efee52d5cfe2ccf28d45/vllm/model_executor/models/qwen3_moe.py#L173-L174). Below error is observed on Gaudi3 with [vllm-guadi-plugin](https://github.com/vllm-project/vllm-gaudi) ``` [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR 09-13 16:16:10 [multiproc_executor.py:672] Traceback (most recent call last): [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR 09-13 16:16:10 [multiproc_executor.py:672] File "/software/users/tattafos/vllm-plugin/vllm-upstream/vllm/v1/executor/multiproc_executor.py", line 667, in worker_busy_loop [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR 09-13 16:16:10 [multiproc_executor.py:672] output = func(*args, **kwargs) [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR 09-13 16:16:10 [multiproc_executor.py:672] ^^^^^^^^^^^^^^^^^^^^^ [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR 09-13 16:16:10 [multiproc_executor.py:672] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR...

## 现有链接修复摘要

#24772 [Compilation Bug] Fix Inductor Graph Output with Shape Issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-moe assertion on hidden_states dims in Qwen3MoeSparseMoeBlock bug ### Your current environment ### 🐛 Describe the bug Assertion introduced in #24772 is problematic for 3d `hidden_states`: [qwen3_moe.py#L173...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [multiproc_executor.py:672] output = self.model_runner.execute_model(scheduler_output) [1;36m(Worker_TP0_EP0 pid=66093)[0;0m ERROR 09-13 16:16:10 [multiproc_executor.py:672] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape #24772 [Compilation Bug] Fix Inductor Graph Output with Shape Issue Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24772](https://github.com/vllm-project/vllm/pull/24772) | mentioned | 0.45 | [Compilation Bug] Fix Inductor Graph Output with Shape Issue | 1 ``` </details> ### 🐛 describe the bug assertion introduced in #24772 is problematic for 3d `hidden_states`: [qwen3_moe.py#l173-174](https://github.com/vllm-project/vllm/blob/3bea |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
