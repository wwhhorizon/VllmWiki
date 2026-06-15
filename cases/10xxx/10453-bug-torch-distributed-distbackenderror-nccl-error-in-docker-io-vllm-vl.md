# vllm-project/vllm#10453: [Bug] torch.distributed.DistBackendError: NCCL error in  docker.io/vllm/vllm-openai:v0.6.4.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#10453](https://github.com/vllm-project/vllm/issues/10453) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] torch.distributed.DistBackendError: NCCL error in  docker.io/vllm/vllm-openai:v0.6.4.post1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run model in docker.io/vllm/vllm-openai:v0.6.4.post1 ``` docker.io/vllm/vllm-openai:latest \ --model Qwen/Qwen2-VL-72B-Instruct \ --served-model-name "Qwen2-VL-72B" \ --port 8003 \ --gpu-memory-utilization 0.95 \ --tensor-parallel-size 4 ``` and got ``` INFO 11-19 06:08:46 utils.py:961] Found nccl from library libnccl.so.2 INFO 11-19 06:08:46 pynccl.py:69] vLLM is using nccl==2.21.5 (VllmWorkerProcess pid=409) INFO 11-19 06:08:46 utils.py:961] Found nccl from library libnccl.so.2 (VllmWorkerProcess pid=409) INFO 11-19 06:08:46 pynccl.py:69] vLLM is using nccl==2.21.5 (VllmWorkerProcess pid=411) INFO 11-19 06:08:46 utils.py:961] Found nccl from library libnccl.so.2 (VllmWorkerProcess pid=411) INFO 11-19 06:08:46 pynccl.py:69] vLLM is using nccl==2.21.5 (VllmWorkerProcess pid=409) ERROR 11-19 06:08:46 multiproc_worker_utils.py:229] Exception in worker VllmWorkerProcess while processing method init_device. (VllmWorkerProcess pid=409) ERROR 11-19 06:08:46 multiproc_worker_utils.py:229] Traceback (most recent call last): (VllmWorkerProcess pid=409) ERROR 11-19 06:08:46 multiproc_worker_ut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug] torch.distributed.DistBackendError: NCCL error in docker.io/vllm/vllm-openai:v0.6.4.post1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run model in docker....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ue to the NCCL developers ``` I have the latest nvidia drivers ``` root@h100-2:~/victor# nvidia-smi Tue Nov 19 14:49:02 2024 +-----------------------------------------------------------------------------------------+ |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: o/vllm/vllm-openai:v0.6.4.post1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run model in docker.io/vllm/vllm-openai:v0.6.4.post1 ``` docker.io/vllm/vllm-openai:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug] torch.distributed.DistBackendError: NCCL error in docker.io/vllm/vllm-openai:v0.6.4.post1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run model in docker....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
