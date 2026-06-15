# vllm-project/vllm#11485: 通过命令行启动api_serverException in worker VllmWorkerProcess while processing method determine_num_available_blocks: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#11485](https://github.com/vllm-project/vllm/issues/11485) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 通过命令行启动api_serverException in worker VllmWorkerProcess while processing method determine_num_available_blocks: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

pytorch 2.3.0 vllm 0.5.0.post1 transformers 4.40.0 cuda12.1 cuda设备Tesla t4 系统信息: Linux ubuntu-13 6.8.0-49-generic #49-Ubuntu SMP PREEMPT_DYNAMIC Mon Nov 4 02:06:24 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux root@ubuntu-13:/app# nvidia-smi Wed Dec 25 15:06:57 2024 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.183.01 Driver Version: 535.183.01 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 Tesla T4 Off | 00000000:04:00.0 Off | 0 | | N/A 31C P8 9W / 70W | 6MiB / 15360MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ | 1 Tesla T4 Off | 00000000:05:00.0 Off | 0 | | N/A 31C P8 9W / 70W | 6MiB / 15360MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ (python31013new) root@ubuntu-13:/app/dms...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: CUDA error: no kernel image is available for execution on the device bug;stale pytorch 2.3.0 vllm 0.5.0.post1 transformers 4.40.0 cuda12.1 cuda设备Tesla t4 系统信息: Linux ubuntu-13 6.8.0-49-generic #49-Ubuntu SMP PREEMPT_DYN...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ----------------------------+ | NVIDIA-SMI 535.183.01 Driver Version: 535.183.01 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: worker VllmWorkerProcess while processing method determine_num_available_blocks: CUDA error: no kernel image is available for execution on the device bug;stale pytorch 2.3.0 vllm 0.5.0.post1 transformers 4.40.0 cuda12.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: > --tensor-parallel-size 2 \ > --gpu-memory-utilization 0.95 \ > --dtype float16 \ > --block-size 8 \ > --port 8001 \ > --host 20.10.1.13 INFO 12-25 12:04:04 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 13:/app/dms_GLM4# python -m vllm.entrypoints.openai.api_server \ > --model /app/models/glm-4-9b-chat \ > --served-model-name glm-api \ > --trust-remote-code \ > --enforce-eager \ > --enable-lora \ > --lora-modules 'ldjh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
