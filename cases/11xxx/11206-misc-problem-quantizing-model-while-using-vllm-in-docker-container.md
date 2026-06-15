# vllm-project/vllm#11206: [Misc]: Problem quantizing model while using vllm in docker container

| 字段 | 值 |
| --- | --- |
| Issue | [#11206](https://github.com/vllm-project/vllm/issues/11206) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Problem quantizing model while using vllm in docker container

### Issue 正文摘录

### Anything you want to discuss about vllm. What am I doing wrong here? When I load, quantize (4 bit) and share the llama 3.1 8b instruct model across 2 A100s, it sucks up all the VRAM: ``` docker run --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=hf_............................" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.1-8B-Instruct \ --tensor-parallel-size 2 \ --quantization bitsandbytes \ --load_format bitsandbytes ``` GPU monitoring: ``` GPU monitoring: +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 555.42.06 Driver Version: 555.42.06 CUDA Version: 12.5 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA A100 80GB PCIe Off | 00000000:4F:00.0 Off | 0 | | N/A 32C P0 64W / 300W | 72129MiB / 81920MiB | 0% Default | | | | Disabled | +-------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Misc]: Problem quantizing model while using vllm in docker container stale ### Anything you want to discuss about vllm. What am I doing wrong here? When I load, quantize (4 bit) and share the llama 3.1 8b instruct mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Misc]: Problem quantizing model while using vllm in docker container stale ### Anything you want to discuss about vllm. What am I doing wrong here? When I load, quantize (4 bit) and share the llama 3.1 8b instruct mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: oad, quantize (4 bit) and share the llama 3.1 8b instruct model across 2 A100s, it sucks up all the VRAM: ``` docker run --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=hf_....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Misc]: Problem quantizing model while using vllm in docker container stale ### Anything you want to discuss about vllm. What am I doing wrong here? When I load, quantize (4 bit) and share the llama 3.1 8b instruct mode...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GI CI PID Type Process name GPU Memory | | ID ID Usage | ``` This simply shouldn't be happening. I am 100% certain there is no other GPU process running as I am consistent

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
