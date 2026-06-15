# vllm-project/vllm#6668: [Bug]  model:DeepSeek-V2-Chat-0628   bug: ChildProcessError: worker died

| 字段 | 值 |
| --- | --- |
| Issue | [#6668](https://github.com/vllm-project/vllm/issues/6668) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]  model:DeepSeek-V2-Chat-0628   bug: ChildProcessError: worker died

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ![image](https://github.com/user-attachments/assets/ccdaeb85-4bc1-4f9c-b197-2973397a74f3) ### 🐛 Describe the bug (VllmWorkerProcess pid=1791034) Process VllmWorkerProcess: (VllmWorkerProcess pid=1791035) Process VllmWorkerProcess: (VllmWorkerProcess pid=1791034) Traceback (most recent call last): (VllmWorkerProcess pid=1791034) File "/mnt/pfs/zhangfan/system/test/conda/envs/swift/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap (VllmWorkerProcess pid=1791034) self.run() (VllmWorkerProcess pid=1791034) File "/mnt/pfs/zhangfan/system/test/conda/envs/swift/lib/python3.10/multiprocessing/process.py", line 108, in run (VllmWorkerProcess pid=1791034) self._target(*self._args, **self._kwargs) (VllmWorkerProcess pid=1791034) File "/mnt/pfs/zhangfan/system/test/conda/envs/swift/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 210, in _run_worker_process (VllmWorkerProcess pid=1791034) worker = worker_factory() (VllmWorkerProcess pid=1791034) File "/mnt/pfs/zhangfan/system/test/conda/envs/swift/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 70, in _...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d") from e ChildProcessError: worker died development attention_kv_cache;ci_build;model_support attention;cuda crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e 148, in which_attn_to_use (VllmWorkerProcess pid=1791034) if torch.cuda.get_device_capability()[0] is closed The above exception was the direct cause of the following exception: Traceback (most recent call last): File...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] model:DeepSeek-V2-Chat-0628 bug: ChildProcessError: worker died bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ![image](https://github.com/user-attachments/assets/ccdaeb85...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ] model:DeepSeek-V2-Chat-0628 bug: ChildProcessError: worker died bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ![image](https://github.com/user-attachments/assets/ccdaeb85-4bc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: py", line 229, in __init__ (VllmWorkerProcess pid=1791034) self.attn_backend = get_attn_backend( (VllmWorkerProcess pid=1791034) File "/mnt/pfs/zhangfan/system/test/conda/envs/swift/lib/python3.10/site-packages/vllm/att...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
