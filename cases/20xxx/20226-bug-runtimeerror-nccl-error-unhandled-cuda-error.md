# vllm-project/vllm#20226: [Bug]: RuntimeError: NCCL error: unhandled cuda error

| 字段 | 值 |
| --- | --- |
| Issue | [#20226](https://github.com/vllm-project/vllm/issues/20226) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: NCCL error: unhandled cuda error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to Gemma 3 27B with vllm==0.9.1, but I am getting this error ```bash (VllmWorker rank=1 pid=305150) DEBUG 06-29 19:19:58 [shm_broadcast.py:313] Connecting to ipc:///tmp/69ea0bbd-db87-4112-a486-0ef61eab157b (VllmWorker rank=0 pid=305149) DEBUG 06-29 19:19:58 [shm_broadcast.py:313] Connecting to ipc:///tmp/69ea0bbd-db87-4112-a486-0ef61eab157b (VllmWorker rank=1 pid=305150) DEBUG 06-29 19:19:58 [shm_broadcast.py:243] Binding to ipc:///tmp/9fd45adb-80db-4c70-8475-5e256abfecb0 (VllmWorker rank=0 pid=305149) DEBUG 06-29 19:19:58 [shm_broadcast.py:243] Binding to ipc:///tmp/ba3fa5c4-fda8-43d8-8abe-5a3dcb4ff26d (VllmWorker rank=1 pid=305150) INFO 06-29 19:19:58 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_026ab1a7'), local_subscribe_addr='ipc:///tmp/9fd45adb-80db-4c70-8475-5e256abfecb0', remote_subscribe_addr=None, remote_addr_ipv6=False) (VllmWorker rank=0 pid=305149) INFO 06-29 19:19:58 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_e6722dfc'), local_subs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ng eth0:159.103.253.238 vllm_node:305149:305149 [0] NCCL INFO cudaDriverVersion 12020 vllm_node:305149:305149 [0] NCCL INFO NCCL version 2.26.2+cuda12.2 vllm_node:305150:305150 [1] NCCL INFO cudaDriverVersion 12020 vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: size=2 rank=0 local_rank=0 distributed_init_method=tcp://127.0.0.1:40035 backend=nccl (VllmWorker rank=1 pid=305150) DEBUG 06-29 19:19:59 [parallel_state.py:918] world_size=2 rank=1 local_rank=1 distributed_init_method=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: CE export CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve /models/gemma-3-27b-it-FP8-Dynamic/ --tensor-parallel-size 2 --gpu-memory-utilization 0.8 ``` ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: NCCL error: unhandled cuda error bug ### Your current environment ### 🐛 Describe the bug I am trying to Gemma 3 27B with vllm==0.9.1, but I am getting this error ```bash (VllmWorker rank=1 pid=30515...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug I am trying to Gemma 3 27B with vllm==0.9.1, but I am getting this error ```bash (VllmWorker rank=1 pid=305150) DEBUG 06-29 19:19:58 [shm_broadcast.py:313] Connecting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
