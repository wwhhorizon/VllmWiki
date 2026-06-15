# vllm-project/vllm#15216: [Bug][Help]: I used vllm 0.8.0 to deploy whisper-large-v3-turbo . The model is only 1.6G , and i use a 3060 with 12G. However, right after the service started, it encountered an out-of-memory (OOM) error.

| 字段 | 值 |
| --- | --- |
| Issue | [#15216](https://github.com/vllm-project/vllm/issues/15216) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Help]: I used vllm 0.8.0 to deploy whisper-large-v3-turbo . The model is only 1.6G , and i use a 3060 with 12G. However, right after the service started, it encountered an out-of-memory (OOM) error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text root@8b927132d0a8:~/whisper-large-v3-turbo# pip list | grep vllm vllm 0.8.0 root@8b927132d0a8:~/whisper-large-v3-turbo# nvidia-smi Thu Mar 20 05:18:02 2025 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.54.03 Driver Version: 535.54.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA GeForce RTX 3060 Off | 00000000:03:00.0 Off | N/A | | 30% 30C P8 11W / 170W | 4MiB / 12288MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ----------------------------+ | NVIDIA-SMI 535.54.03 Driver Version: 535.54.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 0.8.0 root@8b927132d0a8:~/whisper-large-v3-turbo# nvidia-smi Thu Mar 20 05:18:02 2025 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.54.03 Driver Version: 535....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=448, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][Help]: I used vllm 0.8.0 to deploy whisper-large-v3-turbo . The model is only 1.6G , and i use a 3060 with 12G. However, right after the service started, it encountered an out-of-memory (OOM) error. bug ### Your c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 0 LLM engine (v0.8.0) with config: model='/root/whisper-large-v3-turbo', speculative_config=None, tokenizer='/root/whisper-large-v3-turbo', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
