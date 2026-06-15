# vllm-project/vllm#3053: Fatal Python error: Segmentation fault

| 字段 | 值 |
| --- | --- |
| Issue | [#3053](https://github.com/vllm-project/vllm/issues/3053) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Fatal Python error: Segmentation fault

### Issue 正文摘录

*** SIGSEGV received at time=1709021359 on cpu 44 *** PC: @ 0x7f3c5f628350 (unknown) (unknown) @ 0x7f3c945c8630 (unknown) (unknown) @ 0x55b11321eaf0 1247139872 (unknown) @ ... and at least 2 more frames [2024-02-27 16:09:19,106 E 19394 19394] logging.cc:361: *** SIGSEGV received at time=1709021359 on cpu 44 *** [2024-02-27 16:09:19,108 E 19394 19394] logging.cc:361: PC: @ 0x7f3c5f628350 (unknown) (unknown) [2024-02-27 16:09:19,108 E 19394 19394] logging.cc:361: @ 0x7f3c945c8630 (unknown) (unknown) [2024-02-27 16:09:19,110 E 19394 19394] logging.cc:361: @ 0x55b11321eaf0 1247139872 (unknown) [2024-02-27 16:09:19,110 E 19394 19394] logging.cc:361: @ ... and at least 2 more frames Fatal Python error: Segmentation fault Stack (most recent call first): File "/root/.conda/envs/py39/lib/python3.9/site-packages/torch/cuda/graphs.py", line 77 in capture_begin File "/root/.conda/envs/py39/lib/python3.9/site-packages/torch/cuda/graphs.py", line 192 in __enter__ File "/root/.conda/envs/py39/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 782 in capture File "/root/.conda/envs/py39/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 725 in capture_model File "/root/.co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: o/xli/Coder/service/dev/service/model_infer.py", line 268 in development ci_build cuda crash env_dependency *** SIGSEGV received at time=1709021359 on cpu 44 ***
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _ File "/root/.conda/envs/py39/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 782 in capture File "/root/.conda/envs/py39/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 725 in capture_mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: first): File "/root/.conda/envs/py39/lib/python3.9/site-packages/torch/cuda/graphs.py", line 77 in capture_begin File "/root/.conda/envs/py39/lib/python3.9/site-packages/torch/cuda/graphs.py", line 192 in __enter__ File...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Fatal Python error: Segmentation fault stale *** SIGSEGV received at time=1709021359 on cpu 44 *** PC: @ 0x7f3c5f628350 (unknown) (unknown) @ 0x7f3c945c8630 (unknown) (unknown) @ 0x55b11321eaf0 1247139872 (unknown) @ .....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
