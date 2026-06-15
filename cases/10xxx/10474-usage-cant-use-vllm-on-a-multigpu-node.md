# vllm-project/vllm#10474: [Usage]: Cant use vllm on a multiGPU node

| 字段 | 值 |
| --- | --- |
| Issue | [#10474](https://github.com/vllm-project/vllm/issues/10474) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Cant use vllm on a multiGPU node

### Issue 正文摘录

### Your current environment [collect_env.txt](https://github.com/user-attachments/files/17825470/collect_env.txt) ### How would you like to use vllm model: meta-llama/Llama3-8B-Instruct quantization: none tensor_parallel_size: 2 GPUs: 2xA30 vllm: 0.6.4.post1v (also tried with 0.5.4 and 0.5.0) strongly related to this issue: https://github.com/vllm-project/vllm/issues/6152 Can't run the script for multi GPUs (it works for a single GPU). Teh following error occurs: (VllmWorkerProcess pid=13824) ERROR 11-20 12:20:01 multiproc_worker_utils.py:226] RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method I tried to set env variavle to "spawn" or use the latest vllm version: os.environ["VLLM_WORKER_MULTIPROC_METHOD"]="spawn" The problems is that the calling script runs the script again as a child process , but this is not the desired behavior. And as expected, the following error is thrown: ================================================================================ RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase. This probably m...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ### How would you like to use vllm model: meta-llama/Llama3-8B-Instruct quantization: none tensor_parallel_size: 2 GPUs: 2xA30 vllm: 0.6.4.post1v (also tried with 0.5.4 and 0.5.0) strongly related to this issue: https:/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nts/files/17825470/collect_env.txt) ### How would you like to use vllm model: meta-llama/Llama3-8B-Instruct quantization: none tensor_parallel_size: 2 GPUs: 2xA30 vllm: 0.6.4.post1v (also tried with 0.5.4 and 0.5.0) str...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Cant use vllm on a multiGPU node usage;stale ### Your current environment [collect_env.txt](https://github.com/user-attachments/files/17825470/collect_env.txt) ### How would you like to use vllm model: meta-lla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rt method I tried to set env variavle to "spawn" or use the latest vllm version: os.environ["VLLM_WORKER_MULTIPROC_METHOD"]="spawn" The problems is that the calling script runs the script again as a child process , but...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: :20:01 multiproc_worker_utils.py:226] RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method I tried to set env variavle to "spawn" or use t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
