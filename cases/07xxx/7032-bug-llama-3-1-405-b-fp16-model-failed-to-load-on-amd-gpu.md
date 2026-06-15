# vllm-project/vllm#7032: [Bug]: Llama 3.1 405 B  FP16 model failed to load on AMD GPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#7032](https://github.com/vllm-project/vllm/issues/7032) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama 3.1 405 B  FP16 model failed to load on AMD GPU 

### Issue 正文摘录

### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct 8 x AMD MI300x GPU ### 🐛 Describe the bug ``` services: vllm-serving: container_name: vllm-serving image: vllm-rocm:v0.5.3.post1 environment: - LLM_MODEL=$LLM_MODEL - HUGGING_FACE_HUB_TOKEN=$HF_TOKEN command: > sh -c " python3 -m vllm.entrypoints.openai.api_server \ --model $LLM_MODEL --dtype float16 \ --tensor-parallel-size 8 " devices: - /dev/kfd - /dev/dri group_add: - video volumes: - /mnt/model/:/models/ shm_size: 16G ports: - 8000:8000 ``` [rank0]: huggingface_hub.utils._errors.HfHubHTTPError: 416 Client Error: Requested Range Not Satisfiable for url: https://cdn-lfs-us- ..... ERROR 08-01 07:45:19 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 76 died, exit code: -15 INFO 08-01 07:45:19 multiproc_worker_utils.py:123] Killing local vLLM worker processes /opt/conda/envs/py_3.9/lib/python3.9/multiprocessing/resource_tracker.py:216: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ![Screenshot 2024-08-01 152943](https://github.com/user-attachme...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama 3.1 405 B FP16 model failed to load on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct 8 x AMD MI300x GPU ### 🐛 Describe the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Llama 3.1 405 B FP16 model failed to load on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct 8 x AMD MI300x GPU ### 🐛 Describe the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: thon3 -m vllm.entrypoints.openai.api_server \ --model $LLM_MODEL --dtype float16 \ --tensor-parallel-size 8 " devices: - /dev/kfd - /dev/dri group_add: - video volumes: - /mnt/model/:/models/ shm_size: 16G ports: - 8000...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l failed to load on AMD GPU bug;rocm ### Your current environment vLLM version: 0.5.3.post1 (For ROCm) Model: meta-llama/Meta-Llama-3.1-405B-Instruct 8 x AMD MI300x GPU ### 🐛 Describe the bug ``` services: vllm-serving:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [rank0]: huggingface_hub.utils._errors.HfHubHTTPError: 416 Client Error: Requested Range Not Satisfiable for url: https://cdn-lfs-us- ..... ERROR 08-01 07:45:19 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
