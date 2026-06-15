# vllm-project/vllm#12426: [Bug]: vLLM doesn't run on M4 Macbook Pro

| 字段 | 值 |
| --- | --- |
| Issue | [#12426](https://github.com/vllm-project/vllm/issues/12426) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM doesn't run on M4 Macbook Pro

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I built the vLLM following the instructions on my M4 Macbook Pro. When I tried to run the DeepSeek R1 model with it using the command below ```bash $ vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --tensor-parallel-size 2 --max-model-len 32768 --enforce-eager ``` I got the following error ``` INFO 01-25 15:05:01 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_64ea17a8'), local_subscribe_port=56349, remote_subscribe_port=None) (VllmWorkerProcess pid=35133) ERROR 01-25 15:05:01 multiproc_worker_utils.py:240] Exception in worker VllmWorkerProcess while processing method init_device. (VllmWorkerProcess pid=35133) ERROR 01-25 15:05:01 multiproc_worker_utils.py:240] Traceback (most recent call last): (VllmWorkerProcess pid=35133) ERROR 01-25 15:05:01 multiproc_worker_utils.py:240] File "/Users/ /code/pyvenv/vllm/vllm/vllm/executor/multiproc_worker_utils.py", line 234, in _run_worker_process (VllmWorkerProcess pid=35133) ERROR 01-25 15:05:01 multiproc_worker_utils.py:240] output = run_method(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support cuda build_error;crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: _ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_64ea17a8'), local_subscribe_port=56349, remote_subscribe_port=None) (VllmWorkerProcess pid=35133) ERROR 01-25 15:05:01 multiproc_worker_utils.p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: M doesn't run on M4 Macbook Pro bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I built the vLLM following the instructions on my M4 Macbook Pro. When I tried to run the DeepS...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: llowing error ``` INFO 01-25 15:05:01 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_64ea17a8'), local_subscribe_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support cuda build_e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
