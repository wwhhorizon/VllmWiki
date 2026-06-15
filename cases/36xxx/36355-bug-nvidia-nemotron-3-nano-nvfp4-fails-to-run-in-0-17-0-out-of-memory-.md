# vllm-project/vllm#36355: [Bug]: NVIDIA Nemotron 3 Nano NVFP4 fails to run in 0.17.0 (out of memory, but previously worked)

| 字段 | 值 |
| --- | --- |
| Issue | [#36355](https://github.com/vllm-project/vllm/issues/36355) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;kernel |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA Nemotron 3 Nano NVFP4 fails to run in 0.17.0 (out of memory, but previously worked)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run NVIDIA Nemotron 3 Nano NVFP4 in vLLM 0.17.0 it throws a memory related error and shuts down. - CPU: AMD Ryzen 9 9950X - Memory: 4x32 GB TeamGroup DDR5 5200 MT/sec - GPU 0: NVIDIA GeForce RTX 5080 16 GB - GPU 1: NVIDIA GeForce RTX 5060 Ti 16 GB - Windows 11 latest + WSL2 + Docker Desktop 4.61.0 I've cloned the NVIDIA Nemotron 3 Nano NVFP4 repository from Hugging Face: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 I had gotten this working in a previous version of vLLM, but in 0.17.0 it's failing again. The worker process is indicating CUDA out of memory, but considering I had it working in a previous version, and based on the size of the model itself, it should be able to fit into my 2x GPU system: > torch.AcceleratorError: CUDA error: out of memory ```pwsh docker run ` --gpus all ` -v "C:\git\NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4:/model" ` -p 8000:8000 ` --env CUDA_DEVICE_ORDER=PCI_BUS_ID ` --env "CUDA_VISIBLE_DEVICES=0,1" ` --ipc=host ` vllm/vllm-openai:latest ` /model ` --served-model-name nemotron ` --max-model-len 30000 ` --max-num-seqs 8 ` --kv-cache-dtype fp8 ` --trust-remote-code ` --reasonin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: B - GPU 1: NVIDIA GeForce RTX 5060 Ti 16 GB - Windows 11 latest + WSL2 + Docker Desktop 4.61.0 I've cloned the NVIDIA Nemotron 3 Nano NVFP4 repository from Hugging Face: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: NVIDIA Nemotron 3 Nano NVFP4 fails to run in 0.17.0 (out of memory, but previously worked) bug ### Your current environment ### 🐛 Describe the bug When I run NVIDIA Nemotron 3 Nano NVFP4 in vLLM 0.17.0 it throws...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 50X - Memory: 4x32 GB TeamGroup DDR5 5200 MT/sec - GPU 0: NVIDIA GeForce RTX 5080 16 GB - GPU 1: NVIDIA GeForce RTX 5060 Ti 16 GB - Windows 11 latest + WSL2 + Docker Desktop 4.61.0 I've cloned the NVIDIA Nemotron 3 Nano...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: e nemotron ` --max-model-len 30000 ` --max-num-seqs 8 ` --kv-cache-dtype fp8 ` --trust-remote-code ` --reasoning-parser-plugin "/model/nano_v3_reasoning_parser.py" ` --reasoning-parser nano_v3 ` --tensor-parallel-size 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d the NVIDIA Nemotron 3 Nano NVFP4 repository from Hugging Face: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 I had gotten this working in a previous version of vLLM, but in 0.17.0 it's failing aga...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
