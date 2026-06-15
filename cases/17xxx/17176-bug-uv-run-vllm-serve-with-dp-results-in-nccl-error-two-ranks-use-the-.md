# vllm-project/vllm#17176: [Bug]: `uv run vllm serve` with DP results in NCCL error: two ranks use the same device

| 字段 | 值 |
| --- | --- |
| Issue | [#17176](https://github.com/vllm-project/vllm/issues/17176) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `uv run vllm serve` with DP results in NCCL error: two ranks use the same device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (Originally discussed [here](https://github.com/vllm-project/vllm/pull/13923#issuecomment-2817827794).) When trying to serve the model with DP, the following error occurred: ```python $ uv run vllm serve /path/to/model --port 8088 --served-model-name xxx --data-parallel-size 2 ... myhost:2292596:2292596 [0] init.cc:943 NCCL WARN Duplicate GPU detected : rank 0 and rank 1 both on CUDA device 53000 myhost:2292597:2292597 [0] init.cc:943 NCCL WARN Duplicate GPU detected : rank 1 and rank 0 both on CUDA device 53000 ... (EngineCore_1 pid=2292597) File "/ephnvme/colin/code/prizetrain/.venv/lib/python3.12/site-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 39, in __init__ (EngineCore_0 pid=2292596) self.NCCL_CHECK(self._funcs["ncclCommInitRank"](ctypes.byref(comm), (EngineCore_1 pid=2292597) self.pynccl_comm = PyNcclCommunicator( (EngineCore_0 pid=2292596) File "/ephnvme/colin/code/prizetrain/.venv/lib/python3.12/site-packages/vllm/distributed/device_communicators/pynccl_wrapper.py", line 256, in NCCL_CHECK (EngineCore_1 pid=2292597) ^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=2292596) raise RuntimeError(f"NCCL er...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ever, if I just use a conda environment without `uv`, with the same vllm version, running `vllm serve ... -dp 2`, the error above will not happen. ### Before submitting a new issue... - [x] Make sure you already searche...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: init.cc:943 NCCL WARN Duplicate GPU detected : rank 0 and rank 1 both on CUDA device 53000 myhost:2292597:2292597 [0] init.cc:943 NCCL WARN Duplicate GPU detected : rank 1 and rank 0 both on CUDA device 53000 ... (Engin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: serve` with DP results in NCCL error: two ranks use the same device bug;stale ### Your current environment ### 🐛 Describe the bug (Originally discussed [here](https://github.com/vllm-project/vllm/pull/13923#issuecomment...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ject/vllm/pull/13923#issuecomment-2817827794).) When trying to serve the model with DP, the following error occurred: ```python $ uv run vllm serve /path/to/model --port 8088 --served-model-name xxx --data-parallel-size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
