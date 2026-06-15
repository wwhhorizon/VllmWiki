# vllm-project/vllm#31375: [Bug]: vLLM online serve ByteDance-Seed/BAGEL-7B-MoT model error

| 字段 | 值 |
| --- | --- |
| Issue | [#31375](https://github.com/vllm-project/vllm/issues/31375) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM online serve ByteDance-Seed/BAGEL-7B-MoT model error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: We are trying to serve the BAGEL-7B-MoT on our server, and we get the following error: AssertionError: Expected multimodal embeddings to be a list/tuple of 2D tensors, or a single 3D tensor, but got instead. This is most likely due to the incorrect implementation of the model's `embed_multimodal` method. Here are our command and error logs. My command: ``` vllm serve ByteDance-Seed/BAGEL-7B-MoT \ --host 0.0.0.0 \ --port 8022 \ --max-model-len 8192 ``` logs: (Worker_TP1 pid=1156) ERROR 12-25 20:59:15 [multiproc_executor.py:824] WorkerProc hit an exception. (Worker_TP1 pid=1156) ERROR 12-25 20:59:15 [multiproc_executor.py:824] Traceback (most recent call last): (Worker_TP1 pid=1156) ERROR 12-25 20:59:15 [multiproc_executor.py:824] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop (Worker_TP1 pid=1156) ERROR 12-25 20:59:15 [multiproc_executor.py:824] output = func(*args, **kwargs) (Worker_TP1 pid=1156) ERROR 12-25 20:59:15 [multiproc_executor.py:824] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=1156) ERROR 12-25 20:59:15 [multiproc_executor.py:824] File "/usr/l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM online serve ByteDance-Seed/BAGEL-7B-MoT model error bug;stale ### Your current environment ### 🐛 Describe the bug Description: We are trying to serve the BAGEL-7B-MoT on our server, and we get the following...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n outputs. You'll still be able to use a slow processor with `use_fast=False`. (Worker_TP0 pid=1155) WARNING 12-25 20:59:15 [processing.py:1153] BagelProcessor did not return `BatchFeature`. Make sure to match the behav...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vLLM online serve ByteDance-Seed/BAGEL-7B-MoT model error bug;stale ### Your current environment ### 🐛 Describe the bug Description: We are trying to serve the BAGEL-7B-MoT on our server, and we get the following...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
