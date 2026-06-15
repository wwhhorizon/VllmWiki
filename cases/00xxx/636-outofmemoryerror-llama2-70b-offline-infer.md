# vllm-project/vllm#636: OutOfMemoryError Llama2-70b offline_infer

| 字段 | 值 |
| --- | --- |
| Issue | [#636](https://github.com/vllm-project/vllm/issues/636) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OutOfMemoryError Llama2-70b offline_infer

### Issue 正文摘录

code ``` nvidia-smi 8GPUS A800 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 470.161.03 Driver Version: 470.161.03 CUDA Version: 11.7 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 NVIDIA A800-SXM... On | 00000000:65:01.0 Off | 0 | | N/A 30C P0 62W / 400W | 0MiB / 81251MiB | 0% Default | | | | Disabled | +-------------------------------+----------------------+----------------------+ | 1 NVIDIA A800-SXM... On | 00000000:65:02.0 Off | 0 | | N/A 31C P0 61W / 400W | 0MiB / 81251MiB | 0% Default | | | | Disabled | +-------------------------------+----------------------+----------------------+ | 2 NVIDIA A800-SXM... On | 00000000:67:01.0 Off | 0 | | N/A 31C P0 62W / 400W | 0MiB / 81251MiB | 0% Default | | | | Disabled | +-------------------------------+----------------------+----------------------+ | 3 NVIDIA A800-SXM... On | 00000000:67:02.0 Off | 0 | | N/A 30C P0 61W / 400W |...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: OutOfMemoryError Llama2-70b offline_infer code ``` nvidia-smi 8GPUS A800 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 470.161.03 Driver Version: 470.161.03 CUDA Version: 1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --------------------------------------+ | NVIDIA-SMI 470.161.03 Driver Version: 470.161.03 CUDA Version: 11.7 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 048, frequency_penalty=1.1) # Create an LLM. llm = LLM(model=model_path, dtype='bfloat16') # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: OutOfMemoryError Llama2-70b offline_infer code ``` nvidia-smi 8GPUS A800 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 470.161.03 Driver Version: 470.161.03 CUDA Version: 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e='bfloat16') # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. prompts = [] prefix_info = [] with open('all_toxic.respons...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
